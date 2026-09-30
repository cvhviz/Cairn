# MeshCore — CVHBuild for the Seeed Wio Tracker L2 Pro

A customized build of MeshCore companion firmware for the **Seeed Wio Tracker L2 Pro** (ESP32-S3, 3.2″ 320×240 capacitive touchscreen, SX1262 LoRa, L76K GPS, speaker), with a native touch interface written for this board.

It is the sister project of [WioL1Pro-CVHBuild](https://github.com/cvhviz/WioL1Pro-CVHBuild) and shares its mesh and radio code, which tracks stock MeshCore. It remains fully compatible with the official MeshCore apps over BLE. Builds are identified by a **CVHBuild** number shown on the splash screen, and releases are tagged `cvhbuild-vN`.

## The touch interface

- **Side icon rail**: Home, Chats, Nodes, Radio, GPS and Settings, with unread and new-advert badges. A status bar shows the page title, a 12-hour clock, Bluetooth, GPS and battery.
- **Home dashboard**: a large clock plus live cards for battery, chats, nodes, GPS, radio and Bluetooth. Tap a card to open its page.
- **Chats**: channels, direct messages and rooms in one list. Conversations show as bubbles, and there's a full on-screen keyboard with emoji, quick replies and a byte counter.
- **Colour emoji**: 229 Noto emoji drawn inline in messages, previews and node names. The keyboard has an emoji picker with recently used emoji first.
- **Nodes**: recent adverts and saved contacts with hops, last heard and distance in ft/mi. Node detail shows position and bearing, with ping and message.
- **Radio**: frequency and settings, airtime per packet, Now/Floor/Peak/Margin meters, a live spectrum, and the last packets heard.
- **GPS**: position in ft/mph with a course compass, Off / On / Eco modes, and a map of nodes by bearing and distance.
- **Settings**: every change is a draft with Cancel and Save. Radio changes ask a second time, and destructive actions need a hold plus a confirmation.
- **Sound**: 4-step volume and a choice of alert tone per event (direct message, channel, advert, sent).
- **Wake & lock**: tap to wake, auto-lock, and a lock screen that ignores touch in a pocket. Double-press WAKE or User to unlock.
- **Imperial units** (ft, mi, mph, °F) and 12-hour time by default.

Wi-Fi is in development: on-device network setup, clock sync, the MeshCore app over Wi-Fi, and firmware updates over Wi-Fi from this repository's releases.

## Installing

Each release has two files:

| File | Use |
|---|---|
| `MeshCore-WioL2Pro-CVHBuildN-DATE-full.bin` | First install, or recovery. Written at `0x0` after a full erase. |
| `MeshCore-WioL2Pro-CVHBuildN-DATE-update.bin` | Updating a device that already runs CVHBuild. Written at `0x10000`. Keeps your identity, contacts and settings. |

A first install **erases the device completely**. That includes Seeed's factory Meshtastic firmware and its settings.

### Browser (no install needed)

1. Open [Espressif's web flasher](https://espressif.github.io/esptool-js/) in Chrome or Edge and connect to the L2's USB port.
2. First install: **Erase Flash**, then program the `-full.bin` at address `0x0`.
3. Update: program the `-update.bin` at address `0x10000`.

### Command line (esptool)

```bash
pip install esptool
# first install
esptool.py --chip esp32s3 erase_flash
esptool.py --chip esp32s3 -b 921600 write_flash 0x0 MeshCore-WioL2Pro-CVHBuildN-DATE-full.bin
# update
esptool.py --chip esp32s3 -b 921600 write_flash 0x10000 MeshCore-WioL2Pro-CVHBuildN-DATE-update.bin
```

The L2 enters download mode on its own when esptool connects. If it doesn't, hold **Boot**, tap **Reset**, release Boot, and try again. If the screen stays on the old firmware after a flash, tap **Reset** once.

The first boot after a full erase sits on "Loading..." for a while as it formats storage and creates the node's identity. That is normal.

## Hardware

| Component | Detail |
|---|---|
| Board | Seeed Wio Tracker L2 Pro (Wio-S3: ESP32-S3, 16 MB flash, 8 MB PSRAM) |
| Radio | Semtech SX1262 (TCXO at 3.0 V) |
| Display | 3.2″ 320×240 NV3031B LCD, GT911 capacitive touch, LP5814 backlight |
| GPS | Quectel L76K |
| Audio | ES8311 codec and speaker |
| Buttons | User/Boot and the side WAKE button |

## Relationship to upstream

This is a personal build, not a general-purpose distribution. All core mesh and radio behaviour comes from [MeshCore](https://github.com/meshcore-dev/MeshCore); see that project for protocol documentation, the official flasher, supported hardware and the client apps ([web](https://app.meshcore.nz), [Android](https://play.google.com/store/apps/details?id=com.liamcottle.meshcore.android), [iOS](https://apps.apple.com/us/app/meshcore/id6742354151)). Credit to the MeshCore developers and community for the foundation.

## License

MIT, same as upstream MeshCore. The firmware embeds third-party fonts, emoji and libraries under their own licences; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
