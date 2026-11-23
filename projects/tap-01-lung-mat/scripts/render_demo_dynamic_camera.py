"""
Build & Render Test Demo for "Dynamic Multi-Node Canvas & Auto-Fit Bounding Box"
================================================================================
Generates a 5-Element (`N = 5`, non-fixed count) Dynamic Snake/Flow Scene Demo
using real voiceover audio (`scene01.wav`) and 5 distinct Gemini illustrations:
  - Row 1 (Left -> Center -> Right):
    + Node 1: Tứ Đại Bá Chủ Thảo Nguyên (`c1_savanna_apex_predators_giants.png`, Focus Zoom 1.95x)
    + Node 2: Bầy Sư Tử Toát Mồ Hôi Né Đường (`c1_lions_sweating_scared.png`, Focus Zoom 2.05x)
    + Node 3: Kỷ Lục Guinness Kẻ Chí Phèo 12kg (`c1_badger_guinness_fearless.png`, Focus Zoom 2.00x)
  - Row 2 (Snake Right -> Left, safe gap >= 140px):
    + Node 4: Đẳng Cấp Giang Hồ Không Ngán Ai (`c1_badger_thug_sunglasses.png`, Focus Zoom 2.10x)
    + Node 5: Lỗ Vốn Nặng: Sư Tử Rách Môi Mẻ Vuốt (`c1_lions_battered_torn_meat.png`, Focus Zoom 1.95x)
  - Final Phase:
    + Auto-Fit Bounding Box Reveal (`Zoom Out Toàn Cảnh`) smoothly framing all 5 nodes + flow arrows!
"""

import sys
import json
import subprocess
from pathlib import Path
import cv2

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent

sys.path.insert(0, str(ROOT / "src" / "composition"))
sys.path.insert(0, str(ROOT / "src" / "render"))

from editorial_sketchbook_composer import (
    ACCENT_CRIMSON,
    ACCENT_AMBER,
    ACCENT_TEAL,
    ACCENT_ROYAL,
    HIGHLIGHT_YELLOW,
    HIGHLIGHT_MINT,
    HIGHLIGHT_CORAL,
)
from dynamic_flow_layout import WorldNodeConfig, build_dynamic_multi_node_scene
from hybrid_whiteboard_renderer import HybridWhiteboardRenderer

G = PROJ / "assets" / "gemini_downloaded"
AUDIO_DIR = PROJ / "audio"
CANVAS_DIR = PROJ / "assets" / "scenes_composed"
SPECS_DIR = PROJ / "specs"
RENDERS_DIR = PROJ / "renders"
SNAP_DIR = RENDERS_DIR / "snapshots"
SNAP_DIR.mkdir(parents=True, exist_ok=True)


def get_audio_duration_ms(wav_path: Path) -> int:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(wav_path),
    ]
    return int(round(float(subprocess.check_output(cmd, text=True).strip()) * 1000))


def main():
    audio_wav = AUDIO_DIR / "scene01.wav"
    dur_ms = get_audio_duration_ms(audio_wav)

    # 5 dynamic nodes (N = 5) demonstrating non-fixed element count & Snake Flow layout
    nodes = [
        WorldNodeConfig(
            beat_id="node_01",
            img_path=G / "c1_savanna_apex_predators_giants.png",
            caption_text="Bá chủ thảo nguyên: Sư tử, linh cẩu, voi & tê giác",
            start_ms=0,
            end_ms=13800,
            badge_text="01. TỨ ĐẠI BÁ CHỦ",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="node_02",
            img_path=G / "c1_lions_sweating_scared.png",
            caption_text="Nghịch lý: Bầy sư tử toát mồ hôi tự động né đường",
            start_ms=13800,
            end_ms=27200,
            badge_text="02. SƯ TỬ NÉ ĐƯỜNG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="node_03",
            img_path=G / "c1_badger_guinness_fearless.png",
            caption_text="Kỷ lục Guinness: Sinh vật 12kg gan lì nhất hành tinh",
            start_ms=27200,
            end_ms=40500,
            badge_text="03. KỶ LỤC GUINNESS",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="node_04",
            img_path=G / "c1_badger_thug_sunglasses.png",
            caption_text="Chí Phèo thảo nguyên: Thản nhiên đi dạo giữa bầy thú dữ",
            start_ms=40500,
            end_ms=53200,
            badge_text="04. KẺ CHÍ PHÈO 12KG",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.10,
        ),
        WorldNodeConfig(
            beat_id="node_05",
            img_path=G / "c1_lions_battered_torn_meat.png",
            caption_text="Cái giá quá đắt: Rách môi mẻ vuốt đổi miếng thịt dai nhách",
            start_ms=53200,
            end_ms=dur_ms,
            badge_text="05. LỖ VỐN NẶNG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
    ]

    canvas_path = CANVAS_DIR / "demo_dynamic_5nodes_world.png"
    spec_path = SPECS_DIR / "demo_dynamic_5nodes_spec.json"
    out_mp4 = RENDERS_DIR / "demo_dynamic_camera_5nodes.mp4"

    spec = build_dynamic_multi_node_scene(
        scene_id="demo_dynamic_5nodes",
        act_badge="PHẦN 1 (DEMO N=5)",
        title_text="DYNAMIC MULTI-NODE CANVAS & AUTO-FIT BOUNDING BOX",
        accent_color=ACCENT_CRIMSON,
        nodes=nodes,
        duration_ms=dur_ms,
        out_canvas_path=canvas_path,
        viewport_w=1280,
        viewport_h=720,
        fixed_header_h=68,
        node_w=660,
        node_h=430,
        gap_x=200,
        gap_y=150,
        isolate_active_node_during_focus=True,
    )
    spec_path.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[DEMO SPEC] Built World Canvas: {spec['world_width']}x{spec['world_height']} for N={spec['node_count']} nodes")
    print(f"[DEMO SPEC] Safe Inter-Node Gap: >= {spec['min_node_gap_px']}px")
    print(f"[DEMO SPEC] Auto-Fit BBox: {spec['auto_fit_bbox']}")

    renderer = HybridWhiteboardRenderer(spec_path, canvas_path, fps=24)
    renderer.render(out_mp4, audio_wav)

    # Extract verification snapshots showing Fixed Top Header + Isolated Focus on Node 1, Node 2 (zero bleed from Node 1!), Node 4, and Auto-Fit Zoom Out Overview!
    cap = cv2.VideoCapture(str(out_mp4))
    for label, t_ms in [
        ("01_focus_node1_fixed_header", 2200),
        ("02_focus_node2_isolated_zero_bleed", 16000),
        ("03_focus_node3_zoom2x", 35000),
        ("04_focus_node4_snake_row2", 48000),
        ("05_autofit_bbox_zoom_out_overview", dur_ms - 600),
    ]:
        cap.set(cv2.CAP_PROP_POS_MSEC, t_ms)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(str(SNAP_DIR / f"demo_cam_{label}.png"), frame)
    cap.release()
    print(f"[DEMO COMPLETE] Video exported to: {out_mp4}")


if __name__ == "__main__":
    main()
