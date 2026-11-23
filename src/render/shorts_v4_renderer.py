"""
Shorts V4 Premium Renderer — Vẽ Chuyện Hoang Dã
================================================
Reusable 9:16 Shorts engine driven by a JSON spec (one per episode).

Layout (TASTE-53, 1080x1920):
  0    -  200 : empty paper (YouTube search bar)
  200  -  380 : fixed 2-line title pill
  380  - 1250 : stage — ONE large illustration at a time + side callout stickers
  1250 - 1480 : kinetic captions (3-4 word groups, active word highlighted)
  1480 - 1920 : empty paper (channel name / Related Video button)

Per beat:
  A. ink phase   (draw_s)  : real hand (anchor 22,47) traces black ink lines,
                             ink appears only where the pen has passed
  B. colour pop  (0.30 s)  : colour floods in with spring overshoot + pop SFX
  C. hold        (rest)    : slow push-in 1.04 -> 1.12, stickers pop on keywords
  D. exit        (0.22 s)  : image slides up/fades, whoosh into next beat

Audio: narration voice (VoiceStudio) (never truncated) + ducked BGM + scribble during ink
phases + pop/whoosh/impact SFX + 1.5 s outro fade (LESSON-54/60).

Usage:
  python src/render/shorts_v4_renderer.py projects/<ep>/specs/shorts_v4_spec.json [--preview]
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "render"))
import theme_effects as te  # noqa: E402
W, H, FPS = 1080, 1920, 30

STAGE_Y0, STAGE_Y1 = 400, 1235
STAGE_CX = W // 2
STAGE_CY = (STAGE_Y0 + STAGE_Y1) // 2
CAPTION_CY = 1405     # low in the 1250-1480 caption zone (TASTE-55)
CAPTION_SIZE = 56

FONT_BOLD = str(ROOT / "assets/fonts/BeVietnamPro-Bold.ttf")
FONT_HAND = str(ROOT / "assets/fonts/Mali-Bold.ttf")

PALETTE = [(217, 56, 30), (43, 108, 176), (47, 133, 90), (251, 133, 0)]  # RGB


# ----------------------------------------------------------------------------- helpers
def ease_out_cubic(u: float) -> float:
    u = min(1.0, max(0.0, u))
    return 1 - (1 - u) ** 3


def spring(u: float, omega: float = 16.0, zeta: float = 0.55) -> float:
    """Damped spring 0 -> 1 with overshoot (u in seconds)."""
    if u <= 0:
        return 0.0
    wd = omega * math.sqrt(1 - zeta * zeta)
    return 1 - math.exp(-zeta * omega * u) * (math.cos(wd * u) + zeta * omega / wd * math.sin(wd * u))


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def fit_font(path: str, text: str, max_w: int, start: int, min_size: int = 20) -> ImageFont.FreeTypeFont:
    size = start
    while size > min_size:
        f = font(path, size)
        if f.getlength(text) <= max_w:
            return f
        size -= 2
    return font(path, min_size)


def alpha_paste(dst: np.ndarray, src_rgba: np.ndarray, x: int, y: int, opacity: float = 1.0) -> None:
    """Alpha-composite an RGBA (BGR order) image onto a BGR canvas in place."""
    h, w = src_rgba.shape[:2]
    H_, W_ = dst.shape[:2]
    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(W_, x + w), min(H_, y + h)
    if x0 >= x1 or y0 >= y1:
        return
    s = src_rgba[y0 - y:y1 - y, x0 - x:x1 - x]
    a = (s[:, :, 3:4].astype(np.float32) / 255.0) * opacity
    d = dst[y0:y1, x0:x1].astype(np.float32)
    dst[y0:y1, x0:x1] = (s[:, :, :3] * a + d * (1 - a)).astype(np.uint8)


def pil_to_rgba_bgr(img: Image.Image) -> np.ndarray:
    arr = np.array(img)  # RGBA
    return arr[:, :, [2, 1, 0, 3]].copy()


# ----------------------------------------------------------------------------- paper
def make_paper() -> np.ndarray:
    paper = np.full((H, W, 3), 255, np.uint8)
    rng = np.random.default_rng(7)
    noise = rng.normal(0, 1.2, (H, W, 1))
    paper = np.clip(paper.astype(np.float32) - np.abs(noise), 0, 255).astype(np.uint8)
    for y in range(18, H, 36):
        for x in range(18, W, 36):
            cv2.circle(paper, (x, y), 1, (226, 222, 216), -1, cv2.LINE_AA)
    return paper


# ----------------------------------------------------------------------------- hand
class Hand:
    def __init__(self, scale: float = 0.78):
        meta = json.loads((ROOT / "assets/hands/hand_metadata.json").read_text(encoding="utf-8"))
        raw = cv2.imread(str(ROOT / "assets/hands/hand-marker-right.png"), cv2.IMREAD_UNCHANGED)
        self.img = cv2.resize(raw, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        self.ax = int(round(meta["anchor"]["x"] * scale))
        self.ay = int(round(meta["anchor"]["y"] * scale))

    def stamp(self, canvas: np.ndarray, x: float, y: float) -> None:
        alpha_paste(canvas, self.img, int(x) - self.ax, int(y) - self.ay)


# ----------------------------------------------------------------------------- illustration
class Illustration:
    """Prepares cutout colour layer, ink layer and an ordered pen path."""

    def __init__(self, path: Path, box_w: int, box_h: int):
        im = cv2.imread(str(path))
        if im is None:
            raise FileNotFoundError(path)
        if "_raw" in path.stem:
            raise ValueError(f"Refusing raw (watermarked) asset: {path}")  # LESSON-54
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ys, xs = np.where(gray < 240)
        pad = 6
        x0, x1 = max(0, xs.min() - pad), min(im.shape[1], xs.max() + pad)
        y0, y1 = max(0, ys.min() - pad), min(im.shape[0], ys.max() + pad)
        self.src_w, self.src_h = im.shape[1], im.shape[0]
        self.crop_x, self.crop_y = x0, y0
        im = im[y0:y1, x0:x1]  # trims only empty white margin, never artwork
        s = min(box_w / im.shape[1], box_h / im.shape[0])
        self.scale = s
        im = cv2.resize(im, None, fx=s, fy=s, interpolation=cv2.INTER_LANCZOS4)
        self.h, self.w = im.shape[:2]
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # alpha: remove white background connected to the border (organic cutout)
        white = (gray > 242).astype(np.uint8)
        ff = white.copy()
        mask = np.zeros((self.h + 2, self.w + 2), np.uint8)
        for (sx, sy) in [(0, 0), (self.w - 1, 0), (0, self.h - 1), (self.w - 1, self.h - 1)]:
            if ff[sy, sx] == 1:
                cv2.floodFill(ff, mask, (sx, sy), 2)
        for x in range(0, self.w, 8):
            for y in (0, self.h - 1):
                if ff[y, x] == 1:
                    cv2.floodFill(ff, mask, (x, y), 2)
        for y in range(0, self.h, 8):
            for x in (0, self.w - 1):
                if ff[y, x] == 1:
                    cv2.floodFill(ff, mask, (x, y), 2)
        alpha = np.where(ff == 2, 0, 255).astype(np.uint8)
        alpha = cv2.GaussianBlur(alpha, (5, 5), 0)
        bg_ratio = (alpha < 128).mean()
        if bg_ratio < 0.08:  # full-bleed scene: rounded sticker corners instead
            alpha = np.zeros_like(alpha)
            cv2.rectangle(alpha, (0, 0), (self.w - 1, self.h - 1), 255, -1)
            r = 28
            corner = np.zeros((r, r), np.uint8)
            cv2.circle(corner, (r, r), r, 255, -1, cv2.LINE_AA)
            alpha[:r, :r] = corner
            alpha[:r, -r:] = corner[:, ::-1]
            alpha[-r:, :r] = corner[::-1, :]
            alpha[-r:, -r:] = corner[::-1, ::-1]
        self.color = np.dstack([im, alpha])

        # shadow layer
        sh = cv2.GaussianBlur(alpha, (0, 0), 9)
        self.shadow = np.dstack([np.zeros_like(im), (sh * 0.22).astype(np.uint8)])

        # ink layer: dark line-art only
        ink = ((gray < 105) & (alpha > 128)).astype(np.uint8) * 255
        self.ink_mask = ink
        ink_rgba = np.zeros((self.h, self.w, 4), np.uint8)
        ink_rgba[:, :, :3] = (41, 42, 44)
        self.ink_rgba_base = ink_rgba

        # pen path: grid-sampled ink points ordered by greedy nearest neighbour
        step = 7
        pts = []
        for yy in range(0, self.h, step):
            for xx in range(0, self.w, step):
                if ink[yy:yy + step, xx:xx + step].any():
                    pts.append((xx + step // 2, yy + step // 2))
        pts = np.array(pts, np.float32)
        if len(pts) == 0:
            pts = np.array([[self.w / 2, self.h / 2]], np.float32)
        order = [int(np.argmin(pts[:, 1] * 3 + pts[:, 0]))]  # start top-left
        used = np.zeros(len(pts), bool)
        used[order[0]] = True
        cur = pts[order[0]]
        for _ in range(len(pts) - 1):
            d = np.sum((pts - cur) ** 2, axis=1)
            d[used] = np.inf
            j = int(np.argmin(d))
            used[j] = True
            order.append(j)
            cur = pts[j]
        self.path = pts[order]
        self.reveal_r = step + 3

    def local(self, fx: float, fy: float) -> tuple[float, float]:
        """Map a feature position given as fraction of the ORIGINAL image to layer pixels."""
        return ((fx * self.src_w - self.crop_x) * self.scale, (fy * self.src_h - self.crop_y) * self.scale)

    def ink_reveal(self, n_pts: int) -> np.ndarray:
        m = np.zeros((self.h, self.w), np.uint8)
        for (x, y) in self.path[:n_pts]:
            cv2.circle(m, (int(x), int(y)), self.reveal_r, 255, -1)
        out = self.ink_rgba_base.copy()
        out[:, :, 3] = cv2.bitwise_and(self.ink_mask, m)
        return out


# ----------------------------------------------------------------------------- graphics
def _star(d: ImageDraw.ImageDraw, cx: float, cy: float, r: float, fill) -> None:
    pts = []
    for k in range(8):
        ang = math.pi / 4 * k - math.pi / 2
        rr = r if k % 2 == 0 else r * 0.38
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=fill)


def render_title(lines: list[str]) -> tuple[np.ndarray, np.ndarray]:
    """Comic ribbon banner (TASTE-55). Returns (rgba_bgr, body_mask) of size W x 200."""
    S = 2  # supersample for crisp edges
    cw, ch = W * S, 200 * S
    img = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    bx0, by0, bx1, by1 = 92 * S, 16 * S, (W - 92) * S, 176 * S
    navy_dark, gold, red, red_dark, ink = (12, 18, 38, 255), (255, 190, 20, 255), (217, 56, 30, 255), (140, 28, 14, 255), (20, 16, 14, 255)

    # ribbon tails (behind body)
    for side in (-1, 1):
        ox = bx0 if side < 0 else bx1
        outer = ox + side * 86 * S
        ty0, ty1 = by0 + 46 * S, by1 + 18 * S
        tail = [(ox - side * 10 * S, ty0), (outer, ty0), (outer - side * 30 * S, (ty0 + ty1) / 2), (outer, ty1), (ox - side * 10 * S, ty1)]
        d.polygon([(x + 8 * S, y + 10 * S) for x, y in tail], fill=(0, 0, 0, 110))
        d.polygon(tail, fill=red, outline=ink, width=4 * S)
        fold = [(ox, by1), (ox - side * 0 * S, ty1), (ox + side * 22 * S, by1 - 4 * S)]
        d.polygon([(ox, by1 - 2 * S), (ox + side * 24 * S, ty1), (ox + side * 24 * S, by1 - 2 * S)], fill=red_dark)
        for k in range(2):
            yy = ty0 + (ty1 - ty0) * (0.33 + 0.34 * k)
            d.line([(ox + side * 26 * S, yy), (outer - side * 26 * S, yy)], fill=(255, 220, 200, 110), width=2 * S)

    # hard comic shadow + body
    d.rounded_rectangle([bx0 + 9 * S, by0 + 11 * S, bx1 + 9 * S, by1 + 11 * S], 34 * S, fill=(0, 0, 0, 120))
    grad = Image.new("RGBA", (cw, ch))
    gd = ImageDraw.Draw(grad)
    for y in range(by0, by1 + 1):
        u = (y - by0) / (by1 - by0)
        c = (int(38 + (12 - 38) * u), int(56 + (20 - 56) * u), int(104 + (44 - 104) * u), 255)
        gd.line([(0, y), (cw, y)], fill=c)
    body = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(body).rounded_rectangle([bx0, by0, bx1, by1], 34 * S, fill=255)
    img.paste(grad, (0, 0), body)
    d.rounded_rectangle([bx0, by0, bx1, by1], 34 * S, outline=ink, width=5 * S)
    d.rounded_rectangle([bx0 + 6 * S, by0 + 6 * S, bx1 - 6 * S, by1 - 6 * S], 29 * S, outline=gold, width=6 * S)
    d.rounded_rectangle([bx0 + 17 * S, by0 + 17 * S, bx1 - 17 * S, by1 - 17 * S], 20 * S, outline=(255, 214, 90, 120), width=2 * S)
    # gloss on upper half
    gloss = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(gloss).rounded_rectangle([bx0 + 24 * S, by0 + 22 * S, bx1 - 24 * S, by0 + 62 * S], 18 * S, fill=34)
    img.paste(Image.new("RGBA", (cw, ch), (255, 255, 255, 255)), (0, 0), gloss)
    # corner stars
    for (sx, sy, r) in [(bx0 + 40 * S, by0 + 38 * S, 13 * S), (bx1 - 40 * S, by0 + 38 * S, 13 * S),
                        (bx0 + 40 * S, by1 - 38 * S, 9 * S), (bx1 - 40 * S, by1 - 38 * S, 9 * S)]:
        _star(d, sx, sy, r, gold)

    # text — TASTE-56: measure real glyph boxes (Vietnamese stacked diacritics + stroke)
    # and stack the lines with an explicit gap so they can never overlap.
    n = len(lines)
    max_tw = (bx1 - bx0) - 150 * S
    inner_top, inner_bot = by0 + 22 * S, by1 - 20 * S
    gap = 10 * S
    scale = 1.0
    while True:
        fonts, boxes = [], []
        for i, line in enumerate(lines):
            last = i == n - 1
            f = fit_font(FONT_BOLD, line, max_tw, int((64 if last else 50) * S * scale))
            sw = (6 if last else 4) * S
            bb = f.getbbox(line, anchor="ms", stroke_width=sw)  # relative to baseline
            fonts.append(f)
            boxes.append(bb)
        total_h = sum(bb[3] - bb[1] for bb in boxes) + gap * (n - 1)
        if total_h <= inner_bot - inner_top or scale < 0.6:
            break
        scale -= 0.04
    y = (inner_top + inner_bot - total_h) / 2
    baselines = []
    for bb in boxes:
        baselines.append(y - bb[1])  # top of ink box sits at y
        y += (bb[3] - bb[1]) + gap
    for i, line in enumerate(lines):
        f, by = fonts[i], baselines[i]
        cx = cw // 2
        if i < n - 1:
            d.text((cx + 4 * S, by + 5 * S), line, font=f, fill=(0, 0, 0, 150), anchor="ms")
            d.text((cx, by), line, font=f, fill=(255, 255, 255, 255), anchor="ms", stroke_width=4 * S, stroke_fill=ink)
        else:
            d.text((cx + 5 * S, by + 6 * S), line, font=f, fill=(0, 0, 0, 170), anchor="ms", stroke_width=6 * S, stroke_fill=(0, 0, 0, 170))
            d.text((cx, by), line, font=f, fill=ink, anchor="ms", stroke_width=6 * S, stroke_fill=ink)
            mask = Image.new("L", (cw, ch), 0)
            ImageDraw.Draw(mask).text((cx, by), line, font=f, fill=255, anchor="ms")
            tg = Image.new("RGBA", (cw, ch))
            tgd = ImageDraw.Draw(tg)
            gb = f.getbbox(line, anchor="ms")
            ty0, ty1 = int(by + gb[1]), int(by + gb[3])
            for y in range(ty0, ty1 + 1):
                u = (y - ty0) / max(1, ty1 - ty0)
                tgd.line([(0, y), (cw, y)], fill=(255, int(236 - 100 * u), int(120 - 110 * u), 255))
            img.paste(tg, (0, 0), mask)
    img = img.resize((W, 200), Image.LANCZOS)
    body_small = np.array(body.resize((W, 200), Image.LANCZOS))
    return pil_to_rgba_bgr(img), body_small


def load_title_image(path: Path, box_w: int = 1040, box_h: int = 212) -> tuple[np.ndarray, np.ndarray]:
    """AI-drawn banner (TASTE-62, transparent PNG from prep_banners.py) centred on a W x 220 layer.
    Same return contract as render_title: (rgba_bgr, body_mask)."""
    im = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if im is None or im.shape[2] != 4:
        raise ValueError(f"title_image must be an RGBA cutout: {path}")
    s = min(box_w / im.shape[1], box_h / im.shape[0])
    im = cv2.resize(im, None, fx=s, fy=s, interpolation=cv2.INTER_AREA if s < 1 else cv2.INTER_CUBIC)
    layer = np.zeros((220, W, 4), np.uint8)
    x0, y0 = (W - im.shape[1]) // 2, (220 - im.shape[0]) // 2
    layer[y0:y0 + im.shape[0], x0:x0 + im.shape[1]] = im
    return layer, layer[:, :, 3].copy()

def shine_band(xy: np.ndarray, pos: float, width: float) -> np.ndarray:
    """Diagonal gaussian light band; xy is precomputed (x + 0.55*y)."""
    return np.exp(-((xy - pos) ** 2) / (2 * width * width)).astype(np.float32)


def render_sticker(value: str, label: str, color_rgb: tuple, max_w: int = 300,
                   theme: str = "biolab", variant: int = 0) -> np.ndarray:
    return te.render_themed_sticker(value, label, color_rgb, max_w=max_w, theme=theme, variant=variant)


def render_caption(words: list[str], active: int, pop: float) -> np.ndarray:
    f = fit_font(FONT_BOLD, " ".join(words).upper(), 900, CAPTION_SIZE, 34)
    img = Image.new("RGBA", (W, 220), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    up = [w.upper() for w in words]
    space = f.getlength(" ")
    total = sum(f.getlength(w) for w in up) + space * (len(up) - 1)
    x = (W - total) / 2
    for i, w in enumerate(up):
        fill = (255, 214, 10) if i == active else (255, 255, 255)
        wf = f
        dy = 0
        if i > active:
            fill = (255, 255, 255, 150)  # not yet spoken: dimmed
        if i == active and pop < 1.0:
            wf = font(FONT_BOLD, int(f.size * (1.0 + 0.10 * (1 - pop))))
            dy = -4 * (1 - pop)
        d.text((x + f.getlength(w) / 2, 110 + dy), w, font=wf, fill=fill, anchor="mm",
               stroke_width=6, stroke_fill=(10, 10, 10))
        x += f.getlength(w) + space
    return pil_to_rgba_bgr(img)


def render_arrow(progress: float, color_bgr: tuple, flip: bool, length: int = 110) -> np.ndarray:
    """Hand-drawn arrow with a solid triangular head; drawn on progressively (0..1)."""
    Wd, Hd = length + 40, 110
    img = np.zeros((Hd, Wd, 4), np.uint8)
    head = 30
    n = 40
    pts = []
    for i in range(n + 1):
        u = i / n
        x = 8 + u * (length - head * 0.6)
        y = 70 - 34 * math.sin(math.pi * u * 0.85)
        pts.append((x, y))
    shaft_u = min(1.0, progress / 0.75)
    k = max(2, int(len(pts) * shaft_u))
    shaft = np.array(pts[:k], np.int32)
    col = color_bgr + (255,)
    outline = (20, 16, 14, 255)
    cv2.polylines(img, [shaft], False, outline, 13, cv2.LINE_AA)
    cv2.polylines(img, [shaft], False, col, 8, cv2.LINE_AA)
    if progress > 0.75:
        hs = min(1.0, (progress - 0.75) / 0.25)
        (xa, ya), (xb, yb) = pts[-2], pts[-1]
        ang = math.atan2(yb - ya, xb - xa)
        tipx, tipy = xb + math.cos(ang) * head * hs, yb + math.sin(ang) * head * hs
        L, Wh = head * hs, 17 * hs
        bx, by = tipx - math.cos(ang) * L, tipy - math.sin(ang) * L
        px, py = -math.sin(ang), math.cos(ang)
        tri = np.array([[tipx, tipy], [bx + px * Wh, by + py * Wh], [bx - px * Wh, by - py * Wh]], np.int32)
        cv2.fillPoly(img, [tri], outline, cv2.LINE_AA)
        cv2.polylines(img, [tri], True, outline, 6, cv2.LINE_AA)
        inner = np.array([[tipx - math.cos(ang) * 6, tipy - math.sin(ang) * 6],
                          [bx + px * (Wh - 5) + math.cos(ang) * 3, by + py * (Wh - 5) + math.sin(ang) * 3],
                          [bx - px * (Wh - 5) + math.cos(ang) * 3, by - py * (Wh - 5) + math.sin(ang) * 3]], np.int32)
        cv2.fillPoly(img, [inner], col, cv2.LINE_AA)
    return img[:, ::-1].copy() if flip else img


def draw_target_arrow(canvas: np.ndarray, p0: tuple, p1: tuple, progress: float,
                      color_bgr: tuple, bend: float, opacity: float = 1.0,
                      theme: str = "biolab", t: float = 0.0) -> None:
    te.draw_themed_arrow(canvas, p0, p1, progress, color_bgr, bend, opacity=opacity, theme=theme, t=t)


def draw_target_ring(canvas: np.ndarray, p: tuple, t: float, color_bgr: tuple,
                     opacity: float = 1.0, theme: str = "biolab") -> None:
    te.draw_themed_ring(canvas, p, t, color_bgr, opacity=opacity, theme=theme)


# ----------------------------------------------------------------------------- main renderer
def build(spec_path: Path, preview: bool = False) -> Path:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    proj = spec_path.resolve().parents[1]
    beats = spec["beats"]
    voice = proj / spec["voice"]
    voice_end = float(spec["voice_end_s"])
    total = voice_end + float(spec.get("outro_buffer_s", 1.5))
    out = proj / spec["output"]
    out.parent.mkdir(parents=True, exist_ok=True)

    # beat end times
    for i, b in enumerate(beats):
        b["end_s"] = beats[i + 1]["start_s"] if i + 1 < len(beats) else total

    # ---- QA gate before render
    seen = set()
    for b in beats:
        p = proj / b["image"]
        assert p.exists(), f"Missing image {p}"
        h = hash(p.read_bytes())
        assert h not in seen, f"Duplicate image content: {p}"  # LESSON-52
        seen.add(h)
    for b in beats:
        for cap in b["captions"]:
            assert len(cap["text"].split()) <= 5, f"Caption too long: {cap['text']}"

    theme, tpal = te.resolve_theme(proj)
    paper = te.decorate_paper(make_paper(), theme)
    hand = Hand(spec.get("hand_scale", 0.78))
    if spec.get("title_image") and (proj / spec["title_image"]).exists():
        title, title_body = load_title_image(proj / spec["title_image"])
        title_y = 182
    else:
        title, title_body = render_title(spec["title_lines"])
        title_y = 190
    tyy, txx = np.mgrid[0:title.shape[0], 0:title.shape[1]]
    title_xy = (txx + 0.55 * tyy).astype(np.float32)
    title_body_f = title_body.astype(np.float32) / 255.0
    box_w, box_h = spec.get("image_box", [560, 835])
    print("Preparing illustrations ...")
    for b in beats:
        b["ill"] = Illustration(proj / b["image"], box_w, box_h)
        print(f"  {b['id']}: {b['ill'].w}x{b['ill'].h}, pen pts={len(b['ill'].path)}")

    # stickers
    slot_y = {"L": [540, 800, 1060], "R": [520, 780]}  # right side stays high (action buttons)
    for bi, b in enumerate(beats):
        counters = {"L": 0, "R": 0}
        for k, s in enumerate(b.get("stickers", [])):
            side = s["side"]
            col = tpal[(bi + k) % len(tpal)]
            s["img"] = render_sticker(s["value"], s["label"], col, 300, theme=theme, variant=bi + k)
            s["col_bgr"] = (col[2], col[1], col[0])
            s["y"] = s.get("y", slot_y[side][counters[side] % len(slot_y[side])])
            s["rot"] = (-3 if side == "L" else 3) * (1 if k % 2 == 0 else -0.6)
            counters[side] += 1

    # captions: per-word timing aligned to Whisper word stamps (TASTE-55)
    wtl = json.loads((proj / spec["words"]).read_text(encoding="utf-8"))
    caps = []
    for b in beats:
        for c in b["captions"]:
            caps.append({"t": float(c["t"]), "words": c["text"].split()})
    caps.sort(key=lambda c: c["t"])
    for i, c in enumerate(caps):
        nxt = caps[i + 1]["t"] if i + 1 < len(caps) else voice_end + 1.0
        ws = [w for w in wtl if c["t"] - 0.05 <= w["start"] < nxt - 0.05]
        n = len(c["words"])
        if not ws:
            c["word_t"] = [c["t"] + 0.25 * j for j in range(n)]
            c["end"] = min(nxt, c["t"] + 0.25 * n + 0.3)
            continue
        if len(ws) == n:
            c["word_t"] = [w["start"] for w in ws]
        else:  # different tokenisation: spread over spoken span
            s0, s1 = ws[0]["start"], ws[-1]["end"]
            c["word_t"] = [s0 + (s1 - s0) * j / n for j in range(n)]
        c["word_t"][0] = min(c["word_t"][0], c["t"])
        # hide during real pauses, but avoid flicker between tight groups
        c["end"] = nxt if nxt - ws[-1]["end"] < 0.35 else ws[-1]["end"] + 0.2

    caption_cache: dict = {}

    frames_to_render = range(int(round(total * FPS)))
    tmp_video = out.with_name(out.stem + "_video.mp4")
    if preview:
        frames_to_render = [int(t * FPS) for t in spec.get("preview_times", [1, 5, 12, 25, 35, 44, 50, 53])]

    pipe = None
    if not preview:
        pipe = subprocess.Popen([
            "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgr24",
            "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
            "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", str(tmp_video)
        ], stdin=subprocess.PIPE)

    sfx_events = []  # (time, file, volume)
    for i, b in enumerate(beats):
        if i > 0:
            sfx_events.append((b["start_s"] - 0.12, "assets/sfx/pixabay/whoosh-short.mp3", 0.55))
        sfx_events.append((b["start_s"] + b["draw_s"], "assets/sfx/pixabay/pop.mp3", 0.6))
        for s in b.get("stickers", []):
            sfx_events.append((s["t"], "assets/sfx/pixabay/pop.mp3", 0.35))
        for imp in b.get("impacts", []):
            sfx_events.append((imp, "assets/sfx/pixabay/impact-bass-1.mp3", 0.5))

    snaps = []
    for fi in frames_to_render:
        t = fi / FPS
        b = next((x for x in beats if x["start_s"] <= t < x["end_s"]), beats[-1])
        ill: Illustration = b["ill"]
        el = t - b["start_s"]
        bdur = b["end_s"] - b["start_s"]
        draw_s = b["draw_s"]
        canvas = paper.copy()

        # ---- stage illustration
        exit_u = 0.0
        if b is not beats[-1]:
            exit_u = ease_out_cubic((el - (bdur - 0.22)) / 0.22) if el > bdur - 0.22 else 0.0
        pen = None
        sx = sy = 1.0
        rot = 0.0
        bob = 0.0
        if el < draw_s:
            u = b.get("start_progress", 0.0) + (1 - b.get("start_progress", 0.0)) * (el / draw_s)
            n = max(1, int(len(ill.path) * u))
            layer = ill.ink_reveal(n)
            pen = ill.path[n - 1]
        else:
            # TASTE-55: no push-in zoom. Jelly bounce -> shine sweep -> gentle float + sparkles
            pu = el - draw_s
            layer = ill.color
            if pu < 0.30:  # ink -> colour flood
                k = ease_out_cubic(pu / 0.30)
                inkl = ill.ink_reveal(len(ill.path))
                layer = ill.color.copy()
                layer[:, :, 3] = (ill.color[:, :, 3] * k + inkl[:, :, 3] * (1 - k)).astype(np.uint8)
                layer[:, :, :3] = (ill.color[:, :, :3] * k + inkl[:, :, :3] * (1 - k)).astype(np.uint8)
            jelly = math.exp(-5.0 * pu) * math.sin(2 * math.pi * 2.6 * pu)
            sx, sy = 1.0 + 0.045 * jelly, 1.0 - 0.045 * jelly
            ramp = min(1.0, pu / 0.8)
            bob = 6.0 * math.sin(2 * math.pi * pu / 2.4) * ramp
            rot = 1.0 * math.sin(2 * math.pi * pu / 3.1) * ramp
            sh_t = pu - 0.35
            if 0.0 <= sh_t <= 0.75:  # one diagonal light sweep across the artwork
                if not hasattr(ill, "xy"):
                    yy_, xx_ = np.mgrid[0:ill.h, 0:ill.w]
                    ill.xy = (xx_ + 0.55 * yy_).astype(np.float32)
                span = ill.w + 0.55 * ill.h
                band = shine_band(ill.xy, -120 + (span + 240) * ease_out_cubic(sh_t / 0.75), 38.0) * 0.55
                band *= (layer[:, :, 3].astype(np.float32) / 255.0)
                layer = layer.copy()
                layer[:, :, :3] = np.clip(layer[:, :, :3] + band[:, :, None] * 255, 0, 255).astype(np.uint8)
        if sx != 1.0 or sy != 1.0 or rot != 0.0:
            def _xf(img):
                hh, ww = img.shape[:2]
                # p' = P + S.R.(p - P), pivot P at bottom centre
                a = math.radians(rot)
                A = np.array([[sx * math.cos(a), sx * math.sin(a)],
                              [-sy * math.sin(a), sy * math.cos(a)]], np.float32)
                P = np.array([ww / 2, hh * 0.92], np.float32)
                M = np.hstack([A, (P - A @ P).reshape(2, 1)]).astype(np.float32)
                return cv2.warpAffine(img, M, (ww, hh), flags=cv2.INTER_LINEAR,
                                      borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
            layer_s, shadow_s = _xf(layer), _xf(ill.shadow)
        else:
            layer_s, shadow_s = layer, ill.shadow
        lh, lw = layer_s.shape[:2]
        x0 = STAGE_CX - lw // 2
        y0 = STAGE_CY - lh // 2 - int(160 * exit_u) + int(round(bob))
        op = 1.0 - exit_u
        if el >= draw_s:
            alpha_paste(canvas, shadow_s, x0 + 8, y0 + 14 - int(round(bob)) // 2, op)
        alpha_paste(canvas, layer_s, x0, y0, op)
        # twinkling sparkles around the artwork after colour pop
        if el >= draw_s + 0.25:
            rng = np.random.default_rng(sum(map(ord, b["id"])))
            for k in range(7):
                ang = rng.uniform(0, 2 * math.pi)
                px = STAGE_CX + math.cos(ang) * (lw / 2 + rng.uniform(-10, 40))
                py = STAGE_CY + math.sin(ang) * (lh / 2 + rng.uniform(-30, 20))
                ph = rng.uniform(0, 2 * math.pi)
                tw = max(0.0, math.sin(2 * math.pi * 0.9 * (el - draw_s) + ph))
                r = 7 + 9 * tw
                if tw > 0.05 and STAGE_Y0 < py < STAGE_Y1:
                    col = (20, 190, 255) if k % 2 else (230, 160, 60)  # BGR: gold / sky blue
                    pts_ = []
                    for q in range(8):
                        a_ = math.pi / 4 * q
                        rr = r if q % 2 == 0 else r * 0.3
                        pts_.append([px + rr * math.cos(a_), py + rr * math.sin(a_)])
                    cv2.fillPoly(canvas, [np.array(pts_, np.int32)], col, cv2.LINE_AA)

        # ---- stickers
        for s in b.get("stickers", []):
            if t < s["t"]:
                continue
            k = spring(t - s["t"], 15.0, 0.5)
            img = s["img"]
            sc = max(0.05, k)
            M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), s["rot"], sc)
            rimg = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR,
                                  borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
            cx = 165 if s["side"] == "L" else W - 165
            ap = (t - s["t"] - 0.18) / 0.40
            if ap > 0 and "target" in s:
                # TASTE-56: arrow lands exactly on the feature named in the voice-over
                lx, ly = ill.local(*s["target"])
                p1 = (x0 + lx, y0 + ly)
                half = img.shape[1] / 2 - 26
                p0 = (cx + half, s["y"] + 18) if s["side"] == "L" else (cx - half, s["y"] + 18)
                bend = s.get("bend", -0.22 if s["side"] == "L" else 0.22)
                draw_target_arrow(canvas, p0, p1, min(1.0, ap), s["col_bgr"], bend, op, theme=theme, t=t - s["t"])
                if ap >= 1.0:
                    draw_target_ring(canvas, p1, t - s["t"], s["col_bgr"], op, theme=theme)
            elif ap > 0:
                ar = render_arrow(min(1.0, ap), s["col_bgr"], flip=(s["side"] == "R"))
                ax = cx + img.shape[1] // 2 - 34 if s["side"] == "L" else cx - img.shape[1] // 2 - ar.shape[1] + 34
                alpha_paste(canvas, ar, int(ax), int(s["y"] + 10), op)
            alpha_paste(canvas, rimg, int(cx - img.shape[1] / 2), int(s["y"] - img.shape[0] / 2), op)

        # ---- hand
        if pen is not None:
            hx = x0 + pen[0] + 2.0 * math.sin(t * 40)
            hy = y0 + pen[1] + 1.5 * math.cos(t * 33)
            hand.stamp(canvas, hx, hy)
        elif el - draw_s < 0.35:
            u = ease_out_cubic((el - draw_s) / 0.35)
            last = ill.path[-1]
            hand.stamp(canvas, x0 + last[0] + 420 * u, y0 + last[1] + 700 * u)

        # ---- title (fixed)
        cyc = t % 4.0  # light sweep across the banner every 4 s
        if cyc < 0.9:
            band = shine_band(title_xy, -150 + (W + 300) * ease_out_cubic(cyc / 0.9), 30.0) * 0.45 * title_body_f
            tl = title.copy()
            tl[:, :, :3] = np.clip(tl[:, :, :3] + band[:, :, None] * 255, 0, 255).astype(np.uint8)
            alpha_paste(canvas, tl, 0, title_y)
        else:
            alpha_paste(canvas, title, 0, title_y)

        # ---- caption
        cap = next((c for c in caps if c["t"] <= t < c["end"]), None)
        if cap is not None:
            active = max(j for j, wt in enumerate(cap["word_t"]) if wt <= t)
            pop = min(1.0, (t - cap["word_t"][active]) / 0.14)
            key = (id(cap), active, round(pop, 1))
            if key not in caption_cache:
                caption_cache[key] = render_caption(cap["words"], active, pop)
            alpha_paste(canvas, caption_cache[key], 0, CAPTION_CY - 110)

        if preview:
            snaps.append((t, canvas))
        else:
            pipe.stdin.write(canvas.tobytes())
            if fi % 150 == 0:
                print(f"  frame {fi}/{int(total * FPS)}")

    if preview:
        sheet_dir = out.parent / "snapshots_shorts_v4"
        sheet_dir.mkdir(exist_ok=True)
        thumbs = []
        for t, c in snaps:
            cv2.imwrite(str(sheet_dir / f"v4_{t:05.1f}s.png"), c)
            th = cv2.resize(c, (360, 640))
            cv2.putText(th, f"{t:.1f}s", (10, 30), 0, 0.9, (0, 0, 255), 2)
            thumbs.append(th)
        while len(thumbs) % 4:
            thumbs.append(np.full_like(thumbs[0], 255))
        rows = [np.hstack(thumbs[i:i + 4]) for i in range(0, len(thumbs), 4)]
        cv2.imwrite(str(sheet_dir / "contact_sheet.png"), np.vstack(rows))
        print("Preview written to", sheet_dir)
        return sheet_dir

    pipe.stdin.close()
    pipe.wait()

    # ---- audio mix
    print("Mixing audio ...")
    bgm_path = (proj / "audio" / "bgm_seamless_10m.wav") if (proj / "audio" / "bgm_seamless_10m.wav").exists() else (ROOT / spec["bgm"])
    inputs = ["-i", str(tmp_video), "-i", str(voice), "-stream_loop", "-1", "-i", str(bgm_path)]
    filters = [
        "[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,apad=whole_dur=%.2f,asplit=2[voc][vsc]" % total,
        "[2:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,volume=0.10,atrim=0:%.2f[bgmraw]" % total,
        "[bgmraw][vsc]sidechaincompress=threshold=0.06:ratio=3.5:attack=30:release=800[bgm]",
    ]
    mix = ["[voc]", "[bgm]"]
    idx = 3
    for k, (tt, f, vol) in enumerate(sfx_events):
        inputs += ["-i", str(ROOT / f)]
        ms = max(0, int(tt * 1000))
        filters.append(
            f"[{idx}:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,volume={vol},adelay={ms}|{ms}[fx{k}]")
        mix.append(f"[fx{k}]")
        idx += 1
    filters.append(
        "".join(mix) + f"amix=inputs={len(mix)}:duration=first:normalize=0,volume=1.08,alimiter=limit=0.75:attack=5:release=50:asc=1:level=0,"
        f"afade=t=out:st={total - 1.5:.2f}:d=1.5[aout]")
    cmd = ["ffmpeg", "-y", "-loglevel", "error"] + inputs + [
        "-filter_complex", ";".join(filters), "-map", "0:v", "-map", "[aout]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-t", f"{total:.2f}", str(out)]
    subprocess.run(cmd, check=True)
    tmp_video.unlink(missing_ok=True)
    print("DONE:", out)
    return out


if __name__ == "__main__":
    sp = Path(sys.argv[1])
    build(sp, preview="--preview" in sys.argv)
