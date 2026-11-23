"""Nghiên cứu từ khoá + kiểm định SEO cho 1 tập, dùng 4 repo đã cài vào tools/:

  - yt-dlp/yt-dlp                       : tìm video đối thủ trên YouTube (không cần API key)
  - nuhmanpk/YoutubeTags                : tag thật của đối thủ, gợi ý tìm kiếm vi/VN, đếm ký tự tag kiểu YouTube Studio
  - catball912/hybrid-youtube-growth-engine : chấm điểm SEO 0-100 (AuditEngine)
  - kumarAnand05/YouTube-Video-SEO-Analyzer : ý tưởng đếm từ khoá tiêu đề top video, viết lại dùng yt-dlp
                                              (bản gốc cần Google API key + NLTK tiếng Anh)

Cách dùng:
  python src/seo/seo_research.py projects/tap-30-hai-ly            # chỉ nghiên cứu + báo cáo
  python src/seo/seo_research.py projects/tap-30-hai-ly --apply    # ghi tag mở rộng vào episode.json rồi chạy lại pipeline seo

Kết quả: specs/seo_research.json + specs/seo_research.md. Không bao giờ đăng/sửa gì trên YouTube.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "YoutubeTags"))
sys.path.insert(0, str(ROOT / "tools" / "hybrid-youtube-growth-engine"))

from YoutubeTags import analyze_tags, get_video_info, tag_suggestions  # noqa: E402
from hybrid_youtube_growth_engine.core.audit_engine import AuditEngine  # noqa: E402

# Ngân sách tag tính kiểu YouTube Studio (tag có dấu cách +2 ký tự cho dấu ngoặc kép). Giới hạn cứng là 500.
TAG_BUDGET = 470
VI_STOP = set("""là và của có những một các trong được với cho không khi này đó để như từ trên đến về hay nhưng vì ra vào
lại rất cả cũng sẽ đã đang bị bởi theo tại mà thì nếu nó gì nào ai sao thế bạn tôi chúng ta video tập phần full hd
the a an of to in and is for on with how why what you""".split())
# Từ chỉ chủ đề kênh / thể loại: tag chứa các từ này được coi là liên quan dù không nằm trong kịch bản.
NICHE_WORDS = {"động", "vật", "hoang", "dã", "thiên", "nhiên", "sinh", "khoa", "học", "kỳ", "lạ", "thế", "giới",
               "khám", "phá", "animal", "animals", "wildlife", "nature", "facts", "science", "documentary"}


def norm(s: str) -> str:
    return unicodedata.normalize("NFC", s).strip().lower()


def words(s: str) -> list[str]:
    return [w for w in re.findall(r"[^\W\d_]+", norm(s)) if len(w) > 1]


def yt_search(query: str, n: int = 15) -> list[dict]:
    """yt-dlp ytsearch, metadata phẳng (nhanh, không tải video)."""
    try:
        out = subprocess.run(["yt-dlp", "--flat-playlist", "-J", "--no-warnings", f"ytsearch{n}:{query}"],
                             capture_output=True, text=True, encoding="utf-8", timeout=90)
        data = json.loads(out.stdout) if out.returncode == 0 and out.stdout.strip() else {}
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return []
    res = []
    for e in data.get("entries") or []:
        if not e or e.get("_type") not in (None, "url"):
            continue
        res.append({"id": e.get("id"), "title": e.get("title") or "", "views": e.get("view_count") or 0,
                    "duration": e.get("duration") or 0, "channel": e.get("channel") or "",
                    "description": e.get("description") or ""})
    return res


def suggestions(seed: str) -> list[str]:
    try:
        return [norm(x) for x in tag_suggestions(seed, language="vi", region="VN")]
    except Exception:
        return []


def competitor_tags(video_ids: list[str], limit: int = 8) -> dict[str, list[str]]:
    out = {}
    for vid in video_ids[:limit]:
        try:
            out[vid] = [norm(t) for t in get_video_info(vid).get("tags", [])]
        except Exception:
            out[vid] = []
        time.sleep(0.3)
    return out


def relevance_corpus(ep: dict) -> set[str]:
    """Từ vựng của chính tập: kịch bản dài + Shorts + SEO + tên khoa học. Tag chỉ được giữ nếu khớp vốn từ này."""
    txt = [ep.get("animal", ""), ep.get("nickname", ""), ep.get("shorts", {}).get("text", "")]
    for sc in ep.get("longform", {}).get("scenes", []):
        txt.append(sc.get("chapter_title", ""))
        txt += [p.get("text", "") if isinstance(p, dict) else str(p) for p in sc.get("parts", [])]
    seo = ep.get("seo", {})
    txt += [seo.get("title", ""), seo.get("hook_paragraph", "")] + list(seo.get("tags", []))
    return set(words(" ".join(txt)))


def animal_core(animal: str) -> str:
    """Cụm bắt buộc phải có trong tag: tên con vật đúng dấu (tên dài > 2 từ thì lấy 2 từ đầu, vd 'kiến nổ')."""
    w = norm(animal).split()
    return " ".join(w[:2]) if len(w) > 2 else " ".join(w)


def is_relevant(tag: str, cores: list[str], animal_words: set[str], corpus: set[str]) -> bool:
    """Giữ tag khi nó chứa đúng tên một con vật của tập (đúng dấu: 'hải ly' khác 'hải lý') VÀ mọi từ còn lại đều có
    trong kịch bản tập hoặc thuộc chủ đề kênh. Loại kiểu 'hải ly manga review', 'hải ly xe đạp' dù autocomplete trả về."""
    t = norm(tag)
    if not any(re.search(rf"(?<!\w){re.escape(c)}(?!\w)", t) for c in cores):
        return False
    return all(w in animal_words or w in corpus or w in NICHE_WORDS for w in words(t))


FILLER = {"của", "con", "cái", "chú", "những", "các", "một"}


def tag_key(tag: str) -> frozenset:
    """'đập của hải ly' / 'con đập hải ly' / 'đập hải ly' coi là một -> không phí ngân sách cho biến thể gần trùng."""
    return frozenset(w for w in words(tag) if w not in FILLER)


def yt_tag_len(tags: list[str]) -> int:
    return analyze_tags(tags)["total_characters"] if tags else 0


def fill_tags(base: list[str], candidates: list[str], budget: int = TAG_BUDGET) -> list[str]:
    """Tag gốc luôn giữ nguyên (kể cả khi gần trùng nhau); chỉ ứng viên mới bị lọc gần trùng."""
    out, seen = [], set()
    for t in base:
        k = norm(t)
        if k and yt_tag_len(out + [k]) <= budget:
            out.append(k)
            seen.add(tag_key(k))
    for t in candidates:
        k = norm(t)
        if not k or len(k) > 60 or tag_key(k) in seen:
            continue
        if yt_tag_len(out + [k]) <= budget:
            out.append(k)
            seen.add(tag_key(k))
    return out


def title_keyword_stats(videos: list[dict]) -> dict:
    """Chuyển ý tưởng của YouTube-Video-SEO-Analyzer: từ khoá hay dùng trong tiêu đề video đứng top, độ dài TB."""
    if not videos:
        return {"avg_title_len": 0, "avg_title_words": 0, "top_title_words": []}
    c = Counter()
    for v in videos:
        c.update(w for w in words(v["title"]) if w not in VI_STOP)
    return {"avg_title_len": round(sum(len(v["title"]) for v in videos) / len(videos), 1),
            "avg_title_words": round(sum(len(v["title"].split()) for v in videos) / len(videos), 1),
            "top_title_words": [[w, n] for w, n in c.most_common(20) if n > 1]}


def audit(title: str, desc: str, tags: str, keyword: str) -> dict:
    r = AuditEngine().audit(title, desc, tags, target_keyword=keyword)
    # Engine gốc viết cho MV nhạc: cộng điểm khi có tag tiếng Nhật / link ngoài / từ "official".
    # Ghi rõ để người đọc không chạy theo các điểm trừ không phù hợp kênh động vật tiếng Việt.
    ignored = [s for s in r.suggestions if any(k in s.lower() for k in ("lyrics", "streaming", "smart link", "artist"))]
    return {"score": r.overall_score, "grade": r.grade, "title": r.title_score, "desc": r.desc_score,
            "tags": r.tag_score, "hashtags": r.hashtag_score, "strengths": r.strengths, "warnings": r.warnings,
            "suggestions": [s for s in r.suggestions if s not in ignored], "ignored_music_only": ignored}


def research(P: Path, apply: bool, cores_arg: list[str] | None = None) -> dict:
    ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
    up = json.loads((P / "upload.json").read_text(encoding="utf-8")) if (P / "upload.json").exists() else {}
    seo = ep["seo"]
    corpus = relevance_corpus(ep)
    base_tags = [norm(t) for t in seo.get("tags", [])]
    # Tập thường: 1 con vật. Tập tổng hợp (mega): truyền --cores "tôm súng,lươn điện,..." (nhiều con vật).
    cores = [norm(c) for c in (cores_arg or [animal_core(ep["animal"])]) if c.strip()]
    animal = cores[0] if cores_arg else norm(ep["animal"])
    animal_words = set(w for c in cores for w in words(c))
    corpus |= animal_words

    # 1) Gợi ý tìm kiếm thật của người Việt: hạt giống = tên (các) con vật + vài tag gốc chứa tên đó
    if cores_arg:
        seeds = list(cores)
    else:
        seeds = list(dict.fromkeys([animal, cores[0]] + [t for t in base_tags if cores[0] in t and t != animal][:3]))
    sugg_all = []
    for s in seeds:
        sugg_all += suggestions(s)
        time.sleep(0.2)
    sugg = list(dict.fromkeys(sugg_all))
    sugg_ok = [t for t in sugg if is_relevant(t, cores, animal_words, corpus)]

    # 2) Đối thủ: video top cho (từng) con vật (yt-dlp) + tag thật của họ (YoutubeTags)
    videos, seen_ids = [], set()
    per = 15 if not cores_arg else 4
    for c in cores:
        for v in yt_search(c, per):
            if v["id"] not in seen_ids:
                seen_ids.add(v["id"])
                videos.append(v)
    videos.sort(key=lambda v: v["views"], reverse=True)
    ctags = competitor_tags([v["id"] for v in videos], limit=8 if not cores_arg else 12)
    comp_counter = Counter(t for ts in ctags.values() for t in set(ts))
    comp_ok = [t for t, _ in comp_counter.most_common() if is_relevant(t, cores, animal_words, corpus)]

    # 3) Tag mở rộng: giữ nguyên tag gốc (thứ tự ưu tiên), lấp ngân sách bằng từ khoá đã lọc liên quan
    expanded = fill_tags(base_tags, sugg_ok + comp_ok)
    added = [t for t in expanded if t not in base_tags]

    long = up.get("long", {})
    cur_tags = long.get("tags", ", ".join(base_tags))
    before = audit(long.get("title", seo["title"]), long.get("desc", ""), cur_tags, animal)
    after = audit(long.get("title", seo["title"]), long.get("desc", ""), ", ".join(expanded), animal)

    title = long.get("title", seo["title"])
    report = {
        "episode": P.name, "animal": animal, "cores": cores,
        "title_check": {"title": title, "len": len(title),
                        "animal_in_first_40": any(c in norm(title[:40]) for c in cores)},
        "tags_before": {"tags": base_tags, **analyze_tags(base_tags)},
        "tags_after": {"tags": expanded, "added": added, **analyze_tags(expanded)},
        "search_suggestions": {"seeds": seeds, "all": sugg, "relevant": sugg_ok,
                               "rejected": [t for t in sugg if t not in sugg_ok]},
        "competitors": [{**v, "description": v["description"][:160], "tags": ctags.get(v["id"], [])} for v in videos],
        "competitor_tags_relevant": comp_ok[:40],
        "title_keyword_stats": title_keyword_stats(videos),
        "audit_before": before, "audit_after": after,
    }
    (P / "specs").mkdir(exist_ok=True)
    (P / "specs" / "seo_research.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    write_md(P, report)

    if apply and added:
        ep["seo"]["tags"] = expanded
        (P / "episode.json").write_text(json.dumps(ep, ensure_ascii=False, indent=1), encoding="utf-8")
        subprocess.run([sys.executable, str(ROOT / "src/episode/pipeline.py"), "seo", str(P)], check=True,
                       stdout=subprocess.DEVNULL)
    return report


def write_md(P: Path, r: dict) -> None:
    tb, ta, ab, aa = r["tags_before"], r["tags_after"], r["audit_before"], r["audit_after"]
    st = r["title_keyword_stats"]
    lines = [f"# Nghiên cứu SEO — {r['episode']} ({r['animal']})", "",
             f"**Tiêu đề:** {r['title_check']['title']} ({r['title_check']['len']} ký tự; "
             f"tên con vật trong 40 ký tự đầu: {'có' if r['title_check']['animal_in_first_40'] else 'KHÔNG'})", "",
             "## Tag", f"- Trước: {tb['count']} tag, {tb['total_characters']}/500 ký tự (cách đếm YouTube Studio)",
             f"- Sau: {ta['count']} tag, {ta['total_characters']}/500 ký tự", f"- Thêm: {', '.join(ta['added']) or '—'}", "",
             "## Điểm SEO (hybrid-youtube-growth-engine)", f"- Trước: {ab['score']}/100 — {ab['grade']}",
             f"- Sau: {aa['score']}/100 — {aa['grade']}"]
    if aa["suggestions"]:
        lines += ["- Gợi ý còn lại:"] + [f"  - {s}" for s in aa["suggestions"]]
    if aa["ignored_music_only"]:
        lines += ["- Bỏ qua (chỉ hợp MV nhạc):"] + [f"  - {s}" for s in aa["ignored_music_only"]]
    lines += ["", "## Người Việt đang tìm (YouTube autocomplete, đã lọc liên quan)",
              ", ".join(r["search_suggestions"]["relevant"]) or "—",
              f"\n_Loại bỏ vì lạc đề:_ {', '.join(r['search_suggestions']['rejected']) or '—'}", "",
              "## Video đối thủ top (yt-dlp)", "| Lượt xem | Thời lượng | Kênh | Tiêu đề |", "|---:|---:|---|---|"]
    for v in r["competitors"][:10]:
        lines.append(f"| {v['views']:,} | {int(v['duration']) // 60}:{int(v['duration']) % 60:02d} | {v['channel']} | {v['title']} |")
    lines += ["", f"Tiêu đề top: TB {st['avg_title_len']} ký tự / {st['avg_title_words']} từ. "
              f"Từ khoá lặp nhiều: {', '.join(f'{w} ({n})' for w, n in st['top_title_words'][:12]) or '—'}", ""]
    (P / "specs" / "seo_research.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("projects", nargs="+", type=Path)
    ap.add_argument("--apply", action="store_true", help="ghi tag mở rộng vào episode.json + chạy lại pipeline seo")
    ap.add_argument("--cores", help="tập tổng hợp: danh sách tên con vật, phân tách bằng dấu phẩy")
    a = ap.parse_args()
    cores = [c for c in a.cores.split(",")] if a.cores else None
    for P in a.projects:
        r = research(P.resolve(), a.apply, cores)
        ta, ab, aa = r["tags_after"], r["audit_before"], r["audit_after"]
        print(f"{r['episode']:28s} tag {r['tags_before']['total_characters']:3d} -> {ta['total_characters']:3d}/500 "
              f"(+{len(ta['added'])})  SEO {ab['score']} -> {aa['score']}  "
              f"gợi ý liên quan {len(r['search_suggestions']['relevant'])}/{len(r['search_suggestions']['all'])}  "
              f"đối thủ {len(r['competitors'])}{'  [ĐÃ ÁP DỤNG]' if a.apply and ta['added'] else ''}")
