# MQTT Monitor Analysis Report

**Broker:** `45.63.82.34:1883`
**Session start:** 2026-03-26T21:03:38.739484+00:00
**Session end:**   2026-03-26T21:18:39.087380+00:00
**Duration monitored:** 15 min 0 sec
**Total messages received:** 8802
**Unique topics seen:** 621

**Overall message rate:** 586.8 msg/min

---

## House Weather Sensors

**Subscription:** `KTBMES/TWIX/sensors/house_weather_sensors/#`
**Messages received:** 119
**Unique sub-topics:** 7
**Group message rate:** 7.9 msg/min

### Sub-topics

| Sub-topic | Count | Rate (msg/min) | Sample Value |
|-----------|-------|----------------|--------------|
| `KTBMES/TWIX/sensors/house_weather_sensors/DECK` | 15 | 1.00 | `{"device_id": "152", "device_name": "DECK", "protocol_id": "` |
| `KTBMES/TWIX/sensors/house_weather_sensors/DECK-B` | 14 | 0.93 | `{"device_id": "138", "device_name": "DECK-B", "protocol_id":` |
| `KTBMES/TWIX/sensors/house_weather_sensors/DUMMY` | 18 | 1.20 | `{"device_id": "0", "device_name": "DUMMY", "protocol_id": "5` |
| `KTBMES/TWIX/sensors/house_weather_sensors/LIVING_ROOM` | 14 | 0.93 | `{"device_id": "101", "device_name": "LIVING_ROOM", "protocol` |
| `KTBMES/TWIX/sensors/house_weather_sensors/LivingRoom-C` | 15 | 1.00 | `{"device_id": "101", "device_name": "LivingRoom-C", "protoco` |
| `KTBMES/TWIX/sensors/house_weather_sensors/OFFICE` | 28 | 1.87 | `{"device_id": "234", "device_name": "OFFICE", "protocol_id":` |
| `KTBMES/TWIX/sensors/house_weather_sensors/PORCH` | 15 | 1.00 | `{"device_id": "138", "device_name": "PORCH", "protocol_id": ` |

### Payload Analysis

Payloads appear to be **JSON objects**.
Keys observed: `battery_V`, `battery_ok`, `button`, `channel`, `charge_pct`, `charging_error`, `control`, `cranking_error`, `device_id`, `device_name`, `freq`, `health_pct`, `humidity`, `mic`, `mod`, `moisture`, `noise`, `protocol_description`, `protocol_id`, `protocol_name`, `rssi`, `snr`, `starting_V`, `status`, `temperature_C`, `temperature_F`, `time`, `time_last_published_iso`, `time_last_published_ts`, `time_last_seen_iso`, `time_last_seen_ts`, `transmit`, `zone`

**Recent samples:**

```json
{"device_id": "138", "device_name": "PORCH", "protocol_id": "91", "protocol_name": "Multiple Temp & Humidty*SC91", "protocol_description": "inFactory, nor-tec, FreeTec NC-3982-913 temperature humidity sensor", "temperature_C": 8.0, "temperature_F": "67.2", "humidity": 59.0, "battery_ok": "1", "channel": "3", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CRC", "mod": "NO_MOD", "time": "2026-03-26 14:18:21", "time_last_seen_ts": 1774559906.556784, "time_last_seen_iso": "2026-03-26T14:18:26.556784", "time_last_published_ts": 1774559906.560437, "time_last_published_iso": "2026-03-26T14:18:26.560437", "button": "0", "transmit": "AUTO", "moisture": "30", "status": "10"}
```
```json
{"device_id": "234", "device_name": "OFFICE", "protocol_id": "55", "protocol_name": "Acurite 606TX", "protocol_description": "Acurite 606TX Temperature Sensor", "temperature_C": 19.8, "temperature_F": 67.64, "humidity": -999.0, "battery_ok": "1", "channel": "1", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CHECKSUM", "mod": "NO_MOD", "time": "2026-03-26 14:18:34", "time_last_seen_ts": 1774559916.563844, "time_last_seen_iso": "2026-03-26T14:18:36.563844", "time_last_published_ts": 1774559916.564334, "time_last_published_iso": "2026-03-26T14:18:36.564334", "button": "0", "transmit": "AUTO", "moisture": "0"}
```
```json
{"device_id": "0", "device_name": "DUMMY", "protocol_id": "53", "protocol_name": "Temp & Hydro", "protocol_description": "Springfield Temperature and Soil Moisture", "temperature_C": 49.7, "temperature_F": 121.46000000000001, "humidity": 100.0, "battery_ok": "1", "channel": "1", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CHECKSUM", "mod": "NO_MOD", "time": "2026-03-23 00:30:59", "time_last_seen_ts": 1774251061.451752, "time_last_seen_iso": "2026-03-23T00:31:01.451752", "time_last_published_ts": 1774559916.565654, "time_last_published_iso": "2026-03-26T14:18:36.565654", "transmit": "AUTO", "moisture": "0", "button": "0", "control": "Limit (0)", "zone": "3", "health_pct": "0", "cranking_error": "0", "charge_pct": "0", "charging_error": "0", "battery_V": "0", "starting_V": "0", "status": "0"}
```

---

## Other Weather Sensors

**Subscription:** `KTBMES/TWIX/sensors/other_weather_sensors/#`
**Messages received:** 1440
**Unique sub-topics:** 97
**Group message rate:** 96.0 msg/min

### Sub-topics

| Sub-topic | Count | Rate (msg/min) | Sample Value |
|-----------|-------|----------------|--------------|
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_10` | 15 | 1.00 | `{"device_id": "10", "device_name": "UNKNOWN_DEVICE_10", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_102` | 15 | 1.00 | `{"device_id": "102", "device_name": "UNKNOWN_DEVICE_102", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_108` | 15 | 1.00 | `{"device_id": "108", "device_name": "UNKNOWN_DEVICE_108", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_109` | 15 | 1.00 | `{"device_id": "109", "device_name": "UNKNOWN_DEVICE_109", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_11` | 15 | 1.00 | `{"device_id": "11", "device_name": "UNKNOWN_DEVICE_11", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_116` | 15 | 1.00 | `{"device_id": "116", "device_name": "UNKNOWN_DEVICE_116", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_12` | 15 | 1.00 | `{"device_id": "12", "device_name": "UNKNOWN_DEVICE_12", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_128` | 15 | 1.00 | `{"device_id": "128", "device_name": "UNKNOWN_DEVICE_128", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_129` | 15 | 1.00 | `{"device_id": "129", "device_name": "UNKNOWN_DEVICE_129", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_13` | 15 | 1.00 | `{"device_id": "13", "device_name": "UNKNOWN_DEVICE_13", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_130` | 15 | 1.00 | `{"device_id": "130", "device_name": "UNKNOWN_DEVICE_130", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_131` | 15 | 1.00 | `{"device_id": "131", "device_name": "UNKNOWN_DEVICE_131", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_132` | 15 | 1.00 | `{"device_id": "132", "device_name": "UNKNOWN_DEVICE_132", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_134` | 15 | 1.00 | `{"device_id": "134", "device_name": "UNKNOWN_DEVICE_134", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_135` | 15 | 1.00 | `{"device_id": "135", "device_name": "UNKNOWN_DEVICE_135", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_14` | 15 | 1.00 | `{"device_id": "14", "device_name": "UNKNOWN_DEVICE_14", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_140` | 15 | 1.00 | `{"device_id": "140", "device_name": "UNKNOWN_DEVICE_140", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_141` | 15 | 1.00 | `{"device_id": "141", "device_name": "UNKNOWN_DEVICE_141", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_146` | 15 | 1.00 | `{"device_id": "146", "device_name": "UNKNOWN_DEVICE_146", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_15` | 15 | 1.00 | `{"device_id": "15", "device_name": "UNKNOWN_DEVICE_15", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_153` | 15 | 1.00 | `{"device_id": "153", "device_name": "UNKNOWN_DEVICE_153", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_160` | 15 | 1.00 | `{"device_id": "160", "device_name": "UNKNOWN_DEVICE_160", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_161` | 15 | 1.00 | `{"device_id": "161", "device_name": "UNKNOWN_DEVICE_161", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_162` | 15 | 1.00 | `{"device_id": "162", "device_name": "UNKNOWN_DEVICE_162", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_163` | 15 | 1.00 | `{"device_id": "163", "device_name": "UNKNOWN_DEVICE_163", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_168` | 15 | 1.00 | `{"device_id": "168", "device_name": "UNKNOWN_DEVICE_168", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_169` | 15 | 1.00 | `{"device_id": "169", "device_name": "UNKNOWN_DEVICE_169", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_170` | 15 | 1.00 | `{"device_id": "170", "device_name": "UNKNOWN_DEVICE_170", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_172` | 15 | 1.00 | `{"device_id": "172", "device_name": "UNKNOWN_DEVICE_172", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_176` | 15 | 1.00 | `{"device_id": "176", "device_name": "UNKNOWN_DEVICE_176", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_178` | 15 | 1.00 | `{"device_id": "178", "device_name": "UNKNOWN_DEVICE_178", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_182` | 15 | 1.00 | `{"device_id": "182", "device_name": "UNKNOWN_DEVICE_182", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_193` | 15 | 1.00 | `{"device_id": "193", "device_name": "UNKNOWN_DEVICE_193", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_194` | 15 | 1.00 | `{"device_id": "194", "device_name": "UNKNOWN_DEVICE_194", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_195` | 15 | 1.00 | `{"device_id": "195", "device_name": "UNKNOWN_DEVICE_195", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_196` | 15 | 1.00 | `{"device_id": "196", "device_name": "UNKNOWN_DEVICE_196", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_197` | 15 | 1.00 | `{"device_id": "197", "device_name": "UNKNOWN_DEVICE_197", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_198` | 1 | 0.07 | `{"device_id": "198", "device_name": "UNKNOWN_DEVICE_198", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_2` | 15 | 1.00 | `{"device_id": "2", "device_name": "UNKNOWN_DEVICE_2", "proto` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_200` | 15 | 1.00 | `{"device_id": "200", "device_name": "UNKNOWN_DEVICE_200", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_206` | 15 | 1.00 | `{"device_id": "206", "device_name": "UNKNOWN_DEVICE_206", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_208` | 15 | 1.00 | `{"device_id": "208", "device_name": "UNKNOWN_DEVICE_208", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_209` | 15 | 1.00 | `{"device_id": "209", "device_name": "UNKNOWN_DEVICE_209", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_21` | 15 | 1.00 | `{"device_id": "21", "device_name": "UNKNOWN_DEVICE_21", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_210` | 15 | 1.00 | `{"device_id": "210", "device_name": "UNKNOWN_DEVICE_210", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_214` | 15 | 1.00 | `{"device_id": "214", "device_name": "UNKNOWN_DEVICE_214", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_216` | 15 | 1.00 | `{"device_id": "216", "device_name": "UNKNOWN_DEVICE_216", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_218` | 15 | 1.00 | `{"device_id": "218", "device_name": "UNKNOWN_DEVICE_218", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_220` | 15 | 1.00 | `{"device_id": "220", "device_name": "UNKNOWN_DEVICE_220", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_224` | 15 | 1.00 | `{"device_id": "224", "device_name": "UNKNOWN_DEVICE_224", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_226` | 15 | 1.00 | `{"device_id": "226", "device_name": "UNKNOWN_DEVICE_226", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_228` | 15 | 1.00 | `{"device_id": "228", "device_name": "UNKNOWN_DEVICE_228", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_23` | 15 | 1.00 | `{"device_id": "23", "device_name": "UNKNOWN_DEVICE_23", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_236` | 15 | 1.00 | `{"device_id": "236", "device_name": "UNKNOWN_DEVICE_236", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_239` | 15 | 1.00 | `{"device_id": "239", "device_name": "UNKNOWN_DEVICE_239", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_24` | 15 | 1.00 | `{"device_id": "24", "device_name": "UNKNOWN_DEVICE_24", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_240` | 15 | 1.00 | `{"device_id": "240", "device_name": "UNKNOWN_DEVICE_240", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_25` | 15 | 1.00 | `{"device_id": "25", "device_name": "UNKNOWN_DEVICE_25", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_252` | 15 | 1.00 | `{"device_id": "252", "device_name": "UNKNOWN_DEVICE_252", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_255` | 15 | 1.00 | `{"device_id": "255", "device_name": "UNKNOWN_DEVICE_255", "p` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_26` | 15 | 1.00 | `{"device_id": "26", "device_name": "UNKNOWN_DEVICE_26", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_27` | 15 | 1.00 | `{"device_id": "27", "device_name": "UNKNOWN_DEVICE_27", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_28` | 15 | 1.00 | `{"device_id": "28", "device_name": "UNKNOWN_DEVICE_28", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_29` | 15 | 1.00 | `{"device_id": "29", "device_name": "UNKNOWN_DEVICE_29", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_3` | 15 | 1.00 | `{"device_id": "3", "device_name": "UNKNOWN_DEVICE_3", "proto` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_34` | 15 | 1.00 | `{"device_id": "34", "device_name": "UNKNOWN_DEVICE_34", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_36` | 15 | 1.00 | `{"device_id": "36", "device_name": "UNKNOWN_DEVICE_36", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_38` | 15 | 1.00 | `{"device_id": "38", "device_name": "UNKNOWN_DEVICE_38", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_4` | 15 | 1.00 | `{"device_id": "4", "device_name": "UNKNOWN_DEVICE_4", "proto` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_41` | 15 | 1.00 | `{"device_id": "41", "device_name": "UNKNOWN_DEVICE_41", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_42` | 15 | 1.00 | `{"device_id": "42", "device_name": "UNKNOWN_DEVICE_42", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_44` | 14 | 0.93 | `{"device_id": "44", "device_name": "UNKNOWN_DEVICE_44", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_45` | 15 | 1.00 | `{"device_id": "45", "device_name": "UNKNOWN_DEVICE_45", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_4547739` | 15 | 1.00 | `{"device_id": "4547739", "device_name": "UNKNOWN_DEVICE_4547` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_47007` | 15 | 1.00 | `{"device_id": "47007", "device_name": "UNKNOWN_DEVICE_47007"` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_49` | 15 | 1.00 | `{"device_id": "49", "device_name": "UNKNOWN_DEVICE_49", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_54` | 15 | 1.00 | `{"device_id": "54", "device_name": "UNKNOWN_DEVICE_54", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_56` | 15 | 1.00 | `{"device_id": "56", "device_name": "UNKNOWN_DEVICE_56", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_6` | 15 | 1.00 | `{"device_id": "6", "device_name": "UNKNOWN_DEVICE_6", "proto` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_60` | 15 | 1.00 | `{"device_id": "60", "device_name": "UNKNOWN_DEVICE_60", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_64` | 15 | 1.00 | `{"device_id": "64", "device_name": "UNKNOWN_DEVICE_64", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_66` | 15 | 1.00 | `{"device_id": "66", "device_name": "UNKNOWN_DEVICE_66", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_67` | 15 | 1.00 | `{"device_id": "67", "device_name": "UNKNOWN_DEVICE_67", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_69` | 15 | 1.00 | `{"device_id": "69", "device_name": "UNKNOWN_DEVICE_69", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_7` | 15 | 1.00 | `{"device_id": "7", "device_name": "UNKNOWN_DEVICE_7", "proto` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_73` | 15 | 1.00 | `{"device_id": "73", "device_name": "UNKNOWN_DEVICE_73", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_77` | 15 | 1.00 | `{"device_id": "77", "device_name": "UNKNOWN_DEVICE_77", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_79` | 15 | 1.00 | `{"device_id": "79", "device_name": "UNKNOWN_DEVICE_79", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_80` | 15 | 1.00 | `{"device_id": "80", "device_name": "UNKNOWN_DEVICE_80", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_81` | 15 | 1.00 | `{"device_id": "81", "device_name": "UNKNOWN_DEVICE_81", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_82` | 15 | 1.00 | `{"device_id": "82", "device_name": "UNKNOWN_DEVICE_82", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_84` | 15 | 1.00 | `{"device_id": "84", "device_name": "UNKNOWN_DEVICE_84", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_90` | 15 | 1.00 | `{"device_id": "90", "device_name": "UNKNOWN_DEVICE_90", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_92` | 15 | 1.00 | `{"device_id": "92", "device_name": "UNKNOWN_DEVICE_92", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_94` | 15 | 1.00 | `{"device_id": "94", "device_name": "UNKNOWN_DEVICE_94", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_97` | 15 | 1.00 | `{"device_id": "97", "device_name": "UNKNOWN_DEVICE_97", "pro` |
| `KTBMES/TWIX/sensors/other_weather_sensors/UNKNOWN_DEVICE_99` | 15 | 1.00 | `{"device_id": "99", "device_name": "UNKNOWN_DEVICE_99", "pro` |

### Payload Analysis

Payloads appear to be **JSON objects**.
Keys observed: `battery_ok`, `button`, `channel`, `closed`, `control`, `current`, `device_id`, `device_name`, `esn`, `event`, `exception`, `freq`, `humidity`, `interval`, `learn`, `mic`, `mod`, `moisture`, `noise`, `protocol_description`, `protocol_id`, `protocol_name`, `rain_mm`, `rssi`, `snr`, `status`, `status_hex`, `tamper`, `temperature_C`, `temperature_F`, `time`, `time_last_published_iso`, `time_last_published_ts`, `time_last_seen_iso`, `time_last_seen_ts`, `transmit`, `wind_avg_m_s`, `wind_dir_deg`, `wind_max_m_s`, `xactivity`, `xtamper1`, `xtamper2`, `zone`

**Recent samples:**

```json
{"device_id": "73", "device_name": "UNKNOWN_DEVICE_73", "protocol_id": "54", "protocol_name": "Oregon Sci Hygro", "protocol_description": "Oregon Scientific SL109H Remote Thermal Hygro Sensor", "temperature_C": 9.7, "temperature_F": 49.46, "humidity": 100.0, "battery_ok": -1, "channel": "1", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CHECKSUM", "mod": "NO_MOD", "time": "2026-03-23 20:45:01", "time_last_seen_ts": 1774323905.852319, "time_last_seen_iso": "2026-03-23T20:45:05.852319", "time_last_published_ts": 1774559916.587724, "time_last_published_iso": "2026-03-26T14:18:36.587724", "status": "13", "rain_mm": "2047.5"}
```
```json
{"device_id": "146", "device_name": "UNKNOWN_DEVICE_146", "protocol_id": "54", "protocol_name": "Oregon Sci Hygro", "protocol_description": "Oregon Scientific SL109H Remote Thermal Hygro Sensor", "temperature_C": 2.3, "temperature_F": 36.14, "humidity": 108.0, "battery_ok": -1, "channel": "3", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CHECKSUM", "mod": "NO_MOD", "time": "2026-02-18 18:08:34", "time_last_seen_ts": 1771466916.333529, "time_last_seen_iso": "2026-02-18T18:08:36.333529", "time_last_published_ts": 1774559916.587863, "time_last_published_iso": "2026-03-26T14:18:36.587863", "status": "5"}
```
```json
{"device_id": "21", "device_name": "UNKNOWN_DEVICE_21", "protocol_id": "25", "protocol_name": "GlobalTronics", "protocol_description": "Globaltronics GT-WT-02 Sensor", "temperature_C": 19.3, "temperature_F": 66.74000000000001, "humidity": 100.0, "battery_ok": "1", "channel": "1", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CHECKSUM", "mod": "NO_MOD", "time": "2026-03-01 16:49:41", "time_last_seen_ts": 1772412583.890332, "time_last_seen_iso": "2026-03-01T16:49:43.890332", "time_last_published_ts": 1774559916.587997, "time_last_published_iso": "2026-03-26T14:18:36.587997", "button": "0"}
```

---

## Other Pressure Sensors

**Subscription:** `KTBMES/TWIX/sensors/other_pressure_sensors/#`
**Messages received:** 1740
**Unique sub-topics:** 116
**Group message rate:** 116.0 msg/min

### Sub-topics

| Sub-topic | Count | Rate (msg/min) | Sample Value |
|-----------|-------|----------------|--------------|
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_00320F2` | 15 | 1.00 | `{"device_id": "00320F2", "device_name": "UNKNOWN_DEVICE_0032` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_003710E` | 15 | 1.00 | `{"device_id": "003710E", "device_name": "UNKNOWN_DEVICE_0037` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_030A8D5` | 15 | 1.00 | `{"device_id": "030A8D5", "device_name": "UNKNOWN_DEVICE_030A` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_082233` | 15 | 1.00 | `{"device_id": "082233", "device_name": "UNKNOWN_DEVICE_08223` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0943CB9` | 15 | 1.00 | `{"device_id": "0943CB9", "device_name": "UNKNOWN_DEVICE_0943` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0A22847` | 15 | 1.00 | `{"device_id": "0A22847", "device_name": "UNKNOWN_DEVICE_0A22` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0CA724C` | 15 | 1.00 | `{"device_id": "0CA724C", "device_name": "UNKNOWN_DEVICE_0CA7` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0CA72DA` | 15 | 1.00 | `{"device_id": "0CA72DA", "device_name": "UNKNOWN_DEVICE_0CA7` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0DB8BB9` | 15 | 1.00 | `{"device_id": "0DB8BB9", "device_name": "UNKNOWN_DEVICE_0DB8` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0DD0AD8` | 15 | 1.00 | `{"device_id": "0DD0AD8", "device_name": "UNKNOWN_DEVICE_0DD0` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0F3B32C` | 15 | 1.00 | `{"device_id": "0F3B32C", "device_name": "UNKNOWN_DEVICE_0F3B` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0FB2770` | 15 | 1.00 | `{"device_id": "0FB2770", "device_name": "UNKNOWN_DEVICE_0FB2` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0FD5253` | 15 | 1.00 | `{"device_id": "0FD5253", "device_name": "UNKNOWN_DEVICE_0FD5` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0FD5D9D` | 15 | 1.00 | `{"device_id": "0FD5D9D", "device_name": "UNKNOWN_DEVICE_0FD5` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0FD5E41` | 15 | 1.00 | `{"device_id": "0FD5E41", "device_name": "UNKNOWN_DEVICE_0FD5` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0b9f450f` | 15 | 1.00 | `{"device_id": "0b9f450f", "device_name": "UNKNOWN_DEVICE_0b9` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0b9f454e` | 15 | 1.00 | `{"device_id": "0b9f454e", "device_name": "UNKNOWN_DEVICE_0b9` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0bb690ff` | 15 | 1.00 | `{"device_id": "0bb690ff", "device_name": "UNKNOWN_DEVICE_0bb` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0bc0e980` | 15 | 1.00 | `{"device_id": "0bc0e980", "device_name": "UNKNOWN_DEVICE_0bc` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0cdeaca2` | 15 | 1.00 | `{"device_id": "0cdeaca2", "device_name": "UNKNOWN_DEVICE_0cd` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0e04b7` | 15 | 1.00 | `{"device_id": "0e04b7", "device_name": "UNKNOWN_DEVICE_0e04b` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0e04b784` | 15 | 1.00 | `{"device_id": "0e04b784", "device_name": "UNKNOWN_DEVICE_0e0` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0e04b785` | 15 | 1.00 | `{"device_id": "0e04b785", "device_name": "UNKNOWN_DEVICE_0e0` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0e04b788` | 15 | 1.00 | `{"device_id": "0e04b788", "device_name": "UNKNOWN_DEVICE_0e0` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_0e04b78e` | 15 | 1.00 | `{"device_id": "0e04b78e", "device_name": "UNKNOWN_DEVICE_0e0` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_126F645` | 15 | 1.00 | `{"device_id": "126F645", "device_name": "UNKNOWN_DEVICE_126F` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_126F685` | 15 | 1.00 | `{"device_id": "126F685", "device_name": "UNKNOWN_DEVICE_126F` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_1286E4C` | 15 | 1.00 | `{"device_id": "1286E4C", "device_name": "UNKNOWN_DEVICE_1286` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_1E0BAA2` | 15 | 1.00 | `{"device_id": "1E0BAA2", "device_name": "UNKNOWN_DEVICE_1E0B` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_217EEF7` | 15 | 1.00 | `{"device_id": "217EEF7", "device_name": "UNKNOWN_DEVICE_217E` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_21d879d0` | 15 | 1.00 | `{"device_id": "21d879d0", "device_name": "UNKNOWN_DEVICE_21d` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_21d879d9` | 15 | 1.00 | `{"device_id": "21d879d9", "device_name": "UNKNOWN_DEVICE_21d` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_21e61ae4` | 15 | 1.00 | `{"device_id": "21e61ae4", "device_name": "UNKNOWN_DEVICE_21e` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_28d2a007` | 15 | 1.00 | `{"device_id": "28d2a007", "device_name": "UNKNOWN_DEVICE_28d` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_2cca53` | 15 | 1.00 | `{"device_id": "2cca53", "device_name": "UNKNOWN_DEVICE_2cca5` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_2ccb25` | 15 | 1.00 | `{"device_id": "2ccb25", "device_name": "UNKNOWN_DEVICE_2ccb2` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_2cce87` | 15 | 1.00 | `{"device_id": "2cce87", "device_name": "UNKNOWN_DEVICE_2cce8` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_2cd145` | 15 | 1.00 | `{"device_id": "2cd145", "device_name": "UNKNOWN_DEVICE_2cd14` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_319b44b9` | 15 | 1.00 | `{"device_id": "319b44b9", "device_name": "UNKNOWN_DEVICE_319` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_31cd56fa` | 15 | 1.00 | `{"device_id": "31cd56fa", "device_name": "UNKNOWN_DEVICE_31c` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_411e67eb` | 15 | 1.00 | `{"device_id": "411e67eb", "device_name": "UNKNOWN_DEVICE_411` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_41281dc7` | 15 | 1.00 | `{"device_id": "41281dc7", "device_name": "UNKNOWN_DEVICE_412` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_41281df6` | 15 | 1.00 | `{"device_id": "41281df6", "device_name": "UNKNOWN_DEVICE_412` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_41281ef8` | 15 | 1.00 | `{"device_id": "41281ef8", "device_name": "UNKNOWN_DEVICE_412` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_4184b396` | 15 | 1.00 | `{"device_id": "4184b396", "device_name": "UNKNOWN_DEVICE_418` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_419382b5` | 15 | 1.00 | `{"device_id": "419382b5", "device_name": "UNKNOWN_DEVICE_419` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_4193833a` | 15 | 1.00 | `{"device_id": "4193833a", "device_name": "UNKNOWN_DEVICE_419` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_41e66b5e` | 15 | 1.00 | `{"device_id": "41e66b5e", "device_name": "UNKNOWN_DEVICE_41e` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_4d8fd65f` | 15 | 1.00 | `{"device_id": "4d8fd65f", "device_name": "UNKNOWN_DEVICE_4d8` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_5158be02` | 15 | 1.00 | `{"device_id": "5158be02", "device_name": "UNKNOWN_DEVICE_515` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_518ac74e` | 15 | 1.00 | `{"device_id": "518ac74e", "device_name": "UNKNOWN_DEVICE_518` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_518ae138` | 15 | 1.00 | `{"device_id": "518ae138", "device_name": "UNKNOWN_DEVICE_518` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_5D192C` | 15 | 1.00 | `{"device_id": "5D192C", "device_name": "UNKNOWN_DEVICE_5D192` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_5c694f` | 15 | 1.00 | `{"device_id": "5c694f", "device_name": "UNKNOWN_DEVICE_5c694` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_60134432` | 15 | 1.00 | `{"device_id": "60134432", "device_name": "UNKNOWN_DEVICE_601` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_6015fcd3` | 15 | 1.00 | `{"device_id": "6015fcd3", "device_name": "UNKNOWN_DEVICE_601` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_60323976` | 15 | 1.00 | `{"device_id": "60323976", "device_name": "UNKNOWN_DEVICE_603` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_603245bc` | 15 | 1.00 | `{"device_id": "603245bc", "device_name": "UNKNOWN_DEVICE_603` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_6047b8f1` | 15 | 1.00 | `{"device_id": "6047b8f1", "device_name": "UNKNOWN_DEVICE_604` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_6047c16c` | 15 | 1.00 | `{"device_id": "6047c16c", "device_name": "UNKNOWN_DEVICE_604` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_618ec1c3` | 15 | 1.00 | `{"device_id": "618ec1c3", "device_name": "UNKNOWN_DEVICE_618` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_6cc66de1` | 15 | 1.00 | `{"device_id": "6cc66de1", "device_name": "UNKNOWN_DEVICE_6cc` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_6de9270a` | 15 | 1.00 | `{"device_id": "6de9270a", "device_name": "UNKNOWN_DEVICE_6de` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_711087` | 15 | 1.00 | `{"device_id": "711087", "device_name": "UNKNOWN_DEVICE_71108` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_7115F9` | 15 | 1.00 | `{"device_id": "7115F9", "device_name": "UNKNOWN_DEVICE_7115F` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_82a6d4a2` | 15 | 1.00 | `{"device_id": "82a6d4a2", "device_name": "UNKNOWN_DEVICE_82a` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_8476f145` | 15 | 1.00 | `{"device_id": "8476f145", "device_name": "UNKNOWN_DEVICE_847` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_84a25401` | 15 | 1.00 | `{"device_id": "84a25401", "device_name": "UNKNOWN_DEVICE_84a` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_8d2a007c` | 15 | 1.00 | `{"device_id": "8d2a007c", "device_name": "UNKNOWN_DEVICE_8d2` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_8d9010c3` | 15 | 1.00 | `{"device_id": "8d9010c3", "device_name": "UNKNOWN_DEVICE_8d9` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_90b661d2` | 15 | 1.00 | `{"device_id": "90b661d2", "device_name": "UNKNOWN_DEVICE_90b` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_90c7cd80` | 15 | 1.00 | `{"device_id": "90c7cd80", "device_name": "UNKNOWN_DEVICE_90c` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_91856947` | 15 | 1.00 | `{"device_id": "91856947", "device_name": "UNKNOWN_DEVICE_918` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_91856952` | 15 | 1.00 | `{"device_id": "91856952", "device_name": "UNKNOWN_DEVICE_918` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_9185695a` | 15 | 1.00 | `{"device_id": "9185695a", "device_name": "UNKNOWN_DEVICE_918` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_9380c87d` | 15 | 1.00 | `{"device_id": "9380c87d", "device_name": "UNKNOWN_DEVICE_938` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_95b483a8` | 15 | 1.00 | `{"device_id": "95b483a8", "device_name": "UNKNOWN_DEVICE_95b` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_95b483c2` | 15 | 1.00 | `{"device_id": "95b483c2", "device_name": "UNKNOWN_DEVICE_95b` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_9678a4d3` | 15 | 1.00 | `{"device_id": "9678a4d3", "device_name": "UNKNOWN_DEVICE_967` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_9678a5d9` | 15 | 1.00 | `{"device_id": "9678a5d9", "device_name": "UNKNOWN_DEVICE_967` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_9678a5de` | 15 | 1.00 | `{"device_id": "9678a5de", "device_name": "UNKNOWN_DEVICE_967` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_9678b3c5` | 15 | 1.00 | `{"device_id": "9678b3c5", "device_name": "UNKNOWN_DEVICE_967` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_97aaa145` | 15 | 1.00 | `{"device_id": "97aaa145", "device_name": "UNKNOWN_DEVICE_97a` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_97cb4dcd` | 15 | 1.00 | `{"device_id": "97cb4dcd", "device_name": "UNKNOWN_DEVICE_97c` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_97da6e73` | 15 | 1.00 | `{"device_id": "97da6e73", "device_name": "UNKNOWN_DEVICE_97d` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_97e5424a` | 15 | 1.00 | `{"device_id": "97e5424a", "device_name": "UNKNOWN_DEVICE_97e` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_97e542a2` | 15 | 1.00 | `{"device_id": "97e542a2", "device_name": "UNKNOWN_DEVICE_97e` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_A2AAC5` | 15 | 1.00 | `{"device_id": "A2AAC5", "device_name": "UNKNOWN_DEVICE_A2AAC` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_A2AE30` | 15 | 1.00 | `{"device_id": "A2AE30", "device_name": "UNKNOWN_DEVICE_A2AE3` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_ae3f13` | 15 | 1.00 | `{"device_id": "ae3f13", "device_name": "UNKNOWN_DEVICE_ae3f1` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_bb690ff6` | 15 | 1.00 | `{"device_id": "bb690ff6", "device_name": "UNKNOWN_DEVICE_bb6` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_bdc635` | 15 | 1.00 | `{"device_id": "bdc635", "device_name": "UNKNOWN_DEVICE_bdc63` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_c419382b` | 15 | 1.00 | `{"device_id": "c419382b", "device_name": "UNKNOWN_DEVICE_c41` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_c4193833` | 15 | 1.00 | `{"device_id": "c4193833", "device_name": "UNKNOWN_DEVICE_c41` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_c4d92592` | 15 | 1.00 | `{"device_id": "c4d92592", "device_name": "UNKNOWN_DEVICE_c4d` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_c5b9e68a` | 15 | 1.00 | `{"device_id": "c5b9e68a", "device_name": "UNKNOWN_DEVICE_c5b` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_c62bd46a` | 15 | 1.00 | `{"device_id": "c62bd46a", "device_name": "UNKNOWN_DEVICE_c62` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_c7011b5d` | 15 | 1.00 | `{"device_id": "c7011b5d", "device_name": "UNKNOWN_DEVICE_c70` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_c7011b61` | 15 | 1.00 | `{"device_id": "c7011b61", "device_name": "UNKNOWN_DEVICE_c70` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_c7011be0` | 15 | 1.00 | `{"device_id": "c7011be0", "device_name": "UNKNOWN_DEVICE_c70` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_c97da6e7` | 15 | 1.00 | `{"device_id": "c97da6e7", "device_name": "UNKNOWN_DEVICE_c97` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_d1533525` | 15 | 1.00 | `{"device_id": "d1533525", "device_name": "UNKNOWN_DEVICE_d15` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_d1c69de6` | 15 | 1.00 | `{"device_id": "d1c69de6", "device_name": "UNKNOWN_DEVICE_d1c` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_d1c69df3` | 15 | 1.00 | `{"device_id": "d1c69df3", "device_name": "UNKNOWN_DEVICE_d1c` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_d1cd32bb` | 15 | 1.00 | `{"device_id": "d1cd32bb", "device_name": "UNKNOWN_DEVICE_d1c` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_d1cd3322` | 15 | 1.00 | `{"device_id": "d1cd3322", "device_name": "UNKNOWN_DEVICE_d1c` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_d23c8aa6` | 15 | 1.00 | `{"device_id": "d23c8aa6", "device_name": "UNKNOWN_DEVICE_d23` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_d97e5424` | 15 | 1.00 | `{"device_id": "d97e5424", "device_name": "UNKNOWN_DEVICE_d97` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_dc7011b6` | 15 | 1.00 | `{"device_id": "dc7011b6", "device_name": "UNKNOWN_DEVICE_dc7` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_e04b7840` | 15 | 1.00 | `{"device_id": "e04b7840", "device_name": "UNKNOWN_DEVICE_e04` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_ec7011be` | 15 | 1.00 | `{"device_id": "ec7011be", "device_name": "UNKNOWN_DEVICE_ec7` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_ecbbd8` | 15 | 1.00 | `{"device_id": "ecbbd8", "device_name": "UNKNOWN_DEVICE_ecbbd` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_fa9288` | 15 | 1.00 | `{"device_id": "fa9288", "device_name": "UNKNOWN_DEVICE_fa928` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_fa9344` | 15 | 1.00 | `{"device_id": "fa9344", "device_name": "UNKNOWN_DEVICE_fa934` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_fa9359` | 15 | 1.00 | `{"device_id": "fa9359", "device_name": "UNKNOWN_DEVICE_fa935` |
| `KTBMES/TWIX/sensors/other_pressure_sensors/UNKNOWN_DEVICE_fa936d` | 15 | 1.00 | `{"device_id": "fa936d", "device_name": "UNKNOWN_DEVICE_fa936` |

### Payload Analysis

Payloads appear to be **JSON objects**.
Keys observed: `battery_ok`, `centrifugal_acc`, `channel`, `code`, `device_id`, `device_name`, `flags`, `freq`, `has_tick`, `humidity`, `learn`, `maybe_battery`, `mic`, `mod`, `moving`, `noise`, `pressure_PSI`, `pressure_kPa`, `pressure_psi`, `protocol_description`, `protocol_id`, `protocol_name`, `repeat`, `rssi`, `snr`, `state`, `status`, `temperature_C`, `temperature_F`, `tick`, `time`, `time_last_published_iso`, `time_last_published_ts`, `time_last_seen_iso`, `time_last_seen_ts`, `unknown`, `unknown_3`, `wheel`

**Recent samples:**

```json
{"device_id": "c5b9e68a", "device_name": "UNKNOWN_DEVICE_c5b9e68a", "protocol_id": "186", "protocol_name": "Hyundai TPMS", "protocol_description": "Hyundai TPMS (VDO)", "temperature_C": 24.0, "temperature_F": 75.2, "humidity": -999.0, "battery_ok": -1, "channel": "-1", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CRC", "mod": "NO_MOD", "time": "2026-03-14 17:49:27", "time_last_seen_ts": 1773535771.918669, "time_last_seen_iso": "2026-03-14T17:49:31.918669", "time_last_published_ts": 1774559916.587198, "time_last_published_iso": "2026-03-26T14:18:36.587198", "state": "223", "flags": "0", "repeat": "10", "pressure_kPa": "140.25", "pressure_psi": "20.341542716661845", "maybe_battery": "44"}
```
```json
{"device_id": "0FD5D9D", "device_name": "UNKNOWN_DEVICE_0FD5D9D", "protocol_id": "60", "protocol_name": "Schrader TPMS", "protocol_description": "Schrader TPMS", "temperature_C": 19.0, "temperature_F": 66.2, "humidity": -999.0, "battery_ok": -1, "channel": "-1", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CRC", "mod": "NO_MOD", "time": "2026-03-14 18:24:24", "time_last_seen_ts": 1773537869.111689, "time_last_seen_iso": "2026-03-14T18:24:29.111689", "time_last_published_ts": 1774559916.587414, "time_last_published_iso": "2026-03-26T14:18:36.587414", "flags": "26", "pressure_kPa": "427.5", "pressure_psi": "62.003632879664444"}
```
```json
{"device_id": "0FD5E41", "device_name": "UNKNOWN_DEVICE_0FD5E41", "protocol_id": "60", "protocol_name": "Schrader TPMS", "protocol_description": "Schrader TPMS", "temperature_C": 38.0, "temperature_F": 100.4, "humidity": -999.0, "battery_ok": -1, "channel": "-1", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CRC", "mod": "NO_MOD", "time": "2026-03-17 17:46:02", "time_last_seen_ts": 1773794764.920511, "time_last_seen_iso": "2026-03-17T17:46:04.920511", "time_last_published_ts": 1774559916.587456, "time_last_published_iso": "2026-03-26T14:18:36.587456", "flags": "25", "pressure_kPa": "542.5", "pressure_psi": "78.68297271863851"}
```

---

## Unknown Other Sensors

**Subscription:** `KTBMES/TWIX/sensors/unknown_other_sensors/#`
**Messages received:** 5503
**Unique sub-topics:** 401
**Group message rate:** 366.9 msg/min

### Sub-topics

| Sub-topic | Count | Rate (msg/min) | Sample Value |
|-----------|-------|----------------|--------------|
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-101582540` | 15 | 1.00 | `{"device_id": "-101582540", "device_name": "UNKNOWN_DEVICE_-` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-104065491` | 15 | 1.00 | `{"device_id": "-104065491", "device_name": "UNKNOWN_DEVICE_-` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-104066653` | 15 | 1.00 | `{"device_id": "-104066653", "device_name": "UNKNOWN_DEVICE_-` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-120442712` | 15 | 1.00 | `{"device_id": "-120442712", "device_name": "UNKNOWN_DEVICE_-` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-122506053` | 15 | 1.00 | `{"device_id": "-122506053", "device_name": "UNKNOWN_DEVICE_-` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-126394074` | 15 | 1.00 | `{"device_id": "-126394074", "device_name": "UNKNOWN_DEVICE_-` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-130804730` | 15 | 1.00 | `{"device_id": "-130804730", "device_name": "UNKNOWN_DEVICE_-` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-130869414` | 15 | 1.00 | `{"device_id": "-130869414", "device_name": "UNKNOWN_DEVICE_-` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-130875747` | 15 | 1.00 | `{"device_id": "-130875747", "device_name": "UNKNOWN_DEVICE_-` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-131048632` | 15 | 1.00 | `{"device_id": "-131048632", "device_name": "UNKNOWN_DEVICE_-` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-95156642` | 15 | 1.00 | `{"device_id": "-95156642", "device_name": "UNKNOWN_DEVICE_-9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-95750547` | 18 | 1.20 | `{"device_id": "-95750547", "device_name": "UNKNOWN_DEVICE_-9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-95798710` | 15 | 1.00 | `{"device_id": "-95798710", "device_name": "UNKNOWN_DEVICE_-9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_-95926768` | 15 | 1.00 | `{"device_id": "-95926768", "device_name": "UNKNOWN_DEVICE_-9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_003A48B` | 18 | 1.20 | `{"device_id": "003A48B", "device_name": "UNKNOWN_DEVICE_003A` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_003A48C` | 18 | 1.20 | `{"device_id": "003A48C", "device_name": "UNKNOWN_DEVICE_003A` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_003A48D` | 18 | 1.20 | `{"device_id": "003A48D", "device_name": "UNKNOWN_DEVICE_003A` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_008E137` | 15 | 1.00 | `{"device_id": "008E137", "device_name": "UNKNOWN_DEVICE_008E` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_012a5b5f` | 15 | 1.00 | `{"device_id": "012a5b5f", "device_name": "UNKNOWN_DEVICE_012` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_01439002` | 15 | 1.00 | `{"device_id": "01439002", "device_name": "UNKNOWN_DEVICE_014` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0149e9bb` | 15 | 1.00 | `{"device_id": "0149e9bb", "device_name": "UNKNOWN_DEVICE_014` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_01fd3604` | 15 | 1.00 | `{"device_id": "01fd3604", "device_name": "UNKNOWN_DEVICE_01f` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0206c7` | 18 | 1.20 | `{"device_id": "0206c7", "device_name": "UNKNOWN_DEVICE_0206c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_02320aad` | 15 | 1.00 | `{"device_id": "02320aad", "device_name": "UNKNOWN_DEVICE_023` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_02320ac9` | 15 | 1.00 | `{"device_id": "02320ac9", "device_name": "UNKNOWN_DEVICE_023` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_026694d0` | 15 | 1.00 | `{"device_id": "026694d0", "device_name": "UNKNOWN_DEVICE_026` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_026a1963` | 15 | 1.00 | `{"device_id": "026a1963", "device_name": "UNKNOWN_DEVICE_026` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_028a292e` | 15 | 1.00 | `{"device_id": "028a292e", "device_name": "UNKNOWN_DEVICE_028` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_028b7932` | 15 | 1.00 | `{"device_id": "028b7932", "device_name": "UNKNOWN_DEVICE_028` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_028b793c` | 15 | 1.00 | `{"device_id": "028b793c", "device_name": "UNKNOWN_DEVICE_028` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_028b7960` | 15 | 1.00 | `{"device_id": "028b7960", "device_name": "UNKNOWN_DEVICE_028` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_02CB4BD` | 15 | 1.00 | `{"device_id": "02CB4BD", "device_name": "UNKNOWN_DEVICE_02CB` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_02E06BA` | 15 | 1.00 | `{"device_id": "02E06BA", "device_name": "UNKNOWN_DEVICE_02E0` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_02E0B2B` | 15 | 1.00 | `{"device_id": "02E0B2B", "device_name": "UNKNOWN_DEVICE_02E0` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_03D91EE` | 15 | 1.00 | `{"device_id": "03D91EE", "device_name": "UNKNOWN_DEVICE_03D9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_03D9290` | 18 | 1.20 | `{"device_id": "03D9290", "device_name": "UNKNOWN_DEVICE_03D9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0473DD0` | 15 | 1.00 | `{"device_id": "0473DD0", "device_name": "UNKNOWN_DEVICE_0473` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_05417DE` | 15 | 1.00 | `{"device_id": "05417DE", "device_name": "UNKNOWN_DEVICE_0541` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_054266B` | 15 | 1.00 | `{"device_id": "054266B", "device_name": "UNKNOWN_DEVICE_0542` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_05C5C99` | 15 | 1.00 | `{"device_id": "05C5C99", "device_name": "UNKNOWN_DEVICE_05C5` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_08ea6b15` | 18 | 1.20 | `{"device_id": "08ea6b15", "device_name": "UNKNOWN_DEVICE_08e` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_092233` | 15 | 1.00 | `{"device_id": "092233", "device_name": "UNKNOWN_DEVICE_09223` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_09D6127` | 18 | 1.20 | `{"device_id": "09D6127", "device_name": "UNKNOWN_DEVICE_09D6` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_09D68A3` | 18 | 1.20 | `{"device_id": "09D68A3", "device_name": "UNKNOWN_DEVICE_09D6` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_09F19E8` | 15 | 1.00 | `{"device_id": "09F19E8", "device_name": "UNKNOWN_DEVICE_09F1` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0A1A899` | 15 | 1.00 | `{"device_id": "0A1A899", "device_name": "UNKNOWN_DEVICE_0A1A` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0A213F0` | 15 | 1.00 | `{"device_id": "0A213F0", "device_name": "UNKNOWN_DEVICE_0A21` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0A219B9` | 18 | 1.20 | `{"device_id": "0A219B9", "device_name": "UNKNOWN_DEVICE_0A21` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0A22847` | 3 | 0.20 | `{"device_id": "0A22847", "device_name": "UNKNOWN_DEVICE_0A22` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0DC06B6` | 18 | 1.20 | `{"device_id": "0DC06B6", "device_name": "UNKNOWN_DEVICE_0DC0` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0E4329A` | 15 | 1.00 | `{"device_id": "0E4329A", "device_name": "UNKNOWN_DEVICE_0E43` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0F3B32C` | 3 | 0.20 | `{"device_id": "0F3B32C", "device_name": "UNKNOWN_DEVICE_0F3B` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0F3CD35` | 18 | 1.20 | `{"device_id": "0F3CD35", "device_name": "UNKNOWN_DEVICE_0F3C` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0FD5253` | 3 | 0.20 | `{"device_id": "0FD5253", "device_name": "UNKNOWN_DEVICE_0FD5` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0FD5E41` | 3 | 0.20 | `{"device_id": "0FD5E41", "device_name": "UNKNOWN_DEVICE_0FD5` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0FD62D4` | 18 | 1.20 | `{"device_id": "0FD62D4", "device_name": "UNKNOWN_DEVICE_0FD6` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0b221a` | 18 | 1.20 | `{"device_id": "0b221a", "device_name": "UNKNOWN_DEVICE_0b221` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0b9f450f` | 3 | 0.20 | `{"device_id": "0b9f450f", "device_name": "UNKNOWN_DEVICE_0b9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0b9f454e` | 3 | 0.20 | `{"device_id": "0b9f454e", "device_name": "UNKNOWN_DEVICE_0b9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0bb690ff` | 3 | 0.20 | `{"device_id": "0bb690ff", "device_name": "UNKNOWN_DEVICE_0bb` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0bc0e980` | 3 | 0.20 | `{"device_id": "0bc0e980", "device_name": "UNKNOWN_DEVICE_0bc` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0c6907` | 15 | 1.00 | `{"device_id": "0c6907", "device_name": "UNKNOWN_DEVICE_0c690` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0c69071b` | 15 | 1.00 | `{"device_id": "0c69071b", "device_name": "UNKNOWN_DEVICE_0c6` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0caee756` | 15 | 1.00 | `{"device_id": "0caee756", "device_name": "UNKNOWN_DEVICE_0ca` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0cda323b` | 18 | 1.20 | `{"device_id": "0cda323b", "device_name": "UNKNOWN_DEVICE_0cd` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0d3b0d5a` | 18 | 1.20 | `{"device_id": "0d3b0d5a", "device_name": "UNKNOWN_DEVICE_0d3` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0e04b7` | 3 | 0.20 | `{"device_id": "0e04b7", "device_name": "UNKNOWN_DEVICE_0e04b` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0e04b784` | 3 | 0.20 | `{"device_id": "0e04b784", "device_name": "UNKNOWN_DEVICE_0e0` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0e04b785` | 3 | 0.20 | `{"device_id": "0e04b785", "device_name": "UNKNOWN_DEVICE_0e0` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0e04b788` | 3 | 0.20 | `{"device_id": "0e04b788", "device_name": "UNKNOWN_DEVICE_0e0` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0e04b78e` | 3 | 0.20 | `{"device_id": "0e04b78e", "device_name": "UNKNOWN_DEVICE_0e0` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_0f9c3e08` | 15 | 1.00 | `{"device_id": "0f9c3e08", "device_name": "UNKNOWN_DEVICE_0f9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1` | 15 | 1.00 | `{"device_id": "1", "device_name": "UNKNOWN_DEVICE_1", "proto` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_100AC07` | 15 | 1.00 | `{"device_id": "100AC07", "device_name": "UNKNOWN_DEVICE_100A` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_102103` | 15 | 1.00 | `{"device_id": "102103", "device_name": "UNKNOWN_DEVICE_10210` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_106` | 18 | 1.20 | `{"device_id": "106", "device_name": "UNKNOWN_DEVICE_106", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_107` | 18 | 1.20 | `{"device_id": "107", "device_name": "UNKNOWN_DEVICE_107", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_11` | 3 | 0.20 | `{"device_id": "11", "device_name": "UNKNOWN_DEVICE_11", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_113` | 15 | 1.00 | `{"device_id": "113", "device_name": "UNKNOWN_DEVICE_113", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_114` | 18 | 1.20 | `{"device_id": "114", "device_name": "UNKNOWN_DEVICE_114", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_116` | 3 | 0.20 | `{"device_id": "116", "device_name": "UNKNOWN_DEVICE_116", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_120` | 18 | 1.20 | `{"device_id": "120", "device_name": "UNKNOWN_DEVICE_120", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_120e1244` | 18 | 1.20 | `{"device_id": "120e1244", "device_name": "UNKNOWN_DEVICE_120` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_120e127c` | 18 | 1.20 | `{"device_id": "120e127c", "device_name": "UNKNOWN_DEVICE_120` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_121` | 18 | 1.20 | `{"device_id": "121", "device_name": "UNKNOWN_DEVICE_121", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_122` | 18 | 1.20 | `{"device_id": "122", "device_name": "UNKNOWN_DEVICE_122", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1229f56d` | 18 | 1.20 | `{"device_id": "1229f56d", "device_name": "UNKNOWN_DEVICE_122` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_125` | 15 | 1.00 | `{"device_id": "125", "device_name": "UNKNOWN_DEVICE_125", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_127` | 18 | 1.20 | `{"device_id": "127", "device_name": "UNKNOWN_DEVICE_127", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_128` | 3 | 0.20 | `{"device_id": "128", "device_name": "UNKNOWN_DEVICE_128", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_12860B9` | 15 | 1.00 | `{"device_id": "12860B9", "device_name": "UNKNOWN_DEVICE_1286` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_129` | 3 | 0.20 | `{"device_id": "129", "device_name": "UNKNOWN_DEVICE_129", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_12d81575` | 15 | 1.00 | `{"device_id": "12d81575", "device_name": "UNKNOWN_DEVICE_12d` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_12da4542` | 15 | 1.00 | `{"device_id": "12da4542", "device_name": "UNKNOWN_DEVICE_12d` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_13` | 3 | 0.20 | `{"device_id": "13", "device_name": "UNKNOWN_DEVICE_13", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_130` | 3 | 0.20 | `{"device_id": "130", "device_name": "UNKNOWN_DEVICE_130", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1301556928` | 18 | 1.20 | `{"device_id": "1301556928", "device_name": "UNKNOWN_DEVICE_1` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_132` | 3 | 0.20 | `{"device_id": "132", "device_name": "UNKNOWN_DEVICE_132", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_133` | 18 | 1.20 | `{"device_id": "133", "device_name": "UNKNOWN_DEVICE_133", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_134` | 3 | 0.20 | `{"device_id": "134", "device_name": "UNKNOWN_DEVICE_134", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_136` | 18 | 1.20 | `{"device_id": "136", "device_name": "UNKNOWN_DEVICE_136", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_137` | 15 | 1.00 | `{"device_id": "137", "device_name": "UNKNOWN_DEVICE_137", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_139` | 15 | 1.00 | `{"device_id": "139", "device_name": "UNKNOWN_DEVICE_139", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_13AEEC7` | 15 | 1.00 | `{"device_id": "13AEEC7", "device_name": "UNKNOWN_DEVICE_13AE` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_14` | 3 | 0.20 | `{"device_id": "14", "device_name": "UNKNOWN_DEVICE_14", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_140` | 3 | 0.20 | `{"device_id": "140", "device_name": "UNKNOWN_DEVICE_140", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_143` | 18 | 1.20 | `{"device_id": "143", "device_name": "UNKNOWN_DEVICE_143", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1431655722` | 18 | 1.20 | `{"device_id": "1431655722", "device_name": "UNKNOWN_DEVICE_1` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_144` | 18 | 1.20 | `{"device_id": "144", "device_name": "UNKNOWN_DEVICE_144", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_147` | 15 | 1.00 | `{"device_id": "147", "device_name": "UNKNOWN_DEVICE_147", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_14860` | 15 | 1.00 | `{"device_id": "14860", "device_name": "UNKNOWN_DEVICE_14860"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_149` | 15 | 1.00 | `{"device_id": "149", "device_name": "UNKNOWN_DEVICE_149", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_15` | 3 | 0.20 | `{"device_id": "15", "device_name": "UNKNOWN_DEVICE_15", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_152` | 15 | 1.00 | `{"device_id": "152", "device_name": "UNKNOWN_DEVICE_152", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_154` | 15 | 1.00 | `{"device_id": "154", "device_name": "UNKNOWN_DEVICE_154", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_157` | 15 | 1.00 | `{"device_id": "157", "device_name": "UNKNOWN_DEVICE_157", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1591` | 15 | 1.00 | `{"device_id": "1591", "device_name": "UNKNOWN_DEVICE_1591", ` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1599676` | 18 | 1.20 | `{"device_id": "1599676", "device_name": "UNKNOWN_DEVICE_1599` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_159ABAD` | 18 | 1.20 | `{"device_id": "159ABAD", "device_name": "UNKNOWN_DEVICE_159A` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_16` | 18 | 1.20 | `{"device_id": "16", "device_name": "UNKNOWN_DEVICE_16", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_160` | 3 | 0.20 | `{"device_id": "160", "device_name": "UNKNOWN_DEVICE_160", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_161` | 3 | 0.20 | `{"device_id": "161", "device_name": "UNKNOWN_DEVICE_161", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1623D74` | 15 | 1.00 | `{"device_id": "1623D74", "device_name": "UNKNOWN_DEVICE_1623` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_164` | 15 | 1.00 | `{"device_id": "164", "device_name": "UNKNOWN_DEVICE_164", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_167` | 18 | 1.20 | `{"device_id": "167", "device_name": "UNKNOWN_DEVICE_167", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_168` | 3 | 0.20 | `{"device_id": "168", "device_name": "UNKNOWN_DEVICE_168", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_17` | 3 | 0.20 | `{"device_id": "17", "device_name": "UNKNOWN_DEVICE_17", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_170` | 3 | 0.20 | `{"device_id": "170", "device_name": "UNKNOWN_DEVICE_170", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_171` | 15 | 1.00 | `{"device_id": "171", "device_name": "UNKNOWN_DEVICE_171", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_174` | 18 | 1.20 | `{"device_id": "174", "device_name": "UNKNOWN_DEVICE_174", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1780BFF` | 18 | 1.20 | `{"device_id": "1780BFF", "device_name": "UNKNOWN_DEVICE_1780` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_17870` | 15 | 1.00 | `{"device_id": "17870", "device_name": "UNKNOWN_DEVICE_17870"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_18` | 18 | 1.20 | `{"device_id": "18", "device_name": "UNKNOWN_DEVICE_18", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_181` | 15 | 1.00 | `{"device_id": "181", "device_name": "UNKNOWN_DEVICE_181", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_184` | 18 | 1.20 | `{"device_id": "184", "device_name": "UNKNOWN_DEVICE_184", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_189` | 18 | 1.20 | `{"device_id": "189", "device_name": "UNKNOWN_DEVICE_189", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1893745a` | 18 | 1.20 | `{"device_id": "1893745a", "device_name": "UNKNOWN_DEVICE_189` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_18971a22` | 18 | 1.20 | `{"device_id": "18971a22", "device_name": "UNKNOWN_DEVICE_189` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_18971a2c` | 18 | 1.20 | `{"device_id": "18971a2c", "device_name": "UNKNOWN_DEVICE_189` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_18974a1c` | 18 | 1.20 | `{"device_id": "18974a1c", "device_name": "UNKNOWN_DEVICE_189` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_19` | 18 | 1.20 | `{"device_id": "19", "device_name": "UNKNOWN_DEVICE_19", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_192` | 18 | 1.20 | `{"device_id": "192", "device_name": "UNKNOWN_DEVICE_192", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_193` | 3 | 0.20 | `{"device_id": "193", "device_name": "UNKNOWN_DEVICE_193", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_195` | 3 | 0.20 | `{"device_id": "195", "device_name": "UNKNOWN_DEVICE_195", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_197` | 3 | 0.20 | `{"device_id": "197", "device_name": "UNKNOWN_DEVICE_197", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_198` | 4 | 0.27 | `{"device_id": "198", "device_name": "UNKNOWN_DEVICE_198", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_199` | 18 | 1.20 | `{"device_id": "199", "device_name": "UNKNOWN_DEVICE_199", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1CFE5C9` | 18 | 1.20 | `{"device_id": "1CFE5C9", "device_name": "UNKNOWN_DEVICE_1CFE` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1F152FA` | 15 | 1.00 | `{"device_id": "1F152FA", "device_name": "UNKNOWN_DEVICE_1F15` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1F4812F` | 15 | 1.00 | `{"device_id": "1F4812F", "device_name": "UNKNOWN_DEVICE_1F48` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_1b8dfb` | 15 | 1.00 | `{"device_id": "1b8dfb", "device_name": "UNKNOWN_DEVICE_1b8df` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_20` | 18 | 1.20 | `{"device_id": "20", "device_name": "UNKNOWN_DEVICE_20", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_200` | 3 | 0.20 | `{"device_id": "200", "device_name": "UNKNOWN_DEVICE_200", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_2014749568` | 15 | 1.00 | `{"device_id": "2014749568", "device_name": "UNKNOWN_DEVICE_2` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_2014851709` | 18 | 1.20 | `{"device_id": "2014851709", "device_name": "UNKNOWN_DEVICE_2` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_204` | 18 | 1.20 | `{"device_id": "204", "device_name": "UNKNOWN_DEVICE_204", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_2052` | 15 | 1.00 | `{"device_id": "2052", "device_name": "UNKNOWN_DEVICE_2052", ` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_20653` | 15 | 1.00 | `{"device_id": "20653", "device_name": "UNKNOWN_DEVICE_20653"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_208` | 3 | 0.20 | `{"device_id": "208", "device_name": "UNKNOWN_DEVICE_208", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_2080577009` | 15 | 1.00 | `{"device_id": "2080577009", "device_name": "UNKNOWN_DEVICE_2` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_2080702513` | 18 | 1.20 | `{"device_id": "2080702513", "device_name": "UNKNOWN_DEVICE_2` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_2080739043` | 15 | 1.00 | `{"device_id": "2080739043", "device_name": "UNKNOWN_DEVICE_2` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_20a07c5b` | 18 | 1.20 | `{"device_id": "20a07c5b", "device_name": "UNKNOWN_DEVICE_20a` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_211` | 18 | 1.20 | `{"device_id": "211", "device_name": "UNKNOWN_DEVICE_211", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_212` | 18 | 1.20 | `{"device_id": "212", "device_name": "UNKNOWN_DEVICE_212", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_212C598` | 18 | 1.20 | `{"device_id": "212C598", "device_name": "UNKNOWN_DEVICE_212C` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_21799` | 15 | 1.00 | `{"device_id": "21799", "device_name": "UNKNOWN_DEVICE_21799"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_218` | 3 | 0.20 | `{"device_id": "218", "device_name": "UNKNOWN_DEVICE_218", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_219b5187` | 15 | 1.00 | `{"device_id": "219b5187", "device_name": "UNKNOWN_DEVICE_219` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_21a7fe1f` | 18 | 1.20 | `{"device_id": "21a7fe1f", "device_name": "UNKNOWN_DEVICE_21a` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_21a81239` | 18 | 1.20 | `{"device_id": "21a81239", "device_name": "UNKNOWN_DEVICE_21a` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_21b68f09` | 15 | 1.00 | `{"device_id": "21b68f09", "device_name": "UNKNOWN_DEVICE_21b` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_22` | 18 | 1.20 | `{"device_id": "22", "device_name": "UNKNOWN_DEVICE_22", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_22088` | 15 | 1.00 | `{"device_id": "22088", "device_name": "UNKNOWN_DEVICE_22088"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_221` | 15 | 1.00 | `{"device_id": "221", "device_name": "UNKNOWN_DEVICE_221", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_223819` | 18 | 1.20 | `{"device_id": "223819", "device_name": "UNKNOWN_DEVICE_22381` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_223828` | 18 | 1.20 | `{"device_id": "223828", "device_name": "UNKNOWN_DEVICE_22382` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_223858` | 18 | 1.20 | `{"device_id": "223858", "device_name": "UNKNOWN_DEVICE_22385` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_227` | 18 | 1.20 | `{"device_id": "227", "device_name": "UNKNOWN_DEVICE_227", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_229` | 18 | 1.20 | `{"device_id": "229", "device_name": "UNKNOWN_DEVICE_229", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_23` | 3 | 0.20 | `{"device_id": "23", "device_name": "UNKNOWN_DEVICE_23", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_232` | 15 | 1.00 | `{"device_id": "232", "device_name": "UNKNOWN_DEVICE_232", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_234` | 28 | 1.87 | `{"device_id": "234", "device_name": "UNKNOWN_DEVICE_234", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_237` | 18 | 1.20 | `{"device_id": "237", "device_name": "UNKNOWN_DEVICE_237", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_238` | 15 | 1.00 | `{"device_id": "238", "device_name": "UNKNOWN_DEVICE_238", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_23F775` | 15 | 1.00 | `{"device_id": "23F775", "device_name": "UNKNOWN_DEVICE_23F77` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_240` | 3 | 0.20 | `{"device_id": "240", "device_name": "UNKNOWN_DEVICE_240", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_242` | 18 | 1.20 | `{"device_id": "242", "device_name": "UNKNOWN_DEVICE_242", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_243` | 15 | 1.00 | `{"device_id": "243", "device_name": "UNKNOWN_DEVICE_243", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_252` | 3 | 0.20 | `{"device_id": "252", "device_name": "UNKNOWN_DEVICE_252", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_255` | 3 | 0.20 | `{"device_id": "255", "device_name": "UNKNOWN_DEVICE_255", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_26` | 3 | 0.20 | `{"device_id": "26", "device_name": "UNKNOWN_DEVICE_26", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_27` | 3 | 0.20 | `{"device_id": "27", "device_name": "UNKNOWN_DEVICE_27", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_279` | 15 | 1.00 | `{"device_id": "279", "device_name": "UNKNOWN_DEVICE_279", "p` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_28` | 3 | 0.20 | `{"device_id": "28", "device_name": "UNKNOWN_DEVICE_28", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_29` | 3 | 0.20 | `{"device_id": "29", "device_name": "UNKNOWN_DEVICE_29", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_3` | 3 | 0.20 | `{"device_id": "3", "device_name": "UNKNOWN_DEVICE_3", "proto` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_30` | 3 | 0.20 | `{"device_id": "30", "device_name": "UNKNOWN_DEVICE_30", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_3021a7fe` | 18 | 1.20 | `{"device_id": "3021a7fe", "device_name": "UNKNOWN_DEVICE_302` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_32` | 18 | 1.20 | `{"device_id": "32", "device_name": "UNKNOWN_DEVICE_32", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_3215` | 15 | 1.00 | `{"device_id": "3215", "device_name": "UNKNOWN_DEVICE_3215", ` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_33` | 18 | 1.20 | `{"device_id": "33", "device_name": "UNKNOWN_DEVICE_33", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_33083` | 15 | 1.00 | `{"device_id": "33083", "device_name": "UNKNOWN_DEVICE_33083"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_34` | 3 | 0.20 | `{"device_id": "34", "device_name": "UNKNOWN_DEVICE_34", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_3445` | 15 | 1.00 | `{"device_id": "3445", "device_name": "UNKNOWN_DEVICE_3445", ` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_34819` | 15 | 1.00 | `{"device_id": "34819", "device_name": "UNKNOWN_DEVICE_34819"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_35` | 18 | 1.20 | `{"device_id": "35", "device_name": "UNKNOWN_DEVICE_35", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_36` | 3 | 0.20 | `{"device_id": "36", "device_name": "UNKNOWN_DEVICE_36", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_3650c0` | 18 | 1.20 | `{"device_id": "3650c0", "device_name": "UNKNOWN_DEVICE_3650c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_37` | 15 | 1.00 | `{"device_id": "37", "device_name": "UNKNOWN_DEVICE_37", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_37509` | 15 | 1.00 | `{"device_id": "37509", "device_name": "UNKNOWN_DEVICE_37509"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_38` | 3 | 0.20 | `{"device_id": "38", "device_name": "UNKNOWN_DEVICE_38", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_39` | 15 | 1.00 | `{"device_id": "39", "device_name": "UNKNOWN_DEVICE_39", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_396605` | 15 | 1.00 | `{"device_id": "396605", "device_name": "UNKNOWN_DEVICE_39660` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4` | 3 | 0.20 | `{"device_id": "4", "device_name": "UNKNOWN_DEVICE_4", "proto` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_40` | 18 | 1.20 | `{"device_id": "40", "device_name": "UNKNOWN_DEVICE_40", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_401d30b1` | 15 | 1.00 | `{"device_id": "401d30b1", "device_name": "UNKNOWN_DEVICE_401` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_40725` | 15 | 1.00 | `{"device_id": "40725", "device_name": "UNKNOWN_DEVICE_40725"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_41` | 3 | 0.20 | `{"device_id": "41", "device_name": "UNKNOWN_DEVICE_41", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4120e124` | 18 | 1.20 | `{"device_id": "4120e124", "device_name": "UNKNOWN_DEVICE_412` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4167a04e` | 15 | 1.00 | `{"device_id": "4167a04e", "device_name": "UNKNOWN_DEVICE_416` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_42` | 3 | 0.20 | `{"device_id": "42", "device_name": "UNKNOWN_DEVICE_42", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_43` | 15 | 1.00 | `{"device_id": "43", "device_name": "UNKNOWN_DEVICE_43", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_44` | 14 | 0.93 | `{"device_id": "44", "device_name": "UNKNOWN_DEVICE_44", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4547739` | 3 | 0.20 | `{"device_id": "4547739", "device_name": "UNKNOWN_DEVICE_4547` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_46` | 15 | 1.00 | `{"device_id": "46", "device_name": "UNKNOWN_DEVICE_46", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_47631` | 15 | 1.00 | `{"device_id": "47631", "device_name": "UNKNOWN_DEVICE_47631"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4A49BF` | 15 | 1.00 | `{"device_id": "4A49BF", "device_name": "UNKNOWN_DEVICE_4A49B` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4d8fd65f` | 3 | 0.20 | `{"device_id": "4d8fd65f", "device_name": "UNKNOWN_DEVICE_4d8` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4d8fd670` | 15 | 1.00 | `{"device_id": "4d8fd670", "device_name": "UNKNOWN_DEVICE_4d8` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4d8fd758` | 18 | 1.20 | `{"device_id": "4d8fd758", "device_name": "UNKNOWN_DEVICE_4d8` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4d8fd759` | 18 | 1.20 | `{"device_id": "4d8fd759", "device_name": "UNKNOWN_DEVICE_4d8` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4db5f1de` | 15 | 1.00 | `{"device_id": "4db5f1de", "device_name": "UNKNOWN_DEVICE_4db` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_4dbcd5a2` | 15 | 1.00 | `{"device_id": "4dbcd5a2", "device_name": "UNKNOWN_DEVICE_4db` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_5` | 18 | 1.20 | `{"device_id": "5", "device_name": "UNKNOWN_DEVICE_5", "proto` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_50` | 18 | 1.20 | `{"device_id": "50", "device_name": "UNKNOWN_DEVICE_50", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_5018974a` | 18 | 1.20 | `{"device_id": "5018974a", "device_name": "UNKNOWN_DEVICE_501` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_5118974a` | 15 | 1.00 | `{"device_id": "5118974a", "device_name": "UNKNOWN_DEVICE_511` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_51309` | 15 | 1.00 | `{"device_id": "51309", "device_name": "UNKNOWN_DEVICE_51309"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_52` | 15 | 1.00 | `{"device_id": "52", "device_name": "UNKNOWN_DEVICE_52", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_5218974a` | 18 | 1.20 | `{"device_id": "5218974a", "device_name": "UNKNOWN_DEVICE_521` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_523508198` | 15 | 1.00 | `{"device_id": "523508198", "device_name": "UNKNOWN_DEVICE_52` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_523988110` | 15 | 1.00 | `{"device_id": "523988110", "device_name": "UNKNOWN_DEVICE_52` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_52576` | 15 | 1.00 | `{"device_id": "52576", "device_name": "UNKNOWN_DEVICE_52576"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_53` | 15 | 1.00 | `{"device_id": "53", "device_name": "UNKNOWN_DEVICE_53", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_5319` | 15 | 1.00 | `{"device_id": "5319", "device_name": "UNKNOWN_DEVICE_5319", ` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_5F` | 15 | 1.00 | `{"device_id": "5F", "device_name": "UNKNOWN_DEVICE_5F", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_6` | 3 | 0.20 | `{"device_id": "6", "device_name": "UNKNOWN_DEVICE_6", "proto` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_60` | 3 | 0.20 | `{"device_id": "60", "device_name": "UNKNOWN_DEVICE_60", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_600816bf` | 18 | 1.20 | `{"device_id": "600816bf", "device_name": "UNKNOWN_DEVICE_600` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_6014f965` | 15 | 1.00 | `{"device_id": "6014f965", "device_name": "UNKNOWN_DEVICE_601` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_60152dc3` | 15 | 1.00 | `{"device_id": "60152dc3", "device_name": "UNKNOWN_DEVICE_601` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_601533c9` | 15 | 1.00 | `{"device_id": "601533c9", "device_name": "UNKNOWN_DEVICE_601` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_602db295` | 15 | 1.00 | `{"device_id": "602db295", "device_name": "UNKNOWN_DEVICE_602` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_60323a64` | 15 | 1.00 | `{"device_id": "60323a64", "device_name": "UNKNOWN_DEVICE_603` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_603245eb` | 15 | 1.00 | `{"device_id": "603245eb", "device_name": "UNKNOWN_DEVICE_603` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_60433` | 15 | 1.00 | `{"device_id": "60433", "device_name": "UNKNOWN_DEVICE_60433"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_60462ea3` | 15 | 1.00 | `{"device_id": "60462ea3", "device_name": "UNKNOWN_DEVICE_604` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_606d0b68` | 15 | 1.00 | `{"device_id": "606d0b68", "device_name": "UNKNOWN_DEVICE_606` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_60732f1f` | 15 | 1.00 | `{"device_id": "60732f1f", "device_name": "UNKNOWN_DEVICE_607` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_60A8723` | 15 | 1.00 | `{"device_id": "60A8723", "device_name": "UNKNOWN_DEVICE_60A8` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_60A90C6` | 15 | 1.00 | `{"device_id": "60A90C6", "device_name": "UNKNOWN_DEVICE_60A9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_60ACBAC` | 15 | 1.00 | `{"device_id": "60ACBAC", "device_name": "UNKNOWN_DEVICE_60AC` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_61` | 15 | 1.00 | `{"device_id": "61", "device_name": "UNKNOWN_DEVICE_61", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_61769` | 15 | 1.00 | `{"device_id": "61769", "device_name": "UNKNOWN_DEVICE_61769"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_61965b22` | 18 | 1.20 | `{"device_id": "61965b22", "device_name": "UNKNOWN_DEVICE_619` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_6323741c` | 18 | 1.20 | `{"device_id": "6323741c", "device_name": "UNKNOWN_DEVICE_632` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_63237447` | 15 | 1.00 | `{"device_id": "63237447", "device_name": "UNKNOWN_DEVICE_632` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_632377d8` | 18 | 1.20 | `{"device_id": "632377d8", "device_name": "UNKNOWN_DEVICE_632` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_63237c82` | 18 | 1.20 | `{"device_id": "63237c82", "device_name": "UNKNOWN_DEVICE_632` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_63488` | 18 | 1.20 | `{"device_id": "63488", "device_name": "UNKNOWN_DEVICE_63488"` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_68` | 15 | 1.00 | `{"device_id": "68", "device_name": "UNKNOWN_DEVICE_68", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_6cc5321a` | 18 | 1.20 | `{"device_id": "6cc5321a", "device_name": "UNKNOWN_DEVICE_6cc` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_6daa4bed` | 15 | 1.00 | `{"device_id": "6daa4bed", "device_name": "UNKNOWN_DEVICE_6da` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_6f1152` | 18 | 1.20 | `{"device_id": "6f1152", "device_name": "UNKNOWN_DEVICE_6f115` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_6f11e6` | 18 | 1.20 | `{"device_id": "6f11e6", "device_name": "UNKNOWN_DEVICE_6f11e` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_6f87061c` | 15 | 1.00 | `{"device_id": "6f87061c", "device_name": "UNKNOWN_DEVICE_6f8` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_7` | 3 | 0.20 | `{"device_id": "7", "device_name": "UNKNOWN_DEVICE_7", "proto` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_70` | 18 | 1.20 | `{"device_id": "70", "device_name": "UNKNOWN_DEVICE_70", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_71` | 15 | 1.00 | `{"device_id": "71", "device_name": "UNKNOWN_DEVICE_71", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_71854fd3` | 15 | 1.00 | `{"device_id": "71854fd3", "device_name": "UNKNOWN_DEVICE_718` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_71cd8324` | 18 | 1.20 | `{"device_id": "71cd8324", "device_name": "UNKNOWN_DEVICE_71c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_71cd834b` | 18 | 1.20 | `{"device_id": "71cd834b", "device_name": "UNKNOWN_DEVICE_71c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_71d678d1` | 18 | 1.20 | `{"device_id": "71d678d1", "device_name": "UNKNOWN_DEVICE_71d` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_72` | 15 | 1.00 | `{"device_id": "72", "device_name": "UNKNOWN_DEVICE_72", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_73` | 3 | 0.20 | `{"device_id": "73", "device_name": "UNKNOWN_DEVICE_73", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_7495` | 15 | 1.00 | `{"device_id": "7495", "device_name": "UNKNOWN_DEVICE_7495", ` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_75` | 18 | 1.20 | `{"device_id": "75", "device_name": "UNKNOWN_DEVICE_75", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_7541` | 15 | 1.00 | `{"device_id": "7541", "device_name": "UNKNOWN_DEVICE_7541", ` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_7ffc1f45` | 18 | 1.20 | `{"device_id": "7ffc1f45", "device_name": "UNKNOWN_DEVICE_7ff` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8` | 18 | 1.20 | `{"device_id": "8", "device_name": "UNKNOWN_DEVICE_8", "proto` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_80` | 3 | 0.20 | `{"device_id": "80", "device_name": "UNKNOWN_DEVICE_80", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_81` | 3 | 0.20 | `{"device_id": "81", "device_name": "UNKNOWN_DEVICE_81", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_82ac411e` | 18 | 1.20 | `{"device_id": "82ac411e", "device_name": "UNKNOWN_DEVICE_82a` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_82b41753` | 18 | 1.20 | `{"device_id": "82b41753", "device_name": "UNKNOWN_DEVICE_82b` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_83` | 15 | 1.00 | `{"device_id": "83", "device_name": "UNKNOWN_DEVICE_83", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8344409d` | 18 | 1.20 | `{"device_id": "8344409d", "device_name": "UNKNOWN_DEVICE_834` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_83444973` | 15 | 1.00 | `{"device_id": "83444973", "device_name": "UNKNOWN_DEVICE_834` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_84990f47` | 18 | 1.20 | `{"device_id": "84990f47", "device_name": "UNKNOWN_DEVICE_849` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_84991109` | 18 | 1.20 | `{"device_id": "84991109", "device_name": "UNKNOWN_DEVICE_849` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_85` | 15 | 1.00 | `{"device_id": "85", "device_name": "UNKNOWN_DEVICE_85", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_85d8e4bd` | 18 | 1.20 | `{"device_id": "85d8e4bd", "device_name": "UNKNOWN_DEVICE_85d` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_88` | 15 | 1.00 | `{"device_id": "88", "device_name": "UNKNOWN_DEVICE_88", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_89` | 15 | 1.00 | `{"device_id": "89", "device_name": "UNKNOWN_DEVICE_89", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8971a2ca` | 15 | 1.00 | `{"device_id": "8971a2ca", "device_name": "UNKNOWN_DEVICE_897` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8F44E49` | 15 | 1.00 | `{"device_id": "8F44E49", "device_name": "UNKNOWN_DEVICE_8F44` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8c6c4255` | 15 | 1.00 | `{"device_id": "8c6c4255", "device_name": "UNKNOWN_DEVICE_8c6` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8c6c4546` | 15 | 1.00 | `{"device_id": "8c6c4546", "device_name": "UNKNOWN_DEVICE_8c6` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8c6ec175` | 15 | 1.00 | `{"device_id": "8c6ec175", "device_name": "UNKNOWN_DEVICE_8c6` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8d901162` | 15 | 1.00 | `{"device_id": "8d901162", "device_name": "UNKNOWN_DEVICE_8d9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8e9995bf` | 18 | 1.20 | `{"device_id": "8e9995bf", "device_name": "UNKNOWN_DEVICE_8e9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8e9995fc` | 18 | 1.20 | `{"device_id": "8e9995fc", "device_name": "UNKNOWN_DEVICE_8e9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8e999615` | 18 | 1.20 | `{"device_id": "8e999615", "device_name": "UNKNOWN_DEVICE_8e9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8ea6b154` | 18 | 1.20 | `{"device_id": "8ea6b154", "device_name": "UNKNOWN_DEVICE_8ea` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8fc813f0` | 15 | 1.00 | `{"device_id": "8fc813f0", "device_name": "UNKNOWN_DEVICE_8fc` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_8fc817d1` | 15 | 1.00 | `{"device_id": "8fc817d1", "device_name": "UNKNOWN_DEVICE_8fc` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_9` | 18 | 1.20 | `{"device_id": "9", "device_name": "UNKNOWN_DEVICE_9", "proto` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_907d48c9` | 18 | 1.20 | `{"device_id": "907d48c9", "device_name": "UNKNOWN_DEVICE_907` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_907d5619` | 18 | 1.20 | `{"device_id": "907d5619", "device_name": "UNKNOWN_DEVICE_907` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_907d5af3` | 18 | 1.20 | `{"device_id": "907d5af3", "device_name": "UNKNOWN_DEVICE_907` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_90cb572c` | 15 | 1.00 | `{"device_id": "90cb572c", "device_name": "UNKNOWN_DEVICE_90c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_9101a4e4` | 15 | 1.00 | `{"device_id": "9101a4e4", "device_name": "UNKNOWN_DEVICE_910` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_91acf4dd` | 15 | 1.00 | `{"device_id": "91acf4dd", "device_name": "UNKNOWN_DEVICE_91a` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_92` | 3 | 0.20 | `{"device_id": "92", "device_name": "UNKNOWN_DEVICE_92", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_92ce35a1` | 15 | 1.00 | `{"device_id": "92ce35a1", "device_name": "UNKNOWN_DEVICE_92c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_930d500a` | 18 | 1.20 | `{"device_id": "930d500a", "device_name": "UNKNOWN_DEVICE_930` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_9380c47c` | 15 | 1.00 | `{"device_id": "9380c47c", "device_name": "UNKNOWN_DEVICE_938` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_94` | 3 | 0.20 | `{"device_id": "94", "device_name": "UNKNOWN_DEVICE_94", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_9451c706` | 18 | 1.20 | `{"device_id": "9451c706", "device_name": "UNKNOWN_DEVICE_945` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_948300D` | 15 | 1.00 | `{"device_id": "948300D", "device_name": "UNKNOWN_DEVICE_9483` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_95` | 18 | 1.20 | `{"device_id": "95", "device_name": "UNKNOWN_DEVICE_95", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_951CB9D` | 15 | 1.00 | `{"device_id": "951CB9D", "device_name": "UNKNOWN_DEVICE_951C` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_951CCF5` | 15 | 1.00 | `{"device_id": "951CCF5", "device_name": "UNKNOWN_DEVICE_951C` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_95b2cf42` | 18 | 1.20 | `{"device_id": "95b2cf42", "device_name": "UNKNOWN_DEVICE_95b` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_95b483a8` | 3 | 0.20 | `{"device_id": "95b483a8", "device_name": "UNKNOWN_DEVICE_95b` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_95e6ce04` | 15 | 1.00 | `{"device_id": "95e6ce04", "device_name": "UNKNOWN_DEVICE_95e` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_96` | 18 | 1.20 | `{"device_id": "96", "device_name": "UNKNOWN_DEVICE_96", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_97` | 3 | 0.20 | `{"device_id": "97", "device_name": "UNKNOWN_DEVICE_97", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_97a88f35` | 15 | 1.00 | `{"device_id": "97a88f35", "device_name": "UNKNOWN_DEVICE_97a` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_97aaa145` | 3 | 0.20 | `{"device_id": "97aaa145", "device_name": "UNKNOWN_DEVICE_97a` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_97da6e73` | 3 | 0.20 | `{"device_id": "97da6e73", "device_name": "UNKNOWN_DEVICE_97d` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_97e5424a` | 3 | 0.20 | `{"device_id": "97e5424a", "device_name": "UNKNOWN_DEVICE_97e` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_97e542a2` | 3 | 0.20 | `{"device_id": "97e542a2", "device_name": "UNKNOWN_DEVICE_97e` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_98` | 15 | 1.00 | `{"device_id": "98", "device_name": "UNKNOWN_DEVICE_98", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_99` | 3 | 0.20 | `{"device_id": "99", "device_name": "UNKNOWN_DEVICE_99", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_9e5ddf` | 15 | 1.00 | `{"device_id": "9e5ddf", "device_name": "UNKNOWN_DEVICE_9e5dd` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_A4473B` | 18 | 1.20 | `{"device_id": "A4473B", "device_name": "UNKNOWN_DEVICE_A4473` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_A45954` | 18 | 1.20 | `{"device_id": "A45954", "device_name": "UNKNOWN_DEVICE_A4595` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_C1FCDB` | 15 | 1.00 | `{"device_id": "C1FCDB", "device_name": "UNKNOWN_DEVICE_C1FCD` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_C303F7E` | 15 | 1.00 | `{"device_id": "C303F7E", "device_name": "UNKNOWN_DEVICE_C303` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_CB3DD02` | 15 | 1.00 | `{"device_id": "CB3DD02", "device_name": "UNKNOWN_DEVICE_CB3D` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_CB3E81E` | 15 | 1.00 | `{"device_id": "CB3E81E", "device_name": "UNKNOWN_DEVICE_CB3E` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_F5` | 15 | 1.00 | `{"device_id": "F5", "device_name": "UNKNOWN_DEVICE_F5", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_F6` | 18 | 1.20 | `{"device_id": "F6", "device_name": "UNKNOWN_DEVICE_F6", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_FF` | 18 | 1.20 | `{"device_id": "FF", "device_name": "UNKNOWN_DEVICE_FF", "pro` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_a06ff1fa` | 18 | 1.20 | `{"device_id": "a06ff1fa", "device_name": "UNKNOWN_DEVICE_a06` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_a07c5b4d` | 18 | 1.20 | `{"device_id": "a07c5b4d", "device_name": "UNKNOWN_DEVICE_a07` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_a086d2ee` | 15 | 1.00 | `{"device_id": "a086d2ee", "device_name": "UNKNOWN_DEVICE_a08` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_a0d3ed` | 15 | 1.00 | `{"device_id": "a0d3ed", "device_name": "UNKNOWN_DEVICE_a0d3e` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c028b796` | 15 | 1.00 | `{"device_id": "c028b796", "device_name": "UNKNOWN_DEVICE_c02` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c4d93431` | 15 | 1.00 | `{"device_id": "c4d93431", "device_name": "UNKNOWN_DEVICE_c4d` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c5acb11d` | 15 | 1.00 | `{"device_id": "c5acb11d", "device_name": "UNKNOWN_DEVICE_c5a` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c5beb06a` | 15 | 1.00 | `{"device_id": "c5beb06a", "device_name": "UNKNOWN_DEVICE_c5b` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c6541071` | 15 | 1.00 | `{"device_id": "c6541071", "device_name": "UNKNOWN_DEVICE_c65` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c67f09e1` | 15 | 1.00 | `{"device_id": "c67f09e1", "device_name": "UNKNOWN_DEVICE_c67` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c6aec552` | 15 | 1.00 | `{"device_id": "c6aec552", "device_name": "UNKNOWN_DEVICE_c6a` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c6d3209a` | 15 | 1.00 | `{"device_id": "c6d3209a", "device_name": "UNKNOWN_DEVICE_c6d` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c6fc1425` | 15 | 1.00 | `{"device_id": "c6fc1425", "device_name": "UNKNOWN_DEVICE_c6f` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c7b68a5f` | 15 | 1.00 | `{"device_id": "c7b68a5f", "device_name": "UNKNOWN_DEVICE_c7b` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c7d949` | 18 | 1.20 | `{"device_id": "c7d949", "device_name": "UNKNOWN_DEVICE_c7d94` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c82ac411` | 18 | 1.20 | `{"device_id": "c82ac411", "device_name": "UNKNOWN_DEVICE_c82` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c82b4175` | 15 | 1.00 | `{"device_id": "c82b4175", "device_name": "UNKNOWN_DEVICE_c82` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c8344497` | 15 | 1.00 | `{"device_id": "c8344497", "device_name": "UNKNOWN_DEVICE_c83` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c97da6e7` | 3 | 0.20 | `{"device_id": "c97da6e7", "device_name": "UNKNOWN_DEVICE_c97` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_c97e542a` | 18 | 1.20 | `{"device_id": "c97e542a", "device_name": "UNKNOWN_DEVICE_c97` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_cd25ec98` | 15 | 1.00 | `{"device_id": "cd25ec98", "device_name": "UNKNOWN_DEVICE_cd2` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d15f4ed6` | 18 | 1.20 | `{"device_id": "d15f4ed6", "device_name": "UNKNOWN_DEVICE_d15` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d1644a94` | 18 | 1.20 | `{"device_id": "d1644a94", "device_name": "UNKNOWN_DEVICE_d16` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d18b5e81` | 18 | 1.20 | `{"device_id": "d18b5e81", "device_name": "UNKNOWN_DEVICE_d18` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d18b6640` | 18 | 1.20 | `{"device_id": "d18b6640", "device_name": "UNKNOWN_DEVICE_d18` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d1c69de6` | 3 | 0.20 | `{"device_id": "d1c69de6", "device_name": "UNKNOWN_DEVICE_d1c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d1c69df3` | 3 | 0.20 | `{"device_id": "d1c69df3", "device_name": "UNKNOWN_DEVICE_d1c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d1cd32bb` | 3 | 0.20 | `{"device_id": "d1cd32bb", "device_name": "UNKNOWN_DEVICE_d1c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d1cd3322` | 3 | 0.20 | `{"device_id": "d1cd3322", "device_name": "UNKNOWN_DEVICE_d1c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d1e29eb4` | 15 | 1.00 | `{"device_id": "d1e29eb4", "device_name": "UNKNOWN_DEVICE_d1e` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d3b0d5a0` | 18 | 1.20 | `{"device_id": "d3b0d5a0", "device_name": "UNKNOWN_DEVICE_d3b` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d47da6d8` | 15 | 1.00 | `{"device_id": "d47da6d8", "device_name": "UNKNOWN_DEVICE_d47` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d7cf6baf` | 18 | 1.20 | `{"device_id": "d7cf6baf", "device_name": "UNKNOWN_DEVICE_d7c` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_d89540` | 15 | 1.00 | `{"device_id": "d89540", "device_name": "UNKNOWN_DEVICE_d8954` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_db8dcc76` | 18 | 1.20 | `{"device_id": "db8dcc76", "device_name": "UNKNOWN_DEVICE_db8` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_df97e542` | 15 | 1.00 | `{"device_id": "df97e542", "device_name": "UNKNOWN_DEVICE_df9` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_e028a292` | 15 | 1.00 | `{"device_id": "e028a292", "device_name": "UNKNOWN_DEVICE_e02` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_e149d5` | 15 | 1.00 | `{"device_id": "e149d5", "device_name": "UNKNOWN_DEVICE_e149d` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_e149e7` | 18 | 1.20 | `{"device_id": "e149e7", "device_name": "UNKNOWN_DEVICE_e149e` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_e82ac411` | 15 | 1.00 | `{"device_id": "e82ac411", "device_name": "UNKNOWN_DEVICE_e82` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_e97e5424` | 15 | 1.00 | `{"device_id": "e97e5424", "device_name": "UNKNOWN_DEVICE_e97` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_ec6d3209` | 15 | 1.00 | `{"device_id": "ec6d3209", "device_name": "UNKNOWN_DEVICE_ec6` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_fa9288` | 3 | 0.20 | `{"device_id": "fa9288", "device_name": "UNKNOWN_DEVICE_fa928` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_fa9344` | 3 | 0.20 | `{"device_id": "fa9344", "device_name": "UNKNOWN_DEVICE_fa934` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_fa9359` | 3 | 0.20 | `{"device_id": "fa9359", "device_name": "UNKNOWN_DEVICE_fa935` |
| `KTBMES/TWIX/sensors/unknown_other_sensors/UNKNOWN_DEVICE_raw` | 18 | 1.20 | `{"device_id": "raw", "device_name": "UNKNOWN_DEVICE_raw", "p` |

### Payload Analysis

Payloads appear to be **JSON objects**.
Keys observed: `address`, `alarm`, `battery_ok`, `binding_countdown`, `button`, `centrifugal_acc`, `channel`, `closed`, `cmd`, `cmd_id`, `code`, `command`, `control`, `current`, `depth_cm`, `device_id`, `device_name`, `encrypted`, `esn`, `event`, `exception`, `ext`, `facility`, `fixed`, `flags`, `flags1`, `flags2`, `flags3`, `freq`, `has_tick`, `housecode`, `humidity`, `id0`, `id1`, `interval`, `learn`, `learn_mode`, `maybe_battery`, `message_num`, `mic`, `mod`, `moisture`, `moving`, `msg`, `noise`, `pad_id`, `pin`, `pressure_PSI`, `pressure_alert`, `pressure_kPa`, `pressure_psi`, `protocol_description`, `protocol_id`, `protocol_name`, `rain_mm`, `raw`, `raw_message`, `repeat`, `rolling`, `rssi`, `snr`, `state`, `status`, `status_hex`, `switch1`, `switch2`, `switch3`, `switch4`, `switch5`, `switch_id`, `tamper`, `temperature_C`, `temperature_F`, `tick`, `time`, `time_last_published_iso`, `time_last_published_ts`, `time_last_seen_iso`, `time_last_seen_ts`, `transmit`, `uid`, `unknown`, `unknown_3`, `wheel`, `xactivity`, `xtamper1`, `xtamper2`, `zone`

**Recent samples:**

```json
{"device_id": "a06ff1fa", "device_name": "UNKNOWN_DEVICE_a06ff1fa", "protocol_id": "-1", "protocol_name": "NO_PROTOCOL_NAME", "protocol_description": "NO_PROTOCOL_DESCRIPTION", "temperature_C": 41.0, "temperature_F": 105.8, "humidity": -999.0, "battery_ok": -1, "channel": "-1", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CRC", "mod": "NO_MOD", "time": "2026-03-25 20:09:35", "time_last_seen_ts": 1774494576.184507, "time_last_seen_iso": "2026-03-25T20:09:36.184507", "time_last_published_ts": 1774559916.622419, "time_last_published_iso": "2026-03-26T14:18:36.622419", "state": "32", "flags": "12", "repeat": "0", "pressure_kPa": "275.0", "pressure_psi": "39.885377875807535", "maybe_battery": "26"}
```
```json
{"device_id": "6323741c", "device_name": "UNKNOWN_DEVICE_6323741c", "protocol_id": "-1", "protocol_name": "NO_PROTOCOL_NAME", "protocol_description": "NO_PROTOCOL_DESCRIPTION", "temperature_C": 20.0, "temperature_F": 68.0, "humidity": -999.0, "battery_ok": -1, "channel": "-1", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CHECKSUM", "mod": "NO_MOD", "time": "2026-03-26 07:48:41", "time_last_seen_ts": 1774536525.557426, "time_last_seen_iso": "2026-03-26T07:48:45.557426", "time_last_published_ts": 1774559916.622538, "time_last_published_iso": "2026-03-26T14:18:36.622538", "pressure_PSI": "34.75", "moving": "1", "learn": "0", "code": "8b4c46", "unknown": "00", "unknown_3": "2"}
```
```json
{"device_id": "234", "device_name": "UNKNOWN_DEVICE_234", "protocol_id": "-1", "protocol_name": "NO_PROTOCOL_NAME", "protocol_description": "NO_PROTOCOL_DESCRIPTION", "temperature_C": 19.8, "temperature_F": 67.64, "humidity": -999.0, "battery_ok": "1", "channel": "1", "rssi": -999.0, "snr": -999.0, "noise": -999.0, "freq": -999.0, "mic": "CHECKSUM", "mod": "NO_MOD", "time": "2026-03-26 14:18:34", "time_last_seen_ts": 1774559919.060563, "time_last_seen_iso": "2026-03-26T14:18:39.060563", "time_last_published_ts": 1774559919.060719, "time_last_published_iso": "2026-03-26T14:18:39.060719", "button": "0", "transmit": "AUTO", "moisture": "0"}
```

---

## Raw Data

Full message log saved to `mqtt_raw_data.json`.

_Report generated at 2026-03-26T21:18:39.221611+00:00_