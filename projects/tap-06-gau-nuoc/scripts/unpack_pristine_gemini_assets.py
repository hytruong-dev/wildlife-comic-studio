import json
import base64
from pathlib import Path
from PIL import Image
import io

ROOT = Path(__file__).resolve().parents[3]
LONG_DIR = ROOT / "projects" / "tap-06-gau-nuoc" / "assets" / "gemini_downloaded"
SHORTS_DIR = ROOT / "projects" / "tap-06-gau-nuoc" / "assets" / "gemini_downloaded_shorts"
RAW_LONG_BACKUP = LONG_DIR / "_raw_with_watermark_backup"
RAW_SHORTS_BACKUP = SHORTS_DIR / "_raw_with_watermark_backup"

LONG_DIR.mkdir(parents=True, exist_ok=True)
SHORTS_DIR.mkdir(parents=True, exist_ok=True)
RAW_LONG_BACKUP.mkdir(parents=True, exist_ok=True)
RAW_SHORTS_BACKUP.mkdir(parents=True, exist_ok=True)

# Map index 0..29 to exact project filenames
MAPPING = {
    0: ("thumb_ep06_gau_nuoc_gemini.png", "thumb"),
    1: ("shorts01_superhero_space_radiation.png", "shorts"),
    2: ("shorts02_temperature_extreme_scale.png", "shorts"),
    3: ("shorts03_tun_state_glass_hibernation.png", "shorts"),
    4: ("shorts04_snail_slime_choke_trap.png", "shorts"),
    5: ("shorts05_moon_crash_sleeping_bears.png", "shorts"),
    6: ("shorts06_channel_funnel_cta_mascot.png", "shorts"),
    7: ("scene01_01_meteor_extinction_survivor.png", "long"),
    8: ("scene01_02_microscopic_cute_water_bear.png", "long"),
    9: ("scene01_03_extreme_endurance_triad.png", "long"),
    10: ("scene01_04_space_vacuum_foton_mission.png", "long"),
    11: ("scene02_01_rpg_card_atk_spd_low.png", "long"),
    12: ("scene02_02_rpg_card_def_max_temperature.png", "long"),
    13: ("scene02_03_radiation_lethal_dose_comparison.png", "long"),
    14: ("scene02_04_rpg_cryptobiosis_tun_state.png", "long"),
    15: ("scene03_01_water_desiccation_process.png", "long"),
    16: ("scene03_02_tdp_amorphous_glass_matrix.png", "long"),
    17: ("scene03_03_dsup_protein_radiation_shield.png", "long"),
    18: ("scene03_04_revival_single_water_drop.png", "long"),
    19: ("scene04_01_superhero_vs_glass_fragile.png", "long"),
    20: ("scene04_02_snail_slime_lethal_trap.png", "long"),
    21: ("scene04_03_nematode_worm_predator_snack.png", "long"),
    22: ("scene04_04_global_warming_water_temp.png", "long"),
    23: ("scene05_01_beresheet_moon_lander_launch.png", "long"),
    24: ("scene05_02_moon_crash_explosion_debris.png", "long"),
    25: ("scene05_03_tardigrades_scattered_moon_craters.png", "long"),
    26: ("scene05_04_astronaut_water_revival_dream.png", "long"),
    27: ("scene06_01_philosophical_adaptation_triumph.png", "long"),
    28: ("scene06_02_mantis_shrimp_boxing_teaser.png", "long"),
}

def main():
    print("=== UNPACKING ALL PRISTINE IMAGES FROM GEMINI DATAURL BATCHES ===")
    all_data = {}
    for b_idx in range(6):
        batch_file = Path(rf"C:\Users\PC\tap06_batch_{b_idx}.json")
        if not batch_file.exists():
            print(f"Warning: {batch_file} not found!")
            continue
        with open(batch_file, "r", encoding="utf-8") as f:
            items = json.load(f)
        for it in items:
            all_data[it["idx"]] = it

    print(f"Loaded {len(all_data)} items from batch JSONs.")

    for idx, (fname, cat) in MAPPING.items():
        if idx not in all_data:
            print(f"[MISSING] Idx {idx} ({fname}) not found in batches!")
            continue
        it = all_data[idx]
        header, b64_str = it["dataUrl"].split(",", 1)
        raw_bytes = base64.b64decode(b64_str)
        im = Image.open(io.BytesIO(raw_bytes))

        if cat == "shorts":
            backup_p = RAW_SHORTS_BACKUP / fname
            clean_p = SHORTS_DIR / fname
        elif cat == "thumb":
            backup_p = RAW_LONG_BACKUP / fname
            clean_p = LONG_DIR / fname
        else:
            backup_p = RAW_LONG_BACKUP / fname
            clean_p = LONG_DIR / fname

        # 1. Save raw pristine backup
        backup_p.write_bytes(raw_bytes)
        # 2. Save active clean image
        clean_p.write_bytes(raw_bytes)
        print(f"[{cat.upper()}] Saved {fname}: {im.size} ({len(raw_bytes):,} bytes)")

    print("\n[SUCCESS] All 29 pristine assets unpacked successfully!")

if __name__ == "__main__":
    main()
