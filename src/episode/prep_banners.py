"""Gemini banner images -> transparent cutouts for the renderers.

  python src/episode/prep_banners.py projects/<slug> <src_dir>
    <src_dir>/B00.png         -> assets/banners/shorts_title.png   (Shorts header banner, TASTE-62)
    <src_dir>/C01..C0N.png    -> assets/banners/chapter_NN.png     (long-form chapter header bars)
    (.txt dataURL dumps from src/episode/gemini_gen.cjs are decoded to .png first)

White background connected to the border is removed (flood fill) so inner white text/snow stays opaque;
the result is cropped tight to the artwork.
"""
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.image.gemini_watermark import clean_image  # noqa: E402

def cutout(im: np.ndarray) -> np.ndarray:
    h, w = im.shape[:2]
    white = (im.min(axis=2) > 235).astype(np.uint8)
    ff = white.copy()
    mask = np.zeros((h + 2, w + 2), np.uint8)
    for x in range(0, w, 4):
        for y in (0, h - 1):
            if ff[y, x] == 1:
                cv2.floodFill(ff, mask, (x, y), 2)
    for y in range(0, h, 4):
        for x in (0, w - 1):
            if ff[y, x] == 1:
                cv2.floodFill(ff, mask, (x, y), 2)
    alpha = np.where(ff == 2, 0, 255).astype(np.uint8)
    # soften the edge: fade near-white fringe pixels instead of a hard cut
    near = im.min(axis=2).astype(np.float32)
    fringe = (alpha == 0) & (near < 250)
    alpha[fringe] = 0
    alpha = cv2.GaussianBlur(alpha, (3, 3), 0)
    # drop tiny specks (isolated sparkles far away are fine, dust is not)
    n, lab, stats, _ = cv2.connectedComponentsWithStats((alpha > 128).astype(np.uint8))
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] < 25:
            alpha[lab == i] = 0
    ys, xs = np.where(alpha > 20)
    pad = 4
    y0, y1, x0, x1 = max(0, ys.min() - pad), min(h, ys.max() + pad), max(0, xs.min() - pad), min(w, xs.max() + pad)
    return np.dstack([im, alpha])[y0:y1, x0:x1]

def main():
    P, src = Path(sys.argv[1]), Path(sys.argv[2])
    out = P / "assets" / "banners"
    out.mkdir(parents=True, exist_ok=True)
    import base64
    for t in sorted(src.glob("*.txt")):  # dataURL dumps from src/episode/gemini_gen.cjs extra
        png = t.with_suffix(".png")
        if not png.exists() or png.stat().st_mtime < t.stat().st_mtime:
            s = t.read_text(encoding="utf-8").strip().strip('"')
            png.write_bytes(base64.b64decode(s.split(",", 1)[1]))
    for f in sorted(src.glob("*.png")):
        if f.stem == "B00":
            dst = out / "shorts_title.png"
        elif f.stem.startswith("C") and f.stem[1:].isdigit():
            dst = out / f"chapter_{int(f.stem[1:]):02d}.png"
        elif f.stem.startswith("K") and f.stem[1:].isdigit():
            dst = out / f"card_{int(f.stem[1:]):02d}.png"
        else:
            continue
        rgba = cutout(clean_image(cv2.imread(str(f)))[0])  # xóa logo Gemini nếu có (LESSON-88)
        cv2.imwrite(str(dst), rgba)
        (out / "_src").mkdir(exist_ok=True)
        cv2.imwrite(str(out / "_src" / f.name), cv2.imread(str(f)))
        print(f"{f.name} -> {dst.relative_to(P)}  {rgba.shape[1]}x{rgba.shape[0]}")

if __name__ == "__main__":
    main()
