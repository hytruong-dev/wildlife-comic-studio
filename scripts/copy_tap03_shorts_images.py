import os, shutil

src_dir = "projects/tap-03-ca-heo/assets/gemini_downloaded"
dst_dir = "projects/tap-03-ca-heo/assets/shorts"
os.makedirs(dst_dir, exist_ok=True)

shorts_mapping = [
    ("c1_cartoon_angel_dolphin_myth.png", "S01.png"),
    ("c1_permanent_smile_jaw_anatomy.png", "S02.png"),
    ("c1_dolphin_cool_ocean_boss.png", "S03.png"),
    ("c2_dolphin_mirror_selfie_iq.png", "S04.png"),
    ("c3_melon_biosonar_anatomy.png", "S05.png"),
    ("c3_half_brain_sleep_elevator.png", "S06.png"),
    ("c4_dolphin_pufferfish_volleyball_game.png", "S07.png"),
    ("c5_rostrum_torpedo_belly_bump.png", "S08.png")
]

for src, dst in shorts_mapping:
    s = os.path.join(src_dir, src)
    d = os.path.join(dst_dir, dst)
    shutil.copy2(s, d)
    print(f"{dst} <- {src}")

print("Copied all shorts images for tap-03")
