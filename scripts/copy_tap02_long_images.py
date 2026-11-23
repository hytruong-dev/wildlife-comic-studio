import os, shutil

src_dir = "projects/tap-02-rai-ca-bien/assets/gemini_downloaded"
dst_dir = "projects/tap-02-rai-ca-bien/assets/long"
os.makedirs(dst_dir, exist_ok=True)

files = [
    # Scene 1 (6)
    "c1_family_tree_mustelidae.png",
    "c1_otter_cute_holding_hands_hearts.png",
    "c1_otter_myth_busted_thug_mask.png",
    "c1_otter_kelp_seatbelt_anchor.png",
    "c1_otter_drifting_to_orca_jaws.png",
    "c1_otter_hungry_pirate_crab_robber.png",
    # Scene 2 (8)
    "c2_otter_cuteness_hypnotize_humans.png",
    "c2_otter_rpg_cuteness_100.png",
    "c2_otter_no_blubber_vs_whale_seal.png",
    "c2_otter_rpg_fur_armor_95.png",
    "c2_otter_stone_anvil_mechanic.png",
    "c2_otter_rpg_iq_tool_92.png",
    "c2_otter_rpg_trickery_999.png",
    "c2_otter_three_crimes_montage.png",
    # Scene 3 (4)
    "c3_otter_1million_hairs_microscope.png",
    "c3_otter_grooming_laundry_4hours.png",
    "c3_otter_metabolism_furnace_25percent.png",
    "c3_otter_doraemon_armpit_pouch_hammer.png",
    # Scene 4 (4)
    "c4_otter_lazy_male_hungry_scheme.png",
    "c4_otter_pup_cork_float_kelp_crib.png",
    "c4_otter_kidnap_pup_for_ransom.png",
    "c4_otter_mom_pays_crab_ransom_stone_theft.png",
    # Scene 5 (4)
    "c5_kelp_forest_vs_purple_urchin_zombies.png",
    "c5_otter_urchin_slayer_purple_bones.png",
    "c5_otter_841_surfboard_pirate_santa_cruz.png",
    "c5_otter_841_outsmarts_coast_guard_nets.png",
    # Scene 6 (3)
    "c6_otter_keystone_guardian_balance.png",
    "c6_dolphin_cartoon_smile_angel.png",
    "c6_dolphin_pufferfish_volleyball_teaser.png"
]

for i, fn in enumerate(files, 1):
    lid = f"L{i:02d}.png"
    s = os.path.join(src_dir, fn)
    d = os.path.join(dst_dir, lid)
    shutil.copy2(s, d)
    print(f"{lid} <- {fn}")

print(f"Copied all {len(files)} long images to {dst_dir}")
