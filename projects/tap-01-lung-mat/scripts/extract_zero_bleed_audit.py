import subprocess
from pathlib import Path

PROJ = Path(__file__).resolve().parents[1]
RENDERS = PROJ / "renders"
OUT = RENDERS / "snapshots" / "zero_bleed_audit"
OUT.mkdir(parents=True, exist_ok=True)


def snap(mp4: Path, t: float, name: str):
    dst = OUT / name
    subprocess.run(
        ["ffmpeg", "-y", "-ss", str(t), "-i", str(mp4), "-vframes", "1", "-q:v", "2", str(dst)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(f"Captured {dst.name}")


if __name__ == "__main__":
    # Scene 6 Beat 1: p_start=0, p_end=24.68s -> t_img_end ~ 19.0s, t_cap_end ~ 23.2s
    s6 = RENDERS / "scene06_final.mp4"
    snap(s6, 17.5, "s6_b1_phase2_color_wash_end.png")   # Right at the bottom of Phase 2 color wash (BEFORE caption starts)
    snap(s6, 20.8, "s6_b1_phase3_mid_caption_write.png") # Mid-caption writing (ahead of pen must be 100% pure white!)
    snap(s6, 23.8, "s6_b1_completed.png")

    # Scene 1 Beat 5 (Guinness Record 12kg vs 200kg): p_start=44.5s, p_end=52.5s -> t_img_end ~ 50.6s, mid_cap ~ 51.3s
    s1 = RENDERS / "scene01_final.mp4"
    snap(s1, 50.4, "s1_b5_phase2_color_wash_end.png")
    snap(s1, 51.3, "s1_b5_phase3_mid_caption_write.png")

    # Scene 2 Beat 1 (STR 85 RPG): p_start=0, p_end=17.2s -> t_img_end ~ 13.3s, mid_cap ~ 14.7s
    s2 = RENDERS / "scene02_final.mp4"
    snap(s2, 13.0, "s2_b1_phase2_color_wash_end.png")
    snap(s2, 14.5, "s2_b1_phase3_mid_caption_write.png")
