# LilyGO T-Display SF32 (with the keypad board)

✅ Tested on hardware · SiFli SF32LB52 · [install with one double-click](../install/sf32.md) · updates over Wi-Fi

LilyGO's T-Display SF32 has:
- a SiFli SF32LB52 (Cortex-M33)
- a 480×480 AMOLED touchscreen
- an SX1262 LoRa radio and an L76K GPS
- an ESP32-C6 for Wi-Fi
- a BHI260AP motion sensor
- a microphone and speaker
- an IR transmitter and microSD

The keypad board adds a 20-key phone-style keypad with backlight, a haptic motor and a BME280 climate sensor.

Cairn runs a native interface on it, built for the large square screen. It works with the official MeshCore apps over Bluetooth.

## Which file

| You want to… | File | How |
|---|---|---|
| install Cairn, or update over USB | `MeshCore-TDisplaySF32-CairnN-<date>-install.zip` | unzip, then double-click the installer for your computer ([steps](../install/sf32.md)). This keeps your identity, contacts and settings. |
| update over Wi-Fi | `MeshCore-TDisplaySF32-CairnN-<date>-update.bin` | the board fetches it itself: Settings › System › Firmware update |
| recover a board that won't start | the same `-install.zip` | run the installer again. Download mode is in ROM, so it always works. |

## Features

- **Home dashboard of cards:**
  - a big clock;
  - battery, chats, nodes, GPS, radio (frequency, SF / BW and noise floor) and network;
  - board cards: climate, step counter, IR remote, Player, Recorder and Tools.
  - Scroll down for more cards.
- **Sidebar tabs:** Home, Chats, Nodes, Radio, GPS and Settings, with coloured icons.
- **Chats:** channels and direct messages, typed on the keypad (multi-tap) or on the touchscreen.
- **Nodes:** list and cards views, ping, repeater scan and remote admin.
- **Radio:** a live spectrum strip, with a full-screen spectrum and band scan.
- **GPS:** position, satellites and a compass. Tap the compass for a full-screen view with all the GPS details.
- **Sensors:** temperature, humidity and pressure (keypad board), and a step counter.
- **IR remote:** large buttons, with brand and device chosen in its settings.
- **Player and Recorder:** two apps that play music from the microSD card and record from the microphone, with a live audio spectrum. Recordings are saved to the card.
- **Wi-Fi:** clock sync and online firmware updates from this repository. Updates use A/B slots with automatic rollback.
- **Bluetooth:** a companion link to the MeshCore apps, paired with the PIN shown on the screen.
- **Power:** the board sleeps deeply while the screen is off, and can hibernate.

## Buttons and keys

| Control | Does |
|---|---|
| **C** (side) | click: turn the screen off or wake it; double-press: unlock; hold: lock |
| **A** (side) | click: Settings; double-press: new message; hold 1–3 s: back; triple-press: mute; hold 3 s: power menu. It also wakes the board from hibernate. |
| **B** (side) | click: alert profile; hold: flashlight |
| ▲ / ▼ | move up and down. On values and sliders, **up always means more**. |
| OK | select; hold: context menu |
| Back | back. On Home with the sidebar selected, it turns the screen off. |
| Home | Home tab; hold: quick panel |
| Mail | newest unread message; hold: new message |
| Stop | stop an alert or dismiss a pop-up; hold: mute |
| 0–9 | Home card shortcuts; letter jump in lists; typing in chats |

The side buttons can be changed in Settings › Controls. Without the keypad board: B steps forward, B double-press steps back, and A selects.

## Known issues

- **No USB-serial companion.** The board's only USB port is the CH343 console, so connect the MeshCore apps over Bluetooth.
- **Wi-Fi updates start with the next build.** 107 is the first SF32 release, so the online updater has nothing newer to offer yet. Until then, update with the USB installer.
- **No offline map yet.** It's coming in a later release.
- **The IR transmitter hasn't been checked against a TV yet.** Its codes follow the public IR databases.
- **Battery life with the screen off hasn't been measured yet.**
- **Waking on a received LoRa message hasn't been confirmed on hardware yet.**
- **Restarts on a weak USB supply.** One test unit restarted every few minutes on a weak USB supply. If yours does, try another cable or port, and please [report it](https://github.com/cvhviz/Cairn/issues/new?template=bug_report.yml).

Problems? [Report a bug](https://github.com/cvhviz/Cairn/issues/new?template=bug_report.yml). Please include the build number from the splash screen.
