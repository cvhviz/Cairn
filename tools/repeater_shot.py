#!/usr/bin/env python3
"""Screenshot a Cairn compact repeater (REPEATER_UI_COMPACT builds) over its USB serial CLI.

  uvx --with pyserial --with pillow python tools/repeater_shot.py OUT.png [--port PORT] [--scale N]
      [--before "ui click" ...]

Sends "shot" (after any --before commands, e.g. "ui click" to step to the next page), reads
SHOT_BEGIN <w> <h> / R<y>:<hex RGB565 rows> / SHOT_END <pixel sum> (DisplayDriver::dumpFrame),
checks every row arrived and the sum matches, and writes a PNG, scaled up N times (default 3) with
nearest-neighbour so the pixels stay crisp.
"""
import argparse, glob, re, sys, time

import serial
from PIL import Image


def find_port():
    ports = glob.glob('/dev/cu.usbmodem*') + glob.glob('/dev/ttyACM*')
    if not ports:
        sys.exit('no serial port found (is the repeater on USB?)')
    return ports[0]


def cmd(s, line, wait=0.6):
    s.write((line + '\r').encode())
    time.sleep(wait)
    return s.read(65536).decode('utf-8', 'replace')


def shot(s, tries=3):
    for attempt in range(tries):
        s.reset_input_buffer()
        s.write(b'shot\r')
        buf, t0 = '', time.time()
        while time.time() - t0 < 20:
            buf += s.read(65536).decode('utf-8', 'replace')
            if 'SHOT_END' in buf and buf.rstrip().endswith(tuple('0123456789')) or 'SHOT_ERR' in buf:
                time.sleep(0.2)
                buf += s.read(65536).decode('utf-8', 'replace')
                break
        if 'SHOT_ERR' in buf:
            sys.exit(buf[buf.index('SHOT_ERR'):].splitlines()[0])
        b = re.search(r'SHOT_BEGIN (\d+) (\d+)', buf)
        e = re.search(r'SHOT_END (\d+)', buf)
        if not b or not e:
            print('  attempt %d: markers missing' % (attempt + 1), file=sys.stderr)
            continue
        w, h = int(b.group(1)), int(b.group(2))
        rows = {int(m.group(1)): m.group(2) for m in re.finditer(r'R(\d+):([0-9A-F]+)', buf[b.end():e.start()])}
        if len(rows) != h or any(len(rows.get(y, '')) != w * 4 for y in range(h)):
            print('  attempt %d: %d of %d rows complete' % (attempt + 1, sum(len(rows.get(y, '')) == w * 4 for y in range(h)), h), file=sys.stderr)
            continue
        px = [int(rows[y][x * 4:x * 4 + 4], 16) for y in range(h) for x in range(w)]
        if sum(px) != int(e.group(1)):
            print('  attempt %d: checksum mismatch' % (attempt + 1), file=sys.stderr)
            continue
        img = Image.new('RGB', (w, h))
        img.putdata([(((c >> 11) & 31) * 255 // 31, ((c >> 5) & 63) * 255 // 63, (c & 31) * 255 // 31) for c in px])
        return img
    sys.exit('screenshot failed after %d tries' % tries)


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    p.add_argument('out')
    p.add_argument('--port')
    p.add_argument('--scale', type=int, default=3)
    p.add_argument('--before', action='append', default=[], help='a serial command to send first (repeatable)')
    a = p.parse_args()
    s = serial.Serial(a.port or find_port(), 115200, timeout=0.3)
    time.sleep(0.5)
    s.read(65536)
    for c in a.before:
        cmd(s, c)
    img = shot(s)
    if a.scale > 1:
        img = img.resize((img.width * a.scale, img.height * a.scale), Image.NEAREST)
    img.save(a.out)
    print('wrote %s (%dx%d)' % (a.out, img.width, img.height))


if __name__ == '__main__':
    main()
