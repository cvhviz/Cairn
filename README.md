# Cairn

**Cairn** is a customized build of the [MeshCore](https://github.com/meshcore-dev/MeshCore) companion firmware for four boards. Every board is built from the same source tree, shares its mesh and radio code (which tracks stock MeshCore), and stays fully compatible with the official MeshCore apps. Builds are numbered: the splash screen shows **BUILD N**, and releases are tagged `cairn-vN`. L1 releases from before Cairn are in the [older L1 repository](https://github.com/cvhviz/WioL1Pro-CVHBuild).

| Board | Chip | Interface |
|---|---|---|
| Seeed Wio Tracker L1 Pro | nRF52840 | OLED (SH1106), 2.42" SSD1309 "DV1", or e-ink; joystick |
| Seeed Wio Tracker L2 Pro | ESP32-S3 | 3.2" 320x240 touchscreen, native touch UI |
| Heltec WiFi LoRa 32 V4 + Expansion Kit (2.8" touch) | ESP32-S3 | the same touch UI as the L2 |
| Heltec Mesh Node T096 | nRF52840 | 0.96" TFT, one button, themed UI |

## The touch interface (Wio Tracker L2 Pro, Heltec V4)

- **Side icon rail**: Home, Chats, Nodes, Radio, GPS and Settings, with unread and new-advert badges. A status bar shows the page title, a 12-hour clock, Bluetooth, GPS and battery.
- **Home dashboard**: a large clock plus live cards for battery, chats, nodes, GPS, radio and Bluetooth. Tap a card to open its page.
- **Chats**: channels, direct messages and rooms in one list. Conversations show as bubbles, and there's a full on-screen keyboard with emoji, quick replies and a byte counter.
- **Colour emoji**: 229 Noto emoji drawn inline in messages, previews and node names. The keyboard has an emoji picker with recently used emoji first.
- **Nodes**: recent adverts and saved contacts with hops, last heard and distance in ft/mi. Node detail shows position and bearing, with ping and message.
- **Radio**: frequency and settings, airtime per packet, Now/Floor/Peak/Margin meters, a live spectrum, and the last packets heard.
- **GPS**: position in ft/mph with a course compass, Off / On / Eco modes, and a map of nodes by bearing and distance.
- **Settings**: every change is a draft with Cancel and Save. Radio changes ask a second time, and destructive actions need a hold plus a confirmation.
- **Sound**: volume slider and a choice of alert tone per event (direct message, channel, advert, sent).
- **Wake & lock**: tap to wake, auto-lock, and a lock screen that ignores touch in a pocket. Double-press WAKE or User to unlock.
- **Imperial units** (ft, mi, mph, °F) and 12-hour time by default.

- **Wi-Fi**: on-device network setup, clock sync, the MeshCore app over Wi-Fi, local firmware updates from a browser, and **online updates from this repository's releases** (from Cairn 106; checked once a day while on Wi-Fi, and nothing installs without your confirmation).
- **Offline map** from microSD tiles, with pinch to zoom.

## Screens

| | | |
|---|---|---|
| ![Home](docs/screens/01-home.png)<br>Home | ![Chats](docs/screens/02-chats.png)<br>Chats | ![Conversation](docs/screens/03-conversation.png)<br>Conversation |
| ![Keyboard](docs/screens/04-keyboard.png)<br>Keyboard | ![Nodes](docs/screens/05-nodes.png)<br>Nodes | ![Node detail](docs/screens/06-node-detail.png)<br>Node detail |
| ![Radio](docs/screens/07-radio.png)<br>Radio | ![GPS](docs/screens/08-gps.png)<br>GPS | ![Settings](docs/screens/09-settings.png)<br>Settings |
| ![Lock screen](docs/screens/10-lock-screen.png)<br>Lock screen | | |

## Release files

Each release carries the images for every board. Pick the files for yours:

| Board | File | Use |
|---|---|---|
| Wio Tracker L1 Pro | `MeshCore-WioL1Pro-CairnN-DATE.uf2` | SH1106 OLED |
| | `MeshCore-DV1-CairnN-DATE.uf2` | 2.42" SSD1309 on the Grove port |
| | `MeshCore-WioL1Eink-CairnN-DATE.uf2` | e-ink |
| | `MeshCore-WioL1RoomServer-CairnN-DATE.uf2` | room server (no phone app) |
| Wio Tracker L2 Pro | `MeshCore-WioL2Pro-CairnN-DATE-full.bin` | first install or recovery, at `0x0` after a full erase |
| | `MeshCore-WioL2Pro-CairnN-DATE-update.bin` | update, at `0x10000`; also what the online updater installs |
| Heltec V4 touch | `MeshCore-HeltecV4Touch-CairnN-DATE-full.bin` | first install or recovery, at `0x0` after a full erase |
| | `MeshCore-HeltecV4Touch-CairnN-DATE-update.bin` | update, at `0x10000`; also what the online updater installs |
| Heltec T096 | `MeshCore-HeltecT096-CairnN-DATE-ble.uf2` | Bluetooth companion (phone app) |
| | `MeshCore-HeltecT096-CairnN-DATE-usb.uf2` | USB serial companion |

Updates keep your identity, contacts and settings. A first install on an ESP32 board **erases the device completely**, including any factory firmware.

## Installing

### nRF52840 boards (L1 Pro, T096): UF2

Connect USB and double-tap **Reset**. A USB drive appears. Copy the `.uf2` onto it; the board reboots by itself when the copy finishes. A copy that "finishes" in about a second with an error was cut short: do it again.

### ESP32-S3 boards (L2 Pro, Heltec V4): esptool or browser

**Browser:** open [Espressif's web flasher](https://espressif.github.io/esptool-js/) in Chrome or Edge and connect. First install: **Erase Flash**, then program `-full.bin` at `0x0`. Update: program `-update.bin` at `0x10000`.

**Command line:**

```bash
pip install esptool
# first install
esptool.py --chip esp32s3 erase_flash
esptool.py --chip esp32s3 -b 921600 write_flash 0x0 MeshCore-<board>-CairnN-DATE-full.bin
# update
esptool.py --chip esp32s3 -b 921600 write_flash 0x10000 MeshCore-<board>-CairnN-DATE-update.bin
```

If the device was last updated over Wi-Fi, it may be running from its second app slot, and a USB write to `0x10000` would be ignored. Write the boot selector with it: `write_flash 0xe000 boot_app0.bin 0x10000 ...-update.bin` (`boot_app0.bin` ships with the Arduino ESP32 core), or use the `-full.bin`.

The boards enter download mode on their own when esptool connects. If not: L2, hold **Boot** and tap **Reset**; Heltec, hold **PRG** and tap **RST**. If the screen still shows the old firmware afterwards, tap Reset once. The first boot after a full erase sits on "Loading..." for a while as it formats storage and creates the node's identity.

### Over Wi-Fi (L2 Pro, Heltec V4)

- **Online** (from Cairn 106): Settings > System > Firmware update > **Check for updates**. The device also checks this repository once a day while on Wi-Fi and shows a notice when a newer build is out. It downloads the board's `-update.bin` over HTTPS, checks its size, SHA-256 and board marker, and installs only after you confirm.
- **Local:** turn on update mode on the same page and upload the `-update.bin` from a browser at the address it shows.

## Publishing a release (for the online updater)

The devices read `https://api.github.com/repos/cvhviz/Cairn/releases/latest`. For a build to be offered:

- Tag it `cairn-vN`, where N is the build number shown on the splash (it must be higher than the device's own). Publish it as a normal release, not a draft or prerelease.
- Attach each ESP32 board's `-update.bin` under its exact name, `MeshCore-WioL2Pro-CairnN-DATE-update.bin` and `MeshCore-HeltecV4Touch-CairnN-DATE-update.bin`. GitHub records each file's SHA-256, which the device checks.
- The release notes are shown on the device before installing, so keep the top of them short and plain.

## Hardware

| Board | Detail |
|---|---|
| Wio Tracker L1 Pro | nRF52840, SX1262, L76K GPS, joystick, piezo |
| Wio Tracker L2 Pro | Wio-S3 (ESP32-S3, 16 MB flash, 8 MB PSRAM), SX1262 (TCXO 3.0 V), 3.2" NV3031B LCD + GT911 touch, L76K GPS, ES8311 speaker, microSD |
| Heltec V4 + Expansion Kit | ESP32-S3 (16 MB flash, 8 MB PSRAM), SX1262 + front end, 2.8" ST7789 + touch, L76K GPS, piezo, microSD |
| Heltec T096 | nRF52840, SX1262, 0.96" ST7735 TFT, one button |

## Relationship to upstream

This is a personal build, not a general-purpose distribution. All core mesh and radio behaviour comes from [MeshCore](https://github.com/meshcore-dev/MeshCore); see that project for protocol documentation, the official flasher, supported hardware and the client apps ([web](https://app.meshcore.nz), [Android](https://play.google.com/store/apps/details?id=com.liamcottle.meshcore.android), [iOS](https://apps.apple.com/us/app/meshcore/id6742354151)). Credit to the MeshCore developers and community for the foundation.

## License

MIT, same as upstream MeshCore. The firmware embeds third-party fonts, emoji and libraries under their own licences; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
