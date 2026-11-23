import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT))
from src.pipeline.seo_master import build_episode_seo

AUDIO_DIR = PROJ / "audio"
RENDERS_DIR = PROJ / "renders"

def main():
    scene_files = [AUDIO_DIR / f"scene{i:02d}.wav" for i in range(1, 7)]
    intro_file = ROOT / "assets" / "branding" / "intro_ve_chuyen_hoang_da_10s.mp4"

    bullet_secrets = [
        "Sống sót qua cả 5 cuộc đại tuyệt chủng lịch sử của Trái Đất",
        "Chịu nhiệt độ cực đoan từ âm 272°C đến 150°C và áp suất gấp 6 lần đáy rãnh Ma-ri-a-na",
        "Kháng tia phóng xạ hạt nhân cực mạnh gấp 1.000 lần liều gây chết người",
        "Cơ chế Cryptobiosis biến nội tạng thành khối thủy tinh protein T-D-Ps ngủ đông 30 năm không cần nước",
        "Điểm yếu bi hài: Chết ngạt vì chất nhờn dính của ốc sên và dễ bị bọ ve, giun tròn nuốt chửng",
        "Sự cố rơi tàu vũ trụ Beresheet năm 2019 gieo rắc hàng ngàn gấu nước đang ngủ đông khắp Mặt Trăng"
    ]

    scene_titles = [
        "Kẻ Bất Tử Giữa Vũ Trụ (The Myth-Buster Hook)",
        "Bảng Chỉ Số RPG Lỗi Game (DEF 9999/100)",
        "Bí Thuật Thủy Tinh Hóa Cryptobiosis",
        "Điểm Yếu Bi Hài Của Tạo Hóa (Chất Nhầy Ốc Sên)",
        "Đoàn Quân Gấu Nước Đổ Bộ Lên Mặt Trăng",
        "Bài Học Sinh Tồn Vĩ Đại & Teaser Tập 7 (Tôm Tít)"
    ]

    scene_titles_en = [
        "The Immortal Cosmic Survivor (Myth-Buster Hook)",
        "RPG Broken Stats (DEF 9999/100)",
        "Cryptobiosis: Amorphous Glass Bio-Shield",
        "The Hilarious Weakness (Snail Slime Trap)",
        "The Moon Crash & Colony of Frozen Bears",
        "Evolutionary Wisdom & Episode 7 Teaser"
    ]

    tags_list = [
        "gấu nước", "gau nuoc", "tardigrade", "bọ gấu nước", "water bear",
        "sinh vật bất tử", "tuyệt chủng", "cryptobiosis", "vẽ chuyện hoang dã",
        "thế giới động vật", "the gioi dong vat", "whiteboard animation",
        "khoa học kì thú", "động vật độc dị", "sinh vật kỳ lạ", "vũ trụ",
        "mặt trăng", "beresheet", "protein tdps", "bức xạ hạt nhân",
        "rãnh mariana", "ốc sên", "edutainment việt nam", "hoạt hình bảng trắng"
    ]

    community_question = "Nếu bạn sở hữu siêu năng lực ngủ đông bất tử của Gấu Nước, bạn sẽ chọn thức dậy ở năm nào trong tương lai?"

    build_episode_seo(
        episode_num=6,
        subject_vi="Gấu Nước (Tardigrade)",
        subject_en="Tardigrade (Water Bear)",
        title_vi="Sinh Vật Bất Tử Duy Nhất Sống Sót Qua 5 Đại Tuyệt Chủng | Tập 6",
        title_en="The Only Immortal Creature That Survived 5 Mass Extinctions | Episode 6",
        scene_titles=scene_titles,
        scene_titles_en=scene_titles_en,
        scene_files=scene_files,
        intro_file=intro_file,
        bullet_secrets=bullet_secrets,
        community_question=community_question,
        tags_list=tags_list,
        output_dir=PROJ / "scripts"
    )

if __name__ == "__main__":
    main()
