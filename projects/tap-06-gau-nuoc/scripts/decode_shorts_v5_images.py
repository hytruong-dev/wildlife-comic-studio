"""Decode Gemini dataURL dumps (v5_sXX.txt) -> raw PNG backup + watermark-free clean PNG.

The Gemini preview image is 9:16 on white background; the sparkle watermark sits in
the bottom-right corner. Since TASTE-56 prompts force a pure white background, the
corner is restored by detecting the star blob (pixels differing from paper white) in a
corner box and repainting only those pixels white when the box contains no artwork.
"""
import base64
import json
import sys
from pathlib import Path

import cv2
import numpy as np

PROJ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJ.parents[1]))
from src.pipeline.asset_sanitizer import build_astroid_star_mask, clean_gemini_watermark_lossless  # noqa: E402
RAW = PROJ / "assets" / "gemini_downloaded_shorts" / "_raw_with_watermark_backup"
CLEAN = PROJ / "assets" / "gemini_downloaded_shorts"
INBOX = Path.home() / "tap06_v5"  # Playwright MCP may only write under the user profile


def decode(txt: Path) -> np.ndarray:
    s = txt.read_text(encoding="utf-8").strip()
    if s.startswith('"'):
        s = json.loads(s)
    b = base64.b64decode(s.split(",", 1)[1])
    return cv2.imdecode(np.frombuffer(b, np.uint8), cv2.IMREAD_COLOR)


def clean_corner(im: np.ndarray) -> tuple[np.ndarray, str]:
    h, w = im.shape[:2]
    box = int(round(w * 0.16))
    y0, x0 = h - box, w - box
    corner = im[y0:, x0:].astype(np.int16)
    gray = cv2.cvtColor(im[y0:, x0:], cv2.COLOR_BGR2GRAY)
    diff = gray < 246
    n, lab, stats, _ = cv2.connectedComponentsWithStats(diff.astype(np.uint8))
    out = im.copy()
    removed = 0
    for i in range(1, n):
        x, y, bw, bh, area = stats[i]
        touches_edge = x == 0 or y == 0
        squareish = 0.6 < bw / max(1, bh) < 1.6
        # watermark: a single light-grey, square-ish blob not connected to artwork
        mean_v = gray[lab == i].mean()
        if not touches_edge and squareish and mean_v > 150 and area < box * box * 0.35:
            m = cv2.dilate((lab == i).astype(np.uint8), np.ones((5, 5), np.uint8))
            out[y0:, x0:][m > 0] = 255
            removed += 1
    return out, f"removed {removed} blob(s)"


def has_watermark(im: np.ndarray) -> bool:
    """Gemini sparkle = semi-transparent WHITE star: star pixels brighter than the ring around it."""
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32)
    h, w = g.shape
    cx, cy = w - 60, h - 49
    p = g[cy - 35:cy + 36, cx - 35:cx + 36]
    m = build_astroid_star_mask(71) > 0
    ring = (cv2.dilate(m.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0) & ~m
    return p[m].mean() - p[ring].mean() > 4.0


def main(names: list[str]) -> None:
    global RAW, CLEAN
    if names and names[0].startswith("--dest="):  # e.g. --dest=gemini_downloaded_long
        CLEAN = PROJ / "assets" / names[0].split("=", 1)[1]
        RAW = CLEAN / "_raw_with_watermark_backup"
        names = names[1:]
    RAW.mkdir(parents=True, exist_ok=True)
    for name in names:
        txt = INBOX / f"{name}.txt"
        raw_png = RAW / f"{name}_raw.png"
        if txt.exists():
            im = decode(txt)
            cv2.imwrite(str(raw_png), im)
            txt.unlink()
        else:
            im = cv2.imread(str(raw_png))
        if has_watermark(im):
            cleaned = clean_gemini_watermark_lossless(im)  # LESSON-50 inverse alpha deblend
            info = "watermark found -> deblended"
        else:
            cleaned = im  # canvas-extracted preview carries no sparkle: keep pixels intact
            info = "no watermark (kept pristine)"
        cv2.imwrite(str(CLEAN / f"{name}.png"), cleaned)
        print(f"{name}: {im.shape[1]}x{im.shape[0]} -> {info}")


if __name__ == "__main__":
    main(sys.argv[1:])
