import os, shutil

src_dir = "projects/tap-03-ca-heo/assets/gemini_downloaded"
dst_dir = "projects/tap-03-ca-heo/assets/long"
os.makedirs(dst_dir, exist_ok=True)

files = [
    # Scene 1 (6)
    "c1_otter_to_dolphin_bridge.png",
    "c1_cartoon_angel_dolphin_myth.png",
    "c1_permanent_smile_jaw_anatomy.png",
    "c1_dolphin_cool_ocean_boss.png",
    "c1_dolphin_tickling_pufferfish.png",
    "c1_dolphin_chasing_great_white_shark.png",
    # Scene 2 (8)
    "c2_dolphin_mirror_selfie_iq.png",
    "c2_stat_card_iq.png",
    "c2_dolphin_xray_sonar_vision.png",
    "c2_stat_card_sonar.png",
    "c2_dolphin_rocket_acrobatics.png",
    "c2_stat_card_speed.png",
    "c2_stat_card_playfulness.png",
    "c2_dolphin_surfing_bubble_rings.png",
    # Scene 3 (4)
    "c3_melon_biosonar_anatomy.png",
    "c3_half_brain_sleep_elevator.png",
    "c3_signature_whistle_id_card.png",
    "c3_sponge_nose_armor_tool.png",
    # Scene 4 (4)
    "c4_dolphin_pufferfish_volleyball_game.png",
    "c4_dolphin_dizzy_mirror_floating.png",
    "c4_mud_ring_fishing_net.png",
    "c4_aerial_fish_catch_feast.png",
    # Scene 5 (4)
    "c5_shark_vs_dolphin_pod_tactics.png",
    "c5_rostrum_torpedo_belly_bump.png",
    "c5_pelorus_jack_ship_guide.png",
    "c5_dolphin_lifeguard_rescue_circle.png",
    # Scene 6 (3)
    "c6_ocean_geniuses_conservation.png",
    "c6_drawing_challenge_dolphin_art.png",
    "c6_ep04_platypus_teaser.png"
]

for i, fn in enumerate(files, 1):
    lid = f"L{i:02d}.png"
    s = os.path.join(src_dir, fn)
    d = os.path.join(dst_dir, lid)
    shutil.copy2(s, d)
    print(f"{lid} <- {fn}")

print(f"Copied all {len(files)} long images to {dst_dir}")
