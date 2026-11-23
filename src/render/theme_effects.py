# -*- coding: utf-8 -*-
"""
Multi-Style Callout & Visual Effect Engine (TASTE-73 & TASTE-74)
================================================================
Provides episode-specific & chapter-specific themed designs for:
  1. Data Callout Stickers (render_themed_sticker)
  2. Animated Pointer Arrows (draw_themed_arrow)
  3. Target Lock-On Reticles (draw_themed_ring)
  4. Chapter Transition Cards (render_themed_chapter_card)
  5. Subtle Background Paper Accents (decorate_paper)

Themes automatically map from episode.json `format` (F1..F7) or `art.sticker_style`:
  - F5 -> 'biolab'        (Sci-Fi Bio-Lab Containment HUD, Barcode, Hex Grid, Acid Neon Laser)
  - F2 -> 'blueprint'     (Riveted CAD Engineering Plaque, Caliper Ticks, Dimension Arrow, Radar Crosshair)
  - F1 -> 'medical'       (Clinical ECG Monitor, Medical Cross, Pulse Wave Arrow, X-Ray Sonar Ring)
  - F3 -> 'detective'     (Crime-Scene Evidence Tag, Hazard Tape, Red Wax Seal, Red String & Magnifier)
  - F4 -> 'cryo_survival' (Crystalline Frost & Thermal Gauge, Ice-Beam Spear, 6-Point Snowflake Reticle)
  - F6 -> 'syndicate'     (Royal Mafia Baroque Crest, Gold Filigree & Crown, Scepter Arrow, 8-Point Star)
  - F7 -> 'rpg'           (RPG Boss Stat Window, HP/EXP Bar, Lightning Bolt Arrow, Dual Diamond Lock-On)
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
FONT_BOLD = str(ROOT / "assets/fonts/BeVietnamPro-Bold.ttf")
FONT_HAND = str(ROOT / "assets/fonts/Mali-Bold.ttf")

FORMAT_TO_THEME = {
    "F1": "medical",
    "F2": "blueprint",
    "F3": "detective",
    "F4": "cryo_survival",
    "F5": "biolab",
    "F6": "syndicate",
    "F7": "rpg",
    "LEGACY_6CH": "rpg",
    "F_SPECIAL": "syndicate",
}

THEME_PALETTES = {
    "biolab": [
        (57, 255, 20),    # Acid Neon Green
        (0, 245, 212),    # Cyber Bio Cyan
        (255, 214, 10),   # Bio-Hazard Gold
        (255, 42, 133),   # Plasma Mutagen Pink
        (168, 85, 247),   # Laboratory Violet
    ],
    "blueprint": [
        (255, 195, 0),    # Engineering Amber
        (0, 229, 255),    # CAD Cyan
        (255, 107, 0),    # Industrial Orange
        (114, 239, 221),  # Gauge Mint
    ],
    "medical": [
        (0, 229, 255),    # Clinical Cyan
        (46, 230, 166),   # ECG Vital Green
        (255, 77, 109),   # Emergency Pulse Red
        (255, 209, 102),  # Amber Alert
    ],
    "detective": [
        (193, 18, 31),    # Evidence Crimson
        (217, 119, 6),    # Amber Dossier
        (30, 64, 175),    # Ink Stamp Blue
        (153, 27, 27),    # Wax Seal Red
    ],
    "cryo_survival": [
        (72, 202, 228),   # Subzero Ice Cyan
        (255, 107, 0),    # Thermal Survival Orange
        (144, 224, 239),  # Frost Crystal Blue
        (255, 183, 3),    # Solar Flare Gold
    ],
    "syndicate": [
        (255, 215, 0),    # Royal Gold
        (255, 77, 109),   # Ruby Crest
        (244, 162, 97),   # Bronze Crown
        (0, 245, 212),    # Imperial Jade
    ],
    "rpg": [
        (255, 183, 3),    # Legendary Gold
        (255, 77, 0),     # Fire Crit Orange
        (0, 245, 212),    # Mana Cyan
        (181, 23, 158),   # Epic Arcane Purple
    ],
}


def _font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def _fit_font(path: str, text: str, max_w: int, start: int, min_size: int = 18) -> ImageFont.FreeTypeFont:
    size = start
    while size > min_size:
        f = _font(path, size)
        if f.getlength(text) <= max_w:
            return f
        size -= 2
    return _font(path, min_size)


def _pil_to_rgba_bgr(img: Image.Image) -> np.ndarray:
    arr = np.array(img)
    return arr[:, :, [2, 1, 0, 3]].copy()


def resolve_theme(proj: Path | None) -> tuple[str, list[tuple]]:
    """Determine the episode visual effect theme and color palette from episode.json."""
    theme = "biolab"
    if proj is not None:
        ep_file = proj / "episode.json"
        if ep_file.exists():
            try:
                ep = json.loads(ep_file.read_text(encoding="utf-8"))
                art = ep.get("art", {})
                if art.get("sticker_style"):
                    theme = art["sticker_style"]
                else:
                    fmt = ep.get("format", "F5")
                    theme = FORMAT_TO_THEME.get(fmt, "biolab")
            except Exception:
                pass
    palette = THEME_PALETTES.get(theme, THEME_PALETTES["biolab"])
    return theme, palette


def decorate_paper(paper: np.ndarray, theme: str = "biolab") -> np.ndarray:
    """Add subtle, non-intrusive themed HUD/background accents to the outer border of the paper."""
    h, w = paper.shape[:2]
    out = paper.copy()
    if theme == "biolab":
        # Subtle scientific crosshairs '+' and faint corner lab frame ticks
        col = (218, 232, 224)  # very light bio-mint tint in BGR
        step = 72 if w > 1200 else 64
        for y in range(36, h, step):
            for x in range(36, w, step):
                cv2.line(out, (x - 3, y), (x + 3, y), col, 1, cv2.LINE_AA)
                cv2.line(out, (x, y - 3), (x, y + 3), col, 1, cv2.LINE_AA)
    elif theme == "blueprint":
        col = (235, 224, 212)  # light blueprint grid tint
        step = 60
        for x in range(0, w, step):
            cv2.line(out, (x, 0), (x, h), col, 1)
        for y in range(0, h, step):
            cv2.line(out, (0, y), (w, y), col, 1)
    elif theme == "medical":
        col = (232, 232, 214)
        step = 64
        for y in range(32, h, step):
            for x in range(32, w, step):
                cv2.circle(out, (x, y), 2, col, 1, cv2.LINE_AA)
    return out


def _draw_chamfer_rect(d: ImageDraw.ImageDraw, box: list[int], cut: int, fill=None, outline=None, width: int = 1):
    x0, y0, x1, y1 = box
    pts = [
        (x0 + cut, y0),
        (x1 - cut, y0),
        (x1, y0 + cut),
        (x1, y1 - cut),
        (x1 - cut, y1),
        (x0 + cut, y1),
        (x0, y1 - cut),
        (x0, y0 + cut),
    ]
    d.polygon(pts, fill=fill, outline=outline, width=width)


def _draw_hex(d: ImageDraw.ImageDraw, cx: float, cy: float, r: float, fill=None, outline=None, width: int = 2):
    pts = []
    for k in range(6):
        a = math.pi / 3 * k - math.pi / 6
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=fill, outline=outline, width=width)


def render_themed_sticker(value: str, label: str, color_rgb: tuple, max_w: int = 340,
                          theme: str = "biolab", variant: int = 0) -> np.ndarray:
    """Render a custom themed data callout sticker card (2x supersampled for crisp edges)."""
    S = 2
    fv = _fit_font(FONT_BOLD, value, (max_w - 52) * S, 54 * S)
    fl = _fit_font(FONT_BOLD, label.upper(), (max_w - 44) * S, 24 * S)
    vw = fv.getlength(value)
    lw = fl.getlength(label.upper())
    bw = int(max(vw + 96 * S, lw + 76 * S, 240 * S))
    bh = 152 * S
    pad = 16 * S
    cw, ch = bw + pad * 2, bh + pad * 2
    img = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    x0, y0 = pad, pad
    x1, y1 = pad + bw, pad + bh
    cx = (x0 + x1) / 2

    if theme == "biolab":
        # Sci-Fi Bio-Lab Containment HUD Card (Dark Purple/Obsidian + Neon Acid/Cyan Tube Rim + Barcode Header)
        cut = 20 * S
        # Sub-variants cycle chamber background hue slightly (Deep Bio-Purple, Dark Cyber-Teal, Obsidian Lab)
        bg_styles = [
            ((24, 13, 44, 248), (44, 22, 78, 252), "BIO-LAB #32"),
            ((11, 31, 42, 248), (18, 54, 71, 252), "SPECIMEN HUD"),
            ((28, 16, 38, 248), (52, 24, 66, 252), "MUTAGEN SCAN"),
            ((14, 28, 24, 248), (22, 52, 42, 252), "CELL MATRIX"),
        ]
        bg_top, bg_bot, tag_txt = bg_styles[variant % len(bg_styles)]
        neon = color_rgb + (255,)
        neon_dim = (color_rgb[0], color_rgb[1], color_rgb[2], 95)
        ink = (10, 8, 18, 255)

        # Outer neon glow shadow
        _draw_chamfer_rect(d, [x0 + 6 * S, y0 + 8 * S, x1 + 6 * S, y1 + 8 * S], cut, fill=(0, 0, 0, 130))
        _draw_chamfer_rect(d, [x0 - 3 * S, y0 - 3 * S, x1 + 3 * S, y1 + 3 * S], cut + 2 * S, outline=neon_dim, width=4 * S)

        # Main chamfered body
        _draw_chamfer_rect(d, [x0, y0, x1, y1], cut, fill=bg_top, outline=ink, width=5 * S)

        # Top header bar inside card
        hdr_h = 30 * S
        _draw_chamfer_rect(d, [x0 + 5 * S, y0 + 5 * S, x1 - 5 * S, y0 + hdr_h], 14 * S, fill=bg_bot)
        d.line([(x0 + 8 * S, y0 + hdr_h), (x1 - 8 * S, y0 + hdr_h)], fill=neon, width=2 * S)

        # Mini barcode on top-left
        bx = x0 + 22 * S
        for bi, w_bar in enumerate([3, 1, 4, 2, 1, 3, 2, 1, 3]):
            if bi % 2 == 0:
                d.rectangle([bx, y0 + 10 * S, bx + w_bar * S, y0 + 24 * S], fill=neon)
            bx += (w_bar + 2) * S

        # Micro lab tag text in header
        ftag = _font(FONT_BOLD, 14 * S)
        d.text((bx + 8 * S, y0 + 17 * S), tag_txt, font=ftag, fill=(210, 235, 255, 220), anchor="lm")

        # 3 glowing LED dots on top-right
        for li, lcol in enumerate([(57, 255, 20, 255), (255, 214, 10, 255), neon]):
            lx = x1 - (24 + li * 14) * S
            ly = y0 + 17 * S
            d.ellipse([lx - 4 * S, ly - 4 * S, lx + 4 * S, ly + 4 * S], fill=lcol, outline=ink, width=1 * S)

        # Inner glowing neon tube border
        _draw_chamfer_rect(d, [x0 + 5 * S, y0 + 5 * S, x1 - 5 * S, y1 - 5 * S], cut - 3 * S, outline=neon, width=4 * S)

        # Decorative molecular hexagons on left/right sides
        _draw_hex(d, x0 + 24 * S, y0 + 68 * S, 11 * S, fill=(255, 255, 255, 25), outline=neon, width=2 * S)
        _draw_hex(d, x1 - 24 * S, y0 + 68 * S, 11 * S, fill=(255, 255, 255, 25), outline=neon, width=2 * S)

        # Value text (large glowing neon with dark stroke)
        vy = y0 + 69 * S
        d.text((cx + 3 * S, vy + 4 * S), value, font=fv, fill=(0, 0, 0, 180), anchor="mm", stroke_width=6 * S, stroke_fill=(0, 0, 0, 180))
        d.text((cx, vy), value, font=fv, fill=neon, anchor="mm", stroke_width=5 * S, stroke_fill=ink)

        # Bottom label pill bar
        ly0, ly1 = y1 - 44 * S, y1 - 10 * S
        d.rounded_rectangle([x0 + 16 * S, ly0, x1 - 16 * S, ly1], 12 * S, fill=(10, 8, 20, 230), outline=neon_dim, width=2 * S)
        d.text((cx, (ly0 + ly1) / 2), label.upper(), font=fl, fill=(245, 252, 255, 255), anchor="mm")

    elif theme == "blueprint":
        # Riveted CAD Engineering Blueprint Plaque
        bg = (12, 38, 78, 248)
        gold = (255, 195, 0, 255)
        cyan = (0, 229, 255, 255)
        ink = (10, 16, 28, 255)
        d.rounded_rectangle([x0 + 6 * S, y0 + 8 * S, x1 + 6 * S, y1 + 8 * S], 14 * S, fill=(0, 0, 0, 120))
        d.rounded_rectangle([x0, y0, x1, y1], 14 * S, fill=bg, outline=ink, width=5 * S)
        # Engineering grid lines
        for gx in range(x0 + 20 * S, x1 - 10 * S, 24 * S):
            d.line([(gx, y0 + 8 * S), (gx, y1 - 8 * S)], fill=(255, 255, 255, 22), width=1 * S)
        for gy in range(y0 + 20 * S, y1 - 10 * S, 24 * S):
            d.line([(x0 + 8 * S, gy), (x1 - 8 * S, gy)], fill=(255, 255, 255, 22), width=1 * S)
        # Caliper ruler ticks along top edge
        for tx in range(x0 + 28 * S, x1 - 24 * S, 12 * S):
            th = 10 * S if ((tx - x0) // (12 * S)) % 2 == 0 else 6 * S
            d.line([(tx, y0 + 6 * S), (tx, y0 + 6 * S + th)], fill=cyan, width=2 * S)
        d.rounded_rectangle([x0 + 5 * S, y0 + 5 * S, x1 - 5 * S, y1 - 5 * S], 10 * S, outline=gold, width=4 * S)
        # 4 corner hex rivets
        for rx, ry in [(x0 + 16 * S, y0 + 16 * S), (x1 - 16 * S, y0 + 16 * S),
                       (x0 + 16 * S, y1 - 16 * S), (x1 - 16 * S, y1 - 16 * S)]:
            d.ellipse([rx - 5 * S, ry - 5 * S, rx + 5 * S, ry + 5 * S], fill=gold, outline=ink, width=2 * S)
        d.text((cx, y0 + 62 * S), value, font=fv, fill=gold, anchor="mm", stroke_width=5 * S, stroke_fill=ink)
        d.rounded_rectangle([x0 + 22 * S, y1 - 44 * S, x1 - 22 * S, y1 - 12 * S], 8 * S, fill=(6, 20, 44, 230), outline=cyan, width=2 * S)
        d.text((cx, y1 - 28 * S), label.upper(), font=fl, fill=(230, 248, 255, 255), anchor="mm")

    elif theme == "medical":
        # Clinical ECG & X-Ray Monitor Card
        bg = (8, 38, 46, 248)
        cyan = color_rgb + (255,)
        ink = (6, 18, 22, 255)
        d.rounded_rectangle([x0 + 6 * S, y0 + 8 * S, x1 + 6 * S, y1 + 8 * S], 22 * S, fill=(0, 0, 0, 120))
        d.rounded_rectangle([x0, y0, x1, y1], 22 * S, fill=bg, outline=ink, width=5 * S)
        d.rounded_rectangle([x0 + 5 * S, y0 + 5 * S, x1 - 5 * S, y1 - 5 * S], 18 * S, outline=cyan, width=4 * S)
        # Red medical cross badge top-left
        mx, my = x0 + 24 * S, y0 + 24 * S
        d.ellipse([mx - 11 * S, my - 11 * S, mx + 11 * S, my + 11 * S], fill=(220, 38, 38, 255), outline=(255, 255, 255, 255), width=2 * S)
        d.rectangle([mx - 3 * S, my - 7 * S, mx + 3 * S, my + 7 * S], fill=(255, 255, 255, 255))
        d.rectangle([mx - 7 * S, my - 3 * S, mx + 7 * S, my + 3 * S], fill=(255, 255, 255, 255))
        # ECG waveform line above label
        ey = y1 - 48 * S
        ecg_pts = [(x0 + 18 * S, ey), (cx - 28 * S, ey), (cx - 18 * S, ey - 10 * S), (cx - 8 * S, ey + 12 * S),
                   (cx + 4 * S, ey - 18 * S), (cx + 14 * S, ey + 8 * S), (cx + 24 * S, ey), (x1 - 18 * S, ey)]
        d.line(ecg_pts, fill=(46, 230, 166, 200), width=3 * S)
        d.text((cx + 8 * S, y0 + 56 * S), value, font=fv, fill=cyan, anchor="mm", stroke_width=5 * S, stroke_fill=ink)
        d.text((cx, y1 - 24 * S), label.upper(), font=fl, fill=(240, 255, 255, 255), anchor="mm")

    elif theme == "detective":
        # Crime-Scene Classified Dossier Evidence Card
        bg = (255, 245, 214, 252)
        ink = (24, 20, 18, 255)
        red = (193, 18, 31, 255)
        gold = (245, 158, 11, 255)
        d.rounded_rectangle([x0 + 7 * S, y0 + 9 * S, x1 + 7 * S, y1 + 9 * S], 12 * S, fill=(0, 0, 0, 115))
        d.rounded_rectangle([x0, y0, x1, y1], 12 * S, fill=bg, outline=ink, width=5 * S)
        # Yellow-black crime scene hazard stripe top bar
        d.rectangle([x0 + 5 * S, y0 + 5 * S, x1 - 5 * S, y0 + 24 * S], fill=gold)
        for sx in range(x0 + 10 * S, x1 - 10 * S, 24 * S):
            d.polygon([(sx, y0 + 5 * S), (sx + 12 * S, y0 + 5 * S), (sx + 4 * S, y0 + 24 * S), (sx - 8 * S, y0 + 24 * S)], fill=ink)
        d.line([(x0 + 5 * S, y0 + 24 * S), (x1 - 5 * S, y0 + 24 * S)], fill=ink, width=3 * S)
        # Red wax seal dot
        d.ellipse([x0 + 16 * S, y0 + 34 * S, x0 + 34 * S, y0 + 52 * S], fill=red, outline=ink, width=2 * S)
        d.text((cx + 6 * S, y0 + 66 * S), value, font=fv, fill=red, anchor="mm", stroke_width=3 * S, stroke_fill=ink)
        d.rectangle([x0 + 18 * S, y1 - 42 * S, x1 - 18 * S, y1 - 12 * S], fill=(32, 28, 24, 245))
        d.text((cx, y1 - 27 * S), label.upper(), font=fl, fill=(255, 240, 200, 255), anchor="mm")

    elif theme == "cryo_survival":
        # Subzero Frost Crystal & Thermal Gauge Plaque
        cut = 22 * S
        bg = (10, 28, 56, 248)
        ice = (72, 202, 228, 255)
        accent = color_rgb + (255,)
        ink = (8, 14, 28, 255)
        _draw_chamfer_rect(d, [x0 + 6 * S, y0 + 8 * S, x1 + 6 * S, y1 + 8 * S], cut, fill=(0, 0, 0, 125))
        _draw_chamfer_rect(d, [x0, y0, x1, y1], cut, fill=bg, outline=ink, width=5 * S)
        _draw_chamfer_rect(d, [x0 + 5 * S, y0 + 5 * S, x1 - 5 * S, y1 - 5 * S], cut - 3 * S, outline=ice, width=4 * S)
        d.text((cx, y0 + 60 * S), value, font=fv, fill=accent, anchor="mm", stroke_width=5 * S, stroke_fill=ink)
        d.rounded_rectangle([x0 + 18 * S, y1 - 44 * S, x1 - 18 * S, y1 - 12 * S], 12 * S, fill=(6, 18, 38, 235), outline=accent, width=2 * S)
        d.text((cx, y1 - 28 * S), label.upper(), font=fl, fill=(240, 252, 255, 255), anchor="mm")

    elif theme == "syndicate":
        # Royal Baroque Mafia Syndicate Crest
        bg = (38, 8, 18, 250)
        gold = (255, 215, 0, 255)
        ink = (14, 6, 10, 255)
        d.rounded_rectangle([x0 + 6 * S, y0 + 8 * S, x1 + 6 * S, y1 + 8 * S], 20 * S, fill=(0, 0, 0, 130))
        d.rounded_rectangle([x0, y0, x1, y1], 20 * S, fill=bg, outline=ink, width=5 * S)
        d.rounded_rectangle([x0 + 5 * S, y0 + 5 * S, x1 - 5 * S, y1 - 5 * S], 16 * S, outline=gold, width=4 * S)
        d.rounded_rectangle([x0 + 11 * S, y0 + 11 * S, x1 - 11 * S, y1 - 11 * S], 12 * S, outline=(255, 215, 0, 110), width=2 * S)
        d.text((cx, y0 + 60 * S), value, font=fv, fill=gold, anchor="mm", stroke_width=5 * S, stroke_fill=ink)
        d.rounded_rectangle([x0 + 20 * S, y1 - 44 * S, x1 - 20 * S, y1 - 14 * S], 10 * S, fill=(20, 4, 10, 235), outline=gold, width=2 * S)
        d.text((cx, y1 - 29 * S), label.upper(), font=fl, fill=(255, 245, 220, 255), anchor="mm")

    else:
        # RPG Boss Battle HUD Stat Card
        cut = 18 * S
        bg = (24, 18, 36, 248)
        gold = color_rgb + (255,)
        ink = (12, 8, 18, 255)
        _draw_chamfer_rect(d, [x0 + 6 * S, y0 + 8 * S, x1 + 6 * S, y1 + 8 * S], cut, fill=(0, 0, 0, 125))
        _draw_chamfer_rect(d, [x0, y0, x1, y1], cut, fill=bg, outline=ink, width=5 * S)
        _draw_chamfer_rect(d, [x0 + 5 * S, y0 + 5 * S, x1 - 5 * S, y1 - 5 * S], cut - 3 * S, outline=gold, width=4 * S)
        d.text((cx, y0 + 60 * S), value, font=fv, fill=gold, anchor="mm", stroke_width=5 * S, stroke_fill=ink)
        d.rounded_rectangle([x0 + 18 * S, y1 - 44 * S, x1 - 18 * S, y1 - 12 * S], 10 * S, fill=(12, 8, 20, 235), outline=gold, width=2 * S)
        d.text((cx, y1 - 28 * S), label.upper(), font=fl, fill=(255, 250, 235, 255), anchor="mm")

    img = img.resize((cw // S, ch // S), Image.LANCZOS)
    return _pil_to_rgba_bgr(img)


def draw_themed_arrow(canvas: np.ndarray, p0: tuple, p1: tuple, progress: float,
                      color_bgr: tuple, bend: float, opacity: float = 1.0,
                      theme: str = "biolab", t: float = 0.0) -> None:
    """Draw a themed animated pointer arrow from sticker edge p0 to target p1."""
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    L = max(1.0, math.hypot(dx, dy))
    nx, ny = -dy / L, dx / L
    cx, cy = (x0 + x1) / 2 + nx * bend * L, (y0 + y1) / 2 + ny * bend * L
    head = 32.0
    n = 52
    pts = []
    for i in range(n + 1):
        u = i / n
        pts.append(((1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u * u * x1,
                    (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u * u * y1))
    acc, cut = 0.0, n
    for i in range(n, 0, -1):
        acc += math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1])
        if acc >= head * 0.72:
            cut = i
            break
    shaft_u = min(1.0, progress / 0.75)
    k = max(2, int(cut * shaft_u) + 1)
    layer = canvas.copy()
    shaft = np.array(pts[:k], np.int32)
    outline = (18, 12, 22)

    if theme == "biolab":
        # Outer neon plasma aura
        glow_layer = layer.copy()
        cv2.polylines(glow_layer, [shaft], False, color_bgr, 20, cv2.LINE_AA)
        cv2.addWeighted(glow_layer, 0.28, layer, 0.72, 0, dst=layer)

        # Dark conduit casing + bright neon laser core + white inner filament
        cv2.polylines(layer, [shaft], False, outline, 13, cv2.LINE_AA)
        cv2.polylines(layer, [shaft], False, color_bgr, 8, cv2.LINE_AA)
        cv2.polylines(layer, [shaft], False, (245, 255, 245), 2, cv2.LINE_AA)

        # Animated bio-energy pulse orbs traveling along the conduit toward the target
        if progress >= 0.5:
            for orb_k in range(3):
                u_orb = ((t * 1.4 + orb_k / 3.0) % 1.0) * shaft_u
                idx_orb = min(k - 1, max(0, int(u_orb * cut)))
                ox, oy = int(pts[idx_orb][0]), int(pts[idx_orb][1])
                cv2.circle(layer, (ox, oy), 8, color_bgr, -1, cv2.LINE_AA)
                cv2.circle(layer, (ox, oy), 4, (255, 255, 255), -1, cv2.LINE_AA)

        # Sci-Fi Diamond Chevron Lance Head
        if progress > 0.75:
            hs = min(1.0, (progress - 0.75) / 0.25)
            xa, ya = pts[cut]
            ang = math.atan2(y1 - ya, x1 - xa)
            tipx, tipy = x1, y1
            Lh, Wh = head * (0.65 + 0.35 * hs), 19 * (0.65 + 0.35 * hs)
            bx, by = tipx - math.cos(ang) * Lh, tipy - math.sin(ang) * Lh
            mx, my = tipx - math.cos(ang) * (Lh * 0.72), tipy - math.sin(ang) * (Lh * 0.72)
            px, py = -math.sin(ang), math.cos(ang)
            chevron = np.array([
                [tipx, tipy],
                [bx + px * Wh, by + py * Wh],
                [mx, my],
                [bx - px * Wh, by - py * Wh]
            ], np.int32)
            cv2.fillPoly(layer, [chevron], color_bgr, cv2.LINE_AA)
            cv2.polylines(layer, [chevron], True, outline, 4, cv2.LINE_AA)
            cv2.circle(layer, (int(tipx), int(tipy)), 4, (255, 255, 255), -1, cv2.LINE_AA)

    elif theme == "blueprint":
        # Engineering CAD Dimension Leader with perpendicular measurement ticks
        cv2.polylines(layer, [shaft], False, outline, 12, cv2.LINE_AA)
        cv2.polylines(layer, [shaft], False, color_bgr, 6, cv2.LINE_AA)
        for ti in range(4, k - 2, 6):
            tx, ty = pts[ti]
            tx_p, ty_p = pts[ti - 1]
            tang = math.atan2(ty - ty_p, tx - tx_p)
            pnx, pny = -math.sin(tang) * 9, math.cos(tang) * 9
            cv2.line(layer, (int(tx - pnx), int(ty - pny)), (int(tx + pnx), int(ty + pny)), outline, 4, cv2.LINE_AA)
            cv2.line(layer, (int(tx - pnx), int(ty - pny)), (int(tx + pnx), int(ty + pny)), color_bgr, 2, cv2.LINE_AA)
        if progress > 0.75:
            hs = min(1.0, (progress - 0.75) / 0.25)
            xa, ya = pts[cut]
            ang = math.atan2(y1 - ya, x1 - xa)
            Lh, Wh = head * (0.6 + 0.4 * hs), 16 * (0.6 + 0.4 * hs)
            bx, by = x1 - math.cos(ang) * Lh, y1 - math.sin(ang) * Lh
            px, py = -math.sin(ang), math.cos(ang)
            tri = np.array([[x1, y1], [bx + px * Wh, by + py * Wh], [bx - px * Wh, by - py * Wh]], np.int32)
            cv2.fillPoly(layer, [tri], color_bgr, cv2.LINE_AA)
            cv2.polylines(layer, [tri], True, outline, 4, cv2.LINE_AA)

    else:
        # Enhanced high-contrast themed arrow with core highlight
        cv2.polylines(layer, [shaft], False, outline, 13, cv2.LINE_AA)
        cv2.polylines(layer, [shaft], False, color_bgr, 8, cv2.LINE_AA)
        cv2.polylines(layer, [shaft], False, (255, 255, 255), 2, cv2.LINE_AA)
        if progress > 0.75:
            hs = min(1.0, (progress - 0.75) / 0.25)
            xa, ya = pts[cut]
            ang = math.atan2(y1 - ya, x1 - xa)
            Lh, Wh = head * (0.6 + 0.4 * hs), 17 * (0.6 + 0.4 * hs)
            bx, by = x1 - math.cos(ang) * Lh, y1 - math.sin(ang) * Lh
            px, py = -math.sin(ang), math.cos(ang)
            tri = np.array([[x1, y1], [bx + px * Wh, by + py * Wh], [bx - px * Wh, by - py * Wh]], np.int32)
            cv2.fillPoly(layer, [tri], color_bgr, cv2.LINE_AA)
            cv2.polylines(layer, [tri], True, outline, 4, cv2.LINE_AA)

    if opacity >= 0.999:
        canvas[:] = layer
    else:
        cv2.addWeighted(layer, opacity, canvas, 1 - opacity, 0, dst=canvas)


def draw_themed_ring(canvas: np.ndarray, p: tuple, t: float, color_bgr: tuple,
                     opacity: float = 1.0, theme: str = "biolab") -> None:
    """Draw a themed target lock-on reticle around the pointed feature p."""
    cx, cy = int(p[0]), int(p[1])
    layer = canvas.copy()
    outline = (18, 12, 22)

    if theme == "biolab":
        # 1. Rotating Hexagonal Bio-Scanner HUD
        r_hex = 28 + 4 * math.sin(2 * math.pi * 1.4 * t)
        rot = t * 1.1
        hex_pts = []
        for k in range(6):
            a = rot + k * math.pi / 3
            hex_pts.append([int(cx + r_hex * math.cos(a)), int(cy + r_hex * math.sin(a))])
        hex_arr = np.array(hex_pts, np.int32)
        cv2.polylines(layer, [hex_arr], True, outline, 6, cv2.LINE_AA)
        cv2.polylines(layer, [hex_arr], True, color_bgr, 3, cv2.LINE_AA)

        # 2. 4 Corner Lock-On Brackets [ ] pulsing outward
        b_dist = int(36 + 5 * math.cos(2 * math.pi * 1.4 * t))
        b_len = 10
        for sx, sy in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
            bx, by = cx + sx * b_dist, cy + sy * b_dist
            cv2.line(layer, (bx, by), (bx - sx * b_len, by), outline, 5, cv2.LINE_AA)
            cv2.line(layer, (bx, by), (bx, by - sy * b_len), outline, 5, cv2.LINE_AA)
            cv2.line(layer, (bx, by), (bx - sx * b_len, by), (255, 255, 255), 2, cv2.LINE_AA)
            cv2.line(layer, (bx, by), (bx, by - sy * b_len), (255, 255, 255), 2, cv2.LINE_AA)

        # 3. Expanding Sonar Bio-Pulse Ring
        sonar_u = (t * 0.9) % 1.0
        r_sonar = int(14 + 34 * sonar_u)
        cv2.circle(layer, (cx, cy), r_sonar, color_bgr, 2, cv2.LINE_AA)

    elif theme == "blueprint":
        # Engineering Caliper Crosshair Reticle
        r = int(30 + 4 * math.sin(2 * math.pi * 1.2 * t))
        cv2.circle(layer, (cx, cy), r, outline, 5, cv2.LINE_AA)
        cv2.circle(layer, (cx, cy), r, color_bgr, 3, cv2.LINE_AA)
        for k in range(4):
            a = math.pi / 2 * k + t * 0.8
            x_in, y_in = int(cx + (r - 10) * math.cos(a)), int(cy + (r - 10) * math.sin(a))
            x_out, y_out = int(cx + (r + 10) * math.cos(a)), int(cy + (r + 10) * math.sin(a))
            cv2.line(layer, (x_in, y_in), (x_out, y_out), outline, 5, cv2.LINE_AA)
            cv2.line(layer, (x_in, y_in), (x_out, y_out), color_bgr, 3, cv2.LINE_AA)

    elif theme == "cryo_survival":
        # 6-Point Rotating Frost Snowflake Reticle
        r = 32 + 5 * math.sin(2 * math.pi * 1.3 * t)
        for k in range(6):
            a = t * 0.9 + k * math.pi / 3
            x_end, y_end = int(cx + r * math.cos(a)), int(cy + r * math.sin(a))
            cv2.line(layer, (cx, cy), (x_end, y_end), color_bgr, 3, cv2.LINE_AA)
            cv2.circle(layer, (x_end, y_end), 4, (255, 255, 255), -1, cv2.LINE_AA)

    else:
        # Rotating Segmented Tech Ring + Crosshair ticks
        r = int(30 + 5 * math.sin(2 * math.pi * 1.3 * t))
        for k in range(8):
            a0 = k * 45 + t * 70
            cv2.ellipse(layer, (cx, cy), (r, r), 0, a0, a0 + 24, outline, 7, cv2.LINE_AA)
            cv2.ellipse(layer, (cx, cy), (r, r), 0, a0, a0 + 24, color_bgr, 4, cv2.LINE_AA)

    cv2.addWeighted(layer, 0.88 * opacity, canvas, 1 - 0.88 * opacity, 0, dst=canvas)


def render_themed_chapter_card(W: int, H: int, chapter_no: int, title: str, hook: str,
                               badge: str | None = None, theme: str = "biolab") -> np.ndarray:
    """Full-frame themed chapter title card (RGBA) used for ~1.6 s at each act start."""
    S = 2
    img = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    ink = (14, 10, 22, 255)
    f_no = _font(FONT_BOLD, 56 * S)
    f_t = _fit_font(FONT_BOLD, title, 1420 * S, 92 * S)
    f_h = _fit_font(FONT_BOLD, hook, 1360 * S, 42 * S)
    cy = H * S // 2
    no = badge or f"CHƯƠNG {chapter_no}"

    if theme == "biolab":
        # Central dark Bio-Lab HUD containment plaque
        px0, py0, px1, py1 = 160 * S, cy - 260 * S, (W - 160) * S, cy + 220 * S
        _draw_chamfer_rect(d, [px0 + 10 * S, py0 + 12 * S, px1 + 10 * S, py1 + 12 * S], 36 * S, fill=(0, 0, 0, 140))
        _draw_chamfer_rect(d, [px0, py0, px1, py1], 36 * S, fill=(22, 12, 42, 242), outline=ink, width=6 * S)
        _draw_chamfer_rect(d, [px0 + 8 * S, py0 + 8 * S, px1 - 8 * S, py1 - 8 * S], 30 * S, outline=(57, 255, 20, 255), width=5 * S)

        # Badge top pill
        nw = f_no.getlength(no) + 96 * S
        bx0, by0, bx1, by1 = W * S / 2 - nw / 2, cy - 210 * S, W * S / 2 + nw / 2, cy - 116 * S
        _draw_chamfer_rect(d, [bx0, by0, bx1, by1], 18 * S, fill=(147, 51, 234, 255), outline=(57, 255, 20, 255), width=4 * S)
        d.text((W * S / 2, (by0 + by1) / 2), no, font=f_no, fill=(255, 255, 255, 255), anchor="mm", stroke_width=4 * S, stroke_fill=ink)

        # Main chapter title in glowing bio-yellow
        d.text((W * S / 2 + 5 * S, cy + 6 * S), title, font=f_t, fill=(0, 0, 0, 180), anchor="mm", stroke_width=8 * S, stroke_fill=(0, 0, 0, 180))
        d.text((W * S / 2, cy), title, font=f_t, fill=(255, 214, 10, 255), anchor="mm", stroke_width=8 * S, stroke_fill=ink)

        # Hook line in glowing cyan
        d.text((W * S / 2, cy + 126 * S), hook, font=f_h, fill=(0, 245, 212, 255), anchor="mm", stroke_width=3 * S, stroke_fill=ink)
    else:
        nw = f_no.getlength(no) + 80 * S
        d.rounded_rectangle([W * S / 2 - nw / 2 + 8 * S, cy - 230 * S + 10 * S, W * S / 2 + nw / 2 + 8 * S, cy - 130 * S + 10 * S],
                            30 * S, fill=(0, 0, 0, 110))
        d.rounded_rectangle([W * S / 2 - nw / 2, cy - 230 * S, W * S / 2 + nw / 2, cy - 130 * S], 30 * S,
                            fill=(217, 56, 30, 255), outline=ink, width=5 * S)
        d.text((W * S / 2, cy - 180 * S), no, font=f_no, fill=(255, 255, 255, 255), anchor="mm", stroke_width=4 * S, stroke_fill=ink)
        d.text((W * S / 2 + 6 * S, cy + 8 * S), title, font=f_t, fill=(0, 0, 0, 140), anchor="mm", stroke_width=9 * S,
               stroke_fill=(0, 0, 0, 140))
        d.text((W * S / 2, cy), title, font=f_t, fill=(255, 214, 10, 255), anchor="mm", stroke_width=9 * S, stroke_fill=ink)
        d.text((W * S / 2, cy + 130 * S), hook, font=f_h, fill=(44, 42, 41, 255), anchor="mm")

    img = img.resize((W, H), Image.LANCZOS)
    return _pil_to_rgba_bgr(img)
