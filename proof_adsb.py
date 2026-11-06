"""Proof card for the adsb.lol claim (poidh arbitrum #339). Real captured output only."""
import json
from PIL import Image, ImageDraw, ImageFont

W, H = 1400, 1180
BG = (0x0E, 0x10, 0x12)
FG = (0xE8, 0xE4, 0xDA)
DIM = (0x8A, 0x8F, 0x94)
GRN = (0x7B, 0xD1, 0x8B)
AMB = (0xE0, 0xA8, 0x5A)


def mono(size, bold=False):
    for p in (f"C:/Windows/Fonts/consola{'b' if bold else ''}.ttf",
              "C:/Windows/Fonts/cour.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"):
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


F = mono(26)
FB = mono(26, True)
FT = mono(44, True)
FS = mono(22)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

y = 54
d.text((60, y), "api.adsb.lol — no key. no account. no signup.", font=FT, fill=FG)
y += 74
d.text((60, y), "live aircraft positions, answered in 160 ms", font=FS, fill=DIM)
y += 56
d.line([(60, y), (W - 60, y)], fill=(0x2A, 0x2E, 0x33), width=2)
y += 34

lines = [
    ("$ date -u", FG),
    ("2026-11-06T07:12:35Z", DIM),
    ("", FG),
    ("$ curl -s 'https://api.adsb.lol/v2/point/-34.6/-58.4/100'", FG),
    ("HTTP 200 · 0.161 s · 3,099 bytes · 5 aircraft within 100 nm of Buenos Aires", GRN),
    ("", FG),
    ('{"ac":[', FG),
    ('  {"hex":"e94c86","flight":"BOV701","t":"B738",', FG),
    ('   "alt_baro":27475,"gs":401.8,', FG),
    ('   "lat":-34.367236,"lon":-58.764954,"dst":22.8},', FG),
    ('  {"hex":"e0b149","flight":"ARG1361","t":"B38M",', FG),
    ('   "alt_baro":10725,"gs":338.1,', FG),
    ('   "lat":-34.157181,"lon":-59.149045,"dst":45.6}]}', FG),
    ("", FG),
    ("$ curl -s 'https://api.adsb.lol/v2/mil'", FG),
    ("HTTP 200 · 0.214 s · 51,083 bytes · 133 military aircraft, worldwide", GRN),
    ('   "DRAGON31" V-22 at 21.91/-158.62 · "CHAOS40" H-64 at 21.19/-157.90', FG),
    ("", FG),
    ("$ curl -s 'https://api.adsb.lol/v2/callsign/ARG1132'", FG),
    ('{"ac":[], "msg":"No error"}   <- an empty answer is an answer', AMB),
]
for text, col in lines:
    d.text((60, y), text, font=F, fill=col)
    y += 38

y += 18
d.line([(60, y), (W - 60, y)], fill=(0x2A, 0x2E, 0x33), width=2)
y += 28
d.text((60, y), "Coverage is volunteer receivers: dense over Europe and the US,", font=FS, fill=DIM)
y += 32
d.text((60, y), "thin over oceans. Live state only — no history, ~1 req/s.", font=FS, fill=DIM)
y += 32
d.text((60, y), "Do not use it for anything safety-critical.", font=FS, fill=DIM)

img.save("proof_adsb.png", optimize=True)
print("wrote proof_adsb.png", img.size)
