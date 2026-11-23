"""
Build Rich Scene Specs V8.3 for Episode 3: Cá Heo (`tap-03-ca-heo`)
("Dynamic Multi-Node Canvas & Auto-Fit Bounding Box" + Fixed Top Header + Dead-Center Active-Node Isolation + Zero Bleed)
=========================================================================================================================
100% Complete Visual Inventory Integration (29/29 Unique High-Res Illustrations):
  - Scene 1: N = 6 dynamic nodes (Otter to Dolphin Bridge, Cartoon Angel Myth, Permanent Smile Jaw Anatomy, Cool Ocean Boss, Tickling Pufferfish, Chasing Great White Shark)
  - Scene 2: N = 8 dynamic nodes (ALL 4 RPG Stat Cards: Brain IQ 99, Bio-Sonar 100, Torpedo Speed 95, Playfulness 999 + ALL 4 Action Proof Illustrations!)
  - Scene 3: N = 4 dynamic biological anatomy nodes (Melon Bio-Sonar Lens, Half-Brain Sleep Elevator, Signature Whistle ID Card, Sponge Nose Armor Tool)
  - Scene 4: N = 4 dynamic ocean game & hunting nodes (Pufferfish Volleyball Game, Dizzy Mirror Floating, Mud-Ring Fishing Net, Aerial Fish Catch Feast)
  - Scene 5: N = 4 dynamic shark battle & hero nodes (Shark vs Dolphin Pod Tactics, Rostrum Torpedo Belly Bump, Pelorus Jack Ship Guide, Dolphin Lifeguard Rescue Circle)
  - Scene 6: N = 3 dynamic nodes (Ocean Geniuses Conservation, Drawing Challenge Dolphin Art, Episode 4 Teaser: Platypus!)
Total: 29/29 Unique Illustrations (100% Zero-Omission Guarantee!)
"""

import sys
import json
import subprocess
from pathlib import Path
from typing import List

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
BROLL_DIR = PROJ / "assets" / "real_clips" / "clean"
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
    p0 = parts[0] if len(parts) > 0 else dur_ms / 2000.0
    t_p0 = int(round(p0 * 1000))
    t_n1 = int(round(t_p0 * 0.48))
    t_n2 = t_p0
    rem = max(100, dur_ms - t_p0)
    t_n3 = t_p0 + int(rem * 0.30)
    t_n4 = t_p0 + int(rem * 0.55)
    t_n5 = t_p0 + int(rem * 0.78)
    t_n6 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c1_otter_to_dolphin_bridge.png",
            caption_text="Ra khơi xa: Gặp gỡ ngôi sao thông thái Cá Heo Đại Dương",
            start_ms=0,
            end_ms=t_n1,
            badge_text="01. RA KHƠI ĐẠI DƯƠNG",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c1_cartoon_angel_dolphin_myth.png",
            caption_text="Hình tượng hoạt hình: Thiên thần hiền lành cứu người vượt sóng",
            start_ms=t_n1,
            end_ms=t_n2,
            badge_text="02. THIÊN THẦN HOẠT HÌNH?",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c1_permanent_smile_jaw_anatomy.png",
            caption_text="Bí mật nụ cười: Xương hàm dưới uốn cong cố định từ khi mới sinh!",
            start_ms=t_n2,
            end_ms=t_n3,
            badge_text="03. CÚ LỪA XƯƠNG HÀM",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c1_dolphin_cool_ocean_boss.png",
            caption_text="Học sinh siêu quậy: Tinh nghịch và thông minh bậc nhất biển cả",
            start_ms=t_n3,
            end_ms=t_n4,
            badge_text="04. TRÙM CUỐI TINH NGHỊCH",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "c1_dolphin_tickling_pufferfish.png",
            caption_text="Trò đùa lầy lội: Chọc Cá Nóc phồng tròn như quả bóng chuyền!",
            start_ms=t_n4,
            end_ms=t_n5,
            badge_text="05. BÓNG CHUYỀN CÁ NÓC",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_06",
            img_path=G / "c1_dolphin_chasing_great_white_shark.png",
            caption_text="Bất ngờ tột độ: Hợp sức rượt đuổi cả hung thần Cá Mập Trắng!",
            start_ms=t_n5,
            end_ms=t_n6,
            badge_text="06. RƯỢT ĐUỔI CÁ MẬP",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene01_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene01",
        act_badge="PHẦN 1",
        title_text="BÍ MẬT ĐẰNG SAU NỤ CƯỜI HOẠT HÌNH VĨNH CỬU CỦA CÁ HEO",
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
    (SPECS_DIR / "scene01_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8.3 - EP03] Scene 01 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_02():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene02.wav")
    parts = get_parts("scene02")
    t0 = 0
    t1 = int(round(parts[0] * 1000)) if len(parts) > 0 else int(dur_ms * 0.35)
    t2 = t1 + (int(round(parts[1] * 1000)) if len(parts) > 1 else int(dur_ms * 0.20))
    t3 = t2 + (int(round(parts[2] * 1000)) if len(parts) > 2 else int(dur_ms * 0.20))
    t4 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c2_stat_card_iq.png",
            caption_text="Trí tuệ BRAIN IQ 99/100: Tỷ lệ não bộ lớn thứ hai hành tinh!",
            start_ms=t0,
            end_ms=t0 + int((t1 - t0) * 0.48),
            badge_text="01. BRAIN IQ 99/100",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c2_dolphin_mirror_selfie_iq.png",
            caption_text="Thực chiến IQ 99: Tự soi gương nhận diện bản thân và tạo dáng!",
            start_ms=t0 + int((t1 - t0) * 0.48),
            end_ms=t1,
            badge_text="02. TỰ SOI GƯƠNG TẠO DÁNG",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c2_stat_card_sonar.png",
            caption_text="Ra-đa SONAR 100/100: Đôi mắt thần quét xuyên màn đêm đáy biển",
            start_ms=t1,
            end_ms=t1 + int((t2 - t1) * 0.48),
            badge_text="03. BIO-SONAR 100/100",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c2_dolphin_xray_sonar_vision.png",
            caption_text="Thực chiến Sonar 100: Quét sóng âm nhìn xuyên cát như X-quang!",
            start_ms=t1 + int((t2 - t1) * 0.48),
            end_ms=t2,
            badge_text="04. KÍNH X-QUANG ĐÁY BIỂN",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_05",
            img_path=G / "c2_stat_card_speed.png",
            caption_text="Tốc độ SPEED 95/100: Da giảm ma sát và đuôi đập dọc cực khỏe",
            start_ms=t2,
            end_ms=t2 + int((t3 - t2) * 0.48),
            badge_text="05. TORPEDO SPEED 95/100",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_06",
            img_path=G / "c2_dolphin_rocket_acrobatics.png",
            caption_text="Thực chiến Speed 95: Phóng vút 55 km/h, bật nhảy cao tới 6 mét!",
            start_ms=t2 + int((t3 - t2) * 0.48),
            end_ms=t3,
            badge_text="06. BẬT NHẢY CAO 6 MÉT",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_07",
            img_path=G / "c2_stat_card_playfulness.png",
            caption_text="Độ ham chơi PLAYFULNESS 999: Phá vỡ hoàn toàn mọi thang đo!",
            start_ms=t3,
            end_ms=t3 + int((t4 - t3) * 0.48),
            badge_text="07. PLAYFUL 999 ĐIỂM",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_08",
            img_path=G / "c2_dolphin_surfing_bubble_rings.png",
            caption_text="Nghệ sĩ đại dương: Tự thổi vòng bong bóng bạc rồi bơi xuyên qua!",
            start_ms=t3 + int((t4 - t3) * 0.48),
            end_ms=t4,
            badge_text="08. ẢO THUẬT BONG BÓNG",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.00,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene02_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene02",
        act_badge="PHẦN 2",
        title_text="BẢNG CHỈ SỐ SINH TỒN RPG — THIÊN TÀI TINH NGHỊCH BIỂN CẢ",
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
    print(f"[SPEC V8.3 - EP03] Scene 02 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_03():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene03.wav")
    parts = get_parts("scene03")
    t0 = 0
    t1 = int(round(parts[0] * 1000)) if len(parts) > 0 else int(dur_ms * 0.35)
    t2 = t1 + (int(round(parts[1] * 1000)) if len(parts) > 1 else int(dur_ms * 0.35))
    t3 = dur_ms
    t2_mid = t2 + int((t3 - t2) * 0.52)

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c3_melon_biosonar_anatomy.png",
            caption_text="Thấu kính siêu âm Melon: Phát 1.000 click/giây thu âm qua hàm!",
            start_ms=t0,
            end_ms=t1,
            badge_text="01. THẤU KÍNH SIÊU ÂM MELON",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c3_half_brain_sleep_elevator.png",
            caption_text="Ngủ mở một mắt: Một nửa não ngủ, một nửa mở canh cá mập!",
            start_ms=t1,
            end_ms=t2,
            badge_text="02. NGỦ MỞ MỘT MẮT",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c3_signature_whistle_id_card.png",
            caption_text="Tên riêng bằng nốt nhạc: Mỗi chú cá heo có một điệu huýt sáo riêng",
            start_ms=t2,
            end_ms=t2_mid,
            badge_text="03. TÊN RIÊNG BẰNG NỐT NHẠC",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c3_sponge_nose_armor_tool.png",
            caption_text="Găng tay bọt biển: Đeo bọt biển bảo hộ đầu mũi khi đào bới đá cát!",
            start_ms=t2_mid,
            end_ms=t3,
            badge_text="04. GĂNG TAY BỌT BIỂN",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene03_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene03",
        act_badge="PHẦN 3",
        title_text="KÍNH X-QUANG SIÊU ÂM, NGỦ MỞ MỘT MẮT & GĂNG TAY BỌT BIỂN",
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
    print(f"[SPEC V8.3 - EP03] Scene 03 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_04():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene04.wav")
    parts = get_parts("scene04")
    t0 = 0
    t1 = int(round((parts[0] + parts[1]) * 1000)) if len(parts) > 1 else int(dur_ms * 0.40)
    t2 = t1 + (int(round(parts[2] * 1000)) if len(parts) > 2 else int(dur_ms * 0.28))
    t3 = dur_ms
    t3_mid = t2 + int((t3 - t2) * 0.52)

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c4_dolphin_pufferfish_volleyball_game.png",
            caption_text="Bóng chuyền cá nóc: Dùng mõm chuyền qua lại chú cá nóc phồng tròn!",
            start_ms=t0,
            end_ms=t1,
            badge_text="01. BÓNG CHUYỀN CÁ NÓC",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c4_dolphin_dizzy_mirror_floating.png",
            caption_text="Lâng lâng ngắm bóng: Nổi ngửa bụng thư giãn trên mặt nước phẳng lặng!",
            start_ms=t1,
            end_ms=t2,
            badge_text="02. LÂNG LÂNG NGẮM BÓNG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c4_mud_ring_fishing_net.png",
            caption_text="Vòng vây lưới bùn: Quẫy đuôi xoay tròn dựng tường cát nhốt đàn cá!",
            start_ms=t2,
            end_ms=t3_mid,
            badge_text="03. VÒNG VÂY LƯỚI BÙN",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c4_aerial_fish_catch_feast.png",
            caption_text="Đón cá trên không: Xếp hàng chờ sẵn đón cá hoảng sợ nhảy ra ngoài!",
            start_ms=t3_mid,
            end_ms=t3,
            badge_text="04. ĐÓN CÁ TRÊN KHÔNG",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene04_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene04",
        act_badge="PHẦN 4",
        title_text="TRÒ CHƠI BÓNG CHUYỀN CÁ NÓC & VÒNG LƯỚI BÙN MA THUẬT",
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
    (SPECS_DIR / "scene04_spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SPEC V8.3 - EP03] Scene 04 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_05():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene05.wav")
    parts = get_parts("scene05")
    t0 = 0
    t1 = int(round(parts[0] * 1000)) if len(parts) > 0 else int(dur_ms * 0.22)
    t2 = t1 + (int(round(parts[1] * 1000)) if len(parts) > 1 else int(dur_ms * 0.28))
    t3 = t2 + (int(round(parts[2] * 1000)) if len(parts) > 2 else int(dur_ms * 0.28))
    t4 = dur_ms

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c5_shark_vs_dolphin_pod_tactics.png",
            caption_text="Bao vây Cá Mập Trắng: Sức mạnh bầy đàn khắc chế kẻ đi săn đơn độc!",
            start_ms=t0,
            end_ms=t1,
            badge_text="01. BAO VÂY CÁ MẬP TRẮNG",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c5_rostrum_torpedo_belly_bump.png",
            caption_text="Cú húc ngư lôi Rostrum: Dùng mõm xương cứng húc mạnh vào bụng cá mập!",
            start_ms=t1,
            end_ms=t2,
            badge_text="02. CÚ HÚC NGƯ LÔI ROSTRUM",
            badge_color=ACCENT_AMBER,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.05,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c5_pelorus_jack_ship_guide.png",
            caption_text="Hoa tiêu Pelorus Jack: 24 năm dẫn đường tàu biển vượt qua đá ngầm!",
            start_ms=t2,
            end_ms=t3,
            badge_text="03. HOA TIÊU PELORUS JACK",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=2.00,
        ),
        WorldNodeConfig(
            beat_id="beat_04",
            img_path=G / "c5_dolphin_lifeguard_rescue_circle.png",
            caption_text="Hiệp sĩ cứu hộ: Lập vòng tròn bảo vệ người gặp nạn trước sóng gió!",
            start_ms=t3,
            end_ms=t4,
            badge_text="04. HIỆP SĨ CỨU HỘ BIỂN",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene05_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene05",
        act_badge="PHẦN 5",
        title_text="KHẮC TINH CỦA CÁ MẬP TRẮNG & HUYỀN THOẠI PELORUS JACK",
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
    print(f"[SPEC V8.3 - EP03] Scene 05 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


def build_scene_06():
    dur_ms = get_audio_duration_ms(AUDIO_DIR / "scene06.wav")
    parts = get_parts("scene06")
    t0 = 0
    t1 = int(round(parts[0] * 1000)) if len(parts) > 0 else int(dur_ms * 0.45)
    t2 = dur_ms
    t1_mid = int(t1 * 0.52)

    nodes = [
        WorldNodeConfig(
            beat_id="beat_01",
            img_path=G / "c6_ocean_geniuses_conservation.png",
            caption_text="Bảo vệ đại dương: Giữ biển sạch để cá heo mãi tự do nhảy múa!",
            start_ms=t0,
            end_ms=t1_mid,
            badge_text="01. BẢO VỆ ĐẠI DƯƠNG XANH",
            badge_color=ACCENT_TEAL,
            highlight_color=HIGHLIGHT_MINT,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_02",
            img_path=G / "c6_drawing_challenge_dolphin_art.png",
            caption_text="Góc họa sĩ nhí: Cùng vẽ chú cá heo từ một nét cong lượn sóng!",
            start_ms=t1_mid,
            end_ms=t1,
            badge_text="02. GÓC HỌA SĨ NHÍ",
            badge_color=ACCENT_ROYAL,
            highlight_color=HIGHLIGHT_YELLOW,
            focus_zoom=1.95,
        ),
        WorldNodeConfig(
            beat_id="beat_03",
            img_path=G / "c6_ep04_platypus_teaser.png",
            caption_text="Bật mí Tập 4: Thú Mỏ Vịt — Mỏ vịt, đẻ trứng, tiết sữa qua da!",
            start_ms=t1,
            end_ms=t2,
            badge_text="03. TẬP 4: THÚ MỎ VỊT!",
            badge_color=ACCENT_CRIMSON,
            highlight_color=HIGHLIGHT_CORAL,
            focus_zoom=1.95,
        ),
    ]
    canvas_path = CANVAS_DIR / "scene06_canvas.png"
    spec = build_dynamic_multi_node_scene(
        scene_id="scene06",
        act_badge="PHẦN 6",
        title_text="THÔNG ĐIỆP ĐẠI DƯƠNG XANH & BẬT MÍ TẬP 4: THÚ MỎ VỊT",
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
    print(f"[SPEC V8.3 - EP03] Scene 06 built: {dur_ms}ms | N={len(nodes)} nodes | World={spec['world_width']}x{spec['world_height']}")


if __name__ == "__main__":
    print("[BUILD V8.3 - EP03] Generating Dynamic Multi-Node Canvas & Auto-Fit Bounding Box specs (29/29 Assets = 100%)...")
    build_scene_01()
    build_scene_02()
    build_scene_03()
    build_scene_04()
    build_scene_05()
    build_scene_06()
    print("[BUILD V8.3 - EP03] All 6 Scene Canvases & Specs (29/29 dynamic nodes) generated successfully!")
