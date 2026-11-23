"""
Build Rich Scene Specs V8 for Lung Mat Project
("Dynamic Multi-Node Canvas & Auto-Fit Bounding Box" + Fixed Top Header + Active-Node Isolation)
================================================================================================
100% Complete Visual Inventory Integration:
  - Scene 1: N = 6 dynamic nodes (includes BOTH Guinness Record Book & Guinness Size/Weight Comparison Chart!)
  - Scene 2: N = 8 dynamic nodes (includes ALL 4 RPG Stat Cards + ALL 4 Action/Proof Illustrations!)
  - Scene 3: N = 4 dynamic biological weapons nodes
  - Scene 4: N = 4 dynamic venom-immunity nodes
  - Scene 5: N = 4 dynamic Stoffel prison-break nodes
  - Scene 6: N = 3 dynamic nodes (includes Triumphant Badger + Cute Sea Otter Tool + Dark Sea Otter Twist!)
Total: 29/29 Unique Illustrations (100% Zero-Omission Guarantee!)
"""

import sys
import json
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent

sys.path.insert(0, str(ROOT / "src" / "composition"))
sys.path.insert(0, str(ROOT / "src" / "compiler"))

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
from sentence_prompt_architect import export_prompt_catalog_json

G = PROJ / "assets" / "gemini_downloaded"
AUDIO_DIR = PROJ / "audio"
CANVAS_DIR = PROJ / "assets" / "scenes_composed"
SPECS_DIR = PROJ / "specs"
CANVAS_DIR.mkdir(parents=True, exist_ok=True)
SPECS_DIR.mkdir(parents=True, exist_ok=True)


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
    # Scene 1: N = 6 dynamic nodes (3x2 Snake Flow - 100% complete Scene 1 assets)
    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c1_savanna_apex_predators_giants.png",
            caption_text="Bá chủ thảo nguyên: Sư tử, linh cẩu, voi rừng & tê giác",
            start_ms=0,
            end_ms=14500,
            badge_text="01. TỨ ĐẠI BÁ CHỦ",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c1_lions_sweating_scared.png",
            caption_text="Nghịch lý: Bầy sư tử toát mồ hôi tự động né sang một bên đường",
            start_ms=14500,
            end_ms=29680,
            badge_text="02. SƯ TỬ NÉ ĐƯỜNG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c1_badger_thug_sunglasses.png",
            caption_text="Mellivora capensis: Kẻ Chí Phèo số 1 hành tinh — Lửng Mật!",
            start_ms=29680,
            end_ms=37500,
            badge_text="03. KẺ CHÍ PHÈO SỐ 1",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c1_badger_guinness_fearless.png",
            caption_text="Kỷ lục Guinness thế giới: Sinh vật không biết sợ nhất hành tinh",
            start_ms=37500,
            end_ms=44500,
            badge_text="04. KỶ LỤC GUINNESS",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "c1_badger_guinness_record.png",
            caption_text="Tương quan chấn động: 30cm / 12kg đối đầu Sư tử nặng gấp 15 lần",
            start_ms=44500,
            end_ms=52500,
            badge_text="05. TƯƠNG QUAN 1 VS 15",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_06",
            img_path=G / "c1_lions_battered_torn_meat.png",
            caption_text="Cái giá quá đắt: Rách môi mẻ vuốt đổi lấy miếng thịt dai nhách",
            start_ms=52500,
            end_ms=dur_ms,
            badge_text="06. LỖ VỐN NẶNG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene01_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene01",
        act_badge="PHẦN 1",
        title_text="BÁ CHỦ LỲ LỢM & CƠN ÁC MỘNG CỦA CHÚA SƠN LÂM",
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
    (SPECS_DIR / "scene01_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8] Scene 01 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_02():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene02.wav")
    # Scene 2: N = 8 dynamic RPG + Proof nodes (All 4 RPG Stat Cards + All 4 Action Proofs!)
    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c2_badger_muscles_strength.png",
            caption_text="Chỉ số Sức Mạnh STR 85/100: Bó cơ nén đặc kéo nặng gấp 3 lần cơ thể",
            start_ms=0,
            end_ms=17200,
            badge_text="01. CHỈ SỐ STR 85/100",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c2_badger_drag_antelope_3x.png",
            caption_text="Thực chiến STR 85: Kéo lê xác linh dương nặng gấp 3 lần qua thảo nguyên",
            start_ms=17200,
            end_ms=34160,
            badge_text="02. KÉO XÁC LINH DƯƠNG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c2_badger_rubber_armor.png",
            caption_text="Chỉ số Phòng Thủ DEF 99/100: Giáp da cao su di động dày tới 6mm",
            start_ms=34160,
            end_ms=44250,
            badge_text="03. CHỈ SỐ DEF 99/100",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c2_badger_deflect_3_weapons.png",
            caption_text="Thực chiến DEF 99: Đánh bật răng nanh sư tử, kim bọ cạp & mũi giáo thép",
            start_ms=44250,
            end_ms=54350,
            badge_text="04. BẬT 3 ĐÒN TẤN CÔNG",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "c2_badger_iq_genius.png",
            caption_text="Chỉ số Trí Thông Minh IQ 90: Thiên tài bẻ khóa, chế tạo công cụ sinh tồn",
            start_ms=54350,
            end_ms=66000,
            badge_text="05. CHỈ SỐ IQ 90",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_06",
            img_path=G / "c2_badger_tenacity_999_no_surrender.png",
            caption_text="Độ Bền Bỉ & Lì Đòn TENACITY 999: Đạp nát cờ trắng, không bao giờ đầu hàng!",
            start_ms=66000,
            end_ms=77660,
            badge_text="06. TENACITY 999 ĐIỂM",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_07",
            img_path=G / "c2_badger_fear_zero.png",
            caption_text="Chỉ số Sợ Hãi FEAR 0/100: Kim đồng hồ gãy đôi ở mốc 0 tròn trĩnh!",
            start_ms=77660,
            end_ms=86600,
            badge_text="07. CHỈ SỐ FEAR 0/100",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_08",
            img_path=G / "c2_badger_amygdala_wrench.png",
            caption_text="Giải phẫu não bộ: Tạo hóa dùng cờ-lê tháo dỡ hoàn toàn Hạch Hạnh Nhân!",
            start_ms=86600,
            end_ms=dur_ms,
            badge_text="08. THÁO HẠCH HẠNH NHÂN",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene02_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene02",
        act_badge="PHẦN 2",
        title_text="BẢNG CHỈ SỐ SINH TỒN RPG PHÁ VỠ MỌI QUY LUẬT",
        accent_color=ACCENT_TEAL,
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
    (SPECS_DIR / "scene02_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8] Scene 02 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_03():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene03.wav")
    # Scene 3: N = 4 dynamic biological weapons nodes (2x2 Snake Flow)
    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c3_badger_loose_skin_jacket.png",
            caption_text="Cơ chế 1: Lớp da dày hơn da trâu nhưng lỏng lẻo như áo khoác rộng",
            start_ms=0,
            end_ms=26280,
            badge_text="01. ÁO KHOÁC DA RỘNG",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c3_badger_turn_180.png",
            caption_text="Tuyệt kỹ xoay 180 độ: Bị tóm gáy liền xoay ngược cắn mũi báo hoa",
            start_ms=26280,
            end_ms=51320,
            badge_text="02. XOAY 180° PHẢN ĐÒN",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c3_badger_sharp_claws.png",
            caption_text="Vuốt 5cm đào nhanh hơn người xúc xẻng & Hàm nghiền nát mai rùa",
            start_ms=51320,
            end_ms=78360,
            badge_text="03. VUỐT 5CM & HÀM THÉP",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c3_badger_crushing_turtle_musk.png",
            caption_text="Bom xạ hương: Xua đàn ong vò vẽ, sư tử & linh cẩu bịt mũi chạy",
            start_ms=78360,
            end_ms=dur_ms,
            badge_text="04. BOM XẠ HƯƠNG",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene03_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene03",
        act_badge="PHẦN 3",
        title_text="GIẢI PHẪU SINH HỌC & CỖ MÁY CHIẾN ĐẤU HOÀN HẢO",
        accent_color=ACCENT_ROYAL,
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
    (SPECS_DIR / "scene03_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V7] Scene 03 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_04():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene04.wav")
    # Scene 4: N = 4 dynamic venom-immunity nodes (2x2 Snake Flow)
    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c4_badger_venom_diet_3snakes.png",
            caption_text="Thực đơn điên rồ: 1/4 khẩu phần là Rắn Phì, Hổ Mang Thổi Nọc & Hổ Mang Chúa",
            start_ms=0,
            end_ms=30600,
            badge_text="01. THỰC ĐƠN KỊCH ĐỘC",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c4_badger_vs_cobra.png",
            caption_text="Đối đầu sinh tử: Hổ Mang Chúa cắn ngập răng nanh kịch độc vào mặt",
            start_ms=30600,
            end_ms=47480,
            badge_text="02. TỬ CHIẾN HỔ MANG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c4_acetylcholine_molecular_shield.png",
            caption_text="Đột biến thụ thể Acetylcholine: Áo giáp phân tử chặn nọc thần kinh",
            start_ms=47480,
            end_ms=70680,
            badge_text="03. KHIÊN PHÂN TỬ",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c4_badger_sleeping_venom.png",
            caption_text="Ngủ mê 2 tiếng như say rượu lọc độc, rồi tỉnh dậy chén nốt con rắn",
            start_ms=70680,
            end_ms=dur_ms,
            badge_text="04. NGỦ 2 TIẾNG DẬY ĂN TIẾP",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene04_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene04",
        act_badge="PHẦN 4",
        title_text="MIỄN NHIỄM NỌC ĐỘC RẮN & KHIÊN BẢO VỆ PHÂN TỬ",
        accent_color=ACCENT_TEAL,
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
    (SPECS_DIR / "scene04_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V7] Scene 04 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_05():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene05.wav")
    # Scene 5: N = 4 dynamic Stoffel prison-break nodes (2x2 Snake Flow)
    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c5_stoffel_bbc_star.png",
            caption_text="Huyền thoại Stoffel ở Nam Phi: Giới khoa học ngả mũ & lên sóng BBC",
            start_ms=0,
            end_ms=25480,
            badge_text="01. NGÔI SAO PHIM TÀI LIỆU",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c5_stoffel_mud_balls_broom_escape.png",
            caption_text="4 chiêu vượt tường bê tông: Xếp bi bùn, dựng cành cây, lăn đá & trộm chổi",
            start_ms=25480,
            end_ms=60040,
            badge_text="02. 4 CHIÊU VƯỢT NGỤC",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c5_stoffel_escape.png",
            caption_text="Dụ bạn gái làm bàn đạp vượt tường nhẵn thín, nhảy sang chuồng sư tử",
            start_ms=60040,
            end_ms=83000,
            badge_text="03. BÀN ĐẠP BẠN GÁI",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c5_badger_vs_3_lions.png",
            caption_text="Đẳng cấp giang hồ: 1 mình xù lông gầm rít lao vào 3 sư tử đực",
            start_ms=83000,
            end_ms=dur_ms,
            badge_text="04. ĐẠI CHIẾN 1 CHỌI 3",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene05_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene05",
        act_badge="PHẦN 5",
        title_text="THIÊN TÀI VƯỢT NGỤC STOFFEL & TRẬN CHIẾN HUYỀN THOẠI",
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
    (SPECS_DIR / "scene05_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V7] Scene 05 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_06():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene06.wav")
    parts_meta = AUDIO_DIR / "scene06_parts_duration.json"
    if parts_meta.exists():
        part_durs = json.loads(parts_meta.read_text(encoding="utf-8"))
        split_ms = int(round((part_durs[0] + 0.2) * 1000))
    else:
        split_ms = 24680

    mid_p1_ms = split_ms + int((dur_ms - split_ms) * 0.45)

    # Scene 6: N = 3 dynamic nodes (1x3 horizontal flow - includes BOTH Sea Otter assets!)
    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c6_badger_triumphant_rock.png",
            caption_text="Bài học sinh tồn: Kích thước không quyết định vị thế kẻ chiến thắng",
            start_ms=0,
            end_ms=split_ms,
            badge_text="01. Ý CHÍ BẤT KHUẤT",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c6_sea_otter_rock_tool.png",
            caption_text="Đại dương bao la: Rái Cá Biển có vẻ ngoài siêu đáng yêu, nằm ngửa đập vỏ sò",
            start_ms=split_ms,
            end_ms=mid_p1_ms,
            badge_text="02. VẺ NGOÀI ĐÁNG YÊU",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c6_sea_otter_teaser.png",
            caption_text="Bật mí Tập 2: Góc khuất rùng rợn của Rái Cá Biển — bắt cóc hải cẩu con!",
            start_ms=mid_p1_ms,
            end_ms=dur_ms,
            badge_text="03. TẬP 2: GÓC KHUẤT RÁI CÁ",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene06_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene06",
        act_badge="PHẦN 6",
        title_text="BÀI HỌC SINH TỒN & BẬT MÍ TẬP TIẾP THEO",
        accent_color=ACCENT_AMBER,
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
    (SPECS_DIR / "scene06_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8] Scene 06 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


if __name__ == "__main__":
    print("[BUILD V8] Generating Dynamic Multi-Node Canvas & Auto-Fit Bounding Box specs (29/29 Assets = 100%)...")
    export_prompt_catalog_json(SPECS_DIR / "sentence_visual_prompts_v6.json")
    build_scene_01()
    build_scene_02()
    build_scene_03()
    build_scene_04()
    build_scene_05()
    build_scene_06()
    print("[BUILD V8] All 6 Scene Canvases & Specs (29/29 dynamic nodes) generated successfully!")
