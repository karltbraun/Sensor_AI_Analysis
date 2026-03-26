# MQTT Broker Session Analysis
**Broker:** `45.63.82.34:1883`
**Session:** 2026-03-26 21:03–21:18 UTC (15 minutes)
**Total messages:** 8,802 across 621 unique topics
**Overall rate:** 586.8 msg/min

---

## Executive Summary

The broker is highly active, receiving data from what appears to be an **RTL-433-based SDR (Software Defined Radio)** receiver that is passively capturing 433 MHz RF transmissions and republishing them to MQTT. Four distinct topic namespaces were observed, covering named house sensors, unidentified weather sensors, tire pressure monitors from nearby vehicles, and a large catch-all bucket of miscellaneous/unknown devices.

Several issues worth addressing are identified below under each topic space and in the cross-cutting observations section.

---

## Topic Space Analysis

### 1. `house_weather_sensors` — Named House Devices
**119 messages · 7 devices · 7.9 msg/min**

This is the only space with human-assigned device names, suggesting these are intentionally registered/known sensors. All payloads are JSON with a rich schema including `temperature_C`, `temperature_F`, `humidity`, `battery_ok`, `moisture`, `channel`, and metadata fields.

**Devices observed:**

| Device | device_id | Protocol | ~Rate |
|--------|-----------|----------|-------|
| OFFICE | 234 | Acurite 606TX (#55) | 1.87/min |
| DUMMY | 0 | Springfield Temp & Soil Moisture (#53) | 1.20/min |
| LIVING_ROOM | 101 | Multiple Temp & Humidity SC91 (#91) | 0.93/min |
| LivingRoom-C | 101 | Multiple Temp & Humidity SC91 (#91) | 1.00/min |
| PORCH | 138 | Multiple Temp & Humidity SC91 (#91) | 1.00/min |
| DECK | 152 | _(unknown)_ | 1.00/min |
| DECK-B | 138 | _(unknown)_ | 0.93/min |

**Issues identified:**

- **Duplicate device_id 101** — `LIVING_ROOM` and `LivingRoom-C` share the same `device_id`. These are the same physical sensor registered under two names. One registration should be removed.
- **Duplicate device_id 138** — `PORCH` and `DECK-B` share the same `device_id`. Same issue — one physical sensor, two topic registrations.
- **DUMMY device** — `device_id: 0`, protocol "Springfield Temperature and Soil Moisture". Last seen 2026-03-23 with temperature of **49.7°C / 121.46°F** and humidity 100% — clearly invalid/test values. The `time_last_published` is current (2026-03-26) but `time_last_seen` is days old, meaning it is being re-published stale data on schedule. This device should be filtered or removed.
- **OFFICE (device_id 234) also appears in `unknown_other_sensors`** — see cross-cutting observations below.

**Sample real readings (at session time):**
- PORCH: 8.0°C / 46.4°F, 59% humidity
- OFFICE: 19.8°C / 67.64°F (Acurite 606TX, temperature only)

---

### 2. `other_weather_sensors` — Unidentified Weather Devices
**1,440 messages · 97 devices · 96.0 msg/min**

All devices are named `UNKNOWN_DEVICE_<integer_id>` with small integer IDs (roughly 2–255, plus a few larger outliers like `4547739` and `47007`). These are RF devices that have been received by the SDR but not yet assigned names or classified.

**Protocols identified in samples:**
- **Oregon Scientific SL109H** (`Oregon Sci Hygro`, protocol #54) — temperature + humidity sensor
- **Globaltronics GT-WT-02** (`GlobalTronics`, protocol #25) — temperature + humidity
- Others implied by the diversity of `protocol_id` values

**Payload fields** include `temperature_C/F`, `humidity`, `rain_mm`, `wind_avg_m_s`, `wind_dir_deg`, `wind_max_m_s` — indicating some of these are full weather stations, not just temperature probes.

**Issues identified:**

- **Stale data being republished** — Several devices show `time_last_seen` from days or weeks ago (e.g., device 73 last seen 2026-03-23, device 146 last seen 2026-02-18) but are still published every ~minute. Consumers of this data cannot distinguish "live reading" from "last known value from weeks ago" without checking timestamps explicitly.
- **Invalid sensor readings** — Device 146 reports **humidity of 108%** (physically impossible), and device 73 shows `rain_mm: 2047.5` with battery_ok: -1. Both should be treated as bad decodes.
- **No signal quality data** — All `rssi`, `snr`, and `noise` fields are -999, indicating signal quality metrics are not being passed through from RTL-433. This makes it impossible to assess reception quality or filter weak/unreliable decodes.
- **Most devices at exactly 1.00 msg/min** (15 messages in 15 min) — this is a re-publish heartbeat, not live RF activity. Only one device (`UNKNOWN_DEVICE_198`) appeared with just 1 message, suggesting a live transmission was captured mid-session.

---

### 3. `other_pressure_sensors` — Vehicle TPMS Sensors
**1,740 messages · 116 devices · 116.0 msg/min**

This is the most surprising namespace. The devices are **Tire Pressure Monitoring System (TPMS)** sensors from nearby vehicles, passively captured by the SDR. The device IDs are 6–8 character hex strings (a hallmark of TPMS ID formats).

**Protocols confirmed:**
- **Schrader TPMS** (protocol #60) — common OEM fitment on many US vehicles
- **Hyundai TPMS / VDO** (protocol #186)

**Payload fields** include `pressure_kPa`, `pressure_psi`, `temperature_C/F`, `centrifugal_acc`, `moving`, `wheel`, `flags`, `state`, `repeat` — all characteristic TPMS fields.

**Sample readings:**
- `c5b9e68a` (Hyundai TPMS): 24°C, 140.25 kPa / 20.3 PSI — _slightly low, possible slow leak or cold tire_
- `0FD5D9D` (Schrader): 19°C, 427.5 kPa / 62.0 PSI — _unusually high; may be truck/commercial vehicle or a bad decode_
- `0FD5E41` (Schrader): 38°C, 542.5 kPa / 78.7 PSI — _very high pressure and temperature; likely a bad decode_

**Observations:**
- The `0e04b7xx` cluster (devices `0e04b7`, `0e04b784`, `0e04b785`, `0e04b788`, `0e04b78e`) are likely the **four TPMS sensors + a spare** from a single vehicle — the base ID with 4 suffixed variants is a known TPMS enrollment pattern.
- These sensors only transmit while the vehicle is moving or recently parked. The republishing heartbeat is keeping them visible even when the cars are gone.
- **Several TPMS device IDs also appear in `unknown_other_sensors`** — indicating cross-classification (see below).
- 116 unique TPMS devices in a 15-minute window is a significant number — suggests the SDR is in a location with moderate vehicle traffic, or has accumulated a large history of nearby vehicles.

---

### 4. `unknown_other_sensors` — Catch-All / Unclassified
**5,503 messages · 401 devices · 366.9 msg/min**

By far the largest and most diverse namespace — 63% of all broker traffic. This appears to be the default bucket for any RF signal that doesn't fit a known classification rule, plus spillover from the other namespaces.

**Notable sub-observations:**

- **Negative integer device IDs** (e.g., `-101582540`, `-130804730`) — these are 32-bit signed integers that have wrapped around. Likely a consequence of using signed int32 for device IDs in a system that expects unsigned. A type fix upstream would resolve this.
- **`UNKNOWN_DEVICE_raw`** — a special device_id of literally `"raw"` with `protocol_id: "-1"`. This is likely a catch-all for RTL-433's raw output when it cannot decode a signal to any known protocol.
- **Very wide payload key set** — 90+ distinct keys observed, including home security fields (`alarm`, `tamper`, `closed`, `housecode`), home automation (`switch1`–`switch5`, `cmd`, `cmd_id`), liquid/depth sensors (`depth_cm`), and garage/remote controls (`rolling`, `fixed`, `encrypted`). This namespace is genuinely capturing a wide variety of 433 MHz devices in the RF environment.
- **Some devices publish at 1.20/min** (18 messages vs 15) — slightly higher than the standard heartbeat, possibly live active transmitters.

---

## Cross-Cutting Observations

### Topic Overlap / Double Classification
Several device IDs appear in **more than one topic namespace simultaneously**, indicating the classification/routing logic has gaps:

| device_id | Appears in |
|-----------|-----------|
| `234` (OFFICE) | `house_weather_sensors` AND `unknown_other_sensors` |
| `198` | `other_weather_sensors` AND `unknown_other_sensors` |
| `c97da6e7`, `d1c69de6`, `d1c69df3`, `d1cd32bb`, `d1cd3322`, `fa9288`, `fa9344`, `fa9359`, `fa936d` | `other_pressure_sensors` AND `unknown_other_sensors` |

This means consumers subscribing to `unknown_other_sensors/#` are receiving duplicate messages for devices that also have their own classified topics. The routing logic should apply exclusive classification — a device should land in exactly one topic.

### Stale Data vs. Live Data
The system is republishing last-known values on a fixed schedule regardless of how old they are. Many devices have `time_last_seen` days or weeks in the past. Any downstream consumer that doesn't explicitly check `time_last_seen_iso` will treat stale data as current. Consider either:
- Adding a staleness flag to the payload, or
- Suppressing republication of readings older than a configurable threshold

### RTL-433 as the Source
The consistent payload schema across all namespaces — `device_id`, `protocol_id`, `protocol_name`, `protocol_description`, `rssi`, `snr`, `noise`, `freq`, `mic`, `mod`, `time_last_seen_*`, `time_last_published_*` — is the standard output format of **rtl_433** (the open-source SDR decoder). This is the underlying engine. Understanding its configuration (device whitelist/blacklist, output filters, MQTT topic mapping) would be the key to resolving the classification and staleness issues above.

---

## Recommendations

1. **Resolve duplicate device registrations** — Clean up `LIVING_ROOM` / `LivingRoom-C` (both device_id 101) and `PORCH` / `DECK-B` (both device_id 138). Pick one canonical name per physical sensor.

2. **Remove or quarantine the DUMMY device** — device_id 0 with invalid readings should be excluded from the topic or clearly flagged as a test device.

3. **Fix exclusive topic routing** — Device 234 (OFFICE) and several TPMS devices are publishing to multiple namespaces. Classification rules should be mutually exclusive.

4. **Address stale data** — Add staleness awareness to either the publisher (suppress old readings) or document that `time_last_seen_iso` must be checked by consumers.

5. **Investigate and name TPMS devices** — The 116 TPMS devices in `other_pressure_sensors` are from specific vehicles. If these are household vehicles, consider naming them (e.g., `FORD_F150_FL`, `HONDA_CIVIC_RR`) or creating a separate filtered namespace if TPMS data isn't useful in the current pipeline.

6. **Review negative device_id values** — These are signed integer overflow artifacts. Fix the upstream ID type to `uint32` or `string` to avoid this.

7. **Enable RSSI/SNR reporting** — All signal quality fields are -999. If the RTL-433 configuration is suppressing these, enabling them would allow filtering of weak/unreliable decodes, reducing noise in all namespaces.

---

_Analysis based on 15-minute passive observation session, 2026-03-26 21:03–21:18 UTC._
