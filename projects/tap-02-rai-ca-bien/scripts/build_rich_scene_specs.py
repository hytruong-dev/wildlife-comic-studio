"""
Build Rich Scene Specs V8 for Episode 2: Rái Cá Biển (`tap-02-rai-ca-bien`)
("Dynamic Multi-Node Canvas & Auto-Fit Bounding Box" + Fixed Top Header + Active-Node Isolation + Zero Bleed)
=============================================================================================================
100% Complete Visual Inventory Integration (29/29 Unique High-Res Illustrations):
  - Scene 1: N = 6 dynamic nodes (Mustelidae Family Tree, Cute Holding Hands, Thug Mask Twist, Kelp Anchor, Drifting to Orca, Crab Robber)
  - Scene 2: N = 8 dynamic nodes (ALL 4 RPG Stat Cards: Cuteness 100, Fur Armor 95, IQ 92, Trickery 999 + ALL 4 Action Proof Illustrations!)
  - Scene 3: N = 4 dynamic biological anatomy nodes (1 Million Hairs Microscope, 4h Laundry Grooming, 25% Metabolism Furnace, Doraemon Armpit Pouch)
  - Scene 4: N = 4 dynamic hostage-ransom nodes (Lazy Male Scheme, Floating Cork Pup in Kelp Crib, Kidnap Pup for Ransom, Mom Pays Crab & Stone Theft)
  - Scene 5: N = 4 dynamic keystone & Otter 841 nodes (Kelp vs Purple Urchin Zombies, Urchin Slayer Purple Bones, Otter 841 Surfboard Pirate, Outsmarting Coast Guard)
  - Scene 6: N = 3 dynamic nodes (Keystone Ecological Balance, Angel Dolphin Cartoon Smile, Episode 3 Teaser: Dolphin Gang Pufferfish Volleyball!)
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
        data = json.loads(p.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "parts" in data:
            return list(data["parts"].values())
    dur_sec = get_audio_duration_ms(AUDIO_DIR / f"{scene_id}.wav") / 1000.0
    return [dur_sec]


def build_scene_01():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene01.wav")
    parts = get_parts("scene01")
    p0 = parts[0] if len(parts) > 0 else dur_ms / 2000.0
    t_p0 = int(round(p0 * 1000))
    t_n1 = int(round(t_p0 * 0.50))
    t_n2 = t_p0
    rem = max(100, dur_ms - t_p0)
    t_n3 = t_p0 + int(rem * 0.25)
    t_n4 = t_p0 + int(rem * 0.50)
    t_n5 = t_p0 + int(rem * 0.75)
    t_n6 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c1_family_tree_mustelidae.png",
            caption_text="Gia tộc họ Chồn (Mustelidae): Anh em ruột thịt với Lửng Mật dưới đại dương",
            start_ms=0,
            end_ms=t_n1,
            badge_text="01. HỌ HÀNG NHÀ CHỒN",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c1_otter_cute_holding_hands_hearts.png",
            caption_text="Hình tượng triệu view: Cục bông tròn xoe áp má nắm chặt tay nhau ngủ",
            start_ms=t_n1,
            end_ms=t_n2,
            badge_text="02. BIỂU TƯỢNG NGÔN TÌNH?",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c1_otter_myth_busted_thug_mask.png",
            caption_text="Enhydra lutris: Lột mặt nạ thú nhồi bông lộ diện kẻ thu phí đường biển!",
            start_ms=t_n2,
            end_ms=t_n3,
            badge_text="03. CÚ LỪA ĐẠI DƯƠNG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c1_otter_kelp_seatbelt_anchor.png",
            caption_text="Sự thật nắm tay & quấn rong biển: Dây neo sinh tồn chống sóng cuốn trôi",
            start_ms=t_n3,
            end_ms=t_n4,
            badge_text="04. DÂY NEO CHỐNG TRÔI",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "c1_otter_drifting_to_orca_jaws.png",
            caption_text="Hiểm họa ngủ quên: Bị hải lưu cuốn trôi tuột vào hàm Cá Voi Sát Thủ",
            start_ms=t_n4,
            end_ms=t_n5,
            badge_text="05. TRÔI VÀO HÀM ORCA",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_06",
            img_path=G / "c1_otter_hungry_pirate_crab_robber.png",
            caption_text="Khi cơn đói ập đến: Biến hình thành giang hồ cướp cạn tinh quái bậc nhất",
            start_ms=t_n5,
            end_ms=t_n6,
            badge_text="06. GIANG HỒ ĐẠI DƯƠNG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene01_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene01",
        act_badge="PHẦN 1",
        title_text="CÚ LỪA ĐÁNG YÊU NHẤT ĐẠI DƯƠNG & BỘ MẶT THẬT",
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
    (SPECS_DIR / "scene01_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8 - EP02] Scene 01 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_02():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene02.wav")
    parts = get_parts("scene02")
    t0 = 0
    t1 = int(round(parts[0] * 1000)) if len(parts) > 0 else int(dur_ms * 0.25)
    t2 = t1 + (int(round(parts[1] * 1000)) if len(parts) > 1 else int(dur_ms * 0.25))
    t3 = t2 + (int(round(parts[2] * 1000)) if len(parts) > 2 else int(dur_ms * 0.25))
    t4 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c2_otter_rpg_cuteness_100.png",
            caption_text="Chỉ số Ngụy Trang Đáng Yêu CUTENESS 100/100: Đôi mắt tròn & ria mép rung rinh",
            start_ms=t0,
            end_ms=t0 + int((t1 - t0) * 0.50),
            badge_text="01. CUTENESS 100/100",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c2_otter_cuteness_hypnotize_humans.png",
            caption_text="Thực chiến CUTENESS 100: Xoa má làm duyên thôi miên 99% nhân loại",
            start_ms=t0 + int((t1 - t0) * 0.50),
            end_ms=t1,
            badge_text="02. THÔI MIÊN NHÂN LOẠI",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c2_otter_rpg_fur_armor_95.png",
            caption_text="Chỉ số Giáp Lông FUR ARMOR 95/100: Khiên không khí chống nước lạnh 0°C",
            start_ms=t1,
            end_ms=t1 + int((t2 - t1) * 0.50),
            badge_text="03. FUR ARMOR 95/100",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c2_otter_no_blubber_vs_whale_seal.png",
            caption_text="Đối chứng giải phẫu: 0% mỡ dưới da nhưng mặc áo lông 160.000 sợi/cm²",
            start_ms=t1 + int((t2 - t1) * 0.50),
            end_ms=t2,
            badge_text="04. 0% MỠ VS 160K SỢI LÔNG",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "c2_otter_rpg_iq_tool_92.png",
            caption_text="Chỉ số Trí Tuệ Công Cụ IQ 92/100: Thợ cơ khí bậc thầy dưới đáy biển",
            start_ms=t2,
            end_ms=t2 + int((t3 - t2) * 0.50),
            badge_text="05. CHỈ SỐ IQ 92/100",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_06",
            img_path=G / "c2_otter_stone_anvil_mechanic.png",
            caption_text="Thực chiến IQ 92: Dùng búa đá đập vỡ vỏ trai & cua cứng như bê tông",
            start_ms=t2 + int((t3 - t2) * 0.50),
            end_ms=t3,
            badge_text="06. BÚA ĐÁ ĐẬP VỎ SÒ",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_07",
            img_path=G / "c2_otter_rpg_trickery_999.png",
            caption_text="Độ Lầy Lội & Mánh Khóe TRICKERY 999/100: Phá vỡ hoàn toàn mọi thang đo!",
            start_ms=t3,
            end_ms=t3 + int((t4 - t3) * 0.50),
            badge_text="07. TRICKERY 999 ĐIỂM",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_08",
            img_path=G / "c2_otter_three_crimes_montage.png",
            caption_text="Hồ sơ 3 phi vụ: Cướp đồ ăn, bắt cóc con tin đòi hải sản & cướp ván trượt!",
            start_ms=t3 + int((t4 - t3) * 0.50),
            end_ms=t4,
            badge_text="08. HỒ SƠ 3 PHI VỤ",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene02_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene02",
        act_badge="PHẦN 2",
        title_text="BẢNG CHỈ SỐ SINH TỒN RPG — THÁNH ĂN VẠ ĐẠI DƯƠNG",
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
    (SPECS_DIR / "scene02_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8 - EP02] Scene 02 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_03():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene03.wav")
    parts = get_parts("scene03")
    t0 = 0
    t1 = int(round(parts[0] * 1000)) if len(parts) > 0 else int(dur_ms * 0.35)
    t2 = t1 + (int(round(parts[1] * 1000)) if len(parts) > 1 else int(dur_ms * 0.35))
    t3 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c3_otter_1million_hairs_microscope.png",
            caption_text="Kỷ lục thế giới: 1 triệu sợi lông trên 1 inch vuông khóa chặt bọt khí ấm",
            start_ms=t0,
            end_ms=t0 + int((t1 - t0) * 0.55),
            badge_text="01. 1 TRIỆU SỢI LÔNG",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c3_otter_grooming_laundry_4hours.png",
            caption_text="Thợ giặt chuyên nghiệp: Dành 4 giờ mỗi ngày cào lông, thổi khí & vắt nước",
            start_ms=t0 + int((t1 - t0) * 0.55),
            end_ms=t1,
            badge_text="02. 4 GIỜ CHẢI CHUỐT",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c3_otter_metabolism_furnace_25percent.png",
            caption_text="Lò đốt năng lượng gấp 3 lần: Phải ăn lượng hải sản bằng 25-30% cơ thể/ngày!",
            start_ms=t1,
            end_ms=t2,
            badge_text="03. ĂN 25% CƠ THỂ/NGÀY",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c3_otter_doraemon_armpit_pouch_hammer.png",
            caption_text="Túi thần kỳ Doraemon dưới nách: Cất đá búa gia truyền đập 45 nhát/15 giây!",
            start_ms=t2,
            end_ms=t3,
            badge_text="04. TÚI NÁCH DORAEMON",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene03_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene03",
        act_badge="PHẦN 3",
        title_text="ÁO PHAO 1 TRIỆU SỢI LÔNG & TÚI THẦN KỲ DORAEMON",
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
    (SPECS_DIR / "scene03_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8 - EP02] Scene 03 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_04():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene04.wav")
    parts = get_parts("scene04")
    t0 = 0
    t1 = int(round(parts[0] * 1000)) if len(parts) > 0 else int(dur_ms * 0.25)
    t2 = t1 + (int(round(parts[1] * 1000)) if len(parts) > 1 else int(dur_ms * 0.25))
    t3 = t2 + (int(round(parts[2] * 1000)) if len(parts) > 2 else int(dur_ms * 0.25))
    t4 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c4_otter_lazy_male_hungry_scheme.png",
            caption_text="Áp lực 10kg hải sản/ngày: Gã rái cá đực lười lặn sâu nảy sinh âm mưu",
            start_ms=t0,
            end_ms=t1,
            badge_text="01. ÂM MƯU KẺ LƯỜI BIẾNG",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c4_otter_pup_cork_float_kelp_crib.png",
            caption_text="Rái cá con nổi phềnh như phao cứu sinh, được mẹ quấn rong biển làm nôi",
            start_ms=t1,
            end_ms=t2,
            badge_text="02. PHAO CỨU SINH CON NON",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c4_otter_kidnap_pup_for_ransom.png",
            caption_text="Bắt cóc con tin trên mặt nước: Giữ rái cá con ép mẹ giao nộp hải sản!",
            start_ms=t2,
            end_ms=t3,
            badge_text="03. BẮT CON TIN ĐÒI QUÀ",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c4_otter_mom_pays_crab_ransom_stone_theft.png",
            caption_text="Mẹ ngậm ngùi nộp cua & bào ngư chuộc con; đối thủ cướp luôn cả đá búa!",
            start_ms=t3,
            end_ms=t4,
            badge_text="04. NỘP CUA CHUỘC CON",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene04_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene04",
        act_badge="PHẦN 4",
        title_text="MÁNH KHÓE BẮT GIỮ CON TIN ĐÒI CHUỘC BÀO NGƯ",
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
    (SPECS_DIR / "scene04_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8 - EP02] Scene 04 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_05():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene05.wav")
    parts = get_parts("scene05")
    t0 = 0
    t1 = int(round(parts[0] * 1000)) if len(parts) > 0 else int(dur_ms * 0.25)
    t2 = t1 + (int(round(parts[1] * 1000)) if len(parts) > 1 else int(dur_ms * 0.25))
    t3 = t2 + (int(round(parts[2] * 1000)) if len(parts) > 2 else int(dur_ms * 0.25))
    t4 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c5_kelp_forest_vs_purple_urchin_zombies.png",
            caption_text="Đại họa đáy biển: Đội quân Nhím Biển Tím tràn tới gặm trụi rừng Tảo Bẹ",
            start_ms=t0,
            end_ms=t1,
            badge_text="01. ĐỘI QUÂN NHÍM BIỂN",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c5_otter_urchin_slayer_purple_bones.png",
            caption_text="Vệ binh rừng tảo bẹ: Ăn nhiều nhím biển đến mức răng và xương hóa màu tím!",
            start_ms=t1,
            end_ms=t2,
            badge_text="02. XƯƠNG & RĂNG HÓA TÍM",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c5_otter_841_surfboard_pirate_santa_cruz.png",
            caption_text="Huyền thoại rái cá 841 ở Santa Cruz: Chặn đầu cướp ván lướt sóng phơi nắng!",
            start_ms=t2,
            end_ms=t3,
            badge_text="03. HẢI TẶC SỐ HIỆU 841",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c5_otter_841_outsmarts_coast_guard_nets.png",
            caption_text="Đỉnh cao trí tuệ: Lặn né mọi tấm lưới và nhảy lên ván của đội cứu hộ trêu ngươi",
            start_ms=t3,
            end_ms=t4,
            badge_text="04. TRÊU NGƯƠI ĐỘI VÂY BẮT",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene05_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene05",
        act_badge="PHẦN 5",
        title_text="VỆ BINH RỪNG TẢO BẸ & HẢI TẶC CƯỚP VÁN TRƯỢT 841",
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
    (SPECS_DIR / "scene05_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8 - EP02] Scene 05 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_06():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene06.wav")
    parts = get_parts("scene06")
    t0 = 0
    t1 = int(round(parts[0] * 1000)) if len(parts) > 0 else int(dur_ms * 0.45)
    t2 = dur_ms
    mid_p2 = t1 + int((t2 - t1) * 0.48)

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c6_otter_keystone_guardian_balance.png",
            caption_text="Cán cân tự nhiên: Chiếc bụng đói của Rái Cá Biển giữ lá phổi xanh cho đại dương",
            start_ms=t0,
            end_ms=t1,
            badge_text="01. LÁ CHẮN ĐẠI DƯƠNG",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c6_dolphin_cartoon_smile_angel.png",
            caption_text="Ngoài khơi xa: Loài Cá Heo có nụ cười thiên thần thân thiện trên phim hoạt hình",
            start_ms=t1,
            end_ms=mid_p2,
            badge_text="02. NỤ CƯỜI THIÊN THẦN?",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c6_dolphin_pufferfish_volleyball_teaser.png",
            caption_text="Bật mí Tập 3: Băng đảng Cá Heo bắt nạt cá mập & đánh bóng chuyền bằng Cá Nóc!",
            start_ms=mid_p2,
            end_ms=t2,
            badge_text="03. TẬP 3: BỘ MẶT CÁ HEO",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene06_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene06",
        act_badge="PHẦN 6",
        title_text="BÀI HỌC ĐẠI DƯƠNG & BẬT MÍ TẬP 3: BỘ MẶT CÁ HEO",
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
    (SPECS_DIR / "scene06_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8 - EP02] Scene 06 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


if __name__ == "__main__":
    print("[BUILD V8 - EP02] Generating Dynamic Multi-Node Canvas & Auto-Fit Bounding Box specs (29/29 Assets = 100%)...")
    build_scene_01()
    build_scene_02()
    build_scene_03()
    build_scene_04()
    build_scene_05()
    build_scene_06()
    print("[BUILD V8 - EP02] All 6 Scene Canvases & Specs (29/29 dynamic nodes) generated successfully!")
