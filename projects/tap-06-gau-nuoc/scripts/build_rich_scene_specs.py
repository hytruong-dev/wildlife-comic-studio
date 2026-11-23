"""
Build Dynamic Multi-Node Scene Specs V8.3 for Episode 6: Gấu Nước (`tap-06-gau-nuoc`)
22-NODE ULTRA DETAILED VISUAL COVERAGE:
- Fully aligned with ElevenLabs Adam voice narration (489.82s body + 20s intro/outro = 509.82s)
- All 23 assets losslessly cleaned with Inverse Alpha Deblending
- Grid layout: 2x2 with Auto-Fit Bounding Box & Active-Node Isolation
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


def build_scene_01():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene01.wav")
    hold_ms = SCENE_HOLD_MS
    t_step = dur_ms // 4

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene01_01_meteor_extinction_survivor.png",
            caption_text="Thiên thạch quét sạch khủng long, nhưng gấu nước vẫn bình an",
            start_ms=0,
            end_ms=t_step,
            badge_text="01. KẺ SỐNG SÓT QUA ĐẠI TUYỆT CHỦNG",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene01_02_microscopic_cute_water_bear.png",
            caption_text="Kính hiển vi hé lộ sinh vật 8 chân mũm mĩm bò trên rêu xanh",
            start_ms=t_step,
            end_ms=t_step * 2,
            badge_text="02. THIÊN THẦN RÊU TÍ HON",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "scene01_03_extreme_endurance_triad.png",
            caption_text="Đóng băng âm 272 độ C, luộc sôi 150 độ C và ép 6.000 atm",
            start_ms=t_step * 2,
            end_ms=t_step * 3,
            badge_text="03. TAM GIÁC CHỊU ĐỰNG ĐỈNH CAO",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "scene01_04_space_vacuum_foton_mission.png",
            caption_text="Phơi mình trong chân không vũ trụ, nhỏ 1 giọt nước là tỉnh dậy",
            start_ms=t_step * 3,
            end_ms=dur_ms,
            badge_text="04. SỨ MỆNH KHÔNG GIAN FOTON-M3",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene01_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene01",
        act_badge="CHƯƠNG 1",
        title_text="01. QUÁI VẬT 8 CHÂN SIÊU CẤP — KẺ CHẤP CẢ VŨ TRỤ",
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
    print(f"[SPEC CREATED] Scene 1: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms")
    return spec


def build_scene_02():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene02.wav")
    hold_ms = SCENE_HOLD_MS
    t_step = dur_ms // 4

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene02_01_rpg_card_atk_spd_low.png",
            caption_text="Sát thương đồ chơi, tốc độ rùa bò bị ốc sên bỏ xa trong cuộc đua",
            start_ms=0,
            end_ms=t_step,
            badge_text="01. CÔNG KÍCH & TỐC ĐỘ GẦN BẰNG KHÔNG",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene02_02_rpg_card_def_max_temperature.png",
            caption_text="Chỉ số DEF chạm nóc 9999, chấp từ độ không tuyệt đối đến dung nham",
            start_ms=t_step,
            end_ms=t_step * 2,
            badge_text="02. PHÒNG THỦ VƯỢT MỌI GIỚI HẠN",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "scene02_03_radiation_lethal_dose_comparison.png",
            caption_text="Người chịu 5 Gray đã ngã gục, gấu nước thảnh thơi tắm 5.000 Gray",
            start_ms=t_step * 2,
            end_ms=t_step * 3,
            badge_text="03. THẦN HỘ MỆNH CHỐNG PHÓNG XẠ",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "scene02_04_rpg_cryptobiosis_tun_state.png",
            caption_text="Thu gọn 8 chân hóa thành hạt kén ngọc ngủ sâu suốt 30 năm trời",
            start_ms=t_step * 3,
            end_ms=dur_ms,
            badge_text="04. KỸ NĂNG TỐI THƯỢNG CRYPTOBIOSIS",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene02_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene02",
        act_badge="CHƯƠNG 2",
        title_text="02. BẢNG CHỈ SỐ BẤT TỬ RPG — LỖI GAME TIẾN HÓA",
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
    print(f"[SPEC CREATED] Scene 2: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms")
    return spec


def build_scene_03():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene03.wav")
    hold_ms = SCENE_HOLD_MS
    t_step = dur_ms // 4

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene03_01_water_desiccation_process.png",
            caption_text="Tự bốc hơi toàn bộ nước trong cơ thể để đóng băng mọi hoạt động sống",
            start_ms=0,
            end_ms=t_step,
            badge_text="01. RÚT CẠN 99% LƯỢNG NƯỚC",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene03_02_tdp_amorphous_glass_matrix.png",
            caption_text="Protein TDPs đan lưới thủy tinh sinh học bảo vệ ADN nguyên vẹn",
            start_ms=t_step,
            end_ms=t_step * 2,
            badge_text="02. MA TRẬN THỦY TINH VÔ ĐỊNH HÌNH",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "scene03_03_dsup_protein_radiation_shield.png",
            caption_text="Gen Dsup bọc chuỗi ADN như áo giáp hiệp sĩ đánh bật tia phóng xạ",
            start_ms=t_step * 2,
            end_ms=t_step * 3,
            badge_text="03. LÁ CHẮN DUP BẢO VỆ GEN",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "scene03_04_revival_single_water_drop.png",
            caption_text="Nhỏ một giọt nước tinh khiết, hạt kén lập tức nở bung hồi sinh",
            start_ms=t_step * 3,
            end_ms=dur_ms,
            badge_text="04. PHÉP MÀU TỪ MỘT GIỌT NƯỚC",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene03_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene03",
        act_badge="CHƯƠNG 3",
        title_text="03. TUYỆT KỸ HÓA THỦY TINH & KHIÊN CHẮN ADN",
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
    print(f"[SPEC CREATED] Scene 3: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms")
    return spec


def build_scene_04():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene04.wav")
    hold_ms = SCENE_HOLD_MS
    t_step = dur_ms // 4

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene04_01_superhero_vs_glass_fragile.png",
            caption_text="Khi ngủ là kim cương bất hoại, khi thức lại mềm như bóng bay nước",
            start_ms=0,
            end_ms=t_step,
            badge_text="01. SIÊU NHÂN VÀ KẸO DẺO MỎNG MANH",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene04_02_snail_slime_lethal_trap.png",
            caption_text="Ốc sên vô tình bò qua để lại vệt nhớt làm ngạt thở chú gấu nhỏ",
            start_ms=t_step,
            end_ms=t_step * 2,
            badge_text="02. CẠM BẪY CHẤT NHẦY TỬ THẦN",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "scene04_03_nematode_worm_predator_snack.png",
            caption_text="Chẳng có nanh vuốt hay giáp xác, dễ dàng bị giun vi mô nuốt chửng",
            start_ms=t_step * 2,
            end_ms=t_step * 3,
            badge_text="03. MÓN TRÁNG MIỆNG CỦA GIUN TRÒN",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "scene04_04_global_warming_water_temp.png",
            caption_text="Nước ấm lên từ từ khiến cơ thể không kịp bật cơ chế tạo kén Tun",
            start_ms=t_step * 3,
            end_ms=dur_ms,
            badge_text="04. KẺ THÙ MANG TÊN NƯỚC ẤM 38 ĐỘ C",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene04_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene04",
        act_badge="CHƯƠNG 4",
        title_text="04. CHUYẾN DU HÀNH VŨ TRỤ & VỤ ĐÂM TÀU LÊN MẶT TRĂNG",
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
    print(f"[SPEC CREATED] Scene 4: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms")
    return spec


def build_scene_05():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene05.wav")
    hold_ms = SCENE_HOLD_MS
    t_step = dur_ms // 4

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene05_01_beresheet_moon_lander_launch.png",
            caption_text="Năm 2019: Mang theo hàng ngàn gấu nước dehydrated hướng về Mặt Trăng",
            start_ms=0,
            end_ms=t_step,
            badge_text="01. TÀU BERESHEET LÊN ĐƯỜNG",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene05_02_moon_crash_explosion_debris.png",
            caption_text="Tàu đổ bộ nổ tung thành trăm mảnh vỡ, khoang kén gấu nước bung ra",
            start_ms=t_step,
            end_ms=t_step * 2,
            badge_text="02. CÚ VA CHẠM 500 KM/H",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "scene05_03_tardigrades_scattered_moon_craters.png",
            caption_text="Hàng ngàn hạt kén Tun nằm bình thản giữa các miệng hố bụi xám",
            start_ms=t_step * 2,
            end_ms=t_step * 3,
            badge_text="03. CÔNG DÂN ĐẦU TIÊN CỦA MẶT TRĂNG",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "scene05_04_astronaut_water_revival_dream.png",
            caption_text="Chỉ cần một phi hành gia tưới một giọt nước, sự sống sẽ cựa quậy",
            start_ms=t_step * 3,
            end_ms=dur_ms,
            badge_text="04. GIẤC MƠ HỒI SINH TRÊN CUNG TRĂNG",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene05_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene05",
        act_badge="CHƯƠNG 5",
        title_text="05. CÁI CHẾT LÃNG XẸT & CẤU TẠO CƠ THỂ DỊ BIỆT",
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
    print(f"[SPEC CREATED] Scene 5: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms")
    return spec


def build_scene_06():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene06.wav")
    hold_ms = SCENE_HOLD_MS
    t_step = int(27.4 * 1000)

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "scene06_01_philosophical_adaptation_triumph.png",
            caption_text="Sức mạnh tối thượng không nằm ở nanh vuốt, mà ở khả năng thích ứng",
            start_ms=0,
            end_ms=t_step,
            badge_text="01. BÀI HỌC THÍCH NGHI VÀ KHIÊM NHƯỜNG",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "scene06_02_mantis_shrimp_boxing_teaser.png",
            caption_text="Đón xem tập 7: Cú đấm đạn nổ dưới đại dương của võ sĩ tôm tít!",
            start_ms=t_step,
            end_ms=dur_ms,
            badge_text="TẬP TIẾP THEO: TÔM TÍT QUYỀN ANH",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene06_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene06",
        act_badge="CHƯƠNG 6",
        title_text="06. BẮC CẦU SANG TẬP 07: TÔM TÍT MANTIS SHRIMP",
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
    spec_p = SPECS_DIR / "scene06_spec.json"
    spec_p.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC CREATED] Scene 6: {len(nodes)} nodes, dur={dur_ms + hold_ms}ms")
    return spec


def main():
    print("=== BUILDING DYNAMIC MULTI-NODE SCENE SPECS (EPISODE 6) ===")
    build_scene_01()
    build_scene_02()
    build_scene_03()
    build_scene_04()
    build_scene_05()
    build_scene_06()
    print("=== ALL 6 SCENE SPECS & COMPOSED CANVASES GENERATED SUCCESSFULLY ===")


if __name__ == "__main__":
    main()
