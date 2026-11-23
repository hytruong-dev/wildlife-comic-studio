import json
import argparse
from datetime import datetime
from pathlib import Path

MEMORY_DIR = Path(".agent_memory")
SKILLS_LEARNED_DIR = Path(".agents/skills/learned")

TASTE_FILE = MEMORY_DIR / "director_taste.md"
LESSONS_FILE = MEMORY_DIR / "lessons_learned.md"
METAPHOR_FILE = MEMORY_DIR / "visual_metaphor_dictionary.json"
LOG_FILE = MEMORY_DIR / "production_log.md"

def init_memory():
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    SKILLS_LEARNED_DIR.mkdir(parents=True, exist_ok=True)

    if not TASTE_FILE.exists():
        TASTE_FILE.write_text(
            "# HỒ SƠ GU ĐẠO DIỄN & THẨM MỸ (DIRECTOR TASTE PROFILE)\n"
            "> File này được cập nhật tự động sau mỗi lần chủ dự án góp ý. Mọi video mới PHẢI tuân thủ các quy tắc dưới đây.\n\n"
            "## 1. Nhịp độ & Tốc độ Bàn tay (Pacing & Hand Speed)\n"
            "- [TASTE-01] Bàn tay đặt bút vẽ sớm hơn 150ms trước từ khóa chính (`triggerWord`).\n"
            "- [TASTE-02] Tỷ lệ đi nét mực đen `inkRatio` = 0.72, tô màu `hachure` = 0.28.\n"
            "- [TASTE-03] Không bao giờ để bàn tay đứng yên trên màn hình quá 800ms; nếu khoảng nghỉ dài hơn, phải hạ bàn tay ra khỏi khung hình dưới.\n\n"
            "## 2. Quy tắc Bố cục & Chữ viết (Layout & Typography)\n"
            "- [TASTE-04] Mỗi nhãn chữ viết tay tối đa 5 từ, ưu tiên sơ đồ mũi tên nối.\n"
            "- [TASTE-05] Giữ lại các hình vẽ cũ trên cùng một mặt giấy tối đa 25 giây để tạo sơ đồ tổng thể trước khi chuyển trang mới.\n",
            encoding="utf-8"
        )
    if not LESSONS_FILE.exists():
        LESSONS_FILE.write_text(
            "# SỔ TAY KINH NGHIỆM KỸ THUẬT (VERIFIED LESSONS LEARNED)\n"
            "> AI trên máy mới đọc file này để áp dụng ngay giải pháp chuẩn, tuyệt đối không thử lại các hướng đã thất bại.\n\n",
            encoding="utf-8"
        )
    if not METAPHOR_FILE.exists():
        METAPHOR_FILE.write_text(
            json.dumps({"version": "1.0.0", "metaphors": {}}, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
    if not LOG_FILE.exists():
        LOG_FILE.write_text(
            "# NHẬT KÝ SẢN XUẤT & TIẾN HÓA (PRODUCTION LOG)\n"
            "> Nhật ký theo dõi các video đã sản xuất và bài học đúc kết.\n\n",
            encoding="utf-8"
        )

def show_status():
    init_memory()
    taste_lines = [l for l in TASTE_FILE.read_text(encoding="utf-8").splitlines() if l.strip().startswith("- [")]
    lesson_lines = [l for l in LESSONS_FILE.read_text(encoding="utf-8").splitlines() if l.strip().startswith("### [")]
    metaphors = json.loads(METAPHOR_FILE.read_text(encoding="utf-8")).get("metaphors", {})
    learned_skills = [p.name for p in SKILLS_LEARNED_DIR.iterdir() if p.is_dir()]

    print("============================================================")
    print("🧠 TRẠNG THÁI BỘ NHỚ DỰ ÁN (PORTABLE MEMORY BANK STATUS)")
    print("============================================================")
    print(f"  • Quy tắc Gu Đạo diễn (director_taste.md)     : {len(taste_lines)} quy tắc")
    print(f"  • Bài học Kỹ thuật (lessons_learned.md)       : {len(lesson_lines)} bài học")
    print(f"  • Từ điển Ẩn dụ Hình ảnh (metaphors.json)     : {len(metaphors)} khái niệm")
    print(f"  • Kỹ năng Bố cục Đã học (skills/learned/)     : {len(learned_skills)} kỹ năng {learned_skills}")
    print("============================================================")

def add_taste_rule(rule_id: str, content: str):
    init_memory()
    lines = TASTE_FILE.read_text(encoding="utf-8").splitlines()
    updated = False
    new_line = f"- [{rule_id}] {content}"
    for i, line in enumerate(lines):
        if line.strip().startswith(f"- [{rule_id}]"):
            lines[i] = new_line
            updated = True
            break
    if not updated:
        lines.append(new_line)
    # Giữ giới hạn dưới 150 dòng (Memory Compaction)
    if len(lines) > 150:
        header = lines[:5]
        body = lines[-140:]
        lines = header + body
    TASTE_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[MEMORY UPDATED] Đã ghi nhận quy tắc đạo diễn [{rule_id}] vào {TASTE_FILE}")

def add_metaphor(keyword: str, layout: str, primitives: list, colors: list, notes: str):
    init_memory()
    data = json.loads(METAPHOR_FILE.read_text(encoding="utf-8"))
    key = keyword.strip().lower()
    existing = data["metaphors"].get(key, {"approvedCount": 0})
    data["metaphors"][key] = {
        "approvedCount": existing.get("approvedCount", 0) + 1,
        "layoutPattern": layout,
        "primitives": primitives,
        "preferredColors": colors,
        "notes": notes,
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    METAPHOR_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[MEMORY UPDATED] Đã lưu ẩn dụ hình ảnh cho từ khóa '{key}' vào {METAPHOR_FILE}")

def add_lesson(lesson_id: str, symptom: str, dead_end: str, golden_path: str):
    init_memory()
    entry = (
        f"\n### [{lesson_id}] ({datetime.now().strftime('%Y-%m-%d')})\n"
        f"- **Symptom:** {symptom}\n"
        f"- **Ruled-out Dead-end:** {dead_end}\n"
        f"- **Verified Golden Path:** {golden_path}\n"
    )
    with open(LESSONS_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"[MEMORY UPDATED] Đã lưu bài học kỹ thuật [{lesson_id}] vào {LESSONS_FILE}")

def log_production(project_id: str, title: str, duration_s: float, notes: str):
    init_memory()
    entry = (
        f"\n### Video: {project_id} - \"{title}\" ({datetime.now().strftime('%Y-%m-%d %H:%M')})\n"
        f"- **Thời lượng:** {duration_s:.1f}s | **Độ phân giải:** 1920x1080 @ 30fps\n"
        f"- **Bài học rút ra:** {notes}\n"
    )
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"[MEMORY UPDATED] Đã ghi nhật ký sản xuất cho '{project_id}' vào {LOG_FILE}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quản trị Bộ nhớ Tự học Di động")
    parser.add_argument("--status", action="store_true", help="Xem trạng thái bộ nhớ hiện tại")
    parser.add_argument("--add-taste", nargs=2, metavar=("RULE_ID", "CONTENT"), help="Thêm/Cập nhật quy tắc thẩm mỹ")
    parser.add_argument("--add-lesson", nargs=4, metavar=("ID", "SYMPTOM", "DEAD_END", "GOLDEN_PATH"), help="Thêm bài học kỹ thuật")
    parser.add_argument("--add-metaphor", nargs=5, metavar=("KEYWORD", "LAYOUT", "PRIMITIVES_CSV", "COLORS_CSV", "NOTES"), help="Thêm ẩn dụ hình ảnh")
    parser.add_argument("--log-video", nargs=4, metavar=("PROJECT_ID", "TITLE", "DURATION_S", "NOTES"), help="Ghi nhật ký video hoàn thành")
    args = parser.parse_args()

    if args.status:
        show_status()
    elif args.add_taste:
        add_taste_rule(args.add_taste[0], args.add_taste[1])
    elif args.add_lesson:
        add_lesson(*args.add_lesson)
    elif args.add_metaphor:
        kw, layout, prims, cols, notes = args.add_metaphor
        add_metaphor(kw, layout, [x.strip() for x in prims.split(",")], [x.strip() for x in cols.split(",")], notes)
    elif args.log_video:
        log_production(args.log_video[0], args.log_video[1], float(args.log_video[2]), args.log_video[3])
    else:
        show_status()
