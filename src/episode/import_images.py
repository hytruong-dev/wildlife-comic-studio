"""Import Gemini images into an episode (any source: dataURL .txt dumps, downloaded png/jpg).

Put files in projects/<slug>/assets/inbox/ named exactly as the plan expects (L01.png, S03.txt ...),
then:
  python src/episode/import_images.py projects/<slug>            # L* -> assets/long, S* -> assets/shorts, T* -> thumbnail
  python src/episode/import_images.py projects/<slug> --sheet    # contact sheet for visual review

- dataURL text (from canvas.toDataURL in the Gemini page) is decoded losslessly.
- Gemini sparkle watermark is removed only when detected (inverse alpha deblend, LESSON-50).
- Originals are kept in assets/<kind>/_raw/.
- Thumbnail (T*.png): scaled to 1280x720 -> renders/<slug>_thumbnail.jpg (< 2 MB).
"""
import base64
import json
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from src.pipeline.asset_sanitizer import build_astroid_star_mask, clean_gemini_watermark_lossless  # noqa: E402
from src.image.gemini_watermark import clean_image  # noqa: E402

def decode_txt(p: Path) -> np.ndarray:
    s = p.read_text(encoding="utf-8").strip()
    if s.startswith('"'):
        s = json.loads(s)
    return cv2.imdecode(np.frombuffer(base64.b64decode(s.split(",", 1)[1]), np.uint8), cv2.IMREAD_COLOR)

def has_watermark(im: np.ndarray) -> bool:
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32)
    h, w = g.shape
    cx, cy = w - 60, h - 49
    if cx < 40 or cy < 40:
        return False
    p = g[cy - 35:cy + 36, cx - 35:cx + 36]
    m = build_astroid_star_mask(71) > 0
    ring = (cv2.dilate(m.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0) & ~m
    return p[m].mean() - p[ring].mean() > 4.0

def main():
    P = Path(sys.argv[1]).resolve()
    inbox = P / "assets" / "inbox"
    slug = P.name
    done = []
    for f in sorted(inbox.glob("*")):
        if f.suffix.lower() not in (".txt", ".png", ".jpg", ".jpeg", ".webp"):
            continue
        im = decode_txt(f) if f.suffix == ".txt" else cv2.imread(str(f))
        if im is None:
            print("cannot read", f.name); continue
        kind = {"L": "long", "S": "shorts", "T": "thumb"}.get(f.stem[:1].upper(), "long")
        # 1) logo Gemini chuẩn (alpha tham chiếu 48/96 px, vị trí theo kích thước ảnh) — src/image/gemini_watermark.py
        clean, info = clean_image(im)
        wm = info is not None
        # 2) dự phòng: kiểu sao cũ (canvas 1024x572, tâm w-60,h-49)
        if not wm and has_watermark(im):
            clean, wm = clean_gemini_watermark_lossless(im), True
        if kind == "thumb":
            out = P / "renders" / f"{slug}_thumbnail.jpg"
            out.parent.mkdir(parents=True, exist_ok=True)
            cv2.imwrite(str(out), cv2.resize(clean, (1280, 720), interpolation=cv2.INTER_LANCZOS4), [cv2.IMWRITE_JPEG_QUALITY, 92])
        else:
            d = P / "assets" / kind
            (d / "_raw").mkdir(parents=True, exist_ok=True)
            cv2.imwrite(str(d / "_raw" / f"{f.stem}_raw.png"), im)
            out = d / f"{f.stem}.png"
            cv2.imwrite(str(out), clean)
        f.unlink()
        done.append(out)
        print(f"{f.name}: {im.shape[1]}x{im.shape[0]} -> {out.relative_to(P)}{'  (watermark removed)' if wm else ''}")
    if "--sheet" in sys.argv:
        for kind, (tw, th, cols) in {"long": (384, 216, 5), "shorts": (180, 320, 8)}.items():
            ims = sorted((P / "assets" / kind).glob("*.png"))
            if not ims:
                continue
            rows = (len(ims) + cols - 1) // cols
            sheet = np.full((rows * (th + 26), cols * tw, 3), 255, np.uint8)
            for i, p in enumerate(ims):
                r, c = divmod(i, cols)
                sheet[r * (th + 26) + 24:r * (th + 26) + 24 + th, c * tw:(c + 1) * tw] = cv2.resize(cv2.imread(str(p)), (tw, th))
                cv2.putText(sheet, p.stem, (c * tw + 4, r * (th + 26) + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 200), 2)
            out = P / "renders" / "snapshots" / f"sheet_{kind}.jpg"
            out.parent.mkdir(parents=True, exist_ok=True)
            cv2.imwrite(str(out), sheet)
            print("sheet:", out)
    print(f"imported {len(done)} file(s)")

if __name__ == "__main__":
    main()
