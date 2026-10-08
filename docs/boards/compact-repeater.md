# Compact repeater

A repeater image for small one-button boards with a screen. It is the standard MeshCore repeater (the same mesh behaviour, CLI and remote admin) with a minimal Cairn screen and a power save that turns the screen and the TX LED off.

| Board | Screen | Status | File |
|---|---|---|---|
| Heltec Mesh Node T096 | 0.96" colour TFT | ✅ beta | `MeshCore-HeltecT096-CairnN-<date>-repeater.uf2` |
| Heltec T114 | 1.14" TFT | 🧪 | `MeshCore-HeltecT114-CairnN-<date>-repeater.uf2` |
| Heltec WiFi LoRa 32 V2 | 0.96" OLED | 🧪 | `MeshCore-HeltecV2-CairnN-<date>-repeater-full.bin` / `-update.bin` |
| Heltec WiFi LoRa 32 V3 | 0.96" OLED | 🧪 | `MeshCore-HeltecV3-CairnN-<date>-repeater-full.bin` / `-update.bin` |
| Heltec WiFi LoRa 32 V4 | 0.96" OLED | 🧪 | `MeshCore-HeltecV4-CairnN-<date>-repeater-full.bin` / `-update.bin` |
| Heltec V4-R8 | 0.96" OLED | 🧪 | `MeshCore-HeltecV4R8-CairnN-<date>-repeater-full.bin` / `-update.bin` |
| Heltec Wireless Tracker | 0.96" colour TFT | 🧪 | `MeshCore-HeltecTracker-CairnN-<date>-repeater-full.bin` / `-update.bin` |
| Heltec Wireless Tracker V2 | 0.96" colour TFT | 🧪 | `MeshCore-HeltecTrackerV2-CairnN-<date>-repeater-full.bin` / `-update.bin` |

✅ beta: run on hardware. 🧪: built from the same code, not yet tried on that board. Reports are welcome.

## Pages

One button. **Click** moves to the next page; **hold** acts.

| Page | Shows | Hold |
|---|---|---|
| **Status** | repeat on/off, the channel, packets sent and heard, neighbours, noise floor, uptime, battery | — |
| **Spectrum** | the channel's signal over the last ~16 seconds, with the noise floor, the latest and the peak level | send an advert |
| **Settings** | Repeat (on/off), TX power, Send advert, Power save, Reboot | change or run the selected row |

On Settings a click steps down the rows, and a click past the last row returns to Status. Reboot asks for a second hold within 5 seconds. Settings are applied through the repeater's own CLI, so they are saved exactly as `set repeat` or `set tx` would save them over serial or remote admin. TX power steps through 1, 5, 9, 13, 17 and 22 dBm of radio-chip output; boards with a front-end amplifier (T096, V4) add its gain on top.

The screen turns off after 30 seconds (2 minutes on Spectrum); the first press only wakes it.

## Power save

Hold **Power save** in Settings. The screen and the TX LED turn off, and the setting is kept across reboots and power cuts, so a deployed repeater stays dark. **Double-click** the button to wake it; single clicks and holds are ignored while it is dark.

## Install

- **T096, T114 (nRF52840):** double-tap reset to get the board's USB drive, then copy the `.uf2` onto it ([UF2 guide](../install/nrf52-uf2.md)).
- **Heltec V2, V3, V4, V4-R8, Wireless Tracker (ESP32):** the `-repeater-full.bin` at `0x0` for a first install, or the `-repeater-update.bin` at `0x10000` to update ([ESP32 guide](../install/esp32-s3.md)).

A board that already ran a MeshCore repeater keeps its name, radio settings and password. A board coming from a companion image starts as a new repeater with the default admin password `password`: change it with `password <new>` over serial or remote admin.
