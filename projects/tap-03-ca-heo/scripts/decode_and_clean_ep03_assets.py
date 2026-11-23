"""
Decode, Watermark-Clean, and Audit all 29 Gemini Illustrations + 1 Gemini Thumbnail for Episode 3: Cá Heo (`tap-03-ca-heo`)
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
RENDERS_DIR = PROJ / "renders"
QA_DIR = RENDERS_DIR / "qa_audit"

G.mkdir(parents=True, exist_ok=True)
BACKUP.mkdir(parents=True, exist_ok=True)
RENDERS_DIR.mkdir(parents=True, exist_ok=True)
QA_DIR.mkdir(parents=True, exist_ok=True)


def clean_star_watermark_whiteboard(img_bgr: np.ndarray) -> np.ndarray:
    h, w = img_bgr.shape[:2]
    roi = img_bgr[h - 140 : h, w - 140 : w].copy()
    b, g, r = cv2.split(roi)
    yy, xx = np.mgrid[0:140, 0:140]
    star_paper_zone = (yy >= 35) & (xx >= 35) & (b >= 205) & (g >= 205) & (r >= 205)
    roi[star_paper_zone] = [255, 255, 255]
    img_bgr[h - 140 : h, w - 140 : w] = roi
    return img_bgr


def clean_star_watermark_fullbleed(img_bgr: np.ndarray) -> np.ndarray:
    h, w = img_bgr.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)
    # Gemini star sits around (w - 58, h - 58) with radius ~32px
    cv2.circle(mask, (w - 56, h - 56), 36, 255, -1)
    cleaned = cv2.inpaint(img_bgr, mask, 7, cv2.INPAINT_TELEA)
    return cleaned


def main():
    json_path = PROJ / "assets" / "ep03_gemini_30.json"
    if not json_path.exists():
        raise FileNotFoundError(f"Could not find {json_path}")

    data = json.loads(json_path.read_text(encoding="utf-8"))

    saved_items = []
    for filename, b64 in data.items():
        img_bytes = base64.b64decode(b64)
        backup_p = BACKUP / filename
        backup_p.write_bytes(img_bytes)

        arr = np.frombuffer(img_bytes, dtype=np.uint8)
        im_bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)

        if "thumbnail" in filename:
            im_clean = clean_star_watermark_fullbleed(im_bgr)
            out_raw_p = RENDERS_DIR / filename
            cv2.imwrite(str(out_raw_p), im_clean)
            # Upscale to 1280x720 HD YouTube Thumbnail
            im_1280 = cv2.resize(im_clean, (1280, 720), interpolation=cv2.INTER_LANCZOS4)
            cv2.imwrite(str(RENDERS_DIR / "tap03_ca_heo_thumbnail_gemini.png"), im_1280)
            cv2.imwrite(
                str(RENDERS_DIR / "tap03_ca_heo_thumbnail_gemini.jpg"),
                im_1280,
                [int(cv2.IMWRITE_JPEG_QUALITY), 95],
            )
            print(f"[THUMBNAIL SAVED & CLEANED] tap03_ca_heo_thumbnail_gemini.jpg (1280x720)")
        else:
            im_clean = clean_star_watermark_whiteboard(im_bgr)
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
        sheet_p = QA_DIR / f"ep03_assets_sheet_{sheet_idx // 15 + 1}.png"
        sheet.save(sheet_p)
        print(f"[QA SHEET] {sheet_p}")


if __name__ == "__main__":
    main()
