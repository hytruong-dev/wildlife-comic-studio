import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT / "src" / "render"))
sys.path.insert(0, str(PROJ / "scripts"))

from hybrid_whiteboard_renderer import HybridWhiteboardRenderer
from render_master_125x import SPECS_DIR, CANVAS_DIR, AUDIO_DIR, RENDERS_DIR, HAND_ASSET, concat_master_video

if __name__ == "__main__":
    for i in [1, 2, 3, 4, 5, 6]:
        sid = f"scene{i:02d}"
        print(f"=== Re-rendering {sid} with Zero-Bleed Art Clipping & V8 Complete Assets ===")
        r = HybridWhiteboardRenderer(
            SPECS_DIR / f"{sid}_spec.json",
            CANVAS_DIR / f"{sid}_canvas.png",
            hand_path=HAND_ASSET,
            fps=24,
        )
        r.render(RENDERS_DIR / f"{sid}_final.mp4", AUDIO_DIR / f"{sid}.wav")
    concat_master_video()
