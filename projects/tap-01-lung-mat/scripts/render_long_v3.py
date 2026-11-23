"""
Batch Render All 6 Long-form Scenes & Concat Master (V3 Production Engine)
- Native 1920x1080 Full HD 24fps
- Edge-TTS expressive voiceover + word-level sync
- Pop-in reveals with ease_out_back physics
- Hand rig handwriting line-by-line
- Animated RPG stat bars
- Synchronized multi-layer SFX (Pop, Whoosh, Impact, Marker scribble)
"""

import sys
import time
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent

sys.path.insert(0, str(ROOT / "src" / "render"))
from v3_whiteboard_renderer import V3WhiteboardRenderer
from build_v3_specs import get_scene_spec_v3, SCENE_SPECS_V3

RENDERS_DIR = PROJ / "renders_v3"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)


def render_scene(scene_id: str):
    spec = get_scene_spec_v3(scene_id)
    audio_wav = PROJ / "audio_v3" / f"{scene_id}.wav"
    out_mp4 = RENDERS_DIR / f"{scene_id}_v3.mp4"

    print(f"\n=======================================================")
    print(f"[RENDER V3] Starting {scene_id} -> {out_mp4.name}")
    print(f"Duration target: {spec['totalDurationMs']}ms ({spec['totalDurationMs']/1000:.2f}s)")
    print(f"Audio path: {audio_wav}")
    print(f"=======================================================")

    t0 = time.time()
    renderer = V3WhiteboardRenderer(spec, fps=24, w=1920, h=1080)
    renderer.render_video_and_sfx(out_mp4, audio_wav)
    print(f"[SUCCESS] {scene_id} rendered in {time.time() - t0:.1f}s -> {out_mp4}")
    return out_mp4


def concat_master():
    print(f"\n=======================================================")
    print(f"[CONCAT V3] Concatenating all 6 scenes into Master V3...")
    print(f"=======================================================")

    concat_list = RENDERS_DIR / "concat_list_v3.txt"
    lines = []
    for i in range(1, 7):
        sid = f"scene{i:02d}"
        mp4_path = RENDERS_DIR / f"{sid}_v3.mp4"
        if not mp4_path.exists():
            raise FileNotFoundError(f"Missing rendered scene: {mp4_path}")
        p_str = str(mp4_path.resolve()).replace("\\", "/")
        lines.append(f"file '{p_str}'")

    concat_list.write_text("\n".join(lines), encoding="utf-8")
    master_out = RENDERS_DIR / "tap01_lung_mat_master_v3.mp4"

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        str(master_out)
    ]
    subprocess.run(cmd, check=True)
    print(f"[SUCCESS] Master V3 Long-form Exported: {master_out} ({master_out.stat().st_size / 1024 / 1024:.2f} MB)")
    return master_out


def render_all(scene_ids: list[str]):
    total_t0 = time.time()
    for sid in scene_ids:
        render_scene(sid)
    if len(scene_ids) == 6 or all((RENDERS_DIR / f"scene{i:02d}_v3.mp4").exists() for i in range(1, 7)):
        concat_master()
    print(f"\nAll operations completed in {time.time() - total_t0:.1f}s!")


if __name__ == "__main__":
    ids = sys.argv[1:] or [f"scene{i:02d}" for i in range(1, 7)]
    render_all(ids)
