<p align="center"><img src="docs/cairn_mark.png" alt="Cairn" width="140"></p>

<h1 align="center">Cairn</h1>

**Cairn** is a fork of the [MeshCore](https://github.com/meshcore-dev/MeshCore) companion firmware. Every board is built from one source tree that shares MeshCore's mesh and radio code, and every build works with the official MeshCore apps ([web](https://app.meshcore.nz), [Android](https://play.google.com/store/apps/details?id=com.liamcottle.meshcore.android), [iOS](https://apps.apple.com/us/app/meshcore/id6742354151)).

Builds are numbered: the splash screen shows **BUILD N**, releases are tagged `cairn-vN`, and files are named `MeshCore-<Board>-CairnN-<date>…`, so you can match a device to a release from its own screen.

**Download the files from the [latest release](https://github.com/cvhviz/Cairn/releases/latest).** L1 releases from before Cairn are in the [older L1 repository](https://github.com/cvhviz/WioL1Pro-CVHBuild).

## Latest: Cairn 108 (7 Oct 2026)

- **New board:** LilyGO T-Deck / T-Deck Plus (beta), the Cairn interface by touch, keyboard and trackball.
- **L2 Pro and Heltec V4 touch:** the new Battery page (cards above a detailed graph, time left, uptime), a cleaner look across the pages, and an empty-state message in Chats.
- **L2 Pro, Heltec V4 touch, ThinkNode M9, T-Deck:** the Wi-Fi and Bluetooth switches act at once, with no Save. Turning Bluetooth off while your phone is linked asks first.
- **T-Display SF32:** Wi-Fi updates no longer roll back on their first start, and the board stays quiet while the keyboard is detached.
- **Updating:** boards on Cairn 107 update over Wi-Fi in **Settings › System › Firmware update** (the SF32 with its keyboard board attached). An SF32 on the first build (6 Oct) needs the [USB installer](docs/install/sf32.md#if-your-board-has-the-first-sf32-build) once.
- **Still on Cairn 107:** the nRF52840 boards (L1 Pro, T096) and the preview boards; their files are in [Cairn 107](https://github.com/cvhviz/Cairn/releases/tag/cairn-v107).

## Supported boards

✅ **Tested**: used on real hardware before each release. ✅ **Beta**: tested on hardware but new to Cairn; its page lists what hasn't been tried yet. 🧪 **Preview**: builds from the same tree but hasn't been tried on hardware. Reports are welcome.

### nRF52840 (install by copying a `.uf2`)

| Board                                                         | Screen and input               | Status | Install guide                    |
| ------------------------------------------------------------- | ------------------------------ | ------ | -------------------------------- |
| [Seeed Wio Tracker L1 Pro](docs/boards/wio-tracker-l1-pro.md) | OLED or e-ink, joystick        | ✅     | [UF2](docs/install/nrf52-uf2.md) |
| [Heltec Mesh Node T096](docs/boards/heltec-t096.md)           | 0.96" colour TFT, one button   | ✅     | [UF2](docs/install/nrf52-uf2.md) |
| [Preview boards](docs/boards/preview-boards.md)               | OLED or colour TFT, one button | 🧪     | [UF2](docs/install/nrf52-uf2.md) |

The L1 Pro takes the SH1106 OLED, the 2.42" SSD1309 "DV1" OLED or the e-ink display. nRF52840 preview boards: RAK4631, RAK3401, ProMicro, Nano G2 Ultra, Heltec T1, GAT562 boards, Meshtiny, Keepteen LT1, LilyGO T-Impulse Plus.

### ESP32 / ESP32-S3 (install with esptool or a web flasher)

| Board                                                         | Screen and input                      | Status  | Install guide                             |
| ------------------------------------------------------------- | ------------------------------------- | ------- | ----------------------------------------- |
| [Seeed Wio Tracker L2 Pro](docs/boards/wio-tracker-l2-pro.md) | 3.2" touchscreen                      | ✅      | [esptool / web](docs/install/esp32-s3.md) |
| [Heltec V4 + Expansion Kit](docs/boards/heltec-v4-touch.md)   | 2.8" touchscreen                      | ✅      | [esptool / web](docs/install/esp32-s3.md) |
| [Elecrow ThinkNode M9](docs/boards/thinknode-m9.md)           | 2.4" screen, keyboard, d-pad          | ✅ beta | [esptool / web](docs/install/esp32-s3.md) |
| [LilyGO T-Deck / T-Deck Plus](docs/boards/lilygo-t-deck.md)   | 2.8" touchscreen, keyboard, trackball | ✅ beta | [esptool / web](docs/install/esp32-s3.md) |
| [Preview boards](docs/boards/preview-boards.md)               | OLED or colour TFT, one button        | 🧪      | [esptool / web](docs/install/esp32-s3.md) |

The L2 Pro, Heltec V4, ThinkNode M9 and T-Deck run the same Cairn interface; the M9 drives it by keys and the T-Deck by touch or keys.

ESP32 preview boards: Heltec V4 / V4-R8 / V3 (OLED), Heltec Wireless Tracker (V1, V2), LilyGO T-Beam Supreme and T-Beam 1W, T3S3, Station G2 / G3 (USB build only), XIAO ESP32-S3, ThinkNode M2, Meshnology W12, Ebyte EoRa-S3; and on the original ESP32, Heltec V2, LilyGO T-Beam (SX1262 / SX1276, Bluetooth build only), T-LoRa V2.1-1.6 and MeshAdventurer. The original-ESP32 boards install the same way; the [ESP32 guide](docs/install/esp32-s3.md#original-esp32-boards) has the one difference.

### SiFli SF32 (install with one double-click)

| Board                                                         | Screen and input                   | Status | Install guide                     |
| ------------------------------------------------------------- | ---------------------------------- | ------ | --------------------------------- |
| [LilyGO T-Display SF32](docs/boards/lilygo-t-display-sf32.md) | 480×480 AMOLED touchscreen, keypad | ✅     | [installer](docs/install/sf32.md) |

The T-Display SF32 sits on its 20-key keypad board and runs its own card-based interface. The installer runs on Mac, Windows and Linux.

### Coming soon

- **Map downloads on the device**, straight over Wi-Fi, so you won't need a computer to prepare the offline map card. Until then, [tools/l2_maptiles.py](tools/l2_maptiles.py) builds the card on a computer.

Want another board? [Ask for it](https://github.com/cvhviz/Cairn/issues/new?template=board_request.yml).

## Features

| Feature                       |  L1 Pro  | L2 Pro | Heltec V4 touch | ThinkNode M9 |   T-Deck    | T-Display SF32 |   T096   | Preview |
| ----------------------------- | :------: | :----: | :-------------: | :----------: | :---------: | :------------: | :------: | :-----: |
| MeshCore apps over Bluetooth  |    ✅    |   ✅   |       ✅        |      ✅      |     ✅      |       ✅       |    ✅    |   ✅    |
| Input                         | joystick | touch  |      touch      |     keys     | touch, keys | touch, keypad  |  button  | button  |
| Colour emoji                  |    –     |   ✅   |       ✅        |      ✅      |     ✅      |       ✅       |    –     |    –    |
| Wi-Fi                         |    –     |   ✅   |       ✅        |      ✅      |     ✅      |      ✅ ¹      |    –     |    –    |
| Online updates                |    –     |   ✅   |       ✅        |      ✅      |    ✅ ²     |       ✅       |    –     |    –    |
| GPS                           |    ✅    |   ✅   |      ✅ ³       |      ✅      |    Plus     |       ✅       |    ✅    |  some   |
| microSD card                  |    –     |   ✅   |       ✅        |      ✅      |     ✅      |       ✅       |    –     |    –    |
| Offline map                   |    –     |   ✅   |       ✅        |   untried    |     ✅      |     coming     |    –     |    –    |
| Spectrum and band scan        |    –     |   ✅   |       ✅        |      ✅      |     ✅      |       ✅       | spectrum |    –    |
| Repeater scan and admin       |    –     |   ✅   |       ✅        |      ✅      |     ✅      |       ✅       |    –     |    –    |
| USB-serial companion          |    –     |   –    |        –        |      –       |      –      |       –        |    ✅    |   ✅    |
| Room server image             |    ✅    |   –    |        –        |      –       |      –      |       –        |    –     |    –    |
| Colour themes                 |    –     |   –    |        –        |      –       |      –      |       –        |    ✅    | some ⁴  |
| Music, voice, IR, sensors     |    –     |   –    |        –        |      –       |      –      |       ✅       |    –     |    –    |
| Imperial units, 12-hour clock |    ✅    |   ✅   |       ✅        |      ✅      |     ✅      |       ✅       |    ✅    |   ✅    |

¹ Clock sync and online updates; no app link over Wi-Fi. ² From its next build (108 is the T-Deck's first). ³ With the Expansion Kit. ⁴ The colour-screen boards (Wireless Tracker, T1).

## Which file do I need?

Each release carries every board's files, named `MeshCore-<Board>-CairnN-<date>[-<variant>].<ext>`. Your board page lists them all.

| You want to…      | nRF52840 boards       | ESP32 boards                         | T-Display SF32                          |
| ----------------- | --------------------- | ------------------------------------ | --------------------------------------- |
| **First install** | the board's `.uf2`    | `-full.bin` at `0x0` ⚠               | the `-install.zip`: unzip, double-click |
| **Update**        | the board's `.uf2`    | `-update.bin` at `0x10000`, or Wi-Fi | the `-install.zip` again, or Wi-Fi      |
| **Recover**       | copy the `.uf2` again | erase, then `-full.bin` at `0x0`     | hold A for 12 s, then the installer     |

- ⚠ An ESP32 first install erases the device. If it runs MeshCore, export your identity and contacts in the app first. Updates keep everything.
- On ESP32 boards, write the `-full.bin` or the `-update.bin`, never both.
- `SHA256SUMS.txt` in each release covers every file: `shasum -a 256 -c SHA256SUMS.txt`.

Install guides: [nRF52840 (UF2)](docs/install/nrf52-uf2.md) · [ESP32 (esptool or web)](docs/install/esp32-s3.md) · [T-Display SF32 (one-click installer)](docs/install/sf32.md)

## Wio Tracker L2 Pro: brochure, manual and screens

- [Cairn brochure (PDF)](docs/Cairn_Wio_L2_Pro_Brochure.pdf): the firmware, the board and the 3D-printed case, in nine pages.
- [Cairn user manual (PDF)](docs/Cairn_Wio_L2_Pro_User_Manual.pdf): every screen and setting, explained step by step. The offline-map tool it mentions is [tools/l2_maptiles.py](tools/l2_maptiles.py) ([how to use it](tools/L2_MAPTILES.md)).
- The touch features are listed on the [L2 Pro board page](docs/boards/wio-tracker-l2-pro.md). The Heltec V4 touch, ThinkNode M9 and T-Deck run the same interface.

[![Cairn on the Wio Tracker L2 Pro](docs/promo/01_cairn_hero.jpg)](docs/promo/01_cairn_hero.jpg)

More promo images (free to share) are in [docs/promo](docs/promo).

### Screens

|                                                                            |                                                                      |                                                                      |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| ![Home](docs/screens/01-home.png)<br>Home                                  | ![Chats](docs/screens/02-chats.png)<br>Chats                         | ![Conversation](docs/screens/03-conversation.png)<br>Conversation    |
| ![Keyboard](docs/screens/04-keyboard.png)<br>Keyboard                      | ![Nodes](docs/screens/05-nodes.png)<br>Nodes                         | ![Node detail](docs/screens/06-node-detail.png)<br>Node detail       |
| ![Radio](docs/screens/07-radio.png)<br>Radio                               | ![GPS](docs/screens/08-gps.png)<br>GPS                               | ![Settings](docs/screens/09-settings.png)<br>Settings                |
| ![Lock screen](docs/screens/10-lock-screen.png)<br>Lock screen             | ![Quick panel](docs/screens/11-quick-panel.png)<br>Quick panel       | ![Spectrum](docs/screens/12-spectrum.png)<br>Spectrum                |
| ![Band scan](docs/screens/13-band-scan.png)<br>Band scan                   | ![Map](docs/screens/14-map.png)<br>Map                               | ![Repeater scan](docs/screens/15-repeater-scan.png)<br>Repeater scan |
| ![Repeater admin](docs/screens/16-repeater-admin.png)<br>Repeater admin    | ![Nodes as cards](docs/screens/17-nodes-cards.png)<br>Nodes as cards | ![Channels](docs/screens/18-channels.png)<br>Channels                |
| ![Firmware update](docs/screens/19-firmware-update.png)<br>Firmware update |                                                                      |                                                                      |

Screens use fictional sample data.

## Reporting a problem

[Open an issue](https://github.com/cvhviz/Cairn/issues/new/choose) and pick **Bug report**. The form asks for the board, the build number from the splash screen, how you installed it, and what happened. A serial log helps a lot. Reports on 🧪 preview boards are especially useful, including "it works".

## Publishing a release (for the online updater)

The L2, Heltec V4 touch, ThinkNode M9, T-Deck and T-Display SF32 builds read `https://api.github.com/repos/cvhviz/Cairn/releases/latest`. For a build to be offered:

- Tag it `cairn-vN`, where N is the build number shown on the splash (it must be higher than the device's own). Publish it as a normal release, not a draft or prerelease.
- Attach each board's `-update.bin` under its exact name, with nothing between the date and `-update.bin`. The SF32 also accepts a `.sha256` file next to its update.
- GitHub records each file's SHA-256, which the device checks, along with the size and the board's OTA marker inside the image.
- No other asset may start with one of these board prefixes and end in `-update.bin`. Preview boards use their own board names.
- The release notes are shown on the device before installing, so keep the top of them short and plain.

| Board           | Update file                                           |
| --------------- | ----------------------------------------------------- |
| L2 Pro          | `MeshCore-WioL2Pro-CairnN-YYYY-MM-DD-update.bin`      |
| Heltec V4 touch | `MeshCore-HeltecV4Touch-CairnN-YYYY-MM-DD-update.bin` |
| ThinkNode M9    | `MeshCore-ThinkNodeM9-CairnN-YYYY-MM-DD-update.bin`   |
| T-Deck          | `MeshCore-TDeckPlus-CairnN-YYYY-MM-DD-update.bin`     |
| T-Display SF32  | `MeshCore-TDisplaySF32-CairnN-YYYY-MM-DD-update.bin`  |

## Relationship to upstream

This is a personal build, not a general-purpose distribution. All core mesh and radio behaviour comes from [MeshCore](https://github.com/meshcore-dev/MeshCore). See that project for protocol documentation, the official flasher, its own list of supported hardware and the client apps. Cairn tracks MeshCore releases; the release notes say which version each build is based on. Credit to the MeshCore developers and community for the foundation.

## License

MIT, same as upstream MeshCore. The firmware embeds third-party fonts, emoji and libraries under their own licences; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [licenses/](licenses/).
