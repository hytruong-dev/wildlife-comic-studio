"""
Master Render Script - Episode 4: Thú Mỏ Vịt (Full ~9m42s Long-form + ~48s Shorts at Broadcast Male 1.25x Voice + Official Intro/Outro)
Complies with 30-Day Animal World Whiteboard Channel Blueprint & V8.3 Engine:
- Long-form duration: ~9m22s body + ~20s Intro/Outro = ~9m42s (Requirement: 8:15 - 9:30+ min for Mid-roll Ads)
- Shorts duration: ~48.28s (Requirement: 45s - 58s)
- Audio: Broadcast Male 1.25x Voice with DSP Mastering EQ & Compressor
- Visuals: V8.3 Dynamic Multi-Node Canvas (27/27 unique assets), Fixed Top Header, Dead-Center Framing, 1.5s Overview Hold
"""

import sys
import time
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT / "src" / "render"))
sys.path.insert(0, str(PROJ / "scripts"))
from hybrid_whiteboard_renderer import HybridWhiteboardRenderer

HAND_ASSET = ROOT / "assets" / "hands" / "hand-marker-right.png"
SPECS_DIR = PROJ / "specs"
CANVAS_DIR = PROJ / "assets" / "scenes_composed"
AUDIO_DIR = PROJ / "audio"
RENDERS_DIR = PROJ / "renders"
SNAPSHOTS_DIR = RENDERS_DIR / "snapshots"
BRAND_DIR = ROOT / "assets" / "branding"

RENDERS_DIR.mkdir(parents=True, exist_ok=True)
SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)


def render_all_long_scenes(force: bool = False):
    print("=======================================================")
    print("STEP 1: RENDERING ALL 6 FULL-DURATION LONG-FORM SCENES (EP04)")
    print("Voice: Broadcast Male 1.25x | Engine: Hybrid Whiteboard V8.3 24fps")
    print("=======================================================")

    t_start = time.time()
    for i in range(1, 7):
        sid = f"scene{i:02d}"
        spec_p = SPECS_DIR / f"{sid}_spec.json"
        canvas_p = CANVAS_DIR / f"{sid}_canvas.png"
        audio_p = AUDIO_DIR / f"{sid}.wav"
        out_p = RENDERS_DIR / f"{sid}_final.mp4"

        if out_p.exists() and not force:
            print(f"[REUSING EXISTING] Scene {i}: {out_p.name} ({out_p.stat().st_size / 1024 / 1024:.2f} MB)")
            continue

        t_sc = time.time()
        print(f"\n--- [Rendering Scene {i}/6: {sid}] ---")
        renderer = HybridWhiteboardRenderer(spec_p, canvas_p, hand_path=HAND_ASSET, fps=24)
        renderer.render(out_p, audio_p)
        print(f"[COMPLETED] {sid} rendered in {time.time() - t_sc:.1f}s -> {out_p.name}")

    print(f"\nAll 6 scenes ready in {time.time() - t_start:.1f}s!")


def concat_master_and_intro_outro():
    print("\n=======================================================")
    print("STEP 2: CONCATENATING 6 SCENES + OFFICIAL INTRO/OUTRO")
    print("=======================================================")

    concat_list_file = RENDERS_DIR / "concat_list.txt"
    lines = []
    for i in range(1, 7):
        mp4_path = RENDERS_DIR / f"scene{i:02d}_final.mp4"
        lines.append(f"file '{mp4_path.resolve().as_posix()}'")

    concat_list_file.write_text("\n".join(lines), encoding="utf-8")
    master_out = RENDERS_DIR / "tap04_thu_mo_vit_master.mp4"

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", str(concat_list_file),
            "-c", "copy",
            str(master_out),
        ],
        check=True,
    )

    intro_mp4 = BRAND_DIR / "intro_ve_chuyen_hoang_da.mp4"
    outro_mp4 = BRAND_DIR / "outro_ve_chuyen_hoang_da.mp4"
    complete_out = RENDERS_DIR / "tap04_thu_mo_vit_complete_with_intro_outro.mp4"
    complete_alias = RENDERS_DIR / "tap04_thu_mo_vit_complete.mp4"

    full_list = RENDERS_DIR / "complete_concat_list.txt"
    full_lines = [
        f"file '{intro_mp4.resolve().as_posix()}'",
        f"file '{master_out.resolve().as_posix()}'",
        f"file '{outro_mp4.resolve().as_posix()}'",
    ]
    full_list.write_text("\n".join(full_lines), encoding="utf-8")

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", str(full_list),
            "-c:v", "libx264", "-preset", "fast", "-crf", "17",
            "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2",
            str(complete_out),
        ],
        check=True,
    )
    shutil.copy2(complete_out, complete_alias)

    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(complete_out),
    ]
    out = subprocess.check_output(probe_cmd, text=True).strip().split()
    dur_sec = float(out[0])
    size_mb = float(out[1]) / (1024 * 1024)

    print(f"[SUCCESS] Complete Episode 4 Exported: {complete_out}")
    print(f"  Duration: {dur_sec:.2f}s ({int(dur_sec//60)}m {int(dur_sec%60)}s, {dur_sec/60:.2f} minutes)")
    print(f"  Size: {size_mb:.2f} MB")
    return complete_out, dur_sec


def render_shorts_video(force: bool = False):
    print("\n=======================================================")
    print("STEP 3: RENDERING VERTICAL 9:16 SHORTS VIDEO (EP04)")
    print("=======================================================")

    audio_p = AUDIO_DIR / "shorts.wav"
    out_p = RENDERS_DIR / "tap04_thu_mo_vit_shorts.mp4"

    if out_p.exists() and not force:
        probe_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(out_p),
        ]
        dur_sec = float(subprocess.check_output(probe_cmd, text=True).strip())
        print(f"[REUSING EXISTING] Shorts: {out_p.name} ({dur_sec:.2f}s)")
        return out_p, dur_sec

    t0 = time.time()
    from render_shorts_ep04 import ShortsV4Renderer
    renderer = ShortsV4Renderer(fps=30)
    renderer.render_shorts_master(out_p, audio_p)

    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(out_p),
    ]
    out = subprocess.check_output(probe_cmd, text=True).strip().split()
    dur_sec = float(out[0])
    size_mb = float(out[1]) / (1024 * 1024)

    print(f"[SUCCESS] Shorts Video Exported: {out_p}")
    print(f"  Duration: {dur_sec:.2f}s (Target: 45s - 58s)")
    print(f"  Size: {size_mb:.2f} MB")
    print(f"  Render time: {time.time() - t0:.1f}s")
    return out_p, dur_sec


def take_verification_snapshots(complete_mp4: Path, shorts_mp4: Path):
    print("\n=======================================================")
    print("STEP 4: CAPTURING QUALITY VERIFICATION SNAPSHOTS")
    print("=======================================================")

    snap_timestamps = [20, 95, 190, 295, 390, 480]
    for ts in snap_timestamps:
        snap_out = SNAPSHOTS_DIR / f"ep04_snap_{ts}s.png"
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-ss", str(ts),
                "-i", str(complete_mp4),
                "-vframes", "1",
                "-q:v", "2",
                str(snap_out),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if snap_out.exists():
            print(f"  Captured Episode 4 snapshot at {ts}s: {snap_out.name}")

    shorts_snap = SNAPSHOTS_DIR / "ep04_shorts_snap_25s.png"
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-ss", "25",
            "-i", str(shorts_mp4),
            "-vframes", "1",
            "-q:v", "2",
            str(shorts_snap),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if shorts_snap.exists():
        print(f"  Captured Shorts snapshot at 25s: {shorts_snap.name}")


def main():
    print("=================================================================")
    print("PRODUCTION PIPELINE: EPISODE 4 THÚ MỎ VỊT (PLATYPUS)")
    print("=================================================================")

    force = "--force" in sys.argv or True

    # Step 1: Render all 6 long-form scenes
    render_all_long_scenes(force=force)

    # Step 2: Concat master long-form video
    complete_mp4, long_dur = concat_master_and_intro_outro()

    # Step 3: Render vertical Shorts
    shorts_mp4, shorts_dur = render_shorts_video(force=force)

    # Step 4: Capture audit snapshots
    take_verification_snapshots(complete_mp4, shorts_mp4)

    print("\n=================================================================")
    print("ALL RENDERS COMPLETED SUCCESSFULLY!")
    print(f"Long-form Complete: {complete_mp4} ({long_dur:.2f}s, {long_dur/60:.2f} min)")
    print(f"Shorts Complete:    {shorts_mp4} ({shorts_dur:.2f}s)")
    print("=================================================================")


if __name__ == "__main__":
    main()
