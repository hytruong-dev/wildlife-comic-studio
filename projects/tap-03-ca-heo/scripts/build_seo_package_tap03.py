"""
Generate 100/100 Bilingual (Vietnamese + English) YouTube SEO Package for Episode 3: Cá Heo (`tap-03-ca-heo`)
Uses `src/seo/youtube_seo_engine.py` (Open-Tube-SEO + youtube-suggest-scraper + AI-YouTube-Timestamps)
Follows TASTE-41 (All-Ages Drawing-First) and TASTE-42 / LESSON-42 (Global Multi-Language Localization).
"""

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src" / "seo"))

from youtube_seo_engine import (
    harvest_youtube_autocomplete_keywords,
    probe_duration_sec,
    format_mm_ss,
    score_youtube_seo_opentube,
)


def build_tap03_seo_package() -> dict:
    renders_dir = PROJ / "renders"
    intro_mp4 = ROOT / "assets" / "branding" / "intro_ve_chuyen_hoang_da.mp4"

    scene_defs = [
        ("scene01_final.mp4", "Phần 1: Bí Mật Đằng Sau Nụ Cười Hoạt Hình Vĩnh Cửu Của Cá Heo"),
        ("scene02_final.mp4", "Phần 2: Bảng Chỉ Số Sinh Tồn RPG — Trí Tuệ IQ 99 & Độ Ham Chơi 999 Điểm!"),
        ("scene03_final.mp4", "Phần 3: Giải Phẫu Kỳ Diệu — Kính X-Quang Siêu Âm, Ngủ Mở 1 Mắt & Tên Riêng"),
        ("scene04_final.mp4", "Phần 4: Cú Bẻ Lái Hài Hước — Trò Chơi Bóng Chuyền Cá Nóc & Vòng Lưới Bùn"),
        ("scene05_final.mp4", "Phần 5: Khắc Tinh Của Cá Mập Trắng & Huyền Thoại Hoa Tiêu Pelorus Jack"),
        ("scene06_final.mp4", "Phần 6: Thông Điệp Đại Dương Xanh & Bật Mí Tập 4: Thú Mỏ Vịt Kỳ Quặc"),
    ]

    scene_defs_en = [
        ("scene01_final.mp4", "Part 1: The Secret Behind the Dolphin's Permanent Cartoon Smile"),
        ("scene02_final.mp4", "Part 2: Survival RPG Stats — Brain IQ 99 & Playfulness 999!"),
        ("scene03_final.mp4", "Part 3: Super Anatomy — Bio-Sonar X-Ray, Half-Brain Sleep & Signature Whistle Names"),
        ("scene04_final.mp4", "Part 4: Ocean Pranksters — Pufferfish Volleyball Game & Magic Mud-Ring Net"),
        ("scene05_final.mp4", "Part 5: Why Great White Sharks Fear Dolphins & The Legend of Pelorus Jack"),
        ("scene06_final.mp4", "Part 6: Clean Ocean Message & Episode 4 Teaser: The Bizarre Platypus"),
    ]

    intro_dur = probe_duration_sec(intro_mp4) if intro_mp4.exists() else 10.0
    cur_sec = 0.0
    chapters = ["00:00 Mở đầu: Bí Mật Đằng Sau Nụ Cười Của Cá Heo Đại Dương"]
    chapters_en = ["00:00 Intro: The Secret Behind the Dolphin's Cartoon Smile"]
    cur_sec += intro_dur

    for (fname, ch_title), (_, ch_title_en) in zip(scene_defs, scene_defs_en):
        p = renders_dir / fname
        dur = probe_duration_sec(p) if p.exists() else 85.0
        chapters.append(f"{format_mm_ss(cur_sec)} {ch_title}")
        chapters_en.append(f"{format_mm_ss(cur_sec)} {ch_title_en}")
        cur_sec += dur

    chapters_block = "\n".join(chapters)
    chapters_en_block = "\n".join(chapters_en)

    seed_queries = [
        "cá heo",
        "sự thật về cá heo",
        "cá heo và cá mập",
        "cá heo thông minh",
        "vẽ chuyện hoang dã",
        "thế giới động vật",
    ]
    live_harvest = harvest_youtube_autocomplete_keywords(seed_queries, expand_depth=2)
    live_suggestions = live_harvest.get("suggestions", [])

    # Title length between 40-70 chars with number, colon/exclamation, and power word ("giải mã"/"bí mật")
    title = "Giải Mã Cá Heo: Bóng Chuyền Cá Nóc & 3 Bí Mật Điên Rồ! | Tập 3"
    title_en = "Dolphin Secrets Decoded: Pufferfish Volleyball & Shark Battles! | Ep 3"

    description = f"""Giải mã Cá Heo (Dolphin - Delphinidae) — thiên tài đại dương sở hữu bộ não lớn thứ hai hành tinh và luôn xuất hiện trong các bộ phim hoạt hình hay tranh vẽ thiếu nhi với nụ cười thân thiện vĩnh cửu. Thế nhưng trong Tập 3 của series Vẽ Chuyện Hoang Dã (Thế Giới Động Vật Whiteboard Animation), chúng ta sẽ cùng dùng nét vẽ tay hài hước để khám phá những siêu năng lực sinh học đáng kinh ngạc và những trò chơi tinh nghịch bậc nhất biển khơi của loài Cá Heo!

🔥 Những bí mật thú vị về Cá Heo được giải mã bằng nét vẽ Whiteboard trong video:
- Bí mật hội họa đằng sau "Nụ cười hoạt hình vĩnh cửu": Cá Heo không cười vì lúc nào cũng vui, mà do cấu tạo xương hàm dưới uốn cong cố định từ khi mới chào đời!
- Phân tích Bảng Chỉ Số Sinh Tồn RPG của Cá Heo: Siêu Trí Tuệ BRAIN IQ 99/100 (biết tự soi gương tạo dáng), Ra-đa Siêu Âm SONAR 100/100, Tốc Độ Ngư Lôi SPEED 95/100 (55 km/h, nhảy cao 6m), và Độ Ham Chơi Tinh Quái PLAYFULNESS 999 điểm!
- Giải phẫu Kính X-Quang Sinh Học (Khối mỡ thấu kính Melon trên trán): Phát 1.000 tiếng click siêu âm mỗi giây nhìn xuyên qua lớp cát đáy biển.
- Tuyệt kỹ "Ngủ mở một mắt": Tắt đèn đi ngủ luân phiên từng nửa bộ não để vừa nghỉ ngơi vừa canh chừng cá mập và tự động ngoi lên mặt nước thở suốt 8 tiếng!
- Văn hóa đặt tên riêng bằng giai điệu huýt sáo độc nhất vô nhị và tuyệt chiêu đeo bọt biển mềm lên mũi làm găng tay bảo hộ ở vịnh Shark Bay (Úc).
- Trò chơi Bóng Chuyền Cá Nóc lầy lội của những chú cá heo thiếu niên và chiến thuật Vòng Vây Lưới Bùn (Mud-ring feeding) đón cá nhảy trên không trung!
- Tại sao hung thần Cá Mập Trắng cũng phải sợ biệt đội Cá Heo (Cú húc ngư lôi xương cứng Rostrum) và câu chuyện huyền thoại về chú cá heo hoa tiêu Pelorus Jack suốt 24 năm dẫn đường tàu biển ở New Zealand!

⏱️ MỤC LỤC PHÂN CẢNH (CHAPTERS / TIMESTAMPS):
{chapters_block}

🎬 Xem lại các tập trước của Vẽ Chuyện Hoang Dã:
👉 Tập 1 — Lửng Mật: Kẻ Chí Phèo Không Biết Sợ Ai: https://youtu.be/WRAp223qZ60
👉 Tập 2 — Giải Mã Rái Cá Biển: Túi Doraemon & 3 Bí Mật Điên Rồ: https://youtu.be/DOPcbU7gvjs

👉 Đừng quên bấm LIKE, CHIA SẺ và ĐĂNG KÝ KÊNH (Subscribe) "Vẽ Chuyện Hoang Dã" để đón xem Tập 4: Thú Mỏ Vịt — Sinh Vật Kỳ Quặc Nhất Hành Tinh!
💬 Câu hỏi giao lưu: Bạn thích nhất siêu năng lực nào của Cá Heo: Ngủ mở một mắt, Kính X-quang siêu âm hay màn đánh bóng chuyền bằng Cá Nóc? Hãy bình luận bên dưới nhé!

#CaHeo #Dolphin #TheGioiDongVat #VeChuyenHoangDa #KienThucDongVat #WhiteboardAnimation #HoathinhVeTay #KhamPhaDaiDuong #SinhTonHoangDa #DongVatThongMinh"""

    description_en = f"""Decode the Bottlenose Dolphin (Delphinidae) — the ocean genius with the second-largest brain-to-body ratio on Earth, famous in cartoons and children's drawing books for its permanent friendly smile! In Episode 3 of Wild Tales Sketch (Vẽ Chuyện Hoang Dã - Hand-Drawn Whiteboard Animation), we bring science and art together to sketch the astonishing biological superpowers and hilarious underwater games of dolphins!

🔥 What you'll discover in this hand-drawn whiteboard animation episode:
- The art & anatomy secret behind the dolphin's "permanent cartoon smile": how a fixed curved lower jawbone keeps them smiling even when asleep!
- Dolphin RPG Survival Stats: Brain IQ 99/100 (mirror self-recognition), Bio-Sonar 100/100, Torpedo Speed 95/100 (55 km/h & 6m leaps), and Playfulness 999/100!
- Inside the biological X-ray lens (the Melon forehead organ): firing 1,000 echolocation clicks per second to spot fish buried deep under sand.
- Half-Brain Sleep superpower: sleeping with one brain hemisphere and one eye closed while the other half stays awake watching for sharks and surfacing to breathe!
- Unique signature whistle names and wearing sea sponges as protective nose gloves in Shark Bay, Australia.
- Teenage dolphins playing underwater volleyball with a puffed-up pufferfish, plus the genius Mud-Ring net fishing tactic!
- Why Great White Sharks flee from dolphin pods (the bony Rostrum torpedo bump) and the true story of Pelorus Jack, the legendary dolphin ship guide protected by New Zealand law!

⏱️ CHAPTERS / TIMESTAMPS:
{chapters_en_block}

🎬 Watch previous episodes of Wild Tales Sketch (Vẽ Chuyện Hoang Dã):
👉 Episode 1 — Honey Badger (Fearless 12kg Tank): https://youtu.be/WRAp223qZ60
👉 Episode 2 — Sea Otter Secrets (1 Million Hairs & Doraemon Pouch): https://youtu.be/DOPcbU7gvjs

#Dolphin #CaHeo #WildTalesSketch #VeChuyenHoangDa #WhiteboardAnimation #AnimalFacts #OceanAnimals #HandDrawnAnimation #Edutainment #DrawingAnimals"""

    candidate_tags = [
        "cá heo",
        "giải mã cá heo",
        "sự thật về cá heo",
        "cá heo chơi bóng chuyền cá nóc",
        "cá heo và cá mập",
        "cá heo thông minh",
        "bí mật điên rồ cá heo",
        "dolphin",
        "vẽ chuyện hoang dã",
        "vẽ chuyện hoang dã tập 3",
        "thế giới động vật",
        "kiến thức động vật",
        "bí ẩn đại dương",
        "whiteboard animation",
        "hoạt hình vẽ tay",
        "vẽ cá heo",
        "rái cá biển",
        "lửng mật",
    ]
    for s in live_suggestions:
        if s not in candidate_tags:
            candidate_tags.append(s)

    tags_list = []
    cur_len = 0
    for t in candidate_tags:
        add_len = len(t) + (1 if tags_list else 0)
        if cur_len + add_len <= 460 and len(tags_list) < 20:
            tags_list.append(t)
            cur_len += add_len

    tags_csv = ", ".join(tags_list)
    seo_audit = score_youtube_seo_opentube(title, description, tags_list)

    package = {
        "episode": "Tập 03 - Cá Heo (Dolphin)",
        "title": title,
        "title_en": title_en,
        "description": description,
        "description_en": description_en,
        "tags_list": tags_list,
        "tags_csv": tags_csv,
        "chapters": chapters,
        "chapters_en": chapters_en,
        "live_autocomplete_harvest": live_harvest,
        "seo_audit": seo_audit,
        "video_file": str((renders_dir / "tap03_ca_heo_complete_with_intro_outro.mp4").resolve()),
        "shorts_file": str((renders_dir / "tap03_ca_heo_shorts.mp4").resolve()),
        "thumbnail_file": str((renders_dir / "tap03_ca_heo_thumbnail_gemini.jpg").resolve()),
    }

    out_json = PROJ / "specs" / "youtube_seo_package_tap03.json"
    out_json.write_text(json.dumps(package, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SEO ENGINE EP03] Saved Bilingual SEO package to {out_json}")
    print(f"[SEO ENGINE EP03] VI Title ({len(title)} chars): {title}")
    print(f"[SEO ENGINE EP03] EN Title ({len(title_en)} chars): {title_en}")
    print(f"[SEO ENGINE EP03] OpenTube SEO Score: {seo_audit['score']}/100 ({seo_audit['grade']})")
    print(f"[SEO ENGINE EP03] Tags ({len(tags_list)} tags, {cur_len}/500 chars)")
    return package


if __name__ == "__main__":
    build_tap03_seo_package()
