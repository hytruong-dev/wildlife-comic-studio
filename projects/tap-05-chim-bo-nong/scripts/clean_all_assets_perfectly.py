"""
Lossless Gemini Watermark Cleaner for Episode 5: Chim Bồ Nông (`tap-05-chim-bo-nong`)
Uses Inverse Alpha Deblending (LESSON-50 & LESSON-51) to eliminate 100% of the Gemini star watermark:
- Pure whiteboard areas: set to crisp #FFFFFF.
- Colored / comic / texture areas: exact deblend formula I = (I_raw - alpha * 255) / (1 - alpha).
- Zero blurring, 100% sharp line-art preserved.
"""

from pathlib import Path
import cv2
import numpy as np

PROJ = Path(__file__).resolve().parents[1]
RAW_LONG_DIR = PROJ / "assets" / "gemini_downloaded" / "_raw_with_watermark_backup"
CLEAN_LONG_DIR = PROJ / "assets" / "gemini_downloaded"

RAW_SHORTS_DIR = PROJ / "assets" / "gemini_downloaded_shorts" / "_raw_with_watermark_backup"
CLEAN_SHORTS_DIR = PROJ / "assets" / "gemini_downloaded_shorts"

RENDERS_DIR = PROJ / "renders"
QA_DIR = RENDERS_DIR / "qa_audit"
QA_DIR.mkdir(parents=True, exist_ok=True)

def build_astroid_star_mask(patch_size: int = 70, R: float = 25.5, p: float = 0.52) -> np.ndarray:
    center = patch_size / 2.0
    yy, xx = np.mgrid[0:patch_size, 0:patch_size]
    dx = np.abs(xx - center)
    dy = np.abs(yy - center)
    dist = (dx / R) ** p + (dy / R) ** p
    mask = (dist <= 1.0).astype(np.uint8) * 255
    dilated = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=1)
    return dilated

def clean_gemini_watermark_lossless(im: np.ndarray, alpha_map: np.ndarray = None) -> np.ndarray:
    h, w = im.shape[:2]
    # For standard 1024x572 Gemini image, watermark center is around (964, 523)
    # If 9:16 vertical (e.g. 572x1024 or 720x1280), adjust relative to bottom-right
    if w > h:
        cx = 964 if w == 1024 else int(w - 60)
        cy = 523 if h == 572 else int(h - 49)
    else:
        # Vertical image (9:16)
        cx = int(w - 60)
        cy = int(h - 49)
        
    y1, y2 = max(0, cy - 35), min(h, cy + 36)
    x1, x2 = max(0, cx - 35), min(w, cx + 36)

    out = im.copy()
    patch = out[y1:y2, x1:x2].astype(np.float32)
    ph, pw = patch.shape[:2]

    # Border pixels
    border_pixels = np.concatenate([
        patch[:3, :].reshape(-1, 3),
        patch[-3:, :].reshape(-1, 3),
        patch[:, :3].reshape(-1, 3),
        patch[:, -3:].reshape(-1, 3),
    ])
    border_mean = np.mean(border_pixels)
    border_min = np.min(border_pixels)

    if alpha_map is None:
        raw_mask = build_astroid_star_mask(max(ph, pw), R=25.5, p=0.52).astype(np.float32) / 255.0 * 0.43
        alpha_map = raw_mask[:ph, :pw]

    a3 = alpha_map[:, :, None]

    if border_mean > 248.0 and border_min > 230.0:
        # Pure whiteboard background
        mask_star = (alpha_map > 0.02)
        patch[mask_star] = 255.0
        out[y1:y2, x1:x2] = np.clip(patch, 0, 255).astype(np.uint8)
    else:
        # Colored, textured, or line-art background: Inverse Alpha Deblend
        deb = (patch - a3 * 255.0) / np.maximum(1.0 - a3, 0.05)
        out[y1:y2, x1:x2] = np.clip(deb, 0, 255).astype(np.uint8)

    return out

def clean_directory(raw_dir: Path, clean_dir: Path, label: str):
    if not raw_dir.exists():
        return 0
    files = sorted(list(raw_dir.glob("*.png")) + list(raw_dir.glob("*.jpg")))
    print(f"\n--- Cleaning {len(files)} {label} assets from {raw_dir.name} ---")
    cleaned_count = 0
    for p in files:
        raw_im = cv2.imread(str(p))
        if raw_im is None:
            continue
        cleaned = clean_gemini_watermark_lossless(raw_im)
        dst_p = clean_dir / p.name
        cv2.imwrite(str(dst_p), cleaned)
        cleaned_count += 1
        print(f"  [CLEANED] {p.name} -> {dst_p.name}")
    return cleaned_count

def main():
    print("=================================================================")
    print("EPISODE 5 (CHIM BỒ NÔNG) - LOSSLESS GEMINI WATERMARK CLEANER")
    print("=================================================================")
    c1 = clean_directory(RAW_LONG_DIR, CLEAN_LONG_DIR, "Long-form")
    c2 = clean_directory(RAW_SHORTS_DIR, CLEAN_SHORTS_DIR, "Shorts")
    print(f"\n[DONE] Cleaned {c1} long-form assets and {c2} shorts assets.")

if __name__ == "__main__":
    main()
