"""
Decode, Watermark-Clean, and Audit all 27 Gemini Illustrations + 1 Gemini Thumbnail for Episode 4: Thú Mỏ Vịt (`tap-04-thu-mo-vit`)
"""

import json
import base64
import cv2
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw

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
    cv2.circle(mask, (w - 56, h - 56), 36, 255, -1)
    cleaned = cv2.inpaint(img_bgr, mask, 7, cv2.INPAINT_TELEA)
    return cleaned


def main():
    json_candidates = [
        Path(r"C:\Users\PC\.playwright-mcp\ep04_gemini_28.json"),
        Path(r"C:\Users\PC\.playwright-mcp\ep04-gemini-28.json"),
        PROJ / "assets" / "ep04_gemini_28.json",
    ]
    json_path = None
    for p in json_candidates:
        if p.exists():
            json_path = p
            break

    if not json_path:
        raise FileNotFoundError(f"Could not find ep04_gemini_28.json in {[str(p) for p in json_candidates]}")

    print(f"Reading JSON from {json_path}...")
    data = json.loads(json_path.read_text(encoding="utf-8"))

    saved_items = []
    for filename, b64 in data.items():
        img_bytes = base64.b64decode(b64)
        backup_p = BACKUP / filename
        backup_p.write_bytes(img_bytes)

        arr = np.frombuffer(img_bytes, dtype=np.uint8)
        im_bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)

        if "thumb" in filename.lower():
            im_clean = clean_star_watermark_fullbleed(im_bgr)
            out_raw_p = RENDERS_DIR / filename
            cv2.imwrite(str(out_raw_p), im_clean)
            im_1280 = cv2.resize(im_clean, (1280, 720), interpolation=cv2.INTER_LANCZOS4)
            cv2.imwrite(str(RENDERS_DIR / "tap04_thu_mo_vit_thumbnail_gemini.png"), im_1280)
            cv2.imwrite(
                str(RENDERS_DIR / "tap04_thu_mo_vit_thumbnail_gemini.jpg"),
                im_1280,
                [int(cv2.IMWRITE_JPEG_QUALITY), 95],
            )
            print(f"[THUMBNAIL SAVED & CLEANED] tap04_thu_mo_vit_thumbnail_gemini.jpg (1280x720)")
        else:
            im_clean = clean_star_watermark_whiteboard(im_bgr)
            out_p = G / filename
            cv2.imwrite(str(out_p), im_clean)
            h, w = im_clean.shape[:2]
            saved_items.append((filename, out_p, w, h))
            print(f"[SAVED & CLEANED] {filename} ({w}x{h})")

    # Build visual QA contact sheets (14 images per sheet)
    for sheet_idx in range(0, len(saved_items), 14):
        batch = saved_items[sheet_idx : sheet_idx + 14]
        cols = 2
        rows = (len(batch) + cols - 1) // cols
        tw, th = 512, 286
        sheet = Image.new("RGB", (cols * tw, rows * (th + 28)), (245, 245, 245))
        draw = ImageDraw.Draw(sheet)
        for i, (fname, img_p, w, h) in enumerate(batch):
            r = i // cols
            c = i % cols
            x = c * tw
            y = r * (th + 28)
            with Image.open(img_p) as thumb:
                thumb_resized = thumb.resize((tw, th), Image.LANCZOS)
                sheet.paste(thumb_resized, (x, y))
            draw.text((x + 8, y + th + 6), f"{fname} ({w}x{h})", fill=(20, 20, 20))
        sheet_num = (sheet_idx // 14) + 1
        sheet_out = QA_DIR / f"ep04_contact_sheet_0{sheet_num}.png"
        sheet.save(str(sheet_out), quality=95)
        print(f"[QA CONTACT SHEET SAVED] {sheet_out}")

    print(f"\nSuccessfully decoded, cleaned, and audited all {len(saved_items)} illustrations + 1 thumbnail!")


if __name__ == "__main__":
    main()
