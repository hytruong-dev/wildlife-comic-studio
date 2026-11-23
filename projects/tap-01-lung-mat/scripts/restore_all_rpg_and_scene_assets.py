import shutil
import cv2
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJ = ROOT / "projects" / "tap-01-lung-mat"
ALL37 = PROJ / "renders" / "qa_audit" / "all_gemini_37"
G = PROJ / "assets" / "gemini_downloaded"
BACKUP = G / "_raw_with_watermark_backup"
BACKUP.mkdir(parents=True, exist_ok=True)


def clean_star_corner(src_path: Path, dst_path: Path) -> None:
    # Copy to backup first so clean_gemini_watermarks.py always has the true raw image
    backup_path = BACKUP / dst_path.name
    shutil.copy2(src_path, backup_path)

    im = cv2.imread(str(src_path))
    h, w = im.shape[:2]
    roi = im[h - 140 : h, w - 140 : w].copy()
    b, g, r = cv2.split(roi)
    yy, xx = np.mgrid[0:140, 0:140]
    star_paper_zone = (yy >= 40) & (xx >= 40) & (b >= 225) & (g >= 225) & (r >= 225)
    roi[star_paper_zone] = [255, 255, 255]
    im[h - 140 : h, w - 140 : w] = roi
    cv2.imwrite(str(dst_path), im)
    print(f"[RESTORED & CLEANED] {src_path.name} -> {dst_path.name} ({w}x{h})")


if __name__ == "__main__":
    # 1. Restore the 4 original RPG Stat Panel illustrations with full stat bars & labels
    clean_star_corner(ALL37 / "img_02.png", G / "c2_badger_muscles_strength.png")
    clean_star_corner(ALL37 / "img_03.png", G / "c2_badger_rubber_armor.png")
    clean_star_corner(ALL37 / "img_19.png", G / "c2_badger_iq_genius.png")
    clean_star_corner(ALL37 / "img_15.png", G / "c2_badger_fear_zero.png")

    # 2. Also preserve the 4 action/literal illustrations as separate dedicated assets
    clean_star_corner(ALL37 / "img_22.png", G / "c2_badger_drag_antelope_3x.png")
    clean_star_corner(ALL37 / "img_23.png", G / "c2_badger_deflect_3_weapons.png")
    clean_star_corner(ALL37 / "img_24.png", G / "c2_badger_tenacity_999_no_surrender.png")
    clean_star_corner(ALL37 / "img_35.png", G / "c2_badger_amygdala_wrench.png")

    # 3. Also restore the original Guinness Record comparison chart (img_16)
    clean_star_corner(ALL37 / "img_16.png", G / "c1_badger_guinness_record.png")

    # 4. Also restore the authentic Scene 6 Triumphant Badger on Savanna Rock (img_10)
    clean_star_corner(ALL37 / "img_10.png", G / "c6_badger_triumphant_rock.png")

    print("All RPG Stat & Action assets restored and watermark-cleaned!")
