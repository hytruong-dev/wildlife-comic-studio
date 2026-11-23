"""
Batch Render All 6 Scenes Using Card Reveal & Handwriting Whiteboard Engine
- Images appear via smooth Card Entrance / Pop-in (NO hand scribbling over the artwork!)
- Hand rig strictly writes text (Titles, Bullet points, Annotations)
- Integrated with high-speed dynamic audio (tempo 1.24x)
- Automatically concatenates into Master MP4
"""

import sys
import time
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent

sys.path.insert(0, str(ROOT / "src" / "render"))
from card_reveal_handwriting_renderer import CardRevealHandwritingRenderer
from build_scene_specs import get_scene_spec

RENDERS_DIR = PROJ / "renders_v2"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)
HAND_ASSET = PROJ / "assets" / "user_clean_hand.png"

def render_scene(scene_idx: int):
    spec = get_scene_spec(scene_idx)
    sid = spec["id"]
    audio_wav = PROJ / "audio_fast" / f"{sid}.wav"
    out_mp4 = RENDERS_DIR / f"{sid}_card_handwriting.mp4"
    
    print(f"\n=======================================================")
    print(f"[RENDER V2] Starting Scene {scene_idx} -> {out_mp4.name}")
    print(f"Audio : {audio_wav}")
    print(f"Duration target: {spec['totalDurationMs']}ms")
    print(f"=======================================================")
    
    t0 = time.time()
    renderer = CardRevealHandwritingRenderer(spec, hand_path=HAND_ASSET, fps=24)
    renderer.render(out_mp4, audio_wav)
    print(f"[SUCCESS] Scene {scene_idx} rendered in {time.time() - t0:.1f}s -> {out_mp4}")
    return out_mp4

def concat_master():
    print("\n=======================================================")
    print("[CONCAT V2] Merging all 6 scenes into Master MP4...")
    print("=======================================================")
    
    concat_list_file = RENDERS_DIR / "concat_list_v2.txt"
    lines = []
    for i in range(1, 7):
        mp4_path = RENDERS_DIR / f"scene{i:02d}_card_handwriting.mp4"
        if not mp4_path.exists():
            raise FileNotFoundError(f"Missing rendered scene: {mp4_path}")
        p_str = str(mp4_path.resolve()).replace("\\", "/")
        lines.append(f"file '{p_str}'")
        
    concat_list_file.write_text("\n".join(lines), encoding="utf-8")
    
    master_out = RENDERS_DIR / "tap01_lung_mat_master_v2.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list_file),
        "-c", "copy",
        str(master_out)
    ]
    subprocess.run(cmd, check=True)
    print(f"[SUCCESS] Master V2 Video exported: {master_out}")
    return master_out

def render_all(scenes: list[int]):
    total_t0 = time.time()
    for s in scenes:
        render_scene(s)
    if len(scenes) == 6 or all((RENDERS_DIR / f"scene{i:02d}_card_handwriting.mp4").exists() for i in range(1, 7)):
        concat_master()
    print(f"\nAll render operations completed in {time.time() - total_t0:.1f}s!")

if __name__ == "__main__":
    scenes_to_run = [1, 2, 3, 4, 5, 6]
    if len(sys.argv) > 1:
        scenes_to_run = [int(x) for x in sys.argv[1:]]
    render_all(scenes_to_run)
