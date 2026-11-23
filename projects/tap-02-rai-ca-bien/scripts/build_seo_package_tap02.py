"""
Generate 100/100 YouTube SEO Package for Episode 2: Rái Cá Biển (`tap-02-rai-ca-bien`)
Uses `src/seo/youtube_seo_engine.py` (Open-Tube-SEO + youtube-suggest-scraper + AI-YouTube-Timestamps)
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


def build_tap02_seo_package() -> dict:
    renders_dir = PROJ / "renders"
    intro_mp4 = ROOT / "assets" / "branding" / "intro_ve_chuyen_hoang_da.mp4"

    scene_defs = [
        ("scene01_final.mp4", "Phần 1: Cú Lừa Đáng Yêu Nhất Đại Dương — Sự Thật Rái Cá Biển Nắm Tay Nhau"),
        ("scene02_final.mp4", "Phần 2: Bảng Chỉ Số Sinh Tồn RPG — Độ Đáng Yêu 100 & Độ Lầy Lội 999 Điểm!"),
        ("scene03_final.mp4", "Phần 3: Giải Phẫu Kỳ Dị — Áo Phao 1 Triệu Sợi Lông & Túi Thần Kỳ Doraemon"),
        ("scene04_final.mp4", "Phần 4: Cú Bẻ Lái Sinh Tồn — Mánh Khóe Bắt Giữ Con Tin Đòi Chuộc Bào Ngư"),
        ("scene05_final.mp4", "Phần 5: Vệ Binh Rừng Tảo Bẹ & Huyền Thoại Hải Tặc Cướp Ván Lướt Sóng 841"),
        ("scene06_final.mp4", "Phần 6: Bài Học Đại Dương & Bật Mí Tập 3: Bộ Mặt Thật Của Cá Heo"),
    ]

    intro_dur = probe_duration_sec(intro_mp4) if intro_mp4.exists() else 8.0
    cur_sec = 0.0
    chapters = ["00:00 Mở đầu: Cú Lừa Đáng Yêu Nhất Đại Dương — Rái Cá Biển"]
    cur_sec += intro_dur

    for fname, ch_title in scene_defs:
        p = renders_dir / fname
        dur = probe_duration_sec(p) if p.exists() else 85.0
        chapters.append(f"{format_mm_ss(cur_sec)} {ch_title}")
        cur_sec += dur

    chapters_block = "\n".join(chapters)

    seed_queries = [
        "rái cá biển",
        "sự thật về rái cá biển",
        "rái cá biển nắm tay",
        "rái cá biển đập vỏ sò",
        "vẽ chuyện hoang dã",
        "thế giới động vật",
    ]
    live_harvest = harvest_youtube_autocomplete_keywords(seed_queries, expand_depth=2)
    live_suggestions = live_harvest.get("suggestions", [])

    # Title length between 40-70 chars with number, colon/exclamation, and power word ("bí mật"/"giải mã"/"kỷ lục")
    title = "Giải Mã Rái Cá Biển: Túi Doraemon & 3 Bí Mật Điên Rồ! | Tập 2"

    description = f"""Giải mã Rái Cá Biển (Sea Otter - Enhydra lutris) — sinh vật giữ kỷ lục bộ lông dày nhất hành tinh và luôn làm tan chảy hàng triệu trái tim nhờ vẻ ngoài tròn xoe như thú nhồi bông cùng thói quen nắm chặt tay nhau khi ngủ trên mặt sóng. Thế nhưng trong Tập 2 của series Vẽ Chuyện Hoang Dã (Thế Giới Động Vật Whiteboard Animation), chúng ta sẽ khám phá những bí mật sinh học điên rồ và những mánh khóe lầy lội bậc nhất đại dương của loài thú biển thuộc gia tộc họ Chồn (anh em họ hàng ruột thịt với Lửng Mật)!

🔥 Những bí mật đỉnh cao về Rái Cá Biển được giải mã bằng nét vẽ Whiteboard trong video:
- Sự thật đằng sau hành động Rái Cá Biển nắm tay nhau và tự quấn vào rong biển tảo bẹ khi ngủ: Hoàn toàn không phải ngôn tình lãng mạn mà là dây neo sinh tồn chống trôi vào hàm Cá Voi Sát Thủ!
- Phân tích Bảng Chỉ Số Sinh Tồn RPG của Rái Cá Biển: Ngụy Trang Đáng Yêu CUTENESS 100/100, Giáp Lông FUR ARMOR 95/100, Trí Tuệ Công Cụ IQ 92/100, và Độ Lầy Lội TRICKERY 999 điểm!
- Kỷ lục Thế giới Guinness: Bộ lông dày đặc nhất hành tinh với 1.000.000 sợi lông trên mỗi inch vuông (160.000 sợi/cm²) khóa chặt bọt khí ấm giữa biển băng 0°C mà không cần một giọt mỡ dưới da.
- Chiếc túi thần kỳ Doraemon dưới hai nách: Nơi Rái Cá Biển cất giấu viên đá búa gia truyền suốt nhiều năm để đập vỡ vỏ trai, vỏ bào ngư cứng như bê tông với tốc độ 45 nhát búa trong 15 giây!
- Mánh khóe dở khóc dở cười: Vì phải ăn lượng hải sản bằng 25-30% trọng lượng cơ thể mỗi ngày, những gã rái cá đực lười biếng chuyên ôm giữ rái cá con đang nổi như phao trên mặt nước để ép rái cá mẹ phải nộp cua và bào ngư làm tiền chuộc!
- Vệ binh bảo vệ rừng Tảo Bẹ trước đội quân Nhím Biển Tím (ăn nhiều đến mức xương và răng chuyển sang màu tím!) và phi vụ cướp ván lướt sóng có 1-0-2 của cô Rái Cá số hiệu 841 tại Santa Cruz!

⏱️ MỤC LỤC PHÂN CẢNH (CHAPTERS / TIMESTAMPS):
{chapters_block}

🎬 Xem lại Tập 1 — Lửng Mật: Kẻ Chí Phèo Không Biết Sợ Ai (FEAR = 0):
👉 https://youtu.be/WRAp223qZ60

👉 Đừng quên bấm LIKE, CHIA SẺ và ĐĂNG KÝ KÊNH (Subscribe) "Vẽ Chuyện Hoang Dã" để đón xem Tập 3: Bộ Mặt Thật Của Cá Heo — Băng Đảng Giang Hồ Chơi Bóng Chuyền Bằng Cá Nóc!
💬 Câu hỏi thảo luận: Theo bạn, chiếc túi nách Doraemon hay màn cướp ván lướt sóng của Rái Cá 841 thú vị hơn? Hãy bình luận (comment) ngay bên dưới nhé!

#RaiCaBien #SeaOtter #TheGioiDongVat #VeChuyenHoangDa #KienThucDongVat #SinhTonHoangDa #WhiteboardAnimation #DongVatHoangDa #KhamPhaThienNhien #LungMat"""

    candidate_tags = [
        "rái cá biển",
        "giải mã rái cá biển",
        "sự thật về rái cá biển",
        "rái cá biển nắm tay nhau khi ngủ",
        "rái cá biển đập vỏ sò",
        "rái cá biển túi doraemon",
        "bí mật điên rồ rái cá biển",
        "rái cá 841 cướp ván lướt sóng",
        "sea otter",
        "vẽ chuyện hoang dã",
        "vẽ chuyện hoang dã tập 2",
        "thế giới động vật",
        "kiến thức động vật",
        "bí ẩn động vật",
        "whiteboard animation tiếng việt",
        "hoạt hình vẽ tay",
        "lửng mật",
        "động vật biển thông minh",
    ]
    for s in live_suggestions:
        if s not in candidate_tags:
            candidate_tags.append(s)

    tags_list = []
    cur_len = 0
    for t in candidate_tags:
        add_len = len(t) + (1 if tags_list else 0)
        if cur_len + add_len <= 475 and len(tags_list) < 22:
            tags_list.append(t)
            cur_len += add_len

    tags_csv = ", ".join(tags_list)
    seo_audit = score_youtube_seo_opentube(title, description, tags_list)

    package = {
        "episode": "Tập 02 - Rái Cá Biển (Sea Otter)",
        "title": title,
        "description": description,
        "tags_list": tags_list,
        "tags_csv": tags_csv,
        "chapters": chapters,
        "live_autocomplete_harvest": live_harvest,
        "seo_audit": seo_audit,
        "video_file": str((renders_dir / "tap02_rai_ca_bien_complete_with_intro_outro.mp4").resolve()),
        "shorts_file": str((renders_dir / "tap02_rai_ca_bien_shorts.mp4").resolve()),
        "thumbnail_file": str((renders_dir / "tap02_rai_ca_bien_thumbnail.png").resolve()),
    }

    out_json = PROJ / "specs" / "youtube_seo_package_tap02.json"
    out_json.write_text(json.dumps(package, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SEO ENGINE EP02] Saved SEO package to {out_json}")
    print(f"[SEO ENGINE EP02] Title ({len(title)} chars): {title}")
    print(f"[SEO ENGINE EP02] OpenTube SEO Score: {seo_audit['score']}/100 ({seo_audit['grade']})")
    print(f"[SEO ENGINE EP02] Tags ({len(tags_list)} tags, {cur_len}/500 chars)")
    return package


if __name__ == "__main__":
    build_tap02_seo_package()
