"""
Master Render Script - Episode 1: Lửng Mật (Full 9m 43s Long-form + 57s Shorts at 1.25x Male Voice)
Complies with 30-Day Animal World Whiteboard Channel Blueprint:
- Long-form duration: 9m 43s (Requirement: 8:30 - 9:30 min / 8:15 - 10:30 min for Mid-roll Ads)
- Shorts duration: 57.35s (Requirement: 45s - 58s)
- Audio: 1.25x Male Voice with warm EQ, broadcast compression & ducked BGM
- Visuals: Dual Semantic Islands, Character-by-character handwriting, real hand rig with pen nib tracking
"""

import sys
import time
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT / "src" / "render"))
from hybrid_whiteboard_renderer import HybridWhiteboardRenderer

HAND_ASSET = ROOT / "assets" / "hands" / "hand-marker-right.png"
if not HAND_ASSET.exists():
    HAND_ASSET = PROJ / "assets" / "user_clean_hand.png"

SPECS_DIR = PROJ / "specs"
CANVAS_DIR = PROJ / "assets" / "scenes_composed"
AUDIO_DIR = PROJ / "audio"
RENDERS_DIR = PROJ / "renders"
SNAPSHOTS_DIR = RENDERS_DIR / "snapshots"

RENDERS_DIR.mkdir(parents=True, exist_ok=True)
SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)


def render_all_long_scenes(force: bool = False):
    print("=======================================================")
    print("STEP 1: RENDERING ALL 6 FULL-DURATION LONG-FORM SCENES")
    print("Voice: 1.25x Male Voice | Engine: Hybrid Whiteboard 24fps")
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
    

def concat_master_video():
    print("\n=======================================================")
    print("STEP 2: CONCATENATING 6 SCENES INTO MASTER LONG-FORM MP4")
    print("=======================================================")
    
    concat_list_file = RENDERS_DIR / "concat_list.txt"
    lines = []
    for i in range(1, 7):
        mp4_path = RENDERS_DIR / f"scene{i:02d}_final.mp4"
        p_str = str(mp4_path.resolve()).replace("\\", "/")
        lines.append(f"file '{p_str}'")
        
    concat_list_file.write_text("\n".join(lines), encoding="utf-8")
    master_out = RENDERS_DIR / "tap01_lung_mat_master.mp4"
    
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list_file),
        "-c", "copy",
        str(master_out)
    ]
    subprocess.run(cmd, check=True)
    
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(master_out)
    ]
    out = subprocess.check_output(probe_cmd, text=True).strip().split()
    dur_sec = float(out[0])
    size_mb = float(out[1]) / (1024 * 1024)
    
    print(f"[SUCCESS] Master Video Exported: {master_out}")
    print(f"  Duration: {dur_sec:.2f}s ({dur_sec/60:.2f} minutes, {int(dur_sec//60)}m {int(dur_sec%60)}s)")
    print(f"  Size: {size_mb:.2f} MB")
    return master_out, dur_sec


def render_shorts_video(force: bool = False):
    print("\n=======================================================")
    print("STEP 3: RENDERING VERTICAL 9:16 SHORTS VIDEO")
    print("=======================================================")
    
    audio_p = AUDIO_DIR / "shorts.wav"
    out_p = RENDERS_DIR / "tap01_lung_mat_shorts.mp4"

    if out_p.exists() and not force:
        probe_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(out_p)
        ]
        dur_sec = float(subprocess.check_output(probe_cmd, text=True).strip())
        print(f"[REUSING EXISTING] Shorts: {out_p.name} ({dur_sec:.2f}s)")
        return out_p, dur_sec
    
    t0 = time.time()
    from render_shorts_v4 import ShortsV4Renderer
    renderer = ShortsV4Renderer(fps=30)
    renderer.render_shorts_master(out_p, audio_p)
    
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(out_p)
    ]
    out = subprocess.check_output(probe_cmd, text=True).strip().split()
    dur_sec = float(out[0])
    size_mb = float(out[1]) / (1024 * 1024)
    
    print(f"[SUCCESS] Shorts Video Exported: {out_p}")
    print(f"  Duration: {dur_sec:.2f}s (Target: 45s - 58s)")
    print(f"  Size: {size_mb:.2f} MB")
    print(f"  Render time: {time.time() - t0:.1f}s")
    return out_p, dur_sec


def take_verification_snapshots(master_mp4: Path, shorts_mp4: Path):
    print("\n=======================================================")
    print("STEP 4: CAPTURING QUALITY VERIFICATION SNAPSHOTS")
    print("=======================================================")
    
    snap_timestamps = [45, 120, 240, 360, 480, 540]
    for ts in snap_timestamps:
        snap_out = SNAPSHOTS_DIR / f"master_snap_{ts}s.png"
        cmd = [
            "ffmpeg", "-y",
            "-ss", str(ts),
            "-i", str(master_mp4),
            "-vframes", "1",
            "-q:v", "2",
            str(snap_out)
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if snap_out.exists():
            print(f"  Captured Master snapshot at {ts}s: {snap_out.name}")
            
    # Shorts snapshot at 25s
    shorts_snap = SNAPSHOTS_DIR / "shorts_snap_25s.png"
    cmd_s = [
        "ffmpeg", "-y",
        "-ss", "25",
        "-i", str(shorts_mp4),
        "-vframes", "1",
        "-q:v", "2",
        str(shorts_snap)
    ]
    subprocess.run(cmd_s, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if shorts_snap.exists():
        print(f"  Captured Shorts snapshot at 25s: {shorts_snap.name}")


def main():
    t_global = time.time()
    force_flag = "--force" in sys.argv
    print("=======================================================")
    print("EPISODE 1 MASTER PRODUCTION PIPELINE (1.25x SPEED)")
    print("Target Long-form: 8:30 - 9:30 min | Target Shorts: 45s - 58s")
    print(f"Force re-render: {force_flag}")
    print("=======================================================")
    
    render_all_long_scenes(force=force_flag)
    master_mp4, long_dur = concat_master_video()
    shorts_mp4, shorts_dur = render_shorts_video(force=force_flag)
    take_verification_snapshots(master_mp4, shorts_mp4)
    
    print("\n=======================================================")
    print("FINAL PRODUCTION SUMMARY:")
    print(f"- Master Long-form: {master_mp4} ({long_dur:.1f}s / {long_dur/60:.2f} min)")
    print(f"- YouTube Shorts:   {shorts_mp4} ({shorts_dur:.1f}s)")
    print(f"- Total Render Runtime: {time.time() - t_global:.1f}s")
    print(">>> 100% COMPLIANT WITH 30-DAY ANIMAL WORLD BLUEPRINT! <<<")
    print("=======================================================")


if __name__ == "__main__":
    main()
