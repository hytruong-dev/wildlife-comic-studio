import subprocess
from pathlib import Path

out_dir = Path("projects/tap-07-tom-tit/renders/qa_snapshots")
out_dir.mkdir(parents=True, exist_ok=True)

long_mp4 = Path("projects/tap-07-tom-tit/renders/tap-07-tom-tit_long.mp4")
shorts_mp4 = Path("projects/tap-07-tom-tit/renders/tap-07-tom-tit_shorts.mp4")

# Snaps for longform at key moments:
# ~25s (Mike Tyson & 20cm), ~65s (Cua mai dày 1 đấm vỡ nát), ~100s (ATK 9999 / 1500N), ~120s (10400g đạn 22 ly), ~200s (Cavitation 4700°C Mặt Trời), ~250s (Nướng chín cua)
long_times = [
    ("25s_intro_20cm", 25.0),
    ("65s_crab_smash", 65.0),
    ("100s_rpg_atk", 100.0),
    ("120s_speed_10400g", 120.0),
    ("200s_cavitation_sun", 200.0),
    ("235s_cooked_crab", 235.0),
    ("310s_flan_molt", 310.0),
    ("430s_cancer_sensor", 430.0)
]

for name, ts in long_times:
    dst = out_dir / f"long_{name}.jpg"
    subprocess.run(["ffmpeg", "-y", "-ss", str(ts), "-i", str(long_mp4), "-vframes", "1", "-q:v", "2", str(dst)], capture_output=True)
    print(f"Captured long: {dst.name}")

# Snaps for shorts:
# ~5s (4700°C), ~18s (10400g), ~27s (sôi nước), ~42s (16 dải màu)
shorts_times = [
    ("05s_sun_heat", 5.0),
    ("18s_accel_10400g", 18.0),
    ("27s_boil_water", 27.0),
    ("42s_eyes_16colors", 42.0)
]

for name, ts in shorts_times:
    dst = out_dir / f"shorts_{name}.jpg"
    subprocess.run(["ffmpeg", "-y", "-ss", str(ts), "-i", str(shorts_mp4), "-vframes", "1", "-q:v", "2", str(dst)], capture_output=True)
    print(f"Captured shorts: {dst.name}")
