"""
Batch Convert Audio to 1.5x Male Voice (vi-VN-NamMinhNeural), Update Specs, and Render All 6 Scenes + Shorts
"""

import sys
import json
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]
AUDIO_V3_DIR = PROJ / "audio_v3"
AUDIO_DIR = PROJ / "audio"
SPECS_DIR = PROJ / "specs"
RENDERS_DIR = PROJ / "renders"

sys.path.insert(0, str(ROOT / "src" / "render"))
from hybrid_whiteboard_renderer import HybridWhiteboardRenderer

HAND_ASSET = ROOT / "assets" / "hands" / "hand-marker-right.png"
if not HAND_ASSET.exists():
    HAND_ASSET = PROJ / "assets" / "user_clean_hand.png"


def prepare_audio_and_specs():
    print("=======================================================")
    print("[AUDIO 1.5x] Preparing 1.5x Male Voice & Updating Specs...")
    print("=======================================================")
    
    # Target scenes
    scene_ids = [f"scene{i:02d}" for i in range(1, 7)] + ["shorts"]
    
    for sid in scene_ids:
        in_wav = AUDIO_V3_DIR / f"{sid}.wav"
        out_wav = AUDIO_DIR / f"{sid}.wav"
        
        if not in_wav.exists():
            raise FileNotFoundError(f"Missing source audio: {in_wav}")
            
        # Speed up by 1.3043 (1.15 * 1.3043 = 1.50x real-time speed)
        af_chain = (
            "atempo=1.3043,"
            "highpass=f=75,lowpass=f=13500,"
            "equalizer=f=150:width_type=o:w=1.0:g=2.2,"
            "equalizer=f=3200:width_type=o:w=1.0:g=1.8,"
            "acompressor=threshold=-16dB:ratio=3:attack=5:release=50,"
            "volume=1.2"
        )
        cmd_ff = [
            "ffmpeg", "-y",
            "-i", str(in_wav),
            "-filter:a", af_chain,
            "-ar", "48000",
            "-ac", "2",
            "-c:a", "pcm_s16le",
            str(out_wav)
        ]
        subprocess.run(cmd_ff, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        # Probe duration
        probe_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(out_wav)
        ]
        dur_str = subprocess.check_output(probe_cmd, text=True).strip()
        dur_sec = float(dur_str)
        dur_ms = int(round(dur_sec * 1000))
        print(f"  -> {sid}.wav: {dur_sec:.2f}s ({dur_ms}ms)")
        
        # Update spec
        spec_path = SPECS_DIR / f"{sid}_spec.json"
        if spec_path.exists():
            with open(spec_path, "r", encoding="utf-8") as f:
                spec = json.load(f)
                
            old_dur = spec.get("duration_ms", 60000)
            spec["duration_ms"] = dur_ms
            ratio = dur_ms / max(1.0, old_dur)
            
            for p in spec.get("panels", []):
                p["start_ms"] = int(round(p["start_ms"] * ratio))
                p["end_ms"] = int(round(p["end_ms"] * ratio))
                
            with open(spec_path, "w", encoding="utf-8") as f:
                json.dump(spec, f, ensure_ascii=False, indent=2)
            print(f"     Spec updated: {old_dur}ms -> {dur_ms}ms (ratio: {ratio:.3f})")


def render_all_scenes():
    print("\n=======================================================")
    print("[RENDER 1.5x] Rendering All 6 Long-form Scenes...")
    print("=======================================================")
    
    t0 = time.time()
    for i in range(1, 7):
        sid = f"scene{i:02d}"
        canvas_p = PROJ / "assets" / "scenes_composed" / f"{sid}_canvas.png"
        spec_p = SPECS_DIR / f"{sid}_spec.json"
        audio_p = AUDIO_DIR / f"{sid}.wav"
        out_p = RENDERS_DIR / f"{sid}_final.mp4"
        
        t_sc = time.time()
        renderer = HybridWhiteboardRenderer(spec_p, canvas_p, hand_path=HAND_ASSET, fps=24)
        renderer.render(out_p, audio_p)
        print(f"[DONE] Scene {i} rendered in {time.time() - t_sc:.1f}s -> {out_p.name}")
        
    # Concat master
    print("\n=======================================================")
    print("[CONCAT] Merging 6 scenes into Master MP4...")
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
    print(f"[SUCCESS] Master Video exported: {master_out}")
    print(f"Total time for long scenes: {time.time() - t0:.1f}s")


def render_shorts():
    print("\n=======================================================")
    print("[RENDER SHORTS 1.5x] Rendering Vertical Shorts...")
    print("=======================================================")
    c_p = PROJ / "assets" / "scenes_composed" / "shorts_canvas.png"
    spec_p = SPECS_DIR / "shorts_spec.json"
    audio_p = AUDIO_DIR / "shorts.wav"
    out_p = RENDERS_DIR / "tap01_lung_mat_shorts.mp4"
    
    t0 = time.time()
    renderer = HybridWhiteboardRenderer(spec_p, c_p, hand_path=HAND_ASSET, fps=24)
    renderer.render(out_p, audio_p)
    print(f"[SUCCESS] Shorts Video Rendered in {time.time() - t0:.1f}s -> {out_p.name}")


if __name__ == "__main__":
    t_start = time.time()
    prepare_audio_and_specs()
    render_all_scenes()
    render_shorts()
    print(f"\n=======================================================")
    print(f"[ALL COMPLETE] Finished everything in {time.time() - t_start:.1f}s!")
    print("=======================================================")
