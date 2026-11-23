import sys
from pathlib import Path
import cv2

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT))
from src.pipeline.asset_sanitizer import sanitize_image_file
from src.pipeline.thumbnail_master import build_episode_thumbnail

RAW_LONG = PROJ / "assets" / "gemini_downloaded" / "_raw_with_watermark_backup"
CLEAN_LONG = PROJ / "assets" / "gemini_downloaded"

RAW_SHORTS = PROJ / "assets" / "gemini_downloaded_shorts" / "_raw_with_watermark_backup"
CLEAN_SHORTS = PROJ / "assets" / "gemini_downloaded_shorts"

RENDERS_DIR = PROJ / "renders"

def sanitize_folder(raw_dir: Path, clean_dir: Path):
    clean_dir.mkdir(parents=True, exist_ok=True)
    images = list(raw_dir.glob("*.png")) + list(raw_dir.glob("*.jpg"))
    print(f"Sanitizing {len(images)} images in {raw_dir.name} -> {clean_dir.name} ...")
    for img_p in images:
        dst = clean_dir / f"{img_p.stem}.png"
        ok = sanitize_image_file(img_p, dst, clean_bottom_text=True)
        if ok:
            print(f" [CLEAN] {img_p.name} -> {dst.name}")
        else:
            print(f" [FAIL]  {img_p.name}")

def main():
    print("=== AUTOMATED ASSET SANITIZER — EPISODE 06: GẤU NƯỚC ===")
    
    # 1. Longform assets
    if RAW_LONG.exists():
        sanitize_folder(RAW_LONG, CLEAN_LONG)
        
    # 2. Shorts assets
    if RAW_SHORTS.exists():
        sanitize_folder(RAW_SHORTS, CLEAN_SHORTS)
        
    # 3. Thumbnail
    thumb_candidates = list(RAW_LONG.glob("*thumb*.png")) + list(CLEAN_LONG.glob("*thumb*.png"))
    if thumb_candidates:
        t_src = thumb_candidates[0]
        t_out = RENDERS_DIR / "tap06_gau_nuoc_thumbnail_gemini.jpg"
        print(f"\nBuilding 1280x720 High-CTR Thumbnail from: {t_src.name} ...")
        build_episode_thumbnail(t_src, episode_num=6, output_jpg_path=t_out)

if __name__ == "__main__":
    main()
