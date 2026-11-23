"""Batch upload script for Mega 03 and Episodes 31 to 40.
Sequentially calls `upload_youtube.cjs` for each planned item with exact TASTE-68 schedule dates.
Automatically checks for `upload_result.json` to skip already completed items,
and updates `publish_schedule.py` after each success.
"""
import sys
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

QUEUE = [
    {
        "slug": "mega-03-dai-hoi-sinh-ton",
        "title": "Mega 03 — Đại Hội Sinh Tồn (Tập 21-30)",
        "date": "2026-11-28", "time": "17:00",
        "shorts_date": "2026-11-29", "shorts_time": "11:30"
    },
    {
        "slug": "tap-31-chim-cat-lon",
        "title": "Tập 31 — Chim Cắt Lớn",
        "date": "2026-11-29", "time": "17:00",
        "shorts_date": "2026-11-30", "shorts_time": "11:30"
    },
    {
        "slug": "tap-32-chuot-chui-trui",
        "title": "Tập 32 — Chuột Chũi Trũi",
        "date": "2026-11-30", "time": "17:00",
        "shorts_date": "2026-12-01", "shorts_time": "11:30"
    },
    {
        "slug": "tap-33-ech-go-bac-cuc",
        "title": "Tập 33 — Ếch Gỗ Bắc Cực",
        "date": "2026-12-01", "time": "17:00",
        "shorts_date": "2026-12-02", "shorts_time": "11:30"
    },
    {
        "slug": "tap-34-qua-den",
        "title": "Tập 34 — Quạ Đen",
        "date": "2026-12-02", "time": "17:00",
        "shorts_date": "2026-12-03", "shorts_time": "11:30"
    },
    {
        "slug": "tap-35-ca-voi-sat-thu",
        "title": "Tập 35 — Cá Voi Sát Thủ",
        "date": "2026-12-03", "time": "17:00",
        "shorts_date": "2026-12-04", "shorts_time": "11:30"
    },
    {
        "slug": "tap-36-chim-go-kien",
        "title": "Tập 36 — Chim Gõ Kiến",
        "date": "2026-12-04", "time": "17:00",
        "shorts_date": "2026-12-05", "shorts_time": "11:30"
    },
    {
        "slug": "tap-37-lac-da-sa-mac",
        "title": "Tập 37 — Lạc Đà Sa Mạc",
        "date": "2026-12-05", "time": "17:00",
        "shorts_date": "2026-12-06", "shorts_time": "11:30"
    },
    {
        "slug": "tap-38-de-nui-bac-my",
        "title": "Tập 38 — Dê Núi Bắc Mỹ",
        "date": "2026-12-06", "time": "17:00",
        "shorts_date": "2026-12-07", "shorts_time": "11:30"
    },
    {
        "slug": "tap-39-chim-bach-thanh",
        "title": "Tập 39 — Chim Bách Thanh",
        "date": "2026-12-07", "time": "17:00",
        "shorts_date": "2026-12-08", "shorts_time": "11:30"
    },
    {
        "slug": "tap-40-kien-cat-la",
        "title": "Tập 40 — Kiến Cắt Lá",
        "date": "2026-12-08", "time": "17:00",
        "shorts_date": "2026-12-09", "shorts_time": "11:30"
    },
]

def main():
    print(f"=== BẮT ĐẦU TIẾN TRÌNH UPLOAD & LÊN LỊCH ({len(QUEUE)} MỤC) ===")
    
    for idx, item in enumerate(QUEUE, 1):
        slug = item["slug"]
        title = item["title"]
        p_dir = ROOT / "projects" / slug
        res_file = p_dir / "upload_result.json"
        
        print(f"\n[{idx}/{len(QUEUE)}] {title} ({slug})")
        
        if res_file.exists():
            print(f"  -> Đã tải lên trước đó (upload_result.json tồn tại). Bỏ qua.")
            continue
            
        cmd = [
            "node", "src/episode/upload_youtube.cjs",
            f"projects/{slug}",
            "--date", item["date"],
            "--time", item["time"],
            "--shorts-date", item["shorts_date"],
            "--shorts-time", item["shorts_time"]
        ]
        
        print(f"  [LỆNH] {' '.join(cmd)}")
        res = subprocess.run(cmd, cwd=str(ROOT))
        
        if res.returncode != 0:
            print(f"  !! [LỖI] Upload thất bại cho {slug} (exit code {res.returncode}). Tạm dừng quy trình.")
            sys.exit(res.returncode)
            
        print(f"  [THÀNH CÔNG] Đã tải lên và lên lịch cho {slug}")
        
        # Cập nhật lại lịch đăng tổng thể sau mỗi video thành công
        subprocess.run(["python", "src/episode/publish_schedule.py"], cwd=str(ROOT))
        
        # Nghỉ nhẹ giữa các tập để tránh rate limit
        time.sleep(10)
        
    print("\n=== HOÀN TẤT TOÀN BỘ TIẾN TRÌNH UPLOAD & LÊN LỊCH! ===")

if __name__ == "__main__":
    main()
