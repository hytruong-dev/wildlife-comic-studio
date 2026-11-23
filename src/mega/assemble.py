"""Mega Compilation — cut the published episodes, splice the new opening/bridges/finale, master, chapters, SEO, QA.

Spec: docs/strategy/MEGA_COMPILATION.md · skill: .agents/skills/core/mega-compilation/SKILL.md

The mega project is ALSO a normal episode project (episode.json + specs/storyboard.json) whose "scenes" are the NEW
parts only (scene01 opening, scene02..scene10 bridges, scene11 finale) + the mega Shorts. Those are voiced/drawn/rendered
with the normal tools (pipeline.py tts/align/spec/render --long). This script then builds the long video from
mega.json > timeline:  channel intro -> scene01 -> body of source #1 -> scene02 -> body of source #2 ... -> scene11 -> outro.

  python src/mega/assemble.py check  projects/<mega>          # cut points vs transcripts, forbidden words, est. length
  python src/mega/assemble.py plan   projects/<mega>          # timeline + chapters (no encoding; bridges estimated if not rendered)
  python src/mega/assemble.py build  projects/<mega> [--force] [--preset medium]   # -> renders/<slug>_mega.mp4
  python src/mega/assemble.py seo    projects/<mega>          # chapters from the real build -> upload.json, seo_package.md
  python src/mega/assemble.py qa     projects/<mega>          # duration 60-80 min, loudness, chapters, shorts
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
CHANNEL = json.loads((ROOT / "config" / "channel.json").read_text(encoding="utf-8"))

# words that must NOT survive inside a kept source range (old per-episode CTA / teaser / recap — rule 2.2.1)
FORBIDDEN = r"tập trước|tập sau|tập tiếp theo|tập phim|tập \d+|tập (một|hai|ba|bốn|năm|sáu|bảy|tám|chín|mười)\b|đăng ký|đăng kí|subscribe|" \
            r"chuông|bấm ngay|nhấn đăng|hẹn gặp lại|bình luận|hành trình khám phá|qua những nét vẽ hôm nay|phút thứ|video hôm nay"
FADE = 0.20          # dip-to-white at every cut (page-turn feel, hides mid-drawing cuts)
AFADE = 0.06         # de-click
ENC = ["-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
       "-video_track_timescale", "15360"]


def jload(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def jsave(p: Path, d) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def dur(p: Path) -> float:
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                         text=True).strip())


def fmt_ts(s: float) -> str:
    s = int(round(s))
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60:02d}:{s % 60:02d}"


def run(cmd: list[str]) -> None:
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *cmd], check=True)


def load(P: Path):
    mega = jload(P / "mega.json")
    src = {s["slug"]: s for s in mega["sources"]}
    ep = jload(P / "episode.json")
    scenes = {s["id"]: s for s in ep["longform"]["scenes"]}
    return mega, src, ep, scenes


def kept_text(P: Path, slug: str, rng: list[float]) -> tuple[str, str, str]:
    """(full text inside range, first words, last words) from the source transcript."""
    d = jload(P / "sources" / f"{slug}.words.json")
    ws = [w for s in d["segments"] for w in s["words"] if rng[0] - 0.05 <= w["s"] and w["e"] <= rng[1] + 0.05]
    txt = " ".join(w["w"] for w in ws)
    return txt, " ".join(w["w"] for w in ws[:14]), " ".join(w["w"] for w in ws[-14:])


def bridge_seconds(P: Path, ep: dict, sid: str) -> tuple[float, bool]:
    """Real duration if voiced, else estimate (17.6 chars/s at tempo 1.0, avg tempo 1.12 + 0.4 s lead + gaps)."""
    f = P / "audio" / f"{sid}_parts_duration.json"
    if f.exists():
        return jload(f)["total_duration"], True
    sc = next(s for s in ep["longform"]["scenes"] if s["id"] == sid)
    n = sum(len(re.sub(r"\[[^\]]+\]", "", p["text"] if isinstance(p, dict) else p)) for p in sc["parts"])
    return n / (17.6 * 1.12) + 0.4 + 0.35 * (len(sc["parts"]) - 1), False


def timeline_items(P: Path, mega: dict, src: dict, ep: dict, real: bool = False) -> list[dict]:
    """Flatten the timeline into encodable items with durations (estimated or measured)."""
    items = []
    intro_d, outro_d = dur(ROOT / CHANNEL["intro"]), dur(ROOT / CHANNEL["outro"])
    for k, t in enumerate(mega["timeline"]):
        if t["type"] == "intro":
            items.append({"kind": "intro", "dur": intro_d, "chapter": t.get("chapter")})
        elif t["type"] == "outro":
            items.append({"kind": "outro", "dur": outro_d, "chapter": t.get("chapter")})
        elif t["type"] == "bridge":
            d, ok = bridge_seconds(P, ep, t["scene"])
            items.append({"kind": "bridge", "scene": t["scene"], "dur": d, "measured": ok, "chapter": t.get("chapter")})
        elif t["type"] == "source":
            for j, r in enumerate(t["keep"]):
                items.append({"kind": "source", "slug": t["slug"], "range": r, "dur": r[1] - r[0], "part": j,
                              "chapter": t.get("chapter") if j == 0 else None})
        else:
            raise SystemExit(f"timeline[{k}]: unknown type {t['type']}")
    return items


# ----------------------------------------------------------------------------- check / plan

def snap(sil: list, t: float, kind: str, win: float = 0.9) -> float | None:
    """Move a cut point into the nearest voice pause (silences.py). in-point -> just before speech resumes,
    out-point -> just after speech stops. None if no pause within ±win s."""
    def gap(p):  # 0 if t is inside the pause, else distance to its nearest edge
        return 0.0 if p[0] <= t <= p[1] else min(abs(t - p[0]), abs(t - p[1]))
    cands = [p for p in sil if p[1] - p[0] >= 0.12 and gap(p) <= win]
    if not cands:
        return None
    a, b = min(cands, key=gap)
    return round(max(a, b - 0.15), 2) if kind == "in" else round(min(b, a + 0.15), 2)


def cmd_check(P: Path, argv: list[str]) -> None:
    mega, src, ep, scenes = load(P)
    errs, warns = [], []
    if "--snap" in argv:  # rewrite every keep range onto voice pauses, then continue checking
        changed = 0
        for t in mega["timeline"]:
            if t["type"] != "source":
                continue
            sf = P / "sources" / f"{t['slug']}.silences.json"
            if not sf.exists():
                raise SystemExit(f"{sf.name} missing -> python src/mega/silences.py {P.as_posix()}")
            sil = jload(sf)
            for r in t["keep"]:
                for i, kind in ((0, "in"), (1, "out")):
                    s = snap(sil, r[i], kind)
                    if s is None:
                        warns.append(f"{t['slug']} {kind} {r[i]:.2f}s: không có khoảng lặng trong ±0.9s — chọn mốc khác")
                    elif abs(s - r[i]) > 0.01:
                        r[i] = s
                        changed += 1
        jsave(P / "mega.json", mega)
        print(f"snap: {changed} cut points moved onto voice pauses -> mega.json")
    used = []
    order = [t for t in mega["timeline"] if t["type"] == "source"]
    if mega["timeline"][0]["type"] != "intro" or mega["timeline"][-1]["type"] != "outro":
        errs.append("timeline must start with intro and end with outro (1 channel intro + 1 outro only — rule 2.2.1)")
    for i, t in enumerate(mega["timeline"][1:-1], 1):  # sources and bridges must alternate (no 2 bodies glued together)
        prev = mega["timeline"][i - 1]["type"]
        if t["type"] == "source" and prev == "source":
            errs.append(f"timeline[{i}] {t['slug']}: two source bodies in a row — put a bridge between them (rule 2.2.3)")
    for t in mega["timeline"]:
        if t["type"] == "bridge" and t["scene"] not in scenes:
            errs.append(f"bridge {t['scene']} not in episode.json longform.scenes")
    for t in order:
        s = src.get(t["slug"])
        if not s:
            errs.append(f"{t['slug']} not in mega.json sources"); continue
        used.append(t["slug"])
        f = ROOT / s["file"]
        if not f.exists():
            errs.append(f"{t['slug']}: missing file {s['file']}"); continue
        tr = P / "sources" / f"{t['slug']}.words.json"
        if not tr.exists():
            errs.append(f"{t['slug']}: no transcript — run src/mega/transcribe_sources.py"); continue
        D = jload(tr)["duration_s"]
        last = 0.0
        for j, r in enumerate(t["keep"]):
            if not (0 <= r[0] < r[1] <= D) or r[0] < last:
                errs.append(f"{t['slug']} keep[{j}] {r} invalid (duration {D:.1f}s, ranges must be increasing)")
            last = r[1]
            txt, first, lastw = kept_text(P, t["slug"], r)
            print(f"  {t['slug']:22s} keep[{j}] {r[0]:7.2f}-{r[1]:7.2f} ({r[1] - r[0]:5.1f}s)")
            print(f"      IN : {first} ...")
            print(f"      OUT: ... {lastw}")
            for m in re.finditer(FORBIDDEN, txt, flags=re.IGNORECASE):
                ctx = txt[max(0, m.start() - 60):m.end() + 40].replace("\n", " ")
                warns.append(f"{t['slug']} keep[{j}]: '{m.group(0)}' còn trong đoạn giữ lại → kiểm tra: …{ctx}…")
        if t["keep"][0][0] < 9.5:
            warns.append(f"{t['slug']}: in-point {t['keep'][0][0]:.2f}s < intro 10 s — intro kênh của tập lẻ bị lọt vào (rule 2.2.1)")
        if D - t["keep"][-1][1] < 15:
            warns.append(f"{t['slug']}: out-point chỉ cách cuối {D - t['keep'][-1][1]:.1f}s — teaser/outro tập lẻ có thể bị lọt")
    dup = {x for x in used if used.count(x) > 1}
    if dup:
        errs.append(f"source used twice: {dup}")
    miss = [s for s in src if s not in used]
    if miss:
        errs.append(f"sources not in timeline: {miss}")
    if [t["slug"] for t in order] == sorted(used, key=lambda x: src[x]["ep"]):
        errs.append("order = publishing order (Tập 1 → 10) — forbidden: reorder as countdown / tier list (rule 2.2.2)")
    items = timeline_items(P, mega, src, ep)
    total = sum(x["dur"] for x in items)
    lo, hi = mega.get("target_min", [60, 80])
    print(f"\nestimated length {fmt_ts(total)} (target {lo}-{hi} min)")
    if not lo * 60 <= total <= hi * 60:
        errs.append(f"length {total / 60:.1f} min outside {lo}-{hi} min — trim keep ranges (moral/recap first) or add a source")
    for w in warns:
        print("  !!", w)
    for e in errs:
        print("  XX", e)
    print("CHECK", "FAIL" if errs else ("OK (read the !! lines)" if warns else "OK"))
    if errs:
        raise SystemExit(1)


def chapters_from(items: list[dict]) -> list[tuple[float, str]]:
    t, out = 0.0, []
    for x in items:
        if x.get("chapter"):
            out.append((t, x["chapter"]))
        t += x["dur"]
    if not out or out[0][0] != 0:
        out.insert(0, (0.0, "Mở đầu"))
    return out


def cmd_plan(P: Path, argv: list[str]) -> None:
    mega, src, ep, scenes = load(P)
    items = timeline_items(P, mega, src, ep)
    t = 0.0
    for x in items:
        name = x.get("scene") or x.get("slug") or x["kind"]
        extra = f" keep {x['range'][0]:.2f}-{x['range'][1]:.2f}" if x["kind"] == "source" else ""
        est = "" if x["kind"] != "bridge" or x["measured"] else "  (ước lượng — chưa có giọng)"
        print(f"{fmt_ts(t):>8}  {x['kind']:6s} {name:22s} {x['dur']:7.1f}s{extra}{est}")
        t += x["dur"]
    print(f"TOTAL {fmt_ts(t)}\n\nCHAPTERS:")
    for s, c in chapters_from(items):
        print(f"{fmt_ts(s)} {c}")


# ----------------------------------------------------------------------------- build

def norm_intro(src: Path, dst: Path) -> Path:
    if not dst.exists():
        run(["-i", str(src), "-vf", "scale=1920:1080:flags=lanczos,setsar=1,fps=30,format=yuv420p",
             "-af", "aformat=sample_rates=48000:channel_layouts=stereo,loudnorm=I=-16:TP=-1.5", *ENC, "-preset", "medium", str(dst)])
    return dst


def cut_source(src: Path, rng: list[float], dst: Path, preset: str) -> Path:
    a, b = rng
    d = b - a
    vf = (f"scale=1920:1080:flags=lanczos,setsar=1,fps=30,format=yuv420p,"
          f"fade=t=in:st=0:d={FADE}:color=white,fade=t=out:st={d - FADE:.3f}:d={FADE}:color=white")
    af = (f"aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,afade=t=in:st=0:d={AFADE},"
          f"afade=t=out:st={d - AFADE:.3f}:d={AFADE},loudnorm=I=-14:TP=-1.5:LRA=11")
    run(["-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", str(src), "-vf", vf, "-af", af, *ENC, "-preset", preset, str(dst)])
    return dst


def bridge_clip(scene_mkv: Path, dst: Path, preset: str) -> Path:
    """Rendered bridge scene (voice + SFX, no BGM) -> + ducked BGM like the normal master, loudnorm -14."""
    bgm = ROOT / CHANNEL["bgm"]
    d = dur(scene_mkv)
    run(["-i", str(scene_mkv), "-stream_loop", "-1", "-i", str(bgm), "-filter_complex",
         "[0:a]asplit=2[a][sc];[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,volume=0.14[bg];"
         "[bg][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[bgd];"
         f"[a][bgd]amix=inputs=2:duration=first:normalize=0,afade=t=out:st={d - 0.25:.3f}:d=0.25,loudnorm=I=-14:TP=-1.5:LRA=9[ao]",
         "-map", "0:v", "-map", "[ao]", "-vf", "fps=30,format=yuv420p,setsar=1", *ENC, "-preset", preset, "-t", f"{d:.3f}", str(dst)])
    return dst


def cmd_build(P: Path, argv: list[str]) -> None:
    mega, src, ep, scenes = load(P)
    preset = argv[argv.index("--preset") + 1] if "--preset" in argv else "medium"
    force = "--force" in argv
    W = P / "renders" / "mega_parts"
    W.mkdir(parents=True, exist_ok=True)
    items = timeline_items(P, mega, src, ep)
    miss = [x["scene"] for x in items if x["kind"] == "bridge" and not (P / "renders/long_v2" / f"{x['scene']}.mkv").exists()]
    if miss:
        raise SystemExit(f"bridges not rendered yet: {miss} -> python src/episode/pipeline.py render {P.as_posix()} --long")
    files = []
    for k, x in enumerate(items):
        if x["kind"] == "intro":
            f = norm_intro(ROOT / CHANNEL["intro"], W / "intro.mp4")
        elif x["kind"] == "outro":
            f = norm_intro(ROOT / CHANNEL["outro"], W / "outro.mp4")
        elif x["kind"] == "bridge":
            f = W / f"{k:02d}_{x['scene']}.mp4"
            if force or not f.exists():
                print(f"[{k:02d}] bridge {x['scene']}", flush=True)
                bridge_clip(P / "renders/long_v2" / f"{x['scene']}.mkv", f, preset)
        else:
            f = W / f"{k:02d}_{x['slug']}_{x['part']}.mp4"
            if force or not f.exists():
                print(f"[{k:02d}] cut {x['slug']} {x['range']}", flush=True)
                cut_source(ROOT / src[x["slug"]]["file"], x["range"], f, preset)
        x["file"] = str(f)
        x["dur"] = dur(f)
        files.append(f)
    lst = W / "_concat.txt"
    lst.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in files), encoding="utf-8")
    out = P / "renders" / f"{P.name}_mega.mp4"
    run(["-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", str(out)])
    jsave(P / "renders" / "mega_timeline.json", [{k: v for k, v in x.items()} for x in items])
    print(f"MEGA: {out}  {fmt_ts(dur(out))}")
    print("next: python src/mega/assemble.py seo|qa", P.as_posix())


# ----------------------------------------------------------------------------- seo / qa

def cmd_seo(P: Path, argv: list[str]) -> None:
    mega, src, ep, scenes = load(P)
    tl = P / "renders" / "mega_timeline.json"
    items = jload(tl) if tl.exists() else timeline_items(P, mega, src, ep)
    if not tl.exists():
        print("!! chưa build — mốc chương đang là ƯỚC LƯỢNG; chạy lại seo sau khi build")
    total = sum(x["dur"] for x in items)
    chaps = chapters_from(items)
    seo = ep["seo"]
    minutes = int(total // 60)
    title = seo["title"].replace("{MINUTES}", str(minutes))
    assert len(title) <= 100, f"title {len(title)} > 100 chars"
    links = "\n".join(f"👉 {x}" for x in CHANNEL.get("previous_episodes", []))
    # mid-roll suggestions: start of every bridge after the opening (natural pause, never mid-sentence)
    t, mids = 0.0, []
    for x in items:
        if x["kind"] == "bridge" and x["scene"] != "scene01" and t > 120:
            mids.append(t)
        t += x["dur"]
    desc = (f"{seo['hook_paragraph']}\n\n⏱️ MỤC LỤC (bấm để nhảy tới con vật bạn muốn xem):\n"
            + "\n".join(f"{fmt_ts(s)} {c}" for s, c in chaps)
            + "\n\n🏆 BẢNG XẾP HẠNG:\n" + "\n".join(f"• {b}" for b in seo["bullets"])
            + f"\n\n🎬 Xem từng tập đầy đủ:\n{links}"
            + f"\n\n💬 {seo['question']}\n🔔 Đăng ký kênh {CHANNEL['name']}: {seo.get('next_teaser', '')}\n\n{' '.join(seo['hashtags'])}")
    up = {"long": {"file": str(P / "renders" / f"{P.name}_mega.mp4"), "thumb": str(P / "renders" / f"{P.name}_thumbnail.jpg"),
                   "title": title, "desc": desc, "tags": ", ".join(seo["tags"]), "pinned_comment": seo["question"]},
          "shorts": {"file": str(P / "renders" / f"{P.name}_shorts.mp4"), "title": seo["shorts_title"],
                     "desc": seo["shorts_desc"] + "\n\n" + " ".join(["#shorts", *seo["hashtags"]]), "tags": ", ".join(seo["shorts_tags"])},
          "mid_roll_s": [round(m, 1) for m in mids]}
    assert len(up["long"]["tags"]) <= 480, "tags > 500 chars"
    jsave(P / "upload.json", up)
    (P / "seo_package.md").write_text(
        f"# {title}\n\n## Mô tả\n```\n{desc}\n```\n\n## Tags\n{up['long']['tags']}\n\n## Ghim bình luận\n{seo['question']}\n\n"
        f"## Điểm quảng cáo giữa video (mid-roll, đặt tay trong YouTube Studio khi kênh bật kiếm tiền)\n"
        + "\n".join(f"- {fmt_ts(m)}" for m in mids)
        + f"\n\n## Shorts\n**{seo['shorts_title']}**\n```\n{up['shorts']['desc']}\n```\n\n"
        f"## Lịch đăng\n{mega.get('publish_note', '')}\n\n⛔ Không tự đăng — chờ chủ kênh ra lệnh kèm giờ.\n", encoding="utf-8")
    print("\n".join(f"{fmt_ts(s)} {c}" for s, c in chaps))
    print(f"title ({len(title)}): {title}\n-> upload.json + seo_package.md")
    print(f"upload ONLY when the owner says so: node src/episode/upload_youtube.cjs {P.as_posix()} --date YYYY-MM-DD --time HH:MM")


def loudness(p: Path) -> tuple[float, float]:
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(p), "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True, text=True, encoding="utf-8", errors="ignore").stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1]), float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", out)[-1])


def cmd_qa(P: Path, argv: list[str]) -> None:
    mega = jload(P / "mega.json")
    lo, hi = mega.get("target_min", [60, 80])
    ok = True
    for kind, f, dlo, dhi, llo, lhi in (("mega", P / "renders" / f"{P.name}_mega.mp4", lo * 60, hi * 60, -15.5, -12.5),
                                         ("shorts", P / "renders" / f"{P.name}_shorts.mp4", 40, 59.5, -20.0, -13.0)):
        if not f.exists():
            print(f"[{kind}] MISSING {f}"); ok = False; continue
        d = dur(f)
        i, tp = loudness(f)
        v = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate",
                                     "-of", "csv=p=0", str(f)], text=True).strip()
        good = dlo <= d <= dhi and llo <= i <= lhi and tp <= -1.0
        ok &= good
        print(f"[{kind}] {fmt_ts(d)}  {v}  {i:.1f} LUFS  TP {tp:.1f}  -> {'PASS' if good else 'FAIL'}")
    tl = P / "renders" / "mega_timeline.json"
    if tl.exists():
        ch = chapters_from(jload(tl))
        short = [c for (s, c), (s2, _) in zip(ch, ch[1:] + [(1e9, "")]) if s2 - s < 10]
        good = len(ch) >= 3 and ch[0][0] == 0 and not short
        ok &= good
        print(f"[chapters] {len(ch)} chương, bắt đầu 00:00, mỗi chương ≥ 10s -> {'PASS' if good else 'FAIL ' + str(short)}")
    print("QA", "PASS" if ok else "FAIL — fix before publishing")


STAGES = {"check": cmd_check, "plan": cmd_plan, "build": cmd_build, "seo": cmd_seo, "qa": cmd_qa}

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in STAGES:
        print(__doc__)
        raise SystemExit(1)
    STAGES[sys.argv[1]](Path(sys.argv[2]).resolve(), sys.argv[3:])
