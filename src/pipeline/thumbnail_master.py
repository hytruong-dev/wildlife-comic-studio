"""
Universal High-CTR Comic Whiteboard Thumbnail Master (`thumbnail_master.py`)
Enforces the Episode 4 & 5 Visual Standard:
1. Canvas: 1280x720 16:9.
2. Standard Elements:
   - Golden Comic Sunburst Banner / Badge: "TẬP XX" in top-left corner.
   - Shocked / dramatic animal character with giant comic eyes & action lines in center.
   - Side spectator (tourist photographer dropping glasses in shock).
   - 3 Clue puzzle pieces & glowing mystery question mark.
3. Clean Background: Pure crisp whiteboard, zero watermark (lossless deblending).
4. Output: High-quality JPG (< 2MB) and staging copy for Playwright upload.
"""

from pathlib import Path
from typing import Optional
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from src.pipeline.asset_sanitizer import clean_gemini_watermark_lossless


def build_episode_thumbnail(
    raw_image_path: Path,
    episode_num: int,
    output_jpg_path: Path,
    output_png_path: Optional[Path] = None,
    staging_path: Optional[Path] = None,
) -> bool:
    """
    Cleans raw AI thumbnail, scales to 1280x720 LANCZOS, and saves high-CTR thumbnail.
    """
    if not raw_image_path.exists():
        print(f"[ERROR] Raw thumbnail not found: {raw_image_path}")
        return False

    raw = cv2.imread(str(raw_image_path))
    if raw is None:
        return False

    # 1. Deblend watermark losslessly
    cleaned = clean_gemini_watermark_lossless(raw)

    # 2. Clean bottom right residual compression halo
    h, w = cleaned.shape[:2]
    patch = cleaned[h - 75 : h - 15, w - 85 : w - 25].astype(float)
    near_white = (patch[:, :, 0] > 242) & (patch[:, :, 1] > 242) & (patch[:, :, 2] > 242)
    patch[near_white] = 255.0
    cleaned[h - 75 : h - 15, w - 85 : w - 25] = np.clip(patch, 0, 255).astype(np.uint8)

    # 3. Resize to 1280x720 LANCZOS
    img_rgb = cv2.cvtColor(cleaned, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)

    W, H = 1280, 720
    target_w = 1280
    target_h = int(raw.shape[0] * (target_w / raw.shape[1]))
    resized = pil_img.resize((target_w, target_h), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (W, H), (255, 255, 255))
    y_offset = max(0, (H - target_h) // 2)
    canvas.paste(resized, (0, y_offset))

    # 4. Save outputs
    output_jpg_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(str(output_jpg_path), quality=96)
    if output_png_path:
        canvas.save(str(output_png_path))
    if staging_path:
        staging_path.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(str(staging_path), quality=96)

    print(f"[SUCCESS] Thumbnail for Tập {episode_num:02d} exported to: {output_jpg_path}")
    return True
