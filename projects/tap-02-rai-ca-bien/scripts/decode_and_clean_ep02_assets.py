"""
Decode, Watermark-Clean, and Audit all 29 Gemini Illustrations for Episode 2: Rái Cá Biển (`tap-02-rai-ca-bien`)
"""

import json
import base64
import cv2
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]
G = PROJ / "assets" / "gemini_downloaded"
BACKUP = G / "_raw_with_watermark_backup"
QA_DIR = PROJ / "renders" / "qa_audit"

G.mkdir(parents=True, exist_ok=True)
BACKUP.mkdir(parents=True, exist_ok=True)
QA_DIR.mkdir(parents=True, exist_ok=True)


def clean_star_watermark(img_bgr: np.ndarray) -> np.ndarray:
    h, w = img_bgr.shape[:2]
    roi = img_bgr[h - 140 : h, w - 140 : w].copy()
    b, g, r = cv2.split(roi)
    yy, xx = np.mgrid[0:140, 0:140]
    star_paper_zone = (yy >= 40) & (xx >= 40) & (b >= 215) & (g >= 215) & (r >= 215)
    roi[star_paper_zone] = [255, 255, 255]
    img_bgr[h - 140 : h, w - 140 : w] = roi
    return img_bgr


def main():
    candidates = [
        Path(r"C:\Users\PC\.playwright-mcp\uploads\ep02_gemini_29.json"),
        Path(r"C:\Users\PC\ep02_gemini_29.json"),
    ]
    json_path = next((p for p in candidates if p.exists()), None)
    if not json_path:
        raise FileNotFoundError("Could not find ep02_gemini_29.json")

    raw = json_path.read_text(encoding="utf-8").strip()
    if raw.startswith('"'):
        raw = json.loads(raw)
    data = json.loads(raw) if isinstance(raw, str) else raw

    saved_items = []
    for filename, b64 in data.items():
        img_bytes = base64.b64decode(b64)
        backup_p = BACKUP / filename
        backup_p.write_bytes(img_bytes)

        arr = np.frombuffer(img_bytes, dtype=np.uint8)
        im_bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        im_clean = clean_star_watermark(im_bgr)
        out_p = G / filename
        cv2.imwrite(str(out_p), im_clean)
        h, w = im_clean.shape[:2]
        saved_items.append((filename, out_p, w, h))
        print(f"[SAVED & CLEANED] {filename} ({w}x{h})")

    # Build visual QA contact sheets (15 images per sheet)
    for sheet_idx in range(0, len(saved_items), 15):
        batch = saved_items[sheet_idx : sheet_idx + 15]
        cols = 3
        rows = (len(batch) + cols - 1) // cols
        tw, th = 420, 240
        sheet = Image.new("RGB", (cols * tw, rows * (th + 28)), (245, 245, 245))
        draw = ImageDraw.Draw(sheet)
        for i, (fname, img_p, w, h) in enumerate(batch):
            r = i // cols
            c = i % cols
            im = Image.open(img_p).convert("RGB")
            im.thumbnail((tw - 10, th - 10))
            x0 = c * tw + (tw - im.size[0]) // 2
            y0 = r * (th + 28) + 24 + (th - im.size[1]) // 2
            sheet.paste(im, (x0, y0))
            draw.text((c * tw + 8, r * (th + 28) + 4), f"{i+1+sheet_idx:02d}. {fname[:32]} ({w}x{h})", fill=(20, 20, 20))
        sheet_p = QA_DIR / f"ep02_assets_sheet_{sheet_idx // 15 + 1}.png"
        sheet.save(sheet_p)
        print(f"[QA SHEET] {sheet_p}")


if __name__ == "__main__":
    main()
