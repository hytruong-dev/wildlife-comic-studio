"""Đo nhu cầu thật của người Việt cho danh sách con vật / chủ đề (chế độ miễn phí của TubeLab `video-ideation`).

  python src/seo/topic_demand.py "Cá Nóc Nhím" "Tê Tê" ...            # in bảng
  python src/seo/topic_demand.py --file ung_vien.txt --out docs/research/topic_demand_<ngày>.md

Mỗi chủ đề lấy:
- `sugg`  : số gợi ý autocomplete YouTube vi/VN có đúng tên (người Việt đang gõ tìm).
- `vids`  : số video dài (≥ 2 phút) trong 20 kết quả tìm có đúng tên trong tiêu đề, không phải phim/nhạc/game.
- `top`   : lượt xem cao nhất, `med`: trung vị lượt xem các video đó.
- `score` : log10(med) + log10(top)/2 + sugg/5 — so sánh tương đối giữa các ứng viên, KHÔNG phải dự báo lượt xem.
Chỉ đọc dữ liệu công khai.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "seo"))
from episode_research import has_animal, OFF_TOPIC, norm  # noqa: E402
from seo_research import yt_search, suggestions  # noqa: E402


# Ngoài phim/nhạc/game (OFF_TOPIC): bỏ thêm nội dung thiếu nhi, ẩm thực, câu/bắt/nuôi, vlog thử thách —
# để chỉ đo nhu cầu XEM PHIM KIẾN THỨC ĐỘNG VẬT (khán giả của kênh).
NOISE = re.compile(r"thiếu nhi|bé học|dạy bé|dạy trẻ|em bé|hoạt hình|babybus|pinkfong|cá mập con|changcady|búp bê|"
                   r"kids|children|nursery|thức ăn|món|nấu|chế biến|ăn thử|đường phố|câu cá|bắt được|bắt con|săn bắt|"
                   r"nuôi|thả|lấy ong|feed and grow|tôi là|marvel|parody|fap|tập \d+|thử thách|vlog|phần \d+ \|", re.I)


def measure(topic: str) -> dict:
    t = norm(topic).lower()
    sugg = [s for s in dict.fromkeys(x.lower() for x in suggestions(t))
            if has_animal(s, t) and not OFF_TOPIC.search(s) and not NOISE.search(s)]
    seen, vids = set(), []
    for q in (f"{t} thế giới động vật", f"{t} khám phá", t):
        for v in yt_search(q, 20):
            if (v["id"] in seen or not v["views"] or (v["duration"] or 0) < 120
                    or not has_animal(v["title"], t) or OFF_TOPIC.search(v["title"])
                    or NOISE.search(v["title"]) or NOISE.search(v["channel"])):
                continue
            seen.add(v["id"])
            vids.append(v)
        time.sleep(0.3)
    vids.sort(key=lambda v: v["views"], reverse=True)
    views = [v["views"] for v in vids]
    med = statistics.median(views) if views else 0
    top = views[0] if views else 0
    score = (math.log10(med) if med else 0) + (math.log10(top) / 2 if top else 0) + len(sugg) / 5
    return {"topic": topic, "sugg": len(sugg), "sugg_list": sugg[:8], "vids": len(vids), "top": top, "med": int(med),
            "score": round(score, 2), "best": vids[0] if vids else None}


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("topics", nargs="*")
    ap.add_argument("--file", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--json", type=Path)
    a = ap.parse_args()
    topics = list(a.topics)
    if a.file:
        topics += [l.strip() for l in a.file.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    rows = []
    for t in topics:
        r = measure(t)
        rows.append(r)
        print(f"{r['score']:5.2f}  sugg={r['sugg']:2d} vids={r['vids']:2d} med={r['med']:>10,} top={r['top']:>11,}  {t}", flush=True)
    rows.sort(key=lambda r: r["score"], reverse=True)
    if a.json:
        a.json.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    if a.out:
        L = ["# Nhu cầu chủ đề (người Việt, YouTube)", "",
             "Nguồn: autocomplete YouTube vi/VN + 40 kết quả tìm kiếm qua yt-dlp. `score` chỉ để so sánh tương đối.", "",
             "| # | Chủ đề | Score | Gợi ý tìm | Video | Trung vị view | Cao nhất | Video cao nhất |", "|---:|---|---:|---:|---:|---:|---:|---|"]
        for i, r in enumerate(rows, 1):
            b = r["best"]
            link = f"[{b['title'][:55]}](https://youtu.be/{b['id']})" if b else "—"
            L.append(f"| {i} | {r['topic']} | {r['score']} | {r['sugg']} | {r['vids']} | {r['med']:,} | {r['top']:,} | {link} |")
        a.out.write_text("\n".join(L), encoding="utf-8")
        print("->", a.out)
