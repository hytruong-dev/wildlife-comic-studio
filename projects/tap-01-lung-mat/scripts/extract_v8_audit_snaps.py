import subprocess
from pathlib import Path

PROJ = Path(__file__).resolve().parents[1]
RENDERS = PROJ / "renders"
OUT = RENDERS / "snapshots" / "v8_complete_audit"
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
    s1 = RENDERS / "scene01_final.mp4"
    snap(s1, 35.0, "s1_b3_thug_sunglasses.png")
    snap(s1, 42.5, "s1_b4_guinness_fearless.png")
    snap(s1, 50.5, "s1_b5_guinness_record_15x.png")
    snap(s1, 67.2, "s1_overview_6nodes.png")

    s2 = RENDERS / "scene02_final.mp4"
    snap(s2, 14.5, "s2_b1_rpg_str85.png")
    snap(s2, 31.5, "s2_b2_drag_antelope.png")
    snap(s2, 42.0, "s2_b3_rpg_def99.png")
    snap(s2, 52.0, "s2_b4_deflect_3weapons.png")
    snap(s2, 63.5, "s2_b5_rpg_iq90.png")
    snap(s2, 75.0, "s2_b6_tenacity_999.png")
    snap(s2, 84.5, "s2_b7_rpg_fear0.png")
    snap(s2, 92.5, "s2_b8_amygdala_wrench.png")
    snap(s2, 95.2, "s2_overview_8nodes.png")

    s6 = RENDERS / "scene06_final.mp4"
    snap(s6, 38.0, "s6_b2_sea_otter_cute.png")
    snap(s6, 56.0, "s6_b3_sea_otter_teaser.png")
    snap(s6, 61.5, "s6_overview_3nodes.png")
