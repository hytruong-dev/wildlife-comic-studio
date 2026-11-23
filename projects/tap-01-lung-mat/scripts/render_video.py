"""
Batch Render All 6 Scenes + Master Video Concatenation
Project: Tap 01 - Lung Mat (Honey Badger)
Engine: LiveColorWhiteboardRenderer with Clean Hand Rig
"""

import sys
import time
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent

sys.path.insert(0, str(ROOT / "src" / "render"))
from hybrid_whiteboard_renderer import HybridWhiteboardRenderer

RENDERS_DIR = PROJ / "renders"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)

HAND_ASSET = ROOT / "assets" / "hands" / "hand-marker-right.png"
if not HAND_ASSET.exists():
    HAND_ASSET = PROJ / "assets" / "user_clean_hand.png"

def render_scene(scene_idx: int):
    sid = f"scene{scene_idx:02d}"
    canvas_p = PROJ / "assets" / "scenes_composed" / f"{sid}_canvas.png"
    spec_p = PROJ / "specs" / f"{sid}_spec.json"
    audio_p = PROJ / "audio" / f"{sid}.wav"
    out_p = RENDERS_DIR / f"{sid}_final.mp4"
    
    print(f"\n=======================================================")
    print(f"[HYBRID RENDER] Starting Scene {scene_idx} -> {out_p.name}")
    print(f"Canvas: {canvas_p}")
    print(f"Spec  : {spec_p}")
    print(f"Audio : {audio_p}")
    print(f"=======================================================")
    
    t0 = time.time()
    renderer = HybridWhiteboardRenderer(spec_p, canvas_p, hand_path=HAND_ASSET, fps=24)
    renderer.render(out_p, audio_p)
    elapsed = time.time() - t0
    print(f"[DONE] Scene {scene_idx} finished in {elapsed:.1f}s -> {out_p}")
    return out_p

def concat_master():
    print("\n=======================================================")
    print("[CONCAT] Merging all 6 scenes into Master MP4...")
    print("=======================================================")
    
    concat_list_file = RENDERS_DIR / "concat_list.txt"
    lines = []
    for i in range(1, 7):
        mp4_path = RENDERS_DIR / f"scene{i:02d}_final.mp4"
        if not mp4_path.exists():
            raise FileNotFoundError(f"Missing rendered scene: {mp4_path}")
        # Use forward slashes for ffmpeg concat
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
    return master_out

def render_all(scenes: list[int]):
    total_t0 = time.time()
    for s in scenes:
        render_scene(s)
    
    # Check if all 6 exist
    all_exist = all((RENDERS_DIR / f"scene{i:02d}_final.mp4").exists() for i in range(1, 7))
    if all_exist:
        concat_master()
    print(f"\nAll render operations completed in {time.time() - total_t0:.1f}s!")

if __name__ == "__main__":
    scenes_to_run = [1, 2, 3, 4, 5, 6]
    if len(sys.argv) > 1:
        scenes_to_run = [int(x) for x in sys.argv[1:]]
    render_all(scenes_to_run)
