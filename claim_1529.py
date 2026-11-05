"""Claim image for poidh #1529 (Sitting Is the Proof) — deterministic, no AI art.

Draws an 8-node graph of main-stage talks with labelled edges, in the spirit of
the bounty it proposes: every edge is a claim two talks share.

    python claim_1529.py   ->  claim_1529.png  (1400x1500)
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1400, 1500
BG = (0xFA, 0xF8, 0xF3)
INK = (0x14, 0x11, 0x0F)
MUTED = (0x6B, 0x63, 0x5B)
ACCENT = (0xB3, 0x40, 0x2A)


def font(name, size):
    for p in (f"C:/Windows/Fonts/{name}", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


F_TITLE = font("arialbd.ttf", 78)
F_SUB = font("arial.ttf", 34)
F_NODE = font("arialbd.ttf", 25)
F_EDGE = font("arial.ttf", 21)
F_FOOT = font("arial.ttf", 27)
F_SMALL = font("arial.ttf", 22)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

d.text((90, 80), "SITTING IS THE PROOF", font=F_TITLE, fill=INK)
d.text((92, 178), "eight talks. one main stage. read end to end.", font=F_SUB, fill=MUTED)
d.line([(90, 240), (W - 90, 240)], fill=INK, width=2)

NODES = {
    "silicon":  (300, 400, "OPEN SILICON"),
    "boot":     (700, 350, "THE BOOTLOADER"),
    "rpc":      (1090, 440, "RPC SEES TOO MUCH"),
    "pq":       (1170, 760, "POST-QUANTUM"),
    "finality": (760, 690, "FAST FINALITY"),
    "agent":    (330, 740, "AGENT WALLETS"),
    "kzg":      (1070, 1030, "KZG CEREMONY '22"),
    "lavamoat": (400, 1040, "LAVAMOAT '19"),
}

EDGES = [
    ("silicon", "boot", "the same argument, ninety minutes apart", INK, 2),
    ("boot", "rpc", "again, and nobody said it out loud", INK, 2),
    ("pq", "kzg", "the window moved four years", ACCENT, 3),
    ("agent", "lavamoat", "a word that did not exist in 2019", ACCENT, 3),
    ("finality", "rpc", "one number, three different figures", INK, 2),
    ("finality", "pq", "both were promised a date", MUTED, 2),
]


def label(xy, text, f, fill, pad=6):
    tw = d.textlength(text, font=f)
    x, y = xy
    d.rectangle([x - pad, y - pad, x + tw + pad, y + 20 + pad], fill=BG)
    d.text((x, y), text, font=f, fill=fill)


positions = []
for a, b, text, col, width in EDGES:
    x1, y1, _ = NODES[a]
    x2, y2, _ = NODES[b]
    d.line([(x1, y1), (x2, y2)], fill=col, width=width)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    n = (dx * dx + dy * dy) ** 0.5 or 1
    ox, oy = -dy / n * 34, dx / n * 34
    tw = d.textlength(text, font=F_EDGE)
    positions.append((mx + ox - tw / 2, my + oy - 12, text, col))

# labels last, so lines never cross them
for x, y, text, col in positions:
    label((x, y), text, F_EDGE, col)

for key, (x, y, name) in NODES.items():
    r = 15
    col = ACCENT if key in ("kzg", "lavamoat") else INK
    d.ellipse([x - r, y - r, x + r, y + r], fill=col)
    tw = d.textlength(name, font=F_NODE)
    label((x - tw / 2, y + r + 8), name, F_NODE, col)

d.line([(90, 1230), (W - 90, 1230)], fill=MUTED, width=1)
d.text((90, 1262), "Every quote carries a timestamp. One fabricated quote voids the claim.", font=F_FOOT, fill=INK)
d.text((90, 1306), "Red edges cross years. Black edges cross a single morning.", font=F_SMALL, fill=MUTED)
d.text((90, 1360), "This bounty does not pay for insight. It pays for attendance.", font=F_FOOT, fill=ACCENT)
d.text((90, 1408), "Devcon 8, Mumbai, November 2026  ·  from the Ethereum TV archive", font=F_SMALL, fill=MUTED)

img.save("claim_1529.png", optimize=True)
print("wrote claim_1529.png", img.size)
