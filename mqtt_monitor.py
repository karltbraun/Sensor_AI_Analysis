#!/usr/bin/env python3
"""
MQTT Topic Monitor + Analyzer
Subscribes to KTBMES/TWIX/sensors/# for 15 minutes,
saves raw data to JSON, then writes a Markdown analysis report.

Usage:
    uv run mqtt_monitor.py
"""

import json
import time
import signal
import sys
from collections import defaultdict
from datetime import datetime, timezone
import statistics

import paho.mqtt.client as mqtt

# ── Config ─────────────────────────────────────────────────────────────────
BROKER_HOST   = "45.63.82.34"
BROKER_PORT   = 1883
DURATION_SECS = 15 * 60   # 15 minutes
OUTPUT_JSON   = "mqtt_raw_data.json"
OUTPUT_MD     = "mqtt_analysis.md"

TOPIC_GROUPS = {
    "house_weather_sensors":    "KTBMES/TWIX/sensors/house_weather_sensors/#",
    "other_weather_sensors":    "KTBMES/TWIX/sensors/other_weather_sensors/#",
    "other_pressure_sensors":   "KTBMES/TWIX/sensors/other_pressure_sensors/#",
    "unknown_other_sensors":    "KTBMES/TWIX/sensors/unknown_other_sensors/#",
}

# ── Storage ─────────────────────────────────────────────────────────────────
messages = []   # list of {topic, payload, ts}
start_time = None
stop_flag = False


# ── MQTT Callbacks ──────────────────────────────────────────────────────────
def on_connect(client, userdata, flags, rc, properties=None):
    # rc is a ReasonCode object in paho-mqtt v2; use .value for int comparison
    rc_val = int(rc.value) if hasattr(rc, 'value') else int(rc)
    codes = {0:"OK", 1:"Bad protocol", 2:"Client ID rejected",
             3:"Server unavailable", 4:"Bad credentials", 5:"Not authorised"}
    print(f"[connect] rc={rc_val} — {codes.get(rc_val, str(rc))}")
    if rc_val == 0:
        for name, topic in TOPIC_GROUPS.items():
            client.subscribe(topic, qos=0)
            print(f"  ✓ Subscribed: {topic}")


def on_message(client, userdata, msg):
    ts = datetime.now(timezone.utc).isoformat()
    try:
        payload_str = msg.payload.decode("utf-8", errors="replace")
    except Exception:
        payload_str = repr(msg.payload)

    messages.append({
        "topic":   msg.topic,
        "payload": payload_str,
        "ts":      ts,
    })

    elapsed = int(time.time() - start_time)
    remaining = max(0, DURATION_SECS - elapsed)
    print(f"  [{elapsed:>4}s / {remaining:>4}s left]  {msg.topic}  →  {payload_str[:80]}")


def on_disconnect(client, userdata, disconnect_flags, reason_code, properties=None):
    # paho-mqtt v2 passes 5 args; disconnect_flags added between userdata and reason_code
    print(f"[disconnect] reason={reason_code}")


# ── Helpers ─────────────────────────────────────────────────────────────────
def group_for(topic: str) -> str:
    for name, pattern in TOPIC_GROUPS.items():
        prefix = pattern.rstrip("/#")
        if topic.startswith(prefix):
            return name
    return "unknown"


def try_numeric(value: str):
    """Return float if parseable, else None."""
    try:
        return float(value.strip())
    except (ValueError, AttributeError):
        pass
    try:
        obj = json.loads(value)
        if isinstance(obj, (int, float)):
            return float(obj)
    except Exception:
        pass
    return None


def try_json(value: str):
    try:
        return json.loads(value)
    except Exception:
        return None


# ── Analysis ─────────────────────────────────────────────────────────────────
def analyze(msgs: list, duration_secs: int) -> str:
    ts_start = msgs[0]["ts"]  if msgs else "—"
    ts_end   = msgs[-1]["ts"] if msgs else "—"

    # Group messages
    by_group   = defaultdict(list)
    by_topic   = defaultdict(list)
    for m in msgs:
        g = group_for(m["topic"])
        by_group[g].append(m)
        by_topic[m["topic"]].append(m)

    lines = []
    a = lines.append

    a("# MQTT Monitor Analysis Report")
    a(f"\n**Broker:** `{BROKER_HOST}:{BROKER_PORT}`")
    a(f"**Session start:** {ts_start}")
    a(f"**Session end:**   {ts_end}")
    a(f"**Duration monitored:** {duration_secs // 60} min {duration_secs % 60} sec")
    a(f"**Total messages received:** {len(msgs)}")
    a(f"**Unique topics seen:** {len(by_topic)}")
    a("")

    # Overall message rate
    if duration_secs > 0:
        rate = len(msgs) / duration_secs * 60
        a(f"**Overall message rate:** {rate:.1f} msg/min\n")

    a("---\n")

    # Per-group sections
    for group_name, pattern in TOPIC_GROUPS.items():
        group_msgs = by_group.get(group_name, [])
        a(f"## {group_name.replace('_', ' ').title()}")
        a(f"\n**Subscription:** `{pattern}`")
        a(f"**Messages received:** {len(group_msgs)}")

        if not group_msgs:
            a("\n_No messages received on this topic space during the session._\n")
            a("---\n")
            continue

        # Unique sub-topics
        sub_topics = defaultdict(list)
        for m in group_msgs:
            sub_topics[m["topic"]].append(m)

        a(f"**Unique sub-topics:** {len(sub_topics)}")

        if duration_secs > 0:
            grp_rate = len(group_msgs) / duration_secs * 60
            a(f"**Group message rate:** {grp_rate:.1f} msg/min")

        a("\n### Sub-topics\n")
        a("| Sub-topic | Count | Rate (msg/min) | Sample Value |")
        a("|-----------|-------|----------------|--------------|")
        for topic_name, t_msgs in sorted(sub_topics.items()):
            t_rate = len(t_msgs) / duration_secs * 60 if duration_secs > 0 else 0
            sample = t_msgs[-1]["payload"][:60].replace("|", "\\|")
            a(f"| `{topic_name}` | {len(t_msgs)} | {t_rate:.2f} | `{sample}` |")

        # Numeric value analysis
        a("\n### Payload Analysis\n")
        numeric_found = False
        for topic_name, t_msgs in sorted(sub_topics.items()):
            vals = [try_numeric(m["payload"]) for m in t_msgs]
            vals = [v for v in vals if v is not None]
            if vals:
                numeric_found = True
                mn  = min(vals)
                mx  = max(vals)
                avg = statistics.mean(vals)
                med = statistics.median(vals)
                std = statistics.stdev(vals) if len(vals) > 1 else 0.0
                short = topic_name.split("/")[-1]
                a(f"**`{short}`** ({len(vals)} numeric readings)")
                a(f"- Min: `{mn}`  Max: `{mx}`  Mean: `{avg:.3f}`  Median: `{med:.3f}`  StdDev: `{std:.3f}`")
                a("")

        if not numeric_found:
            # Try JSON payloads
            json_found = False
            all_json_keys = set()
            for m in group_msgs:
                obj = try_json(m["payload"])
                if isinstance(obj, dict):
                    json_found = True
                    all_json_keys.update(obj.keys())

            if json_found:
                a("Payloads appear to be **JSON objects**.")
                if all_json_keys:
                    a(f"Keys observed: {', '.join(f'`{k}`' for k in sorted(all_json_keys))}\n")
                # Show last 3 unique samples
                a("**Recent samples:**\n")
                seen = []
                for m in reversed(group_msgs):
                    if m["payload"] not in seen:
                        seen.append(m["payload"])
                    if len(seen) == 3:
                        break
                for s in reversed(seen):
                    a(f"```json\n{s}\n```")
            else:
                a("Payloads are **non-numeric strings**. Sample values:\n")
                unique_payloads = list(dict.fromkeys(m["payload"] for m in group_msgs))
                for p in unique_payloads[:8]:
                    a(f"- `{p}`")
                a("")

        a("\n---\n")

    # Footer
    a("## Raw Data")
    a(f"\nFull message log saved to `{OUTPUT_JSON}`.")
    a(f"\n_Report generated at {datetime.now(timezone.utc).isoformat()}_")

    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    global start_time, stop_flag

    print(f"Connecting to {BROKER_HOST}:{BROKER_PORT} …")
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect    = on_connect
    client.on_message    = on_message
    client.on_disconnect = on_disconnect

    def _sigint(sig, frame):
        global stop_flag
        print("\nInterrupted — wrapping up early …")
        stop_flag = True

    signal.signal(signal.SIGINT, _sigint)

    client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
    client.loop_start()

    start_time   = time.time()
    deadline     = start_time + DURATION_SECS
    print(f"\nListening for {DURATION_SECS // 60} minutes … (Ctrl-C to stop early)\n")

    while time.time() < deadline and not stop_flag:
        time.sleep(1)

    actual_duration = int(time.time() - start_time)
    client.loop_stop()
    try:
        client.disconnect()
    except Exception as e:
        print(f"[disconnect] warning: {e} (ignored — data will still be saved)")

    print(f"\n✓ Collection complete — {len(messages)} messages in {actual_duration}s")

    # Save raw data
    with open(OUTPUT_JSON, "w") as f:
        json.dump({"meta": {"broker": BROKER_HOST, "port": BROKER_PORT,
                             "duration_secs": actual_duration,
                             "topic_groups": TOPIC_GROUPS},
                   "messages": messages}, f, indent=2)
    print(f"✓ Raw data → {OUTPUT_JSON}")

    # Generate report
    md = analyze(messages, actual_duration)
    with open(OUTPUT_MD, "w") as f:
        f.write(md)
    print(f"✓ Analysis report → {OUTPUT_MD}")
    print("\nDone!")


if __name__ == "__main__":
    main()
