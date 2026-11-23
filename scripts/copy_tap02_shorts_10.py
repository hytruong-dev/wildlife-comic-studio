import os, shutil

src = "projects/tap-02-rai-ca-bien/assets/gemini_downloaded"
dst = "projects/tap-02-rai-ca-bien/assets/shorts"

mapping = [
    ("c1_otter_cute_holding_hands_hearts.png", "S01.png"),
    ("c1_family_tree_mustelidae.png", "S02.png"),
    ("c1_otter_myth_busted_thug_mask.png", "S03.png"),
    ("c1_otter_kelp_seatbelt_anchor.png", "S04.png"),
    ("c1_otter_drifting_to_orca_jaws.png", "S05.png"),
    ("c3_otter_doraemon_armpit_pouch_hammer.png", "S06.png"),
    ("c2_otter_stone_anvil_mechanic.png", "S07.png"),
    ("c3_otter_metabolism_furnace_25percent.png", "S08.png"),
    ("c4_otter_kidnap_pup_for_ransom.png", "S09.png"),
    ("c5_otter_841_surfboard_pirate_santa_cruz.png", "S10.png")
]

for s_fn, d_fn in mapping:
    shutil.copy2(os.path.join(src, s_fn), os.path.join(dst, d_fn))
    print(f"{d_fn} <- {s_fn}")

print("Copied 10 images for tap-02 shorts")
