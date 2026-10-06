# Seeed Wio Tracker L1 Pro

✅ Tested on hardware · nRF52840 · [install with UF2](../install/nrf52-uf2.md)

nRF52840, SX1262 LoRa, L76K GPS, piezo buzzer, a five-way joystick and a Back button. Cairn has four images for it: three companion builds for different screens, and a room server.

## Which file

| Your L1 has… | File |
|---|---|
| the stock SH1106 OLED (most units) | `MeshCore-WioL1Pro-CairnN-<date>.uf2` |
| a 2.42" SSD1309 OLED on the Grove port ("DV1") | `MeshCore-DV1-CairnN-<date>.uf2` |
| a 2.13" e-ink panel | `MeshCore-WioL1Eink-CairnN-<date>.uf2` |
| a room server role (no phone app; SH1106 OLED) | `MeshCore-WioL1RoomServer-CairnN-<date>.uf2` |

Install, update and recovery all use the same file: double-tap **Reset** and copy the `.uf2` onto the drive that appears ([details](../install/nrf52-uf2.md)). Updating keeps your identity, contacts, channels and settings. Switching between the screen variants keeps them too.

## Buttons

| Button | Does |
|---|---|
| Joystick up / down / left / right | move between pages and items |
| Joystick press | select |
| Back (menu) | back out of a page or menu |
| Reset | restart; **double-tap** for the UF2 drive |

## Features

- Works with the official MeshCore apps over Bluetooth (PIN on the screen).
- Cairn splash with the build number and build stamp.
- Page tabs along the bottom or down the side (Settings > Page tabs).
- Settings grouped to match the touch builds.
- GPS with distances in miles, 12-hour clock.
- Room server image with the CLI over USB serial.

## Known issues

- The three-colour e-ink panel isn't supported: every refresh is a ~15 s full flash. Use a black-and-white 2.13" panel.
- Check the release notes of each build for anything new.

Problems? [Report a bug](https://github.com/cvhviz/Cairn/issues/new?template=bug_report.yml) with the image name and the build number from the splash.
