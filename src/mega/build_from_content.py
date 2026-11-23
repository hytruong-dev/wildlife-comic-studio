"""Long-form content DSL -> episode.json + specs/storyboard.json (Mega "nội dung mới hoàn toàn", 40-70 phút).

Viết 60 phút lời + 400 ảnh bằng tay trong 2 file JSON rất dễ lệch nhau. File nội dung đặt LỜI và BỐ CỤC ẢNH cạnh nhau,
công cụ này tự ghép part, tự chọn cụm mốc 'at' duy nhất cho từng ảnh, kiểm tra độ dài, rồi ghi:
  <P>/episode.json            (meta từ content/meta.json + scenes từ content/sNN.md + shorts từ content/shorts.md)
  <P>/specs/storyboard.json   (characters từ content/characters.json)

  python src/mega/build_from_content.py projects/<mega>
  sau đó: python src/episode/build_plans.py <P> · python src/episode/extra_prompts.py <P> · python src/episode/pipeline.py check <P>

ĐỊNH DẠNG content/sNN.md (1 file = 1 scene = 1 chương YouTube):
  # scene02 | BADGE ≤16 | BANNER TITLE ≤32 | Chapter title cho mục lục | HOOK THẺ CHƯƠNG | mood=don_dap
  @ hao_hung                      <- bắt đầu part mới, mood của part (hao_hung don_dap tram_bi_an nghiem_trang_gia bi_hai am_ap)
  @cast tham_phan                 <- part cameo (giọng vai phụ, config/voice_personas.json > cast)
  Lời đọc của ảnh này. Có thể 1-2 câu. :: Bố cục ảnh, dùng {KOALA} {MC} {NO_HERO}... || at;side;y;value;label;x,y
  // dòng chú thích
  - Mỗi dòng có '::' = 1 ảnh (beat). Lời đọc 60-270 ký tự (≈ 3-14 giây). Sticker (tùy chọn) sau '||':
    at = chữ DẠNG PHỤ ĐỀ (sau display_fix, vd "13.000km"), side L/R, y 300-560, value ≤ 10, label ≤ 22, x,y = mũi tên trỏ (0-1).
  - Nhiều sticker: '||' lặp lại. Số trong lời PHẢI viết bằng chữ + display_fix trong meta.json (lint của pipeline check).
ĐỊNH DẠNG content/shorts.md: dòng '## DÒNG 1 | DÒNG 2' (banner) + '@ mood' + các dòng 'lời :: bố cục || sticker'.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "episode"))
from pipeline import norm, script_tokens  # noqa: E402

CPS = 17.6 * 1.12  # ký tự/giây ở tempo trung bình 1.12 (hiệu chỉnh Tập 9)


def parse_sticker(s: str, where: str) -> dict:
    f = [x.strip() for x in s.split(";")]
    if len(f) != 6:
        raise SystemExit(f"{where}: sticker cần 6 trường at;side;y;value;label;x,y — có: {s!r}")
    x, y = (float(v) for v in f[5].split(","))
    return {"at": f[0], "side": f[1], "y": int(f[2]), "value": f[3], "label": f[4], "target": [x, y]}


def parse_beat(line: str, where: str) -> dict:
    text, rest = line.split("::", 1)
    bits = rest.split("||")
    beat_id = None
    stickers = []
    for b in bits[1:]:
        s = b.strip()
        if not s:
            continue
        if s.startswith("id="):
            beat_id = s[3:].strip()
        else:
            stickers.append(parse_sticker(s, where))
    out = {"text": " ".join(text.split()), "layout": bits[0].strip(), "stickers": stickers}
    if beat_id:
        out["id"] = beat_id
    return out


def parse_scene(path: Path) -> dict:
    lines = [ln.rstrip() for ln in path.read_text(encoding="utf-8-sig").splitlines()]
    head = next(ln for ln in lines if ln.startswith("# "))
    f = [x.strip() for x in head[2:].split("|")]
    if len(f) != 6:
        raise SystemExit(f"{path.name}: header cần 6 trường: id | badge | banner | chapter | hook | mood=...")
    sc = {"id": f[0], "badge": f[1], "banner_title": f[2], "chapter_title": f[3], "hook": f[4],
          "mood": f[5].split("=", 1)[1].strip(), "parts": []}
    cur = None
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s or s.startswith("//") or s.startswith("# "):
            continue
        if s.startswith("@"):
            spec = s[1:].strip()
            cur = {"cast": spec.split(None, 1)[1].strip()} if spec.startswith("cast") else {"mood": spec or sc["mood"]}
            cur["beats"] = []
            sc["parts"].append(cur)
            continue
        if "::" not in s:
            raise SystemExit(f"{path.name}:{i}: dòng không có '::' (lời :: bố cục): {s[:80]}")
        if cur is None:
            raise SystemExit(f"{path.name}:{i}: beat nằm trước '@ mood' đầu tiên")
        cur["beats"].append(parse_beat(s, f"{path.name}:{i}"))
    return sc


def pick_at(toks: list[str], o: int, where: str) -> str:
    n = [norm(t) for t in toks]
    if not n[o]:
        raise SystemExit(f"{where}: ảnh bắt đầu bằng ký hiệu rời ({toks[o]!r}) — viết liền hoặc đổi câu")
    for k in range(3, 10):
        win = toks[o:o + k]
        if len(win) < k or not all(norm(t) for t in win):
            break
        want = [norm(t) for t in win]
        first = next(i for i in range(len(n) - k + 1) if n[i:i + k] == want)
        if first == o:
            return " ".join(win)
    raise SystemExit(f"{where}: không tìm được cụm mốc duy nhất cho '{' '.join(toks[o:o + 8])}' — đổi chữ mở đầu câu này "
                     f"(đã xuất hiện y hệt ở trước trong cùng chương)")


def find(n: list[str], phrase: str, lo: int) -> int:
    want = [norm(x) for x in phrase.split() if norm(x)]
    for i in range(lo, len(n) - len(want) + 1):
        if n[i:i + len(want)] == want:
            return i
    return -1


def resolve_at(raw: str, display: dict, n: list[str], lo: int, hi: int) -> str | None:
    """Mốc sticker có thể viết bằng chữ ('mười chú'); thử dạng phụ đề trực tiếp, rồi mọi display_fix chứa nó."""
    cands = [" ".join(script_tokens(raw, display))]
    cands += [" ".join(script_tokens(k, display)) for k in display if raw in k and k != raw]
    for c in cands:
        k = find(n, c, lo)
        if 0 <= k < hi:
            return c
    return None


def build_long(scenes: list[dict], display: dict) -> tuple[list, list, list]:
    ep_scenes, sb_long, warns = [], [], []
    for sc in scenes:
        parts_out, beats_flat = [], []
        for p in sc["parts"]:
            text = " ".join(b["text"] for b in p["beats"])
            q = {"text": text}
            q.update({"cast": p["cast"]} if "cast" in p else {"mood": p["mood"]})
            parts_out.append(q)
            beats_flat += p["beats"]
            clean = re.sub(r"\[[^\]]+\]", "", text)
            if len(clean) > 1300:
                warns.append(f"{sc['id']}: part dài {len(clean)} ký tự > 1300 — thêm '@ mood' để tách")
        toks = script_tokens(" ".join(q["text"] for q in parts_out), display)
        n = [norm(t) for t in toks]
        o = 0
        for j, b in enumerate(beats_flat):
            bt = script_tokens(b["text"], display)
            where = f"{sc['id']} ảnh {j + 1} ('{b['text'][:40]}…')"
            at = 0 if o == 0 else pick_at(toks, o, where)
            end = o + len(bt)
            for s in b["stickers"]:
                got = resolve_at(s["at"], display, n, o, end)  # cho phép viết mốc sticker bằng chữ
                if got is None:
                    raise SystemExit(f"{where}: sticker at={s['at']!r} không nằm trong lời của ảnh này (dạng phụ đề)")
                s["at"] = got
            secs = len(re.sub(r"\[[^\]]+\]", "", b["text"])) / CPS
            if secs > 14.5:
                warns.append(f"{where}: ≈{secs:.1f}s > 14,5s — tách thành 2 ảnh")
            if secs < 2.2 and j:
                warns.append(f"{where}: ≈{secs:.1f}s < 2,2s — gộp với ảnh kề")
            item = {"scene": sc["id"], "at": at, "layout": b["layout"], "stickers": b["stickers"], "impacts": []}
            if b.get("id"):
                item["id"] = b["id"]
            sb_long.append(item)
            o = end
        if o != len(toks):
            raise SystemExit(f"{sc['id']}: lệch token ({o} != {len(toks)}) — display_fix nhiều chữ bị cắt ngang 2 ảnh?")
        ep_scenes.append({k: sc[k] for k in ("id", "badge", "banner_title", "chapter_title", "hook", "mood")} | {"parts": parts_out})
    return ep_scenes, sb_long, warns


def parse_shorts(path: Path, display: dict) -> tuple[dict, list, list]:
    lines = [ln.strip() for ln in path.read_text(encoding="utf-8-sig").splitlines()]
    title = next(ln[3:] for ln in lines if ln.startswith("## "))
    mood = next((ln[1:].strip() for ln in lines if ln.startswith("@")), "don_dap")
    beats = [parse_beat(ln, f"shorts:{i}") for i, ln in enumerate(lines, 1) if "::" in ln and not ln.startswith("//")]
    text = " ".join(b["text"] for b in beats)
    toks = script_tokens(text, display)
    n = [norm(t) for t in toks]
    o, sb = 0, []
    for j, b in enumerate(beats):
        bt = script_tokens(b["text"], display)
        at = 0 if o == 0 else pick_at(toks, o, f"shorts ảnh {j + 1}")
        for s in b["stickers"]:
            got = resolve_at(s["at"], display, n, o, o + len(bt))
            if got is None:
                raise SystemExit(f"shorts ảnh {j + 1}: sticker at={s['at']!r} không nằm trong lời của ảnh")
            s["at"] = got
        sb.append({"at": at, "layout": b["layout"], "stickers": b["stickers"]})
        o += len(bt)
    return {"target_s": 53.0, "mood": mood, "text": text}, sb, [x.strip() for x in title.split("|")]


def main():
    P = Path(sys.argv[1]).resolve()
    C = P / "content"
    meta = json.loads((C / "meta.json").read_text(encoding="utf-8-sig"))
    chars = json.loads((C / "characters.json").read_text(encoding="utf-8-sig"))
    display = meta.get("display_fix", {})
    scenes = [parse_scene(f) for f in sorted(C.glob("s[0-9][0-9].md"))]
    ep_scenes, sb_long, warns = build_long(scenes, display)
    if (C / "shorts.md").exists():
        shorts, sb_shorts, title_lines = parse_shorts(C / "shorts.md", display)
    else:
        print("  !! chưa có content/shorts.md")
        shorts, sb_shorts, title_lines = {"target_s": 53.0, "mood": "don_dap", "text": ""}, [], ["?", "?"]
    ep = {k: v for k, v in meta.items() if k not in ("characters_doc",)}
    ep["longform"] = {"scenes": ep_scenes}
    ep["shorts"] = shorts
    (P / "episode.json").write_text(json.dumps(ep, ensure_ascii=False, indent=1), encoding="utf-8")
    sb = {"_doc": "SINH BỞI src/mega/build_from_content.py từ content/*.md — sửa content rồi chạy lại, KHÔNG sửa file này.",
          "characters": chars["characters"], "side_characters": chars.get("side_characters", []),
          "shorts_side_characters": chars.get("shorts_side_characters", []), "shorts_title_lines": title_lines,
          "skip_numbers": chars.get("skip_numbers", []), "long": sb_long, "shorts": sb_shorts}
    (P / "specs").mkdir(exist_ok=True)
    (P / "specs" / "storyboard.json").write_text(json.dumps(sb, ensure_ascii=False, indent=1), encoding="utf-8")
    nch = sum(len(re.sub(r"\[[^\]]+\]", "", q["text"])) for s in ep_scenes for q in s["parts"])
    print(f"{len(ep_scenes)} chương | {len(sb_long)} ảnh dài | {len(sb_shorts)} ảnh Shorts | {nch} ký tự lời "
          f"≈ {nch / CPS / 60:.1f} phút (+ intro/outro)")
    for s in ep_scenes:
        c = sum(len(re.sub(r"\[[^\]]+\]", "", q["text"])) for q in s["parts"])
        print(f"  {s['id']} {s['badge']:<18} {c:6d} ký tự ≈ {c / CPS / 60:4.1f}' | {sum(1 for b in sb_long if b['scene'] == s['id'])} ảnh")
    for w in warns:
        print("  !!", w)


if __name__ == "__main__":
    main()
