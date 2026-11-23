"""Nghiên cứu cho 1 tập theo 3 skill TubeLab (chế độ miễn phí: yt-dlp + YoutubeTags), gắn vào episode-production.

  python src/seo/episode_research.py projects/<slug> ideas      # Bước 1: comment-mining  -> specs/research_ideas.md
  python src/seo/episode_research.py projects/<slug> titles     # Bước 8: title-formulas  -> specs/research_titles.md
  python src/seo/episode_research.py projects/<slug> thumbs     # Bước 4: thumbnail-concepts -> specs/research_thumbs.md + ảnh
  python src/seo/episode_research.py projects/<slug> all

Đầu vào: tên con vật từ episode.json (`animal`) hoặc `--animal "Tên"` khi episode.json chưa có.
Chỉ đọc dữ liệu công khai, không sửa gì trên YouTube. Kết quả là TƯ LIỆU để agent đọc rồi tự quyết theo humor-voice /
director_taste — KHÔNG chép nguyên tiêu đề hay thumbnail của kênh khác.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
import sys
import time
import unicodedata
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "YoutubeTags"))
sys.path.insert(0, str(ROOT / "src" / "seo"))
from YoutubeTags import tag_suggestions  # noqa: E402
from seo_research import words, VI_STOP, yt_search, animal_core  # noqa: E402

EN: str | None = None  # tên tiếng Anh của con vật, đặt trong __main__

# Video không phải nội dung động vật dù có tên con vật (phim, nhạc, game, truyện).
OFF_TOPIC = re.compile(r"review|phim|movie|trailer|\bost\b|official|music video|\bmv\b|karaoke|cover|lyric|bolero|"
                       r"play together|minecraft|roblox|manga|truyện|audio|kể chuyện|tập \d+:|ss\d+e\d+", re.I)
QUESTION = re.compile(r"\?|tại sao|vì sao|sao lại|có phải|làm sao|bao nhiêu|như thế nào|thật không|liệu|ở đâu|ăn gì", re.I)
REQUEST = re.compile(r"làm (thêm |tiếp |về |video )|ra tập|mong|ước gì|nên làm|video về|tập về|kể về", re.I)


def norm(s: str) -> str:
    return unicodedata.normalize("NFC", s or "").strip()


def ytjson(args: list[str], timeout: int = 120) -> dict:
    p = subprocess.run(["yt-dlp", "--no-warnings", *args], capture_output=True, text=True, encoding="utf-8", timeout=timeout)
    return json.loads(p.stdout) if p.returncode == 0 and p.stdout.strip() else {}


def has_animal(text: str, animal: str) -> bool:
    """Đúng tên con vật, đúng dấu, nguyên từ: 'hải ly' khớp, 'Lý Hải' / 'Hải Lý' / 'Phan Hải Lý' không khớp."""
    t = norm(text).lower()
    return any(re.search(rf"(?<!\w){re.escape(c)}(?!\w)", t) for c in {animal, animal_core(animal)})


def top_videos(animal: str, n: int = 15, min_dur: int = 120, en: str | None = None) -> list[dict]:
    """Video top về con vật. Tìm kèm ngữ cảnh động vật để tránh trùng tên người/bài hát, rồi lọc theo tên trong tiêu đề.
    Loài hiếm (tiếng Việt gần như không có video): thêm tên tiếng Anh `en` để lấy video quốc tế làm tư liệu."""
    seen, vids = set(), []
    queries = [f"{animal} động vật", animal] + ([en] if en else [])
    names = [animal] + ([norm(en).lower()] if en else [])
    for q in queries:
        for v in yt_search(q, n):
            if (v["id"] in seen or not v["views"] or (v["duration"] or 0) < min_dur
                    or not any(has_animal(v["title"], nm) for nm in names) or OFF_TOPIC.search(v["title"])):
                continue
            seen.add(v["id"])
            vids.append(v)
    vids.sort(key=lambda v: v["views"], reverse=True)
    return vids


def channel_medians(vids: list[dict]) -> None:
    """Ratio = lượt xem ÷ trung vị video dài của chính kênh đó (chỉ số cốt lõi của TubeLab)."""
    cache: dict[str, float] = {}
    for v in vids:
        url = v.get("channel_url") or ""
        if not url:
            d = ytjson(["-J", "--skip-download", f"https://www.youtube.com/watch?v={v['id']}"], 90)
            url = d.get("channel_url", "")
            v["subs"] = d.get("channel_follower_count")
        if url and url not in cache:
            d = ytjson(["--flat-playlist", "-J", "--playlist-end", "30", f"{url}/videos"], 120)
            views = [e.get("view_count") for e in (d.get("entries") or []) if e and e.get("view_count")]
            cache[url] = statistics.median(views) if views else 0
        med = cache.get(url, 0)
        v["channel_median"] = med
        v["ratio"] = round(v["views"] / med, 1) if med else None


# ---------------------------------------------------------------- comment-mining (Bước 1)

def mine_comments(animal: str, vids: list[dict], per_video: int = 60) -> dict:
    qs, reqs, all_words = [], [], Counter()
    for v in vids[:5]:
        d = ytjson(["--skip-download", "--write-comments", "--extractor-args",
                    f"youtube:max_comments={per_video},all,all,0", "-J", f"https://www.youtube.com/watch?v={v['id']}"], 180)
        for c in d.get("comments") or []:
            t = norm(c.get("text", "")).replace("\n", " ")
            if len(t) < 15 or len(set(t)) < 8:  # bỏ bình luận quá ngắn / toàn emoji
                continue
            item = {"text": t[:220], "likes": c.get("like_count") or 0, "video": v["id"], "title": v["title"]}
            if QUESTION.search(t):
                qs.append(item)
            if REQUEST.search(t):
                reqs.append(item)
            all_words.update(w for w in words(t) if w not in VI_STOP and len(w) > 2)
        time.sleep(0.4)
    key = lambda x: -x["likes"]
    return {"questions": sorted(qs, key=key)[:15], "requests": sorted(reqs, key=key)[:10],
            "top_words": all_words.most_common(25)}


def english_name(P: Path) -> str | None:
    """Tên tiếng Anh của con vật, lấy từ seo.en_title / en_shorts_title (vd 'Diving Bell Spider') nếu có."""
    m = re.match(r"tap-(\d+)", P.name)
    if m:  # config/series_roadmap.json > animal_en (có cho Tập 51-60 trở đi)
        road = json.loads((ROOT / "config" / "series_roadmap.json").read_text(encoding="utf-8"))["episodes"]
        en = next((e.get("animal_en") for e in road if e["ep"] == int(m.group(1))), None)
        if en:
            return en
    f = P / "episode.json"
    if not f.exists():
        return None
    seo = json.loads(f.read_text(encoding="utf-8")).get("seo", {})
    en = seo.get("animal_en")
    if en:
        return en
    m = re.search(r"\|\s*([A-Za-z][A-Za-z' -]{2,40}?)\s*\|\s*Ep", seo.get("en_title", ""))
    return m.group(1).strip() if m else None


def run_ideas(P: Path, animal: str) -> Path:
    core = animal_core(animal)
    sugg = []
    for s in dict.fromkeys([animal, core, f"tại sao {core}", f"{core} ăn gì", f"{core} sống ở đâu"]):
        try:
            sugg += tag_suggestions(s, language="vi", region="VN")
        except Exception:
            pass
        time.sleep(0.2)
    sugg = [x for x in dict.fromkeys(norm(x).lower() for x in sugg) if has_animal(x, animal) and not OFF_TOPIC.search(x)]
    vids = top_videos(animal, en=EN)
    m = mine_comments(animal, vids)
    L = [f"# Nghiên cứu khán giả — {animal}", "",
         "Skill `comment-mining` (TubeLab, chế độ miễn phí). Dùng để chọn **hook, câu hỏi bí ẩn, chương bào chữa, câu hỏi ghim**.",
         "Không chép nguyên văn bình luận vào kịch bản.", ""]
    if not sugg and len(vids) < 3:
        L += [f"⚠️ **Người Việt gần như chưa tìm loài này** ({len(sugg)} gợi ý tìm kiếm, {len(vids)} video)."
              + ("" if EN else " Thêm `--en \"English name\"` để đọc bình luận video quốc tế.")
              + " Đây vừa là rủi ro (ít người tìm) vừa là cơ hội (chưa ai làm): tiêu đề phải bán bằng **nghịch lý**,"
              " không bằng tên con vật.", ""]
    L += [
          "## Người Việt đang gõ tìm (YouTube autocomplete vi/VN)", ", ".join(sugg) or "—", "",
         "## Câu hỏi khán giả hay hỏi (bình luận video top, xếp theo lượt thích)"]
    L += [f"- ({q['likes']}👍) {q['text']} — [video](https://youtu.be/{q['video']})" for q in m["questions"]] or ["- —"]
    L += ["", "## Khán giả xin làm thêm / mong muốn"]
    L += [f"- ({q['likes']}👍) {q['text']} — [video](https://youtu.be/{q['video']})" for q in m["requests"]] or ["- —"]
    L += ["", "## Từ lặp nhiều trong bình luận", ", ".join(f"{w} ({n})" for w, n in m["top_words"]) or "—", "",
          "## Video đã đọc bình luận"]
    L += [f"- [{v['title']}](https://youtu.be/{v['id']}) · {v['views']:,} view · {v['channel']}" for v in vids[:5]]
    L += ["", "## Cách dùng trong kịch bản",
          "- Câu hỏi nhiều like nhất → ứng viên cho **hook scene01** hoặc nghịch lý cần giải.",
          "- Hiểu lầm phổ biến trong bình luận → **cú bẻ lái** (như Tập 9 cánh cụt), sau khi kiểm chứng bằng nguồn khoa học.",
          "- Câu hỏi chưa video nào trả lời → **câu hỏi ghim** (`seo.question`)."]
    out = P / "specs" / "research_ideas.md"
    out.write_text("\n".join(L), encoding="utf-8")
    return out


# ---------------------------------------------------------------- title-formulas (Bước 8)

def shape(title: str, animal: str) -> str:
    """Rút khuôn tiêu đề: thay tên con vật bằng [CON VẬT], số bằng [SỐ]."""
    t = norm(title)
    for a in sorted({animal, animal_core(animal)}, key=len, reverse=True):
        t = re.sub(re.escape(a), "[CON VẬT]", t, flags=re.I)
    t = re.sub(r"\d[\d.,]*\s*(kg|m|cm|km/h|°c|v|giây|năm|tấn|lít|%)?", "[SỐ]", t, flags=re.I)
    return t


def run_titles(P: Path, animal: str) -> Path:
    vids = top_videos(animal, 20, en=EN)[:12]
    channel_medians(vids)
    won = [v for v in vids if v.get("ratio") and v["ratio"] >= 1.5]
    vids.sort(key=lambda v: (v.get("ratio") or 0), reverse=True)
    ep = json.loads((P / "episode.json").read_text(encoding="utf-8")) if (P / "episode.json").exists() else {}
    cur = ep.get("seo", {}).get("title", "")
    lens = [len(v["title"]) for v in won] or [len(v["title"]) for v in vids]
    first = sum(1 for v in won if animal_core(animal) in norm(v["title"][:40]).lower())
    L = [f"# Tiêu đề — {animal}", "",
         "Skill `title-formulas` (TubeLab, chế độ miễn phí). Ratio = lượt xem ÷ trung vị video dài của chính kênh đó.",
         "✅ = công thức đã thắng (ratio ≥ 1.5) ở chủ đề này. Không có index công thức thịnh hành toàn YouTube (cần TubeLab trả phí).", "",
         f"**Tiêu đề hiện tại:** {cur} ({len(cur)} ký tự)" if cur else "**Tiêu đề hiện tại:** (chưa có)"]
    if len(vids) < 5:
        L += ["", f"⚠️ **Tín hiệu mỏng:** chỉ {len(vids)} video về con vật này"
              + ("" if EN else " — thử lại với `--en \"English name\"` để lấy video quốc tế")
              + ". Dựa vào khuôn tiêu đề đã thắng của **chính kênh** (`python src/seo/channel_outliers.py`) thay vì ở đây."]
    if lens:
        L.append(f"- Video thắng: dài TB {statistics.mean(lens):.0f} ký tự; {first}/{len(won)} để tên con vật trong 40 ký tự đầu.")
    L += ["", "| Ratio | Lượt xem | Kênh | Tiêu đề | Khuôn |", "|---:|---:|---|---|---|"]
    for v in vids:
        r = v.get("ratio")
        mark = " ✅" if r and r >= 1.5 else ""
        L.append(f"| {r if r is not None else '?'}{mark} | {v['views']:,} | {v['channel']} | "
                 f"[{v['title'][:70]}](https://youtu.be/{v['id']}) | {shape(v['title'], animal)[:60]} |")
    L += ["", "## Việc của agent (trước `pipeline.py seo`)",
          "1. Chọn 2-3 khuôn ✅ hợp với nghịch lý chính của tập; viết lại bằng **giọng kênh** (phần trước `| Tập N` ≤ 60 ký tự, có ?! hoặc số).",
          "2. Ưu tiên đưa tên con vật vào 40 ký tự đầu nếu đa số video thắng làm vậy (loài ít người tìm: bán bằng nghịch lý).",
          "3. Giữ luật kênh: **luôn có đuôi `| Tập N`** (TASTE-72, `format_long_title` tự gắn), không hứa điều video không có. "
          "Ghi tiêu đề chọn vào `seo.title`.",
          "4. Ghi 2 phương án còn lại vào `seo.title_alternatives` để thử A/B trong Studio (Test & Compare)."]
    out = P / "specs" / "research_titles.md"
    out.write_text("\n".join(L), encoding="utf-8")
    return out


# ---------------------------------------------------------------- thumbnail-concepts (Bước 4)

def run_thumbs(P: Path, animal: str) -> Path:
    vids = top_videos(animal, 20, en=EN)[:10]
    channel_medians(vids)
    vids.sort(key=lambda v: (v.get("ratio") or 0), reverse=True)
    d = P / "specs" / "research_thumbs"
    d.mkdir(parents=True, exist_ok=True)
    for v in vids:
        f = d / f"{v['id']}.jpg"
        if not f.exists():
            try:
                urllib.request.urlretrieve(f"https://i.ytimg.com/vi/{v['id']}/mqdefault.jpg", f)
            except Exception:
                pass
    L = [f"# Thumbnail — {animal}", "",
         "Skill `thumbnail-concepts` (TubeLab, chế độ miễn phí). Ảnh đã tải vào `specs/research_thumbs/` — **agent phải MỞ XEM từng ảnh**",
         "(skill cấm mô tả ảnh chưa xem). Xếp theo ratio (lượt xem ÷ trung vị kênh).", "",
         "| Ratio | Lượt xem | Ảnh | Tiêu đề |", "|---:|---:|---|---|"]
    for v in vids:
        L.append(f"| {v.get('ratio', '?')} | {v['views']:,} | `research_thumbs/{v['id']}.jpg` | "
                 f"[{v['title'][:70]}](https://youtu.be/{v['id']}) |")
    L += ["", "## Việc của agent (trước khi viết `art.thumb_*` / sinh T01)",
          "1. Mở xem các ảnh ratio cao nhất. Ghi 3 điểm chung: bố cục, khoảng cách chủ thể, màu, có chữ không, cảm xúc.",
          "2. Ghép **điểm chung đó + nghịch lý riêng của tập** thành `art.thumb_scene` / `thumb_gag` / `thumb_title` "
          "(giữ phong cách vẽ tay của kênh, TASTE-57).",
          "3. Không sao chép ảnh hay chữ của kênh khác."]
    out = P / "specs" / "research_thumbs.md"
    out.write_text("\n".join(L), encoding="utf-8")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project", type=Path)
    ap.add_argument("what", choices=["ideas", "titles", "thumbs", "all"])
    ap.add_argument("--animal")
    ap.add_argument("--en", help="tên tiếng Anh (loài hiếm, ít video tiếng Việt); mặc định lấy từ seo.en_title")
    a = ap.parse_args()
    P = a.project.resolve()
    (P / "specs").mkdir(parents=True, exist_ok=True)
    EN = a.en or english_name(P)
    animal = a.animal
    if not animal and (P / "episode.json").exists():
        animal = json.loads((P / "episode.json").read_text(encoding="utf-8")).get("animal")
    if not animal:
        sys.exit("thiếu tên con vật: thêm --animal \"Tên\" hoặc tạo episode.json trước")
    animal = norm(animal).lower()
    jobs = {"ideas": run_ideas, "titles": run_titles, "thumbs": run_thumbs}
    for k in (["ideas", "titles", "thumbs"] if a.what == "all" else [a.what]):
        print(f"{k:7s} ->", jobs[k](P, animal))
