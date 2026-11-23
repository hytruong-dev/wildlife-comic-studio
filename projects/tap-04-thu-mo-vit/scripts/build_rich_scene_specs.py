"""
Build Dynamic Multi-Node Scene Specs V8.3 for Episode 4: Thú Mỏ Vịt (`tap-04-thu-mo-vit`)
EXPANDED 37-NODE VISUAL COVERAGE:
- Fully aligned with ElevenLabs Adam voice narration (502.5s body)
- Every sentence has a dedicated high-impact whiteboard illustration
- Includes all 9 newly generated Playwright Gemini supplemental assets
- Grid layout: 2x3 or 2x4 with Auto-Fit Bounding Box & Active-Node Isolation
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

SCENE_HOLD_MS = 1500  # 1.5s sweet-spot hold on completed overview before transitioning to next act


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
        return json.loads(p.read_text(encoding="utf-8"))
    dur_sec = get_audio_duration_ms(AUDIO_DIR / f"{scene_id}.wav") / 1000.0
    return [dur_sec]


def build_scene_01():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene01.wav")
    parts = get_parts("scene01")
    p0 = parts[0] if len(parts) > 0 else dur_ms / 3000.0
    p1 = parts[1] if len(parts) > 1 else dur_ms / 3000.0
    
    t_p0 = int(round(p0 * 1000))
    t_p1 = t_p0 + int(round(p1 * 1000))

    # P0 (24.9s): Bridge from dolphin to creek, intro platypus & Shaw opening crate
    t_n1 = int(round(t_p0 * 0.50))
    t_n2 = t_p0
    # P1 (26.5s): Sailors prank suspicion, cutting with scissors
    t_n3 = t_p0 + int(round((t_p1 - t_p0) * 0.48))
    t_n4 = t_p1
    # P2 (30.6s): Skull X-ray no stitches, chimera taxonomy puzzle
    t_n5 = t_p1 + int(round((dur_ms - t_p1) * 0.48))
    t_n6 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c1_dolphin_to_platypus_bridge.png",
            caption_text="Tạm biệt cá heo đại dương: Đặt chân đến dòng suối mát lành miền đông nước Úc",
            start_ms=0,
            end_ms=t_n1,
            badge_text="01. CẦU NỐI ĐẠI DƯƠNG -> NƯỚC NGỌT",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c1_george_shaw_wooden_box_shock.png",
            caption_text="Năm 1798: Tiến sĩ George Shaw mở hộp mẫu vật gửi từ Úc và bàng hoàng không thốt nên lời",
            start_ms=t_n1,
            end_ms=t_n2,
            badge_text="02. CÚ SỐC THẾ KỶ 18",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c1_sailor_prank_stitching_beak.png",
            caption_text="Nghi ngờ trò lừa: Quả quyết thủy thủ khâu mỏ vịt vào đầu rái cá và đuôi hải ly!",
            start_ms=t_n2,
            end_ms=t_n3,
            badge_text="03. TRÒ ĐÙA CỦA THỦY THỦ?",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c1_scissors_cutting_beak_hoax_search.png",
            caption_text="Dùng kéo rạch tìm chỉ khâu: Tiến sĩ Shaw cố vạch trần đường may chắp vá của trò chơi khăm",
            start_ms=t_n3,
            end_ms=t_n4,
            badge_text="04. VẾT KÉO NGHI HOẶC",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "c1_skull_xray_no_stitches_connected.png",
            caption_text="Bàng hoàng tột độ: Không có một mũi chỉ! Mỏ vịt mọc liền một khối với hộp sọ!",
            start_ms=t_n4,
            end_ms=t_n5,
            badge_text="05. MỎ LIỀN HỘP SỌ",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_06",
            img_path=G / "c1_taxonomic_crisis_chimera_puzzle.png",
            caption_text="Khủng hoảng phân loại học: Mỏ vịt, đuôi hải ly, chân màng, lông thú — Nó là loài gì?",
            start_ms=t_n5,
            end_ms=t_n6,
            badge_text="06. CÂU ĐỐ CHIMERA HOANG DÃ",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene01_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene01",
        act_badge="PHẦN 1: CÚ SỐC THẾ KỶ 18",
        title_text="TIẾN SĨ GEORGE SHAW VÀ CÚ LỪA NGHĨ LÀ THỦY THỦ KHÂU VÁ",
        accent_color=ACCENT_ROYAL,
        nodes=nodes,
        duration_ms=dur_ms + SCENE_HOLD_MS,
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
    print(f"[SPEC V8.3] Scene 01 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")
    return spec


def build_scene_02():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene02.wav")
    parts = get_parts("scene02")
    p0 = parts[0] if len(parts) > 0 else dur_ms * 0.25
    p1 = parts[1] if len(parts) > 1 else dur_ms * 0.25
    p2 = parts[2] if len(parts) > 2 else dur_ms * 0.25

    t_p0 = int(round(p0 * 1000))
    t_p1 = t_p0 + int(round(p1 * 1000))
    t_p2 = t_p1 + int(round(p2 * 1000))

    t_c1 = int(round(t_p0 * 0.45))
    t_a1 = t_p0
    t_c2 = t_p0 + int(round((t_p1 - t_p0) * 0.45))
    t_a2 = t_p1
    
    # In P2 (Venom Spur): stat card + spur close-up + dog pain
    dur_p2 = t_p2 - t_p1
    t_c3 = t_p1 + int(round(dur_p2 * 0.35))
    t_a3 = t_p1 + int(round(dur_p2 * 0.70))
    t_a3_dog = t_p2

    t_c4 = t_p2 + int(round((dur_ms - t_p2) * 0.45))
    t_a4 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="stat_card_01",
            img_path=G / "c2_stat_card_mutation.png",
            caption_text="Chỉ số Đột Biến: 999/100! Đẻ trứng vỏ mềm, ấp bụng chim, nuôi con sữa thú",
            start_ms=0,
            end_ms=t_c1,
            badge_text="CARD 01: ĐỘ ĐỘT BIẾN DỊ BIỆT",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.15,
        ),
        WorldNodeConfig(
            beat_id="action_01",
            img_path=G / "c2_platypus_reptile_bird_mammal_trio.png",
            caption_text="Thực chiến dị biệt: Ấp 2 quả trứng vỏ da dẻo trong hang ấm rồi ôm con uống sữa",
            start_ms=t_c1,
            end_ms=t_a1,
            badge_text="01. QUÁI KIỆT 3 TRONG 1",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="stat_card_02",
            img_path=G / "c2_stat_card_electro_radar.png",
            caption_text="Chỉ số Rada Sinh Học: 100/100! 40.000 thụ thể điện trường & 60.000 xúc giác",
            start_ms=t_a1,
            end_ms=t_c2,
            badge_text="CARD 02: GIÁC QUAN ĐIỆN TRƯỜNG",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.15,
        ),
        WorldNodeConfig(
            beat_id="action_02",
            img_path=G / "c2_platypus_hunting_underwater_sonar.png",
            caption_text="Săn mồi mù: Nhắm mắt bịt tai nhưng bắt trọn từng xung điện cơ bắp của con tôm",
            start_ms=t_c2,
            end_ms=t_a2,
            badge_text="02. RADA ĐÁY SUỐI",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="stat_card_03",
            img_path=G / "c2_stat_card_venom_spur.png",
            caption_text="Chỉ số Vũ Khí Độc: 95/100! Cựa sừng 15mm nối tuyến độc hạ gục chó săn",
            start_ms=t_a2,
            end_ms=t_c3,
            badge_text="CARD 03: CỰA ĐỘC CHÂN SAU",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.15,
        ),
        WorldNodeConfig(
            beat_id="action_03",
            img_path=G / "c2_platypus_hind_foot_venom_spur.png",
            caption_text="Cận cảnh cựa độc: Chiếc cựa sừng 15mm nối liền tuyến độc cực mạnh ở gót chân",
            start_ms=t_c3,
            end_ms=t_a3,
            badge_text="03. MŨI TIÊM TÊ LIỆT",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="action_03_dog",
            img_path=G / "c2_hunting_dog_limping_venom_pain.png",
            caption_text="Nọc độc khủng khiếp: Hạ gục chó săn và gây đau đớn dữ dội không thuốc nào dập tắt được!",
            start_ms=t_a3,
            end_ms=t_a3_dog,
            badge_text="04. NỌC ĐỘC KHÔNG THUỐC CHỮA",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="stat_card_04",
            img_path=G / "c2_stat_card_milk_sweat.png",
            caption_text="Chỉ số Tiết Sữa: 98/100! Không có núm vú, sữa rỉ qua lỗ chân lông da bụng",
            start_ms=t_a3_dog,
            end_ms=t_c4,
            badge_text="CARD 04: NUÔI CON ĐỘC DỊ",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.15,
        ),
        WorldNodeConfig(
            beat_id="action_04",
            img_path=G / "c2_platypus_milk_sweat_nursing.png",
            caption_text="Con non liếm láp: Các giọt sữa bổ dưỡng đọng trên rãnh lông bụng mẹ như sương mai",
            start_ms=t_c4,
            end_ms=t_a4,
            badge_text="05. GIỌT SỮA MỒ HÔI",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene02_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene02",
        act_badge="PHẦN 2: BẢNG CHỈ SỐ SINH TỒN RPG",
        title_text="QUÁI KIỆT TIẾN HÓA: ĐỘT BIẾN 999/100, RADA ĐIỆN TRƯỜNG & CỰA ĐỘC",
        accent_color=ACCENT_CRIMSON,
        nodes=nodes,
        duration_ms=dur_ms + SCENE_HOLD_MS,
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
    print(f"[SPEC V8.3] Scene 02 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")
    return spec


def build_scene_03():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene03.wav")
    parts = get_parts("scene03")
    p0 = parts[0] if len(parts) > 0 else dur_ms * 0.25
    p1 = parts[1] if len(parts) > 1 else dur_ms * 0.25
    p2 = parts[2] if len(parts) > 2 else dur_ms * 0.25

    t_p0 = int(round(p0 * 1000))
    t_p1 = t_p0 + int(round(p1 * 1000))
    t_p2 = t_p1 + int(round(p2 * 1000))

    # P0 (25.1s): Diving blind anatomy & muddy creek
    t_n1 = int(round(t_p0 * 0.50))
    t_n2 = t_p0
    # P1 (25.9s): Dual GPS signals & brain microsecond calculation
    t_n3 = t_p0 + int(round((t_p1 - t_p0) * 0.48))
    t_n4 = t_p1
    # P2 (20.0s): Beaver tail fat storage
    t_n5 = t_p2
    # P3 (21.8s): UV biofluorescence glow & night secret communication
    t_n6 = t_p2 + int(round((dur_ms - t_p2) * 0.50))
    t_n7 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c3_blind_underwater_diving_anatomy.png",
            caption_text="Lặn mù hoàn toàn: Mắt nhắm chặt, rãnh tai khép kín, mũi bịt lại để chống nước tràn",
            start_ms=0,
            end_ms=t_n1,
            badge_text="01. GIẢI PHẪU KHI LẶN",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c2_platypus_hunting_underwater_sonar.png",
            caption_text="Mù điếc dưới nước: Hoàn toàn mất thị giác và khứu giác khi lặn sâu dưới đáy suối",
            start_ms=t_n1,
            end_ms=t_n2,
            badge_text="02. LẶN ĐÁY SUỐI ĐỤC",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c3_dual_radar_gps_signals.png",
            caption_text="GPS sinh học kép: Thu nhận đồng thời sóng cơ và xung điện siêu nhỏ từ con tôm",
            start_ms=t_n2,
            end_ms=t_n3,
            badge_text="03. RADA TÍN HIỆU KÉP",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c3_brain_microsecond_radar_calculation.png",
            caption_text="Tính toán microsecond: Não bộ đo độ lệch thời gian giữa sóng điện và sóng cơ chuẩn xác từng milimét!",
            start_ms=t_n3,
            end_ms=t_n4,
            badge_text="04. SIÊU MÁY TÍNH NÃO BỘ",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "c3_beaver_tail_fat_storage.png",
            caption_text="Đuôi dẹt hải ly: Kho dự trữ năng lượng khổng lồ chứa tới 50% mỡ thừa vượt qua mùa đông",
            start_ms=t_n4,
            end_ms=t_n5,
            badge_text="05. KHO PIN MỠ DỰ TRỮ",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_06",
            img_path=G / "c3_uv_light_biofluorescence_glow.png",
            caption_text="Bí ẩn tia cực tím: Dưới đèn UV, bộ lông thú mỏ vịt phát sáng huỳnh quang xanh ngọc bích!",
            start_ms=t_n5,
            end_ms=t_n6,
            badge_text="06. PHÁT SÁNG HUỲNH QUANG UV",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_07",
            img_path=G / "c3_night_secret_agent_underwater_glow.png",
            caption_text="Điệp viên đáy suối: Nhận diện đồng loại trong đêm tối mà kẻ săn mồi trên bờ không hề hay biết!",
            start_ms=t_n6,
            end_ms=t_n7,
            badge_text="07. GIAO TIẾP ĐÊM HUYỀN BÍ",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene03_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene03",
        act_badge="PHẦN 3: CƠ CHẾ SINH TỒN ĐỘC DỊ",
        title_text="RADA ĐIỆN TRƯỜNG, ĐUÔI CHỨA MỠ & PHÁT SÁNG DƯỚI ĐÈN UV",
        accent_color=ACCENT_TEAL,
        nodes=nodes,
        duration_ms=dur_ms + SCENE_HOLD_MS,
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
    print(f"[SPEC V8.3] Scene 03 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")
    return spec


def build_scene_04():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene04.wav")
    parts = get_parts("scene04")
    p0 = parts[0] if len(parts) > 0 else dur_ms * 0.25
    p1 = parts[1] if len(parts) > 1 else dur_ms * 0.25
    p2 = parts[2] if len(parts) > 2 else dur_ms * 0.25

    t_p0 = int(round(p0 * 1000))
    t_p1 = t_p0 + int(round(p1 * 1000))
    t_p2 = t_p1 + int(round(p2 * 1000))

    # P0 (17.9s): Zero stomach tract
    t_n1 = t_p0
    # P1 (22.4s): Evolution deleted stomach genes
    t_n2 = t_p1
    # P2 (17.0s): Baby teeth lost & hard shell prey challenge
    t_n3 = t_p1 + int(round((t_p2 - t_p1) * 0.50))
    t_n4 = t_p2
    # P3 (30.4s): Cheek pouches gravel scoop & floating grinding mill
    t_n5 = t_p2 + int(round((dur_ms - t_p2) * 0.48))
    t_n6 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c4_zero_stomach_digestive_tract.png",
            caption_text="Biến mất dạ dày: Thực quản nối thẳng tuột vào ruột non, toàn bộ gen tiết axit bị xóa sạch!",
            start_ms=0,
            end_ms=t_n1,
            badge_text="01. BI KỊCH KHÔNG DẠ DÀY",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c4_evolution_scissors_deleting_stomach_genes.png",
            caption_text="Xóa sổ gen dạ dày: Gen axit HCl và enzym pepsin bị xóa sổ khỏi bộ gen tiến hóa!",
            start_ms=t_n1,
            end_ms=t_n2,
            badge_text="02. BỘ GEN BỊ CẮT BỎ",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c4_toothless_keratin_pads.png",
            caption_text="Hai phiến sừng thô ráp: Răng sữa rụng sau vài tuần, thay thế bằng phiến keratin nghiền mồi",
            start_ms=t_n2,
            end_ms=t_n3,
            badge_text="03. RĂNG SỮA RỤNG SẠCH",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c4_hard_shell_crayfish_snail_feast.png",
            caption_text="Thách thức vỏ cứng: Tôm càng vỏ gai, ốc suối giáp cứng thách thức chiếc mỏ không răng!",
            start_ms=t_n3,
            end_ms=t_n4,
            badge_text="04. THÁCH THỨC VỎ CỨNG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "c4_cheek_pouches_gravel_scoop.png",
            caption_text="Mánh khóe túi má: Nhét sỏi và cát thô đầy hai bên má phúng phính cùng tôm cá dưới đáy suối",
            start_ms=t_n4,
            end_ms=t_n5,
            badge_text="05. XÚC ĐẦY SỎI VÀO MÁ",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_06",
            img_path=G / "c4_floating_gravel_grinding_feast.png",
            caption_text="Nằm ngửa nghiền mồi: Dùng sỏi giã nát vụn vỏ tôm giòn tan rồi nuốt thịt, nhổ sỏi ra ngoài!",
            start_ms=t_n5,
            end_ms=t_n6,
            badge_text="06. CỐI GIÃ GẠO NỔI",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene04_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene04",
        act_badge="PHẦN 4: CÚ BẺ LÁI CỦA TẠO HÓA",
        title_text="ĂN CƠM BẰNG SỎI ĐÁ & BI KỊCH HOÀN TOÀN KHÔNG CÓ DẠ DÀY",
        accent_color=ACCENT_AMBER,
        nodes=nodes,
        duration_ms=dur_ms + SCENE_HOLD_MS,
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
    print(f"[SPEC V8.3] Scene 04 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")
    return spec


def build_scene_05():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene05.wav")
    parts = get_parts("scene05")
    p0 = parts[0] if len(parts) > 0 else dur_ms * 0.25
    p1 = parts[1] if len(parts) > 1 else dur_ms * 0.25
    p2 = parts[2] if len(parts) > 2 else dur_ms * 0.25

    t_p0 = int(round(p0 * 1000))
    t_p1 = t_p0 + int(round(p1 * 1000))
    t_p2 = t_p1 + int(round(p2 * 1000))

    # P0 (21.0s): T-Rex swimming
    t_n1 = t_p0
    # P1 (16.9s): Underground burrow asteroid survival
    t_n2 = t_p1
    # P2 (21.9s): 10 chromosomes ring & human comparison
    t_n3 = t_p1 + int(round((t_p2 - t_p1) * 0.50))
    t_n4 = t_p2
    # P3 (20.5s): Webbed feet folding
    t_n5 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c5_platypus_swimming_with_t_rex.png",
            caption_text="Chiến binh 160 triệu năm: Thú mỏ vịt bơi lội dưới suối từ thời khủng long bạo chúa T-Rex!",
            start_ms=0,
            end_ms=t_n1,
            badge_text="01. BƠI CÙNG KHỦNG LONG",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c5_underground_burrow_asteroid_survival.png",
            caption_text="Sống sót qua tuyệt chủng: Hệ thống hang ngầm 30m dọc bờ suối giúp vượt qua thảm họa thiên thạch",
            start_ms=t_n1,
            end_ms=t_n2,
            badge_text="02. HẦM TRÚ ẨN THIÊN THẠCH",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c5_ten_sex_chromosomes_chain.png",
            caption_text="Bí ẩn di truyền học: Mang chuỗi 10 NST giới tính (5X và 5Y) tạo thành vòng hoa kỳ lạ!",
            start_ms=t_n2,
            end_ms=t_n3,
            badge_text="03. CHUỖI 10 NHIỄM SẮC THỂ",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c5_human_vs_platypus_chromosome_comparison.png",
            caption_text="Đối chiếu bộ gen: Người chỉ có 2 NST (XY), thú mỏ vịt mang trọn vẹn gen chim, bò sát và thú!",
            start_ms=t_n3,
            end_ms=t_n4,
            badge_text="04. BẢNG MÃ GEN ĐẶC BIỆT",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "c5_retractable_webbed_feet_digging.png",
            caption_text="Màng bơi thông minh: Khi bơi xòe rộng như mái chèo, lên bờ tự gập vào để lộ vuốt cào đất!",
            start_ms=t_n4,
            end_ms=t_n5,
            badge_text="05. BÀN CHÂN BIẾN HÌNH",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene05_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene05",
        act_badge="PHẦN 5: HÓA THẠCH SỐNG 160 TRIỆU NĂM",
        title_text="BƠI CÙNG KHỦNG LONG T-REX & BÍ ẨN 10 NHIỄM SẮC THỂ GIỚI TÍNH",
        accent_color=ACCENT_ROYAL,
        nodes=nodes,
        duration_ms=dur_ms + SCENE_HOLD_MS,
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
    print(f"[SPEC V8.3] Scene 05 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")
    return spec


def build_scene_06():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene06.wav")
    parts = get_parts("scene06")
    p0 = parts[0] if len(parts) > 0 else dur_ms * 0.5
    t_p0 = int(round(p0 * 1000))

    # P0 (25.6s): Climate drought threat & creek conservation
    t_n1 = int(round(t_p0 * 0.50))
    t_n2 = t_p0
    # P1 (30.1s): Drawing challenge & Pelican teaser
    t_n3 = t_p0 + int(round((dur_ms - t_p0) * 0.45))
    t_n4 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c6_climate_change_drought_threat.png",
            caption_text="Nguy cơ biến đổi khí hậu: Dòng suối cạn kiệt đe dọa mái nhà của loài hóa thạch sống",
            start_ms=0,
            end_ms=t_n1,
            badge_text="01. MỐI NGUY HẠN HÁN",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c6_australia_creek_conservation.png",
            caption_text="Bảo vệ dòng suối trong: Hãy chung tay giữ gìn nguồn nước sạch cho mái nhà thú mỏ vịt",
            start_ms=t_n1,
            end_ms=t_n2,
            badge_text="02. BẢO TỒN DÒNG SUỐI ÚC",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c6_drawing_platypus_art_challenge.png",
            caption_text="Cùng vẽ thú mỏ vịt: Tự tay phác thảo chú thú mỏ vịt ngộ nghĩnh và chia sẻ cùng cộng đồng!",
            start_ms=t_n2,
            end_ms=t_n3,
            badge_text="03. THỬ THÁCH VẼ TRANH BẢNG TRẮNG",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c6_episode05_pelican_teaser.png",
            caption_text="Bật mí Tập 5: Chim Bồ Nông — Kẻ mỏ túi rác không đáy nuốt chửng cả thế giới!",
            start_ms=t_n3,
            end_ms=t_n4,
            badge_text="04. HẸN GẶP TẬP 5: CHIM BỒ NÔNG",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
    ]

    canvas_path = CANVAS_DIR / "scene06_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene06",
        act_badge="PHẦN 6: THÔNG ĐIỆP BẢO TỒN & OUTRO",
        title_text="BẢO TỒN DÒNG SUỐI NƯỚC NGỌT & BẬT MÍ TẬP 5: CHIM BỒ NÔNG THAM LAM",
        accent_color=ACCENT_TEAL,
        nodes=nodes,
        duration_ms=dur_ms + SCENE_HOLD_MS,
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
    print(f"[SPEC V8.3] Scene 06 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")
    return spec


def main():
    print("=================================================================")
    print("BUILDING EXPANDED DYNAMIC MULTI-NODE SCENE SPECS (37 NODES)")
    print("=================================================================")
    build_scene_01()
    build_scene_02()
    build_scene_03()
    build_scene_04()
    build_scene_05()
    build_scene_06()
    print("\n[SUCCESS] All 6 expanded scene specs and composed canvases built successfully!")


if __name__ == "__main__":
    main()
