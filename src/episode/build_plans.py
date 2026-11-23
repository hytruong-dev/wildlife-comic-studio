"""Storyboard -> plans + Gemini prompts (chuẩn Tập 9 Chim Cánh Cụt).

  python src/episode/build_plans.py projects/<slug>

Đọc  projects/<slug>/specs/storyboard.json   (người/AI viết — mỗi câu thoại = 1 beat = 1 ảnh)
Ghi  specs/longform_plan.json, specs/shorts_plan.json   (pipeline.py spec đọc)
     specs/image_prompts.json   (_first_long, _first_shorts, L01.., S01.. — src/episode/gemini_gen.cjs gửi lên Gemini)
     specs/image_catalog.md     (ảnh <-> lời thoại khi ảnh hiện)

Kiểm tra TRƯỚC khi tạo giọng/ảnh (chạy được ngay sau khi viết kịch bản, không cần audio):
  - mọi cụm 'at' có trong lời (dạng phụ đề, đã qua display_fix) và xuất hiện LẦN ĐẦU sau beat trước
    (pipeline.spec tìm lần xuất hiện đầu tiên -> cụm trùng lặp làm beat nhảy ngược)
  - mọi sticker có target [x,y] và con số được đọc trong lúc ảnh đang hiện
  - lời thoại nguyên văn của từng ảnh được chép vào prompt (Gemini vẽ đúng ý hơn hẳn)

storyboard.json (xem examples/ep09_reference/storyboard.json):
{
 "characters": {"HERO": "mô tả đầy đủ nhân vật chính", "HERO_S": "mô tả ngắn", "NO_HERO": "KHÔNG có ... trong cảnh này", "JUDGE": "..."},
 "side_characters": ["JUDGE"],            # đưa vào prompt mở chat
 "shorts_title_lines": ["DÒNG 1", "DÒNG 2?!"],
 "skip_numbers": [],                      # số ảnh L bỏ khỏi plan nhưng giữ số (ảnh đã tạo rồi bị gộp beat)
 "long":   [{"scene": "scene01", "at": 0, "layout": "Bố cục... {HERO} ...", "stickers": [{"at": "-40°C", "side": "R", "y": 360,
             "value": "-40°C", "label": "lạnh thấu xương", "target": [0.78, 0.6]}], "impacts": [], "id": "L85 (tùy chọn)"}],
 "shorts": [{"at": 0, "layout": "...", "stickers": [...], "id": "S13 (tùy chọn)"}]
}
'id' chỉ dùng khi CHÈN beat mới sau khi đã tạo ảnh: các beat khác giữ nguyên số, ảnh cũ không bị lệch tên.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline import norm, ptext, script_tokens  # noqa: E402
from prompt_sanitizer import sanitize_prompt  # noqa: E402

# TASTE-73: Cho phép visual_style tùy biến theo từng tập (mỗi tập 1 phong cách vẽ riêng biệt)
DEFAULT_STYLE = ("tỉ lệ {AR}; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, "
                 "màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, "
                 "không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng")



def fill(s: str, chars: dict) -> str:
    for k in sorted(chars, key=len, reverse=True):  # HERO_S before HERO
        s = s.replace("{" + k + "}", chars[k])
    if "{" in s and "}" in s:
        raise SystemExit(f"unknown placeholder in: {s[:120]}")
    return s


def find(toks: list[str], phrase, after: int = 0) -> int:
    if phrase in (0, "0", ""):
        return 0
    want = [norm(x) for x in str(phrase).split() if norm(x)]
    n = [norm(t) for t in toks]
    for i in range(after, len(toks) - len(want) + 1):
        if n[i:i + len(want)] == want:
            return i
    raise SystemExit(f"phrase not found: {phrase!r} — chép đúng chữ trong lời đọc (dạng phụ đề: số đã qua display_fix)")


def stickers(sts: list, toks: list[str], lo: int, hi: int, where: str) -> list:
    out = []
    for s in sts:
        if not s.get("target"):
            raise SystemExit(f"{where}: sticker {s.get('value')} thiếu target [x,y] (luật 4 — không có mũi tên)")
        i = find(toks, s["at"], lo)
        if i >= hi:
            print(f"  !! {where}: sticker {s['at']!r} được đọc sau khi ảnh đã chuyển")
        if len(str(s["value"])) > 10 or len(s["label"]) > 22:
            print(f"  !! {where}: sticker quá dài (value ≤ 10, label ≤ 22 ký tự)")
        out.append({k: s[k] for k in ("at", "side", "y", "value", "label", "target")})
    if len(out) > 2:
        print(f"  !! {where}: > 2 sticker trên 1 ảnh")
    return out


def main() -> None:
    P = Path(sys.argv[1]).resolve()
    ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
    sb = json.loads((P / "specs" / "storyboard.json").read_text(encoding="utf-8"))
    chars, display = sb["characters"], ep.get("display_fix", {})
    animal = ep["animal"]
    hero_s = chars.get("HERO_S", chars["HERO"])
    titles = {s["id"]: s for s in ep["longform"]["scenes"]}
    skip = set(sb.get("skip_numbers", []))
    art = ep.get("art", {}) or {}
    visual_style = art.get("visual_style") or sb.get("visual_style")
    style_rule = visual_style or DEFAULT_STYLE
    style_label = art.get("style_label") or sb.get("style_label") or "quy chuẩn minh họa nghệ thuật độc bản"


    plan = {"_doc": "Sinh bởi src/episode/build_plans.py từ specs/storyboard.json — sửa storyboard rồi chạy lại.",
            "targets": {}, "scenes": {}}
    prompts, catalog = {}, []
    by_scene: dict = {}
    for b in sb["long"]:
        if b["scene"] not in titles:
            raise SystemExit(f"storyboard scene {b['scene']} không có trong episode.json")
        by_scene.setdefault(b["scene"], []).append(b)
    missing = [s for s in titles if s not in by_scene]
    if missing:
        raise SystemExit(f"chương chưa có beat: {missing}")
    n = 0
    for k, sid in enumerate(titles, 1):
        beats = by_scene[sid]
        toks = script_tokens(" ".join(ptext(x) for x in titles[sid]["parts"]), display)
        idx = []
        for b in beats:
            i = find(toks, b["at"])
            if b["at"] not in (0, "0", "") and idx and i <= idx[-1]:
                raise SystemExit(f"{sid}: cụm {b['at']!r} xuất hiện lần đầu TRƯỚC beat trước — chọn cụm khác (duy nhất trong chương)")
            if b["at"] in (0, "0", "") and idx:
                raise SystemExit(f"{sid}: chỉ beat đầu chương được có at = 0")
            idx.append(i)
        if idx[0] != 0:
            raise SystemExit(f"{sid}: beat đầu chương phải có at = 0")
        st = titles[sid]
        sp = {"chapter_no": k, "title": st["chapter_title"].split(":", 1)[-1].strip().upper(),
              "hook": st.get("hook", ""), "card": k != 1, "beats": []}
        if st.get("badge"):
            sp["badge"] = st["badge"]
        for j, b in enumerate(beats):
            if b.get("id"):
                img = b["id"]
            else:
                n += 1
                while n in skip:
                    n += 1
                img = f"L{n:02d}"
            if img in prompts:
                raise SystemExit(f"ảnh {img} bị dùng 2 lần (luật 1)")
            end = idx[j + 1] if j + 1 < len(beats) else len(toks)
            line = " ".join(toks[idx[j]:end])
            sp["beats"].append({"at": b["at"], "image": f"assets/long/{img}.png",
                                "stickers": stickers(b.get("stickers", []), toks, idx[j], end, f"{sid}/{img}"),
                                "impacts": b.get("impacts", [])})
            for imp in b.get("impacts", []):
                find(toks, imp, idx[j])
            raw_prompt = (f"HÌNH {img} (16:9 ngang, {style_label} và nhân vật {hero_s}; nền trắng tinh "
                          f"hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: \"{line}\". Bố cục: {fill(b['layout'], chars)}")
            prompts[img] = sanitize_prompt(raw_prompt)
            catalog.append(f"| {img} | {sid} | {line[:110]} |")
        plan["scenes"][sid] = sp

    stoks = script_tokens(ep["shorts"]["text"], display)
    sidx = []
    for b in sb["shorts"]:
        i = find(stoks, b["at"])
        if sidx and i <= sidx[-1]:
            raise SystemExit(f"shorts: cụm {b['at']!r} không đứng sau beat trước")
        sidx.append(i)
    splan = {"title_lines": sb["shorts_title_lines"], "beats": []}
    ks = 0
    for j, b in enumerate(sb["shorts"]):
        if b.get("id"):
            img = b["id"]
        else:
            ks += 1
            img = f"S{ks:02d}"
        end = sidx[j + 1] if j + 1 < len(sb["shorts"]) else len(stoks)
        bt = {"at": b["at"], "draw_s": b.get("draw_s", 1.0), "image": f"assets/shorts/{img}.png",
              "stickers": stickers(b.get("stickers", []), stoks, sidx[j], end, f"shorts/{img}")}
        if b.get("captions"):
            bt["captions"] = b["captions"]
        if j == 0:
            bt = {"at_s": 0.0, **{x: y for x, y in bt.items() if x != "at"}}
        splan["beats"].append(bt)
        line = " ".join(stoks[sidx[j]:end])
        raw_prompt = (f"HÌNH {img} (DỌC 9:16, {style_label} và nhân vật {hero_s}; nền trắng tinh "
                      f"hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). "
                      f"Lời thoại: \"{line}\". Bố cục: {fill(b['layout'], chars)}")
        prompts[img] = sanitize_prompt(raw_prompt)
        catalog.append(f"| {img} | shorts | {line[:110]} |")

    side = "; ".join(chars[c] for c in sb.get("side_characters", []))
    side_s = "; ".join(chars[c] for c in sb.get("shorts_side_characters", sb.get("side_characters", [])))
    n_long = sum(len(v) for v in by_scene.values())
    first_l = sanitize_prompt(f"Tạo hình ảnh (cảnh 1/{n_long} của video YouTube về {animal}). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: "
                              f"{style_rule.replace('{AR}', 'NGANG 16:9')}. NHÂN VẬT CHÍNH cố định: {chars['HERO']}. "
                              + (f"Nhân vật phụ cố định: {side}. " if side else ""))
    first_s = sanitize_prompt(f"Tạo hình ảnh (cảnh 1/{len(sb['shorts'])} của video YouTube Shorts về {animal}). QUY CHUẨN CHUNG cho mọi cảnh: "
                              f"{style_rule.replace('{AR}', 'DỌC 9:16')}. NHÂN VẬT CHÍNH cố định: {chars['HERO']}. "
                              + (f"Nhân vật phụ: {side_s}. " if side_s else ""))
    out = {"_first_long": first_l, "_first_shorts": first_s, **prompts}
    (P / "specs" / "longform_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
    (P / "specs" / "shorts_plan.json").write_text(json.dumps(splan, ensure_ascii=False, indent=1), encoding="utf-8")
    (P / "specs" / "image_prompts.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    (P / "specs" / "image_catalog.md").write_text("| Ảnh | Chương | Lời thoại khi ảnh hiện |\n|---|---|---|\n"
                                                  + "\n".join(catalog) + "\n", encoding="utf-8")
    nl = sum(1 for k in prompts if k.startswith("L"))
    print(f"plans OK: {nl} ảnh dài (16:9), {len(sb['shorts'])} ảnh Shorts (9:16), {len(prompts)} prompt -> specs/image_prompts.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(1)
    main()
