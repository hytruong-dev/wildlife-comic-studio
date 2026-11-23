"""
Build Dynamic Multi-Node Scene Specs V8.3 for Episode 5: Chim Bồ Nông (`tap-05-chim-bo-nong`)
25-NODE ULTRA DETAILED VISUAL COVERAGE:
- Fully aligned with ElevenLabs Adam voice narration (454.5s body)
- Every sentence has a dedicated high-impact whiteboard illustration
- All 25 assets losslessly cleaned with Inverse Alpha Deblending
- Grid layout: 2x2 or 2x3 with Auto-Fit Bounding Box & Active-Node Isolation
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src" / "composition"))

from dynamic_flow_layout import (
    WorldNodeConfig,
    build_dynamic_multi_node_scene,
    ACCENT_ROYAL,
    ACCENT_TEAL,
    ACCENT_AMBER,
    ACCENT_CRIMSON,
    HIGHLIGHT_YELLOW,
)
from editorial_sketchbook_composer import (
    HIGHLIGHT_MINT,
    HIGHLIGHT_CORAL,
)

PROJ = Path(__file__).resolve().parents[1]
G = PROJ / "assets" / "gemini_downloaded"
AUDIO_DIR = PROJ / "audio"
CANVAS_DIR = PROJ / "assets" / "scenes_composed"
SPECS_DIR = PROJ / "specs"
CANVAS_DIR.mkdir(parents=True, exist_ok=True)
SPECS_DIR.mkdir(parents=True, exist_ok=True)

SCENE_HOLD_MS = 1500  # 1.5s sweet-spot hold on completed overview before transition


def get_audio_duration_ms(wav_path: Path) -> int:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(wav_path),
    ]
    dur_sec = float(subprocess.check_output(cmd, text=True).strip())
    return int(round(dur_sec * 1000))


def get_parts(scene_id: str) -> List[float]:
    p = AUDIO_DIR / f"{scene_id}_parts_duration.json"
    if p.exists():
        data = json.loads(p.read_text(encoding="utf-8"))
        parts_dict = data.get("parts", {})
        return [parts_dict[k] for k in sorted(parts_dict.keys())]
    dur_sec = get_audio_duration_ms(AUDIO_DIR / f"{scene_id}.wav") / 1000.0
    return [dur_sec]


def build_scene_01():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene01.wav")
    parts = get_parts("scene01")
    p0 = parts[0] if len(parts) > 0 else 13.32
    p1 = parts[1] if len(parts) > 1 else 17.12
    p2 = parts[2] if len(parts) > 2 else 14.70
    p3 = parts[3] if len(parts) > 3 else 22.35

    lead_in = 400
    gap = 350
    t_p0 = lead_in + int(round(p0 * 1000))
    t_p1 = t_p0 + gap + int(round(p1 * 1000))
    t_p2 = t_p1 + gap + int(round(p2 * 1000))
    t_p3 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene01_01_pelican_intro.png",
            caption_text="Chim bồ nông trắng Úc: Mỏ khổng lồ dài gần nửa mét",
            start_ms=0,
            end_ms=t_p0,
            badge_text="01. KẺ SĂN MỒI DUYÊN HẢI",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene01_02_pelican_clamp_everything.png",
            caption_text="Thấy gì cử động là kẹp thử: Từ Capybara đến cả flycam",
            start_ms=t_p0,
            end_ms=t_p1,
            badge_text="02. PHẢN XẠ KẸP MỌI THỨ",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "scene01_03_western_explorers_shock.png",
            caption_text="Thế kỷ 18: Thám hiểm bàng hoàng thấy bồ nông nuốt vịt",
            start_ms=t_p1,
            end_ms=t_p2,
            badge_text="03. CÚ SỐC THẾ KỶ 18",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "scene01_04_diagram_gular_pouch_bucket.png",
            caption_text="Túi da dưới mỏ chứa 13 lít nước, gấp 3 lần dạ dày!",
            start_ms=t_p2,
            end_ms=t_p3,
            badge_text="04. MỎ THẦN KỲ 13 LÍT",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
    ]

    hold_ms = 1500  # Director Taste Standard: 1.5s sweet-spot overview hold (no boring dead pause)
    canvas_path = CANVAS_DIR / "scene01_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene01",
        act_badge="PHẦN 1: THE MYTH-BUSTER HOOK",
        title_text="KẺ THAM ĂN SỐ MỘT HÀNH TINH VÀ CHIẾC MỎ NUỐT CẢ VŨ TRỤ",
        accent_color=ACCENT_ROYAL,
        nodes=nodes,
        duration_ms=dur_ms + hold_ms,
        out_canvas_path=canvas_path,
        viewport_w=1280,
        viewport_h=720,
        fixed_header_h=68,
        node_w=660,
        node_h=430,
        gap_x=75,
        gap_y=60,
        isolate_active_node_during_focus=True,
    )
    spec_p = SPECS_DIR / "scene01_spec.json"
    spec_p.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC CREATED] Scene 1: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms -> {spec['scene_id']}")
    return spec


def build_scene_02():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene02.wav")
    parts = get_parts("scene02")
    p0 = parts[0] if len(parts) > 0 else 20.32
    p1 = parts[1] if len(parts) > 1 else 19.35
    p2 = parts[2] if len(parts) > 2 else 15.40
    p3 = parts[3] if len(parts) > 3 else 11.01

    lead_in = 400
    gap = 350
    t_p0 = lead_in + int(round(p0 * 1000))
    t_p1 = t_p0 + gap + int(round(p1 * 1000))
    t_p2 = t_p1 + gap + int(round(p2 * 1000))
    t_p3 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene02_01_rpg_pouch_capacity.png",
            caption_text="POUCH CAPACITY: 999/100 — Túi mỏ 13 lít gấp 3 lần dạ dày",
            start_ms=0,
            end_ms=t_p0,
            badge_text="01. CHỈ SỐ SỨC CHỨA: 999/100",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene02_02_rpg_gluttony_max.png",
            caption_text="GLUTTONY: 999/100 — Tham ăn vô độ kẹp thử Capybara",
            start_ms=t_p0,
            end_ms=t_p1,
            badge_text="02. ĐỘ THAM ĂN: 999/100",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "scene02_03_rpg_spinal_cooling.png",
            caption_text="SPINAL COOLING: 900/100 — Lộn cột sống qua họng tản nhiệt",
            start_ms=t_p1,
            end_ms=t_p2,
            badge_text="03. TẢN NHIỆT LỘN CỔ: 900/100",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "scene02_04_rpg_water_drain_speed.png",
            caption_text="WATER DRAIN SPEED: 45/100 — Dốc nước 1 phút mỏ nặng như đá",
            start_ms=t_p2,
            end_ms=t_p3,
            badge_text="04. TỐC ĐỘ DỐC NƯỚC: 45/100",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
    ]

    hold_ms = 1500  # Director Taste: 1.5s sweet-spot
    canvas_path = CANVAS_DIR / "scene02_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene02",
        act_badge="PHẦN 2: BẢNG CHỈ SỐ SINH TỒN RPG",
        title_text="BẢNG ĐIỂM STATS DỊ BIỆT CỦA CỖ MÁY VỢT LƯỚI ĐẠI DƯƠNG",
        accent_color=ACCENT_AMBER,
        nodes=nodes,
        duration_ms=dur_ms + hold_ms,
        out_canvas_path=canvas_path,
        viewport_w=1280,
        viewport_h=720,
        fixed_header_h=68,
        node_w=660,
        node_h=430,
        gap_x=75,
        gap_y=60,
        isolate_active_node_during_focus=True,
    )
    spec_p = SPECS_DIR / "scene02_spec.json"
    spec_p.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC CREATED] Scene 2: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms -> {spec['scene_id']}")
    return spec


def build_scene_03():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene03.wav")
    parts = get_parts("scene03")
    p0 = parts[0] if len(parts) > 0 else 21.06
    p1 = parts[1] if len(parts) > 1 else 18.68
    p2 = parts[2] if len(parts) > 2 else 18.98
    p3 = parts[3] if len(parts) > 3 else 12.50
    p4 = parts[4] if len(parts) > 4 else 23.59

    lead_in = 400
    gap = 350
    t_p0 = lead_in + int(round(p0 * 1000))
    t_p1 = t_p0 + gap + int(round(p1 * 1000))
    t_p2 = t_p1 + gap + int(round(p2 * 1000))
    t_p3 = t_p2 + gap + int(round(p3 * 1000))
    t_p4 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene03_01_longest_bill_hook.png",
            caption_text="Mỏ dài gần nửa mét kỷ lục thế giới với móc sừng nhọn",
            start_ms=0,
            end_ms=t_p0,
            badge_text="01. MỎ DÀI KỶ LỤC 47CM",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene03_02_flexible_jaw_basket.png",
            caption_text="Xương hàm dẻo uốn cong mở rộng thành lồng lưới cuốn cá",
            start_ms=t_p0,
            end_ms=t_p1,
            badge_text="02. XƯƠNG HÀM DẺO CỰC ĐẠI",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "scene03_03_v_formation_fleet.png",
            caption_text="Hạm đội chữ V: Đàn bồ nông đập cánh lùa đàn cá vào cạn",
            start_ms=t_p1,
            end_ms=t_p2,
            badge_text="03. HẠM ĐỘI CHỮ V SĂN MỒI",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "scene03_04_pelican_pickup_truck.png",
            caption_text="Xe bán tải xúc cá: Cản xe gắn bồn 13L càn quét dòng suối",
            start_ms=t_p2,
            end_ms=t_p3,
            badge_text="04. CHIẾC BÁN TẢI CÀN QUÉT",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "scene03_05_microvascular_network.png",
            caption_text="Mao mạch đàn hồi giúp màng túi không rách khi chứa 13L",
            start_ms=t_p3,
            end_ms=t_p4,
            badge_text="05. MẠNG LƯỚI MAO MẠCH ĐÀN HỒI",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
    ]

    hold_ms = 1500  # Director Taste: 1.5s sweet-spot
    canvas_path = CANVAS_DIR / "scene03_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene03",
        act_badge="PHẦN 3: CƠ CHẾ SINH TỒN ĐỘC DỊ",
        title_text="GIẢI PHẪU MỎ VỢT DẺO VÀ HẠM ĐỘI BẮT CÁ CHIẾN THUẬT CHỮ V",
        accent_color=ACCENT_TEAL,
        nodes=nodes,
        duration_ms=dur_ms + hold_ms,
        out_canvas_path=canvas_path,
        viewport_w=1280,
        viewport_h=720,
        fixed_header_h=68,
        node_w=660,
        node_h=430,
        gap_x=75,
        gap_y=60,
        isolate_active_node_during_focus=True,
    )
    spec_p = SPECS_DIR / "scene03_spec.json"
    spec_p.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC CREATED] Scene 3: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms -> {spec['scene_id']}")
    return spec


def build_scene_04():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene04.wav")
    parts = get_parts("scene04")
    p0 = parts[0] if len(parts) > 0 else 20.09
    p1 = parts[1] if len(parts) > 1 else 20.61
    p2 = parts[2] if len(parts) > 2 else 12.13
    p3 = parts[3] if len(parts) > 3 else 23.29
    p4 = parts[4] if len(parts) > 4 else 21.66

    lead_in = 400
    gap = 350
    t_p0 = lead_in + int(round(p0 * 1000))
    t_p1 = t_p0 + gap + int(round(p1 * 1000))
    t_p2 = t_p1 + gap + int(round(p2 * 1000))
    t_p3 = t_p2 + gap + int(round(p3 * 1000))
    t_p4 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene04_01_tourists_gasp_spinal_neck.png",
            caption_text="Bồ nông bẻ gập cổ 180 độ lộ cột sống chồi qua túi họng",
            start_ms=0,
            end_ms=t_p0,
            badge_text="01. CÚ BẺ CỔ DỊ BIỆT",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene04_02_air_conditioner_cooling_relief.png",
            caption_text="Mở màng túi đón gió mát hạ nhiệt như bật điều hòa 16 độ",
            start_ms=t_p0,
            end_ms=t_p1,
            badge_text="02. ĐIỀU HÒA 16 ĐỘ TỰ NHIÊN",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "scene04_03_physics_scale_13kg_water.png",
            caption_text="Cân vật lý: Nước trong túi mỏ nặng 13kg hơn cả cơ thể!",
            start_ms=t_p1,
            end_ms=t_p2,
            badge_text="03. ĐỊNH LUẬT VẬT LÝ ÉO LÈ",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "scene04_04_grounded_heavy_pelican.png",
            caption_text="Mỏ nặng mất bay, bồ nông buộc đứng đơ dốc nước 1 phút",
            start_ms=t_p2,
            end_ms=t_p3,
            badge_text="04. CẮM ĐẦU XUỐNG BÙN",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "scene04_05_mouth_breathing_no_nostrils.png",
            caption_text="Không có lỗ mũi ngoài trên mỏ, thở hoàn toàn bằng miệng",
            start_ms=t_p3,
            end_ms=t_p4,
            badge_text="05. THỞ HOÀN TOÀN BẰNG MIỆNG",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
    ]

    hold_ms = 1500  # Director Taste: 1.5s sweet-spot
    canvas_path = CANVAS_DIR / "scene04_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene04",
        act_badge="PHẦN 4: CÚ BẺ LÁI CỦA TẠO HÓA",
        title_text="MÀN LỘN CỔ DỊ BIỆT VÀ CƠN ÁC MỘNG VẬT LÝ MƯỜI BA CÂN NƯỚC",
        accent_color=ACCENT_CRIMSON,
        nodes=nodes,
        duration_ms=dur_ms + hold_ms,
        out_canvas_path=canvas_path,
        viewport_w=1280,
        viewport_h=720,
        fixed_header_h=68,
        node_w=660,
        node_h=430,
        gap_x=75,
        gap_y=60,
        isolate_active_node_during_focus=True,
    )
    spec_p = SPECS_DIR / "scene04_spec.json"
    spec_p.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC CREATED] Scene 4: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms -> {spec['scene_id']}")
    return spec


def build_scene_05():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene05.wav")
    parts = get_parts("scene05")
    p0 = parts[0] if len(parts) > 0 else 23.22
    p1 = parts[1] if len(parts) > 1 else 20.61
    p2 = parts[2] if len(parts) > 2 else 21.58
    p3 = parts[3] if len(parts) > 3 else 16.74
    p4 = parts[4] if len(parts) > 4 else 23.14

    lead_in = 400
    gap = 350
    t_p0 = lead_in + int(round(p0 * 1000))
    t_p1 = t_p0 + gap + int(round(p1 * 1000))
    t_p2 = t_p1 + gap + int(round(p2 * 1000))
    t_p3 = t_p2 + gap + int(round(p3 * 1000))
    t_p4 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene05_01_seagull_stealing_fish.png",
            caption_text="Mòng biển ranh mãnh đậu lên đầu cướp sạch cá trong mỏ",
            start_ms=0,
            end_ms=t_p0,
            badge_text="01. MÒNG BIỂN CƯỚP TRÊN ĐẦU",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene05_02_london_park_pigeon_swallow.png",
            caption_text="Công viên London: Bồ nông dìm chết nuốt sống chim bồ câu",
            start_ms=t_p0,
            end_ms=t_p1,
            badge_text="02. NUỐT CHỬNG BỒ CÂU LUÂN ĐÔN",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "scene05_03_capybara_deer_cat_victims.png",
            caption_text="Bồ nông há to mỏ kẹp thử chó mèo và du khách qua đường",
            start_ms=t_p1,
            end_ms=t_p2,
            badge_text="03. BỘ SƯU TẬP NẠN NHÂN BI HÀI",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "scene05_04_veterinary_surgery_gular_repair.png",
            caption_text="Phẫu thuật thú y: Khâu lành túi mỏ bị rách do lưỡi câu",
            start_ms=t_p2,
            end_ms=t_p3,
            badge_text="04. BÁC SĨ THÚ Y CỨU NẠN",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "scene05_05_visual_reflex_brain.png",
            caption_text="Phản xạ thị giác: Cứ thấy cử động là há mỏ kẹp tức thì",
            start_ms=t_p3,
            end_ms=t_p4,
            badge_text="05. PHẢN XẠ THỊ GIÁC SIÊU TỐC",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
    ]

    hold_ms = 1500  # Director Taste: 1.5s sweet-spot
    canvas_path = CANVAS_DIR / "scene05_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene05",
        act_badge="PHẦN 5: ĐẠI CHIẾN SĂN MỒI",
        title_text="MÒNG BIỂN CƯỚP CÁ TRÊN ĐẦU VÀ NẠN NHÂN CAPYBARA BI HÀI",
        accent_color=ACCENT_ROYAL,
        nodes=nodes,
        duration_ms=dur_ms + hold_ms,
        out_canvas_path=canvas_path,
        viewport_w=1280,
        viewport_h=720,
        fixed_header_h=68,
        node_w=660,
        node_h=430,
        gap_x=75,
        gap_y=60,
        isolate_active_node_during_focus=True,
    )
    spec_p = SPECS_DIR / "scene05_spec.json"
    spec_p.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC CREATED] Scene 5: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms -> {spec['scene_id']}")
    return spec


def build_scene_06():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene06.wav")
    parts = get_parts("scene06")
    p0 = parts[0] if len(parts) > 0 else 18.46
    p1 = parts[1] if len(parts) > 1 else 19.35

    lead_in = 400
    gap = 350
    t_p0 = lead_in + int(round(p0 * 1000))
    t_p1 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene06_01_pelican_majestic_wingspan.png",
            caption_text="Sải cánh 3 mét kiêu hãnh bay lượn trên vùng biển cả",
            start_ms=0,
            end_ms=t_p0,
            badge_text="01. SẢI CÁNH BA MÉT HÙNG VĨ",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene06_02_tardigrade_teaser.png",
            caption_text="Đón xem tập tiếp theo lúc 18:00: Gấu Nước Tardigrade",
            start_ms=t_p0,
            end_ms=t_p1,
            badge_text="02. TEASER: GẤU NƯỚC TARDIGRADE",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
    ]

    hold_ms = 1500  # Director Taste: 1.5s sweet-spot
    canvas_path = CANVAS_DIR / "scene06_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene06",
        act_badge="PHẦN 6: LỜI NHẮN NHỦ SINH THÁI",
        title_text="BIỂU TƯỢNG SẢI CÁNH TỰ DO VÀ TEASER BẤT TỬ GẤU NƯỚC TARDIGRADE",
        accent_color=ACCENT_TEAL,
        nodes=nodes,
        duration_ms=dur_ms + hold_ms,
        out_canvas_path=canvas_path,
        viewport_w=1280,
        viewport_h=720,
        fixed_header_h=68,
        node_w=660,
        node_h=430,
        gap_x=75,
        gap_y=60,
        isolate_active_node_during_focus=True,
    )
    spec_p = SPECS_DIR / "scene06_spec.json"
    spec_p.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC CREATED] Scene 6: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms -> {spec['scene_id']}")
    return spec


if __name__ == "__main__":
    print("=======================================================")
    print("BUILDING DYNAMIC MULTI-NODE SCENE SPECS FOR EPISODE 5")
    print("=======================================================")
    build_scene_01()
    build_scene_02()
    build_scene_03()
    build_scene_04()
    build_scene_05()
    build_scene_06()
    print("ALL 6 SCENE SPECS BUILT SUCCESSFULLY!")
