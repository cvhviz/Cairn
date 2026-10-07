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

The files in Cairn 107 were replaced on 7 Oct 2026 with a fixed build: the first ones (6 Oct) didn't charge the battery, could restart the board on USB and couldn't update over Wi-Fi. A board on the first build needs the [USB installer](../install/sf32.md#if-your-board-has-the-first-sf32-build) once.

## Which file

| You want to… | File | How |
|---|---|---|
| install Cairn, or update over USB | `MeshCore-TDisplaySF32-CairnN-<date>-install.zip` | unzip, then double-click the installer for your computer ([steps](../install/sf32.md)). This keeps your identity, contacts and settings. |
| update over Wi-Fi | `MeshCore-TDisplaySF32-CairnN-<date>-update.bin` | the board fetches it itself: Settings › System › Firmware update (Cairn 107 and later), with the keyboard board attached: it carries the Wi-Fi chip |
| recover a board that won't start | the same `-install.zip` | hold A for 12 s, then run the installer again. Download mode is in ROM, so it always works. |

## Features

- **Home dashboard of cards:**
  - a big clock;
  - battery, chats, nodes, GPS, radio (frequency, SF / BW and noise floor) and network;
  - board cards: climate, step counter, IR remote, Player, Recorder and Tools.
  - Scroll down for more cards.
- **Sidebar tabs:** Home, Chats, Nodes, Radio, GPS and Settings, with coloured icons.
- **Chats:** channels and direct messages, typed on the keypad (multi-tap) or on the touchscreen.
- **Nodes:** list and cards views, ping, repeater scan and remote admin.
- **Node pages:** selecting a companion, repeater, room server or sensor opens a page of cards for it: signal, route, battery, last ping and, once logged in, its status, neighbours, readings and clock. The bar at the bottom follows the session: Message or Log in, Ping, then More, Admin or Refresh. The full admin console is one step further.
- **Radio:** a live spectrum strip, with a full-screen spectrum and band scan.
- **GPS:** position, satellites and a compass. Tap the compass for a full-screen view with all the GPS details.
- **Sensors:** temperature, humidity and pressure (keypad board), and a step counter.
- **IR remote:** large buttons, with brand and device chosen in its settings.
- **Player and Recorder:** two apps that play music from the microSD card and record from the microphone, with a live audio spectrum. Recordings are saved to the card.
- **Charging:** the battery charges on USB. Cairn sets up the battery charger at boot and checks it every few seconds. The Battery page shows the charge state and, if the battery has a temperature sensor, whether it is too cold or too hot to charge.
- **Low battery:** on battery, below 3.55 V for a minute, a 30-second countdown starts, then the board powers off to protect the cell. Any key or USB cancels it. To wake it, plug in USB or hold D for 2 seconds.
- **Wi-Fi:** the keyboard's ESP32-C6 joins your network (Settings › Network). While Wi-Fi is on, the GPS is paused: the two share one connection.
- **Internet time:** on Wi-Fi the clock is set from the internet. On the Wi-Fi page (Settings › Network › Join network), Internet time is Off, Ask (the default) or **Always**. Ask corrects small differences silently and asks before a change of more than an hour ("Set clock from internet?": Not now, Set, Always). Always sets it without asking. A GPS fix still comes first.
- **Clock after a power loss:** the board saves the time to its flash every 15 minutes and before a restart or power-off. After a power loss it comes back with the last known time, shown as "Last known", until the GPS, the internet or the app sets it.
- **Wi-Fi updates:** Settings › System › Firmware update checks this repository's latest release, downloads the board's `-update.bin`, and checks its size, SHA-256 and board marker before it offers to install. The new build goes into a spare slot and runs on trial; it is kept only after it has run for a minute, otherwise the board goes back to the build it had. It needs USB with the battery switched on, or 30 % battery.
- **Bluetooth:** a companion link to the MeshCore apps, paired with the PIN shown on the screen.
- **Power:** the board sleeps deeply while the screen is off, and can hibernate.

## Power switch and the keyboard's battery

The side power switch picks which battery feeds the board:

| Switch | Core on its own | Docked on the keyboard |
|---|---|---|
| **ON** | the core's own battery | the core's own battery |
| **OFF** | no battery: the board runs only from USB | the keyboard's battery |

- **Install and update with the switch ON**, with the core off the keyboard. With the switch OFF and no keyboard, a USB install fails: the board restarts every 20 to 40 seconds once the flash tool takes over.
- **Docked, the switch doesn't turn the unit off**; it only changes battery. To turn it off, hold A for 3 seconds and choose Hibernate. A wakes it.
- The Battery page and the battery icon show whichever battery the switch connects. Cairn can't tell which one that is.
- Moving the switch while running on battery restarts the board: the power breaks for a moment as the switch moves.
- On USB with a flat battery, Cairn shows the USB symbol instead of a percentage and won't start a Wi-Fi update.

## Buttons and keys

| Control | Does |
|---|---|
| **C** (side) | click: turn the screen off or wake it; double-press: unlock; hold: lock |
| **A** (side) | click: Settings; double-press: new message; hold 1–3 s: back; triple-press: mute; hold 3 s: power menu (Hibernate, Restart). It also wakes the board from hibernate. Held 12 s, it restarts the chip even when the firmware is stuck. |
| **B** (side) | click: alert profile; hold: flashlight |
| **D** (side) | not used by the interface. Hold 2 s: wakes the board after a low-battery power-off. Hold about 20 s: the battery charger cuts the power for a moment and the board restarts, for a board that stops responding. |
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
- **Wi-Fi after re-docking.** After the core is taken off the keyboard and docked again, Wi-Fi may not come back by itself. Restart the board (hold A for 3 seconds, Restart) and it reconnects. Wi-Fi updates from GitHub work: 107 to 108 was tested end to end.
- **The Windows installer hasn't been run on a Windows PC yet.** Please [report](https://github.com/cvhviz/Cairn/issues/new?template=bug_report.yml) how it goes.
- **No offline map yet.** It's coming in a later release.
- **The IR transmitter hasn't been checked against a TV yet.** Its codes follow the public IR databases.
- **Battery life with the screen off hasn't been measured yet.**
- **Waking on a received LoRa message hasn't been confirmed on hardware yet.**
- **Node pages are new in this build.** Please report anything that looks wrong.

Problems? [Report a bug](https://github.com/cvhviz/Cairn/issues/new?template=bug_report.yml). Please include the build number from the splash screen.
