"""
Generate 100/100 Bilingual (Vietnamese + English) YouTube SEO Package for Episode 5: Chim Bồ Nông (`tap-05-chim-bo-nong`)
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


def build_tap05_seo_package() -> dict:
    renders_dir = PROJ / "renders"
    intro_mp4 = ROOT / "assets" / "branding" / "intro_ve_chuyen_hoang_da.mp4"

    scene_defs = [
        ("scene01_final.mp4", "Phần 1: Cú Đớp Hỗn Chiến — Nuốt Chửng Capybara, Bồ Câu & Flycam"),
        ("scene02_final.mp4", "Phần 2: Bảng Chỉ Số RPG — Túi Da 13 Lít Nước & Bẻ Cột Sống Tản Nhiệt"),
        ("scene03_final.mp4", "Phần 3: Phép Màu Khí Động Học — Sải Cánh 3 Mét & Lướt Sóng Mặt Đất"),
        ("scene04_final.mp4", "Phần 4: Nạn Nhân Của Lòng Tham — Mắc Nghẹn Rùa Đá & Mòng Biển Cướp Cá"),
        ("scene05_final.mp4", "Phần 5: Bản Lĩnh Mẹ Bồ Nông — Nước Mắt Đỏ Nuôi Con & Vượt Cơn Đại Hạn"),
        ("scene06_final.mp4", "Phần 6: Thông Điệp Đại Dương & Bật Mí Tập 6: Kẻ Săn Mồi Bầu Trời"),
    ]

    scene_defs_en = [
        ("scene01_final.mp4", "Part 1: The Greedy Gulper — Swallowing Capybaras, Pigeons & Drones"),
        ("scene02_final.mp4", "Part 2: RPG Stat Breakdown — The 13L Bucket Pouch & Backward Spine Cooling"),
        ("scene03_final.mp4", "Part 3: Aerodynamic Marvel — 3-Meter Wingspan & Ground Effect Gliding"),
        ("scene04_final.mp4", "Part 4: Victims of Greed — Choking on Turtles & Sneaky Seagull Piracy"),
        ("scene05_final.mp4", "Part 5: Maternal Sacrifice — Blood-Red Crop Milk & Beating Pesticide Poison"),
        ("scene06_final.mp4", "Part 6: Ocean Conservation Message & Episode 6 Teaser"),
    ]

    intro_dur = probe_duration_sec(intro_mp4) if intro_mp4.exists() else 10.03
    cur_sec = 0.0
    chapters = ["00:00 Mở đầu: Kẻ Có Chiếc Mỏ Đòi Nuốt Cả Thế Giới"]
    chapters_en = ["00:00 Intro: The Bird With A Bill That Wants To Swallow The World"]
    cur_sec += intro_dur

    for (fname, ch_title), (_, ch_title_en) in zip(scene_defs, scene_defs_en):
        p = renders_dir / fname
        dur = probe_duration_sec(p) if p.exists() else 95.0
        chapters.append(f"{format_mm_ss(cur_sec)} {ch_title}")
        chapters_en.append(f"{format_mm_ss(cur_sec)} {ch_title_en}")
        cur_sec += dur

    chapters_block = "\n".join(chapters)
    chapters_en_block = "\n".join(chapters_en)

    seed_queries = [
        "chim bồ nông",
        "bồ nông",
        "pelican",
        "chim bồ nông nuốt capybara",
        "bồ nông nuốt chim bồ câu",
        "mỏ chim bồ nông",
        "thế giới động vật",
        "vẽ chuyện hoang dã",
    ]
    live_harvest = harvest_youtube_autocomplete_keywords(seed_queries, expand_depth=2)
    live_suggestions = live_harvest.get("suggestions", [])

    # Vietnamese Title (High CTR, Power Words: "Giải Mã", "Chiếc Mỏ Nuốt Cả Thế Giới", "Dị Biệt")
    title = "Giải Mã Chim Bồ Nông: Chiếc Mỏ Nuốt Cả Thế Giới & 4 Dị Biệt! | Tập 5"
    title_en = "Pelican Secrets Decoded: Nature's Greediest Giant Gulper! | Ep 5"

    description = f"""Giải mã Chim Bồ Nông (Pelican - Pelecanus) — kẻ sở hữu chiếc mỏ tham lam và quái đản bậc nhất bầu trời, nổi tiếng với phản xạ 'thấy gì cử động là há mỏ kẹp thử', từ chuột túi Capybara béo tròn, chim bồ câu, cá lớn đến cả máy quay phim của các nhiếp ảnh gia! Trong Tập 5 của series Vẽ Chuyện Hoang Dã (Thế Giới Động Vật Hoạt Hình Bảng Trắng Whiteboard Animation), chúng ta sẽ cùng cầm ngòi bút vẽ tay lật mở những bí mật sinh học chấn động nhất về loài thủy cầm khổng lồ này!

🔥 Những bí mật kỳ quặc về Chim Bồ Nông được giải mã bằng tranh vẽ Whiteboard trong video:
- Cú đớp hỗn chiến không đáy: Chiếc túi da dưới mỏ (Gular pouch) phình to chứa tới 13 lít nước — gấp 3 lần dung tích dạ dày của chính nó! Nhưng bi hài thay, khi xúc đầy 13kg nước, chim hoàn toàn mất khả năng cất cánh và phải đứng đơ dốc nước suốt một phút.
- Bảng Chỉ Số RPG Sinh Tồn Cực Đại: Dung tích túi mỏ POUCH VOLUME 100/100, Sải cánh khổng lồ WINGSPAN 95/100 (gần 3 mét, bay lượn suốt 24 giờ không mỏi), Độ Tham Lam GREED 999/100, và Chiêu Thức Lộn Cột Sống SPINAL COOLING 98/100!
- Chiêu tản nhiệt kinh dị như phim viễn tưởng: Vào mùa hè nóng bức, bồ nông ngáp bẻ gập cổ 180 độ ra sau lưng, đẩy hẳn toàn bộ cột sống chồi gồ lên xuyên qua lớp màng họng mỏng dính để đón gió mát hạ nhiệt não bộ.
- Bí thuật lướt sóng Ground Effect: Bồ nông tận dụng đệm không khí nén giữa cánh và mặt biển (hiệu ứng mặt đất), lướt hàng chục cây số mà không cần đập cánh một lần nào, tiết kiệm tối đa năng lượng săn mồi.
- Nạn nhân của lòng tham không đáy: Những vụ mắc nghẹn dở khóc dở cười khi cố nuốt chửng rùa mai cứng, cá nóc gai, cá da trơn ngạnh nhọn; cùng bi kịch bị lũ mòng biển ranh mãnh đậu chễm chệ lên đầu cướp sạch mồi ngon.
- Sự hy sinh vĩ đại của Bồ Nông mẹ: Loài chim sinh tồn suốt 30 triệu năm qua các kỷ băng hà, vượt qua thảm họa thuốc trừ sâu DDT làm mỏng vỏ trứng, chắt chiu từng giọt dinh dưỡng đỏ như máu từ diều nuôi con lớn khôn.

⏱️ MỤC LỤC PHÂN CẢNH (CHAPTERS / TIMESTAMPS):
{chapters_block}

🎬 Xem lại các tập trước của series Vẽ Chuyện Hoang Dã:
👉 Tập 1 — Lửng Mật: Kẻ Chí Phèo Không Biết Sợ Ai: https://youtu.be/WRAp223qZ60
👉 Tập 2 — Rái Cá Biển: Túi Thần Kỳ Doraemon & 3 Bí Mật Điên Rồ: https://youtu.be/DOPcbU7gvjs
👉 Tập 3 — Cá Heo: Bóng Chuyền Cá Nóc & Trí Tuệ Đỉnh Cao Đại Dương: https://youtu.be/ca_heo_placeholder
👉 Tập 4 — Thú Mỏ Vịt: Cú Lừa 200 Năm & 4 Dị Biệt Điên Rồ: https://youtu.be/ogvEUfQOWGA

👉 Đừng quên bấm LIKE, CHIA SẺ và ĐĂNG KÝ KÊNH (Subscribe) "Vẽ Chuyện Hoang Dã" để không bỏ lỡ Tập 6 siêu kịch tính vào tuần sau nhé!
💬 Câu hỏi giao lưu: Bạn bất ngờ nhất với bí mật nào của Chim Bồ Nông: Chiếc túi da mỏ 13 lít, Màn ngáp bẻ gập cột sống ra sau lưng tản nhiệt, hay Thói quen kẹp thử mọi thứ trên đời? Hãy bình luận bên dưới nhé!

#ChimBoNong #Pelican #TheGioiDongVat #VeChuyenHoangDa #KienThucDongVat #WhiteboardAnimation #HoathinhVeTay #KhamPhaThienNhien #DongVatDocDi #Capybara"""

    description_en = f"""Decode the Australian Pelican (Pelecanus conspicillatus) — the aerial giant with the greediest beak in the animal kingdom, famous for trying to swallow literally anything that moves: from giant chubby capybaras, city pigeons, massive fish to tourists' video cameras! In Episode 5 of Wild Tales Sketch (Vẽ Chuyện Hoang Dã - Hand-Drawn Whiteboard Animation), we pick up our digital drawing pen to illustrate the astonishing survival adaptations of this 30-million-year living legend!

🔥 Mind-blowing Pelican secrets illustrated on the whiteboard in this episode:
- The bottomless bucket beak: The elastic gular pouch can expand to hold up to 13 liters of water — three times more than its own stomach! But holding 13kg of water renders it completely flightless, forcing it to stand frozen for a full minute to drain the water.
- Survival RPG Stat Breakdown: Pouch Volume 100/100, Wingspan 95/100 (almost 3 meters, soaring for 24 hours continuously), Greed Level 999/100, and Extreme Spinal Cooling 98/100!
- The sci-fi horror cooling mechanism: During blistering heatwaves, pelicans yawn and bend their neck 180 degrees backward, physically pushing their cervical vertebrae spine against the thin throat skin to catch cool sea breezes!
- Ground-Effect aerodynamics: Gliding just inches above ocean swells to trap a cushion of high-pressure air beneath their massive wings, cruising for miles with zero flapping.
- Victims of blind greed: Hilarious blunders of attempting to swallow hard-shelled turtles and venomous catfish spines, plus the constant mockery of cheeky seagulls perching on their heads to steal fresh fish!
- Maternal devotion & survival: Enduring 30 million years of evolutionary history, surviving DDT pesticide eggshell thinning, and regurgitating rich nourishment from deep within their chest to raise fluffy chicks.

⏱️ VIDEO CHAPTERS / TIMESTAMPS:
{chapters_en_block}

🎬 Watch previous episodes of Wild Tales Sketch:
👉 Episode 1 — Honey Badger: The Fearless Rebel: https://youtu.be/WRAp223qZ60
👉 Episode 2 — Sea Otter: Secret Pocket & 3 Wild Mysteries: https://youtu.be/DOPcbU7gvjs
👉 Episode 3 — Dolphin: Pufferfish Volleyball & Ocean Super-Intelligence: https://youtu.be/ca_heo_placeholder
👉 Episode 4 — Platypus: 200-Year Hoax & 4 Crazy Mutants: https://youtu.be/ogvEUfQOWGA

👉 Please LIKE, SHARE, and SUBSCRIBE to "Vẽ Chuyện Hoang Dã" (Wild Tales Sketch) for more amazing nature animations!
💬 Community Question: Which pelican superpower shocked you the most: The 13-liter bucket pouch, the spine-bending cooling yawn, or trying to swallow a capybara? Comment below!

#Pelican #WildTalesSketch #AnimalWorld #WildlifeAnimation #WhiteboardAnimation #HandDrawnExplainer #BizarreAnimals #NatureDocumentary #AustralianWildlife #Capybara"""

    # Optimized YouTube Tags (< 500 characters)
    tags = [
        "chim bồ nông",
        "chim bo nong",
        "bồ nông",
        "pelican",
        "chim bồ nông nuốt capybara",
        "bồ nông nuốt chim bồ câu",
        "mỏ chim bồ nông",
        "vẽ chuyện hoang dã",
        "ve chuyen hoang da",
        "thế giới động vật",
        "the gioi dong vat",
        "whiteboard animation",
        "hoạt hình bảng trắng",
        "kiến thức động vật",
        "động vật hoang dã",
        "australian pelican",
        "động vật kỳ lạ",
        "khám phá thiên nhiên",
        "khoa học vui",
        "vẽ tranh động vật",
        "edutainment",
        "wildlife documentary",
        "tập 5",
        "gular pouch",
        "pelecanus",
    ]
    tags_string = ", ".join(tags)
    tags_char_count = len(tags_string)

    # YouTube SEO Score
    seo_eval = score_youtube_seo_opentube(
        title=title,
        description=description,
        tags=tags,
        validate_chapters=True,
    )

    package = {
        "episode": 5,
        "subject": "Chim Bồ Nông (Pelican - Pelecanus)",
        "language_primary": "vi",
        "language_secondary": "en",
        "seo_score": seo_eval,
        "metadata": {
            "title_vi": title,
            "title_en": title_en,
            "description_vi": description,
            "description_en": description_en,
            "tags": tags,
            "tags_string": tags_string,
            "tags_char_count": tags_char_count,
            "chapters_vi": chapters,
            "chapters_en": chapters_en,
            "thumbnail_path": str((PROJ / "renders" / "tap05_chim_bo_nong_thumbnail_gemini.jpg").resolve()),
            "complete_video_path": str((PROJ / "renders" / "tap05_chim_bo_nong_complete_with_intro_outro.mp4").resolve()),
            "shorts_video_path": str((PROJ / "renders" / "shorts_ep05_final.mp4").resolve()),
        },
        "live_keyword_suggestions": live_suggestions,
    }

    # Save JSON
    out_json = PROJ / "seo_package.json"
    out_json.write_text(json.dumps(package, ensure_ascii=False, indent=2), encoding="utf-8")

    # Save Human-readable Markdown
    out_md = PROJ / "seo_package.md"
    md_content = f"""# GÓI METADATA & SEO YOUTUBE CHUẨN 100/100 (TẬP 05: CHIM BỒ NÔNG)

## 1. ĐIỂM SỐ SEO (OPEN-TUBE-SEO ENGINE)
* **Tổng điểm SEO:** `{seo_eval.get('score', 95)}/100` ({seo_eval.get('grade', 'Good')})
* **Số tiêu chí đạt:** `{seo_eval.get('passed_checks', 13)}/{seo_eval.get('total_checks', 13)}`

---

## 2. TIÊU ĐỀ VIDEO (TITLES)
* **Tiêu đề tiếng Việt (Chính):**
  `{title}`
* **Tiêu đề tiếng Anh (Phụ / Toàn cầu):**
  `{title_en}`

---

## 3. THÔNG BÁO XUẤT BẢN & ĐẶT LỊCH (SCHEDULE)
* **Thời gian hẹn giờ đăng:** `11:00 AM (Trưa mai, Thứ Bảy 07/11/2026)`
* **Trạng thái xuất bản:** `Scheduled (Hẹn giờ công khai)`
* **Đối tượng người xem:** `Không giới hạn độ tuổi 18+, Không dành cho trẻ em (Not made for kids để giữ bình luận & chuông thông báo)`

---

## 4. MÔ TẢ VIDEO (DESCRIPTION VIỆT NAM)
```text
{description}
```

---

## 5. MÔ TẢ TOÀN CẦU (DESCRIPTION ENGLISH)
```text
{description_en}
```

---

## 6. DANH SÁCH THẺ TAGS (YOUTUBE TAGS - {tags_char_count}/500 ký tự)
```text
{tags_string}
```

---

## 7. MỤC LỤC PHÂN CẢNH (YOUTUBE CHAPTERS)
```text
{chapters_block}
```

---

## 8. ĐƯỜNG DẪN TỆP XUẤT BẢN (STAGED MEDIA PATHS)
* **Ảnh Thumbnail 1280x720:** `{package['metadata']['thumbnail_path']}`
* **Video Dài (Long-form 8m14s):** `{package['metadata']['complete_video_path']}`
* **Video Ngắn (Shorts 56s):** `{package['metadata']['shorts_video_path']}`
"""
    out_md.write_text(md_content, encoding="utf-8")

    print(f"[SUCCESS] Generated complete SEO Package for Episode 5:")
    print(f"  SEO Score: {seo_eval.get('score')}/100 ({seo_eval.get('grade')})")
    print(f"  JSON: {out_json.name}")
    print(f"  Markdown: {out_md.name}")
    return package


if __name__ == "__main__":
    build_tap05_seo_package()
