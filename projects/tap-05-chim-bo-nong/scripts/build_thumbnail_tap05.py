"""
Build High-CTR 1280x720 YouTube Thumbnail for Episode 5: Chim Bồ Nông (`tap-05-chim-bo-nong`)
Uses the official AI-generated artwork approved by the Director:
- Shocked Pelican with giant wide open beak trying to swallow Capybara
- Tourist photographer dropping camera screaming in shock
- Official AI-illustrated 'TẬP 05' sunburst scroll banner
- 3 clue puzzle pieces & mystery question mark
- Clean 100% whiteboard background with zero watermark (Inverse Alpha Deblended)
- Crisp 1280x720 16:9 master export (< 2MB)
"""

from pathlib import Path
import cv2
import numpy as np
from PIL import Image
import sys

PROJ = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJ / "scripts"))
from clean_all_assets_perfectly import clean_gemini_watermark_lossless

RENDERS_DIR = PROJ / "renders"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)

OUT_JPG = RENDERS_DIR / "tap05_chim_bo_nong_thumbnail_gemini.jpg"
OUT_PNG = RENDERS_DIR / "tap05_chim_bo_nong_thumbnail_gemini.png"
STAGE_JPG = Path(r"C:\Users\PC\.playwright-mcp\tap05_chim_bo_nong_thumbnail.jpg")
STAGE_PNG = Path(r"C:\Users\PC\.playwright-mcp\tap05_chim_bo_nong_thumbnail.png")

SRC_CANDIDATES = [
    RENDERS_DIR / "thumb_prompt_raw_var2.png",
    RENDERS_DIR / "thumb_ep05_chim_bo_nong_raw.png",
]

def main():
    src_file = None
    for c in SRC_CANDIDATES:
        if c.exists():
            src_file = c
            break

    if not src_file:
        raise FileNotFoundError("Could not find thumbnail raw source image!")

    print(f"[INFO] Using official AI thumbnail source: {src_file.name}")
    raw = cv2.imread(str(src_file))
    cleaned = clean_gemini_watermark_lossless(raw)

    # Clean residual compression near-white at watermark area
    h, w = cleaned.shape[:2]
    patch = cleaned[h - 75 : h - 15, w - 85 : w - 25].astype(float)
    near_white = (patch[:, :, 0] > 245) & (patch[:, :, 1] > 245) & (patch[:, :, 2] > 245)
    patch[near_white] = 255.0
    cleaned[h - 75 : h - 15, w - 85 : w - 25] = np.clip(patch, 0, 255).astype(np.uint8)

    # Scale to 1280x720 LANCZOS
    img_rgb = cv2.cvtColor(cleaned, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)

    W, H = 1280, 720
    target_w = 1280
    target_h = int(raw.shape[0] * (target_w / raw.shape[1]))
    resized = pil_img.resize((target_w, target_h), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (W, H), (255, 255, 255))
    y_offset = (H - target_h) // 2
    canvas.paste(resized, (0, y_offset))

    canvas.save(str(OUT_JPG), quality=96)
    canvas.save(str(OUT_PNG))

    STAGE_JPG.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(str(STAGE_JPG), quality=96)
    canvas.save(str(STAGE_PNG))

    print(f"[SUCCESS] Built official AI Thumbnail 1280x720:")
    print(f"  JPG: {OUT_JPG} ({OUT_JPG.stat().st_size / 1024:.1f} KB)")
    print(f"  PNG: {OUT_PNG} ({OUT_PNG.stat().st_size / 1024:.1f} KB)")
    print(f"  Staged: {STAGE_JPG}")

if __name__ == "__main__":
    main()
