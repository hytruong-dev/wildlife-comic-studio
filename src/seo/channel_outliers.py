"""Outlier ratio miễn phí (thay phần cốt lõi của TubeLab MCP, không cần API key) — dùng yt-dlp.

Outlier ratio = lượt xem của video ÷ trung vị lượt xem các video cùng loại của CHÍNH kênh đó.
Ratio > 1.5 = video đang thắng so với mức bình thường của kênh (đây là chỉ số mà mọi skill TubeLab dựa vào).

  python src/seo/channel_outliers.py                       # kênh mình (config/channel.json)
  python src/seo/channel_outliers.py @NhatKyHoangDa UCxxxx  # kênh đối thủ (handle, ID hoặc URL)
  python src/seo/channel_outliers.py --min-age-days 3       # bỏ video mới đăng < 3 ngày (chưa đủ view)

Ghi docs/research/outliers_<kênh>_<ngày>.md. Chỉ đọc dữ liệu công khai, không sửa gì trên YouTube.
"""
from __future__ import annotations

import argparse
import json
import statistics
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "research"


def channel_url(ch: str) -> str:
    if ch.startswith("http"):
        return ch.rstrip("/")
    if ch.startswith("@"):
        return f"https://www.youtube.com/{ch}"
    return f"https://www.youtube.com/channel/{ch}"


def list_tab(url: str, tab: str) -> tuple[list[dict], str]:
    p = subprocess.run(["yt-dlp", "--flat-playlist", "-J", "--no-warnings", f"{url}/{tab}"],
                       capture_output=True, text=True, encoding="utf-8", timeout=180)
    if p.returncode != 0 or not p.stdout.strip():
        return [], url
    d = json.loads(p.stdout)
    out = []
    for e in d.get("entries") or []:
        if not e or not e.get("id"):
            continue
        out.append({"id": e["id"], "title": e.get("title") or "", "views": e.get("view_count"),
                    "duration": e.get("duration") or 0, "ts": e.get("timestamp")})
    return out, (d.get("channel") or d.get("uploader") or d.get("title") or url)


def exact_dates(videos: list[dict]) -> None:
    """Danh sách phẳng thường thiếu ngày đăng -> đọc từng video (chậm, chỉ cho kênh nhỏ)."""
    for v in videos:
        if v["ts"]:
            continue
        p = subprocess.run(["yt-dlp", "-J", "--skip-download", "--no-warnings",
                            f"https://www.youtube.com/watch?v={v['id']}"],
                           capture_output=True, text=True, encoding="utf-8", timeout=90)
        if p.returncode == 0 and p.stdout.strip():
            j = json.loads(p.stdout)
            v["ts"] = j.get("timestamp")
            v["views"] = j.get("view_count", v["views"])


def score(videos: list[dict], min_age_days: float) -> tuple[list[dict], float]:
    now = datetime.now(timezone.utc).timestamp()
    pool = [v for v in videos if v["views"] is not None
            and (not v["ts"] or (now - v["ts"]) / 86400 >= min_age_days)]
    if not pool:
        return [], 0.0
    med = statistics.median(v["views"] for v in pool) or 1
    for v in pool:
        v["ratio"] = round(v["views"] / med, 2)
        v["age_days"] = round((now - v["ts"]) / 86400, 1) if v["ts"] else None
    pool.sort(key=lambda v: v["ratio"], reverse=True)
    return pool, med


def table(rows: list[dict], kind: str) -> list[str]:
    link = (lambda i: f"https://www.youtube.com/shorts/{i}") if kind == "shorts" else (lambda i: f"https://youtu.be/{i}")
    out = ["| Ratio | Lượt xem | Tuổi (ngày) | Tiêu đề |", "|---:|---:|---:|---|"]
    for v in rows:
        tag = " 🔥" if v["ratio"] >= 2 else (" ✅" if v["ratio"] >= 1.5 else (" ⚠️" if v["ratio"] < 0.5 else ""))
        age = "" if v["age_days"] is None else f"{v['age_days']:g}"
        out.append(f"| {v['ratio']:.2f}{tag} | {v['views']:,} | {age} | [{v['title'][:80]}]({link(v['id'])}) |")
    return out


def run(ch: str, min_age_days: float, dates: bool) -> Path:
    url = channel_url(ch)
    long_, name = list_tab(url, "videos")
    shorts, _ = list_tab(url, "shorts")
    if dates and len(long_) <= 60:
        exact_dates(long_)
    L, lmed = score(long_, min_age_days)
    S, smed = score(shorts, min_age_days)
    day = datetime.now().strftime("%Y-%m-%d")
    label = ch.lstrip("@") if ch.startswith("@") else name
    safe = "_".join("".join(c if c.isalnum() else " " for c in label).split())[:40]
    OUT.mkdir(parents=True, exist_ok=True)
    f = OUT / f"outliers_{safe}_{day}.md"
    lines = [f"# Outlier — {name} ({day})", "",
             f"Nguồn: yt-dlp, {url}. Ratio = lượt xem ÷ trung vị cùng loại của kênh. "
             f"🔥 ≥ 2 · ✅ ≥ 1.5 · ⚠️ < 0.5. Bỏ video < {min_age_days:g} ngày tuổi.", "",
             f"## Video dài ({len(L)} video, trung vị {lmed:,.0f} lượt xem)", *table(L, "long"), "",
             f"## Shorts ({len(S)} video, trung vị {smed:,.0f} lượt xem)", *table(S, "shorts"), ""]
    win = [v for v in L if v["ratio"] >= 1.5]
    lose = [v for v in L if v["ratio"] < 0.5]
    lines += ["## Đọc nhanh",
              f"- Video dài thắng (≥ 1.5×): {len(win)}/{len(L)}. Thua (< 0.5×): {len(lose)}/{len(L)}.",
              (f"- Shorts trung vị {smed:,.0f} so với video dài {lmed:,.0f} lượt xem." if S
               else "- Kênh không có Shorts (hoặc không đọc được tab Shorts).")]
    f.write_text("\n".join(lines), encoding="utf-8")
    return f


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("channels", nargs="*", help="handle (@x), channel ID (UC...) hoặc URL; trống = kênh mình")
    ap.add_argument("--min-age-days", type=float, default=2.0)
    ap.add_argument("--no-dates", action="store_true", help="không đọc ngày đăng từng video (nhanh hơn)")
    a = ap.parse_args()
    chans = a.channels or [json.loads((ROOT / "config/channel.json").read_text(encoding="utf-8"))["channel_id"]]
    for c in chans:
        print("->", run(c, a.min_age_days, not a.no_dates))
