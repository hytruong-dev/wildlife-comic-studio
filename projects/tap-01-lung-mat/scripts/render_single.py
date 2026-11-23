import sys
import time
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

def render_single_scene(sid: str):
    spec_p = SPECS_DIR / f"{sid}_spec.json"
    canvas_p = CANVAS_DIR / f"{sid}_canvas.png"
    audio_p = AUDIO_DIR / f"{sid}.wav"
    out_p = RENDERS_DIR / f"{sid}_final.mp4"
    
    t0 = time.time()
    print(f"[RENDER] Starting {sid} (target audio: {audio_p.name})...")
    renderer = HybridWhiteboardRenderer(spec_p, canvas_p, hand_path=HAND_ASSET, fps=24)
    renderer.render(out_p, audio_p)
    print(f"[RENDER] Finished {sid} in {time.time() - t0:.1f}s -> {out_p.name}")

if __name__ == "__main__":
    sid = sys.argv[1] if len(sys.argv) > 1 else "scene03"
    render_single_scene(sid)
