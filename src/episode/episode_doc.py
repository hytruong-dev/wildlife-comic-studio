"""Build the full production document of one episode from its real data -> projects/<slug>/EPISODE_SPEC.md

Everything another AI/editor needs to rebuild or extend the episode exactly: settings, VoiceStudio input text
(with emotion tags), display fixes, every long-form/Shorts beat with its time, the narration spoken while the image
is on screen, image file, Gemini prompt, stickers (value/label/side/y/target) and render/QA status.

usage: python src/episode/episode_doc.py projects/<slug>
Prompts come from specs/image_prompts.json (keep it updated when you generate images:
python scripts/harvest_prompts.py <chat transcript.jsonl> projects/<slug> [prompts.json ...]).
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
P = Path(sys.argv[1]).resolve()
J = lambda p: json.loads(p.read_text(encoding="utf-8")) if p.exists() else None
CH = J(ROOT / "config/channel.json")
ep = J(P / "episode.json")
lplan, splan = J(P / "specs/longform_plan.json"), J(P / "specs/shorts_plan.json")
lspec, sspec = J(P / "specs/longform_spec.json"), J(P / "specs/shorts_spec.json")
words = J(P / "audio/long_words_fixed.json") or {}
swords = J(P / "audio/shorts_words.json") or []
prompts = J(P / "specs/image_prompts.json") or {}
# fallback: what is really in the image (specs/image_catalog.md "| L01 | ... |") for images whose prompt was lost
_cat = P / "specs/image_catalog.md"
catalog = dict(re.findall(r"^\| ([LST]\d{2}) \| (.+?) \|\s*$", _cat.read_text(encoding="utf-8"), re.M)) if _cat.exists() else {}
voice = {**CH["voice"], **ep.get("voice", {})}


def ts(s: float) -> str:
    return f"{int(s // 60):02d}:{s % 60:04.1f}"


def probe(f: Path) -> str:
    if not f.exists():
        return "chưa render"
    d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                       str(f)], text=True))
    return f"{int(d // 60)}:{d % 60:04.1f} ({d:.1f}s)"


def esc(t: str) -> str:
    return t.replace("|", "\\|").replace("\n", " ")


L = []
w = L.append
slug = P.name
w(f"# {(ep.get('series_label') or 'TẬP %s' % ep['episode_no']).upper()} — {ep['animal'].upper()} · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`{slug}`)\n")
w("> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/" + slug + "`.")
w("> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.")
w("> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.\n")
if ep.get("format"):
    w(f"> **Format kể chuyện:** `{ep['format']}` · **Persona giọng:** `{ep.get('persona', '')}` "
      "(`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).\n")

w("## 1. Tổng quan & kết quả\n")
w("| Mục | Giá trị |\n|---|---|")
w(f"| Con vật | {ep['animal']} |")
w(f"| Tiêu đề YouTube | {esc(ep['seo']['title'])} |")
w(f"| Video dài | `renders/{slug}_long.mp4` — {probe(P / f'renders/{slug}_long.mp4')} |")
w(f"| Shorts | `renders/{slug}_shorts.mp4` — {probe(P / f'renders/{slug}_shorts.mp4')} |")
w(f"| Thumbnail | `renders/{slug}_thumbnail.jpg` |")
nl = sum(len(s['beats']) for s in lspec['scenes']) if lspec else 0
w(f"| Số hình | dài {nl} beat / {len({b['image'] for s in lspec['scenes'] for b in s['beats']}) if lspec else 0} ảnh riêng; "
  f"Shorts {len(sspec['beats']) if sspec else 0} beat |")
w(f"| Giọng | VoiceStudio OmniVoice, clone `{voice['reference']}`, speed {voice['speed']}, steps {voice['steps']}, "
  f"**tempo dài {voice.get('tempo_long', 1.0)}**, Shorts tempo tự tính (≥ {voice.get('tempo_shorts_min', 1.0)}) |")
w(f"| Thời lượng tối thiểu video dài | {ts(voice.get('min_long_s', 510))} (TASTE-61) |")
if (P / "upload_result.json").exists():
    up = J(P / "upload_result.json") or {}
    if up.get("long_url"):
        w(f"| YouTube Video Dài | [{up['long_url']}]({up['long_url']}) — Lên lịch: `{up.get('long_schedule', '')}` |")
    if up.get("shorts_url"):
        w(f"| YouTube Shorts | [{up['shorts_url']}]({up['shorts_url']}) — Lên lịch: `{up.get('shorts_schedule', '')}` |")
w("")

w("## 2. Nhân vật & quy chuẩn hình\n")
first = next((v for k, v in sorted(prompts.items()) if "QUY CHUẨN CHUNG" in v), "")
if first:
    w("Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:\n")
    w("```text\n" + first + "\n```\n")
w("Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; "
  "nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: \"<câu>\". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, "
  "biểu cảm, đạo cụ hình ảnh hóa con số>`\n")

w("## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)\n")
w("Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.\n")
for sc in ep["longform"]["scenes"]:
    meta = (lplan or {}).get("scenes", {}).get(sc["id"], {})
    w(f"### {sc['id']} — {meta.get('title', sc.get('chapter_title', ''))}")
    if meta.get("hook"):
        w(f"*Thẻ chương:* {meta['hook']}\n")
    if sc.get("badge") or sc.get("mood"):
        w(f"*Badge:* `{sc.get('badge', '')}` · *mood mặc định:* `{sc.get('mood', ep.get('persona', ''))}`\n")
    for i, p in enumerate(sc["parts"]):
        t = p["text"] if isinstance(p, dict) else p
        role = (f" · 🎭 cameo `{p['cast']}`" if isinstance(p, dict) and p.get("cast") else
                f" · mood `{p['mood']}`" if isinstance(p, dict) and p.get("mood") else "")
        w(f"**Part {i}** → `audio/vs/{sc['id']}_p{i}.wav` ({len(t)} ký tự){role}\n")
        w("```text\n" + t + "\n```")
    w("")
w("### Shorts → `audio/vs/shorts.wav`\n")
w("```text\n" + ep["shorts"]["text"] + "\n```\n")
w(f"**Whisper prompt:** `{ep.get('whisper_prompt', '')}`\n")
w("**display_fix (chữ đọc → chữ hiện trên phụ đề):**\n")
w("| Lời đọc | Phụ đề |\n|---|---|")
for k, v in ep.get("display_fix", {}).items():
    w(f"| {esc(k)} | {esc(v)} |")
w("")

w("## 4. Phân cảnh video dài — từng beat\n")
w("Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). "
  "Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).\n")
for sc in (lspec or {}).get("scenes", []):
    ws = words.get(sc["id"], [])
    w(f"### {sc['id']} · {sc.get('title', '')} · {sc['duration_s']:.1f}s")
    w("| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |\n|---|---|---|---|---|---|")
    bs = sc["beats"]
    for i, b in enumerate(bs):
        s = b["start_s"]
        e = bs[i + 1]["start_s"] if i + 1 < len(bs) else sc["duration_s"]
        txt = " ".join(x["w"] for x in ws if s - 0.05 <= x["s"] < e - 0.05)
        img = Path(b["image"]).stem
        st = "<br>".join(f"**{x['value']}** · {x.get('label', '')} · {x['side']}/{x['y']} · {x.get('target')}"
                         for x in b.get("stickers", []))
        pr = prompts.get(img, "")
        m = re.search(r"Bố cục:\s*(.*)", pr, re.S)
        pr = (m.group(1) if m else pr)[:420] or (f"_(nội dung ảnh)_ {catalog[img]}" if img in catalog else "")
        w(f"| {b['id'][-3:]} | {ts(s)}–{ts(e)} ({e - s:.1f}s) | {img} | {esc(txt)} | {esc(st)} | {esc(pr)} |")
    w("")

w("## 5. Phân cảnh Shorts — từng beat\n")
if sspec:
    w(f"Banner: **{' / '.join(sspec.get('title_lines', []))}** · giọng {sspec.get('voice_end_s', 0):.1f}s + đệm {sspec.get('outro_buffer_s', 0)}s\n")
    w("| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |\n|---|---|---|---|---|")
    bs = sspec["beats"]
    for i, b in enumerate(bs):
        s = b["start_s"]
        e = bs[i + 1]["start_s"] if i + 1 < len(bs) else sspec.get("voice_end_s", s + 5)
        txt = " ".join(x["word"] for x in swords if s - 0.05 <= x["start"] < e - 0.05)
        st = "<br>".join(f"**{x['value']}** · {x.get('label', '')} · {x['side']}/{x['y']} · {x.get('target')}"
                         for x in b.get("stickers", []))
        w(f"| {b['id']} | {ts(s)} | {Path(b['image']).stem} | {esc(txt)} | {esc(st)} |")
    w("")

w("## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)\n")
if prompts:
    for k, v in sorted(prompts.items()):
        w(f"<details><summary>{k}</summary>\n\n```text\n{v}\n```\n</details>\n")
else:
    w("_Chưa có `specs/image_prompts.json` — chạy `scripts/harvest_prompts.py`._\n")

w("## 7. SEO\n")
seo = ep["seo"]
for k in ("title", "hook_paragraph", "question", "next_teaser", "shorts_title", "shorts_desc"):
    if seo.get(k):
        w(f"- **{k}:** {seo[k]}")
if seo.get("bullets"):
    w("- **bullets:** " + " · ".join(seo["bullets"]))
if seo.get("tags"):
    w("- **tags:** " + ", ".join(seo["tags"]))
if seo.get("hashtags"):
    w("- **hashtags:** " + " ".join(seo["hashtags"]))
w("")

w("## 8. Lệnh tái tạo tập này (theo thứ tự)\n")
w("```bash\n"
  f"python src/episode/pipeline.py check  projects/{slug}\n"
  f"python src/episode/pipeline.py tts    projects/{slug}     # chạy nền; part đã có trong audio/vs/ được giữ\n"
  f"python src/episode/pipeline.py align  projects/{slug}     # match >= 0.9 mỗi chương\n"
  f"python src/episode/pipeline.py spec   projects/{slug}     # phải in 'spec OK'\n"
  f"python scripts/audit_beats.py projects/{slug}              # Image reuse: {{}} ; mọi hold 3-15s\n"
  f"python src/episode/pipeline.py render projects/{slug} --force\n"
  f"python scripts/beat_sheet.py projects/{slug}               # xem renders/beat_audit/sceneXX.jpg\n"
  f"python scripts/hum_probe.py projects/{slug}/audio/shorts.wav projects/{slug}/renders/{slug}_shorts.mp4\n"
  f"python src/episode/pipeline.py qa     projects/{slug}\n"
  f"python src/episode/pipeline.py seo    projects/{slug}\n"
  f"python src/episode/episode_doc.py     projects/{slug}\n"
  "```\n")

out = P / "EPISODE_SPEC.md"
out.write_text("\n".join(L), encoding="utf-8")
print(out, f"{len(L)} lines")

