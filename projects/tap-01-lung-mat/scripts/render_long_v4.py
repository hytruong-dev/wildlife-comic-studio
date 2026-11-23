"""
Batch Render All 6 Long-form Scenes & Concat Master (V4 HyperFrames & Remotion Engine)
- Native 1920x1080 Full HD 24fps
- 100% True Sequential Line-by-Line, Word-by-Word, Char-by-Char Handwriting (Zero "Tô" / Zero Wipe)
- Remotion Damped Harmonic Spring Physics (omega=16.0, zeta=0.82)
- Hand Rig with Carriage Return Lift Arcs & Space Hops
- HyperFrames Modern Editorial Palette & Multilayer Shadows
- 4-Layer Master Audio: Expressive Narration + Line-Synced SFX + Sidechain Ducked BGM
"""

import sys
import time
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent

sys.path.insert(0, str(ROOT))
from src.render.hyper_handwriting_engine import HyperWhiteboardRenderer

import importlib.util
spec_path = SCRIPT_DIR / "build_v3_specs.py"
spec_mod_spec = importlib.util.spec_from_file_location("build_v3_specs", str(spec_path))
build_v3_specs = importlib.util.module_from_spec(spec_mod_spec)
spec_mod_spec.loader.exec_module(build_v3_specs)
get_scene_spec_v3 = build_v3_specs.get_scene_spec_v3

RENDERS_DIR = PROJ / "renders_v4"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)
BGM_WAV = ROOT / "assets" / "bgm" / "calm-acoustic.wav"


def render_scene(scene_id: str):
    spec = get_scene_spec_v3(scene_id)
    audio_wav = PROJ / "audio_v3" / f"{scene_id}.wav"
    out_mp4 = RENDERS_DIR / f"{scene_id}_v4.mp4"

    print(f"\n=======================================================")
    print(f"[RENDER V4 HYPERFRAMES & REMOTION] Starting {scene_id} -> {out_mp4.name}")
    print(f"Duration target: {spec['totalDurationMs']}ms ({spec['totalDurationMs']/1000:.2f}s)")
    print(f"Audio path: {audio_wav}")
    print(f"=======================================================")

    t0 = time.time()
    renderer = HyperWhiteboardRenderer(spec, fps=24)
    renderer.render_video_and_sfx(out_mp4, audio_wav, BGM_WAV if BGM_WAV.exists() else None)
    print(f"[SUCCESS] {scene_id} rendered in {time.time() - t0:.1f}s -> {out_mp4}")
    return out_mp4


def concat_master():
    print(f"\n=======================================================")
    print(f"[CONCAT V4] Concatenating all 6 scenes into Master V4...")
    print(f"=======================================================")

    concat_list = RENDERS_DIR / "concat_list_v4.txt"
    lines = []
    for i in range(1, 7):
        sid = f"scene{i:02d}"
        mp4_path = RENDERS_DIR / f"{sid}_v4.mp4"
        if not mp4_path.exists():
            raise FileNotFoundError(f"Missing rendered scene: {mp4_path}")
        p_str = str(mp4_path.resolve()).replace("\\", "/")
        lines.append(f"file '{p_str}'")

    concat_list.write_text("\n".join(lines), encoding="utf-8")
    master_out = RENDERS_DIR / "tap01_lung_mat_master_v4.mp4"

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        str(master_out)
    ]
    subprocess.run(cmd, check=True)
    print(f"[SUCCESS] Master V4 Long-form Exported: {master_out} ({master_out.stat().st_size / 1024 / 1024:.2f} MB)")
    return master_out


def render_all(scene_ids: list[str]):
    total_t0 = time.time()
    for sid in scene_ids:
        render_scene(sid)
    if len(scene_ids) == 6 or all((RENDERS_DIR / f"scene{i:02d}_v4.mp4").exists() for i in range(1, 7)):
        concat_master()
    print(f"\nAll operations completed in {time.time() - total_t0:.1f}s!")


if __name__ == "__main__":
    ids = sys.argv[1:] or ["scene01"]
    render_all(ids)
