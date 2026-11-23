"""Episode Pipeline — Vẽ Chuyện Hoang Dã (golden path distilled from EP06 Gấu Nước).

One command per stage, every stage is idempotent (cached) and driven by files inside
projects/<slug>/ :

  episode.json            narration text (long-form scenes + Shorts), SEO, voice settings
  specs/longform_plan.json  beats: phrase -> image, stickers (callouts + arrow targets), impacts
  specs/shorts_plan.json    same for the 9:16 Shorts

Usage:
  python src/episode/pipeline.py init   projects/tap-07-tom-tit --no 7 --animal "Tôm Tít"
  python src/episode/pipeline.py check  projects/<slug>     # VoiceStudio ready, files, missing images
  python src/episode/pipeline.py tts    projects/<slug>     # VoiceStudio (local OmniVoice clone) -> audio/sceneXX.wav, shorts.wav
  python src/episode/pipeline.py align  projects/<slug>     # Whisper word stamps + script spelling
  python src/episode/pipeline.py spec   projects/<slug>     # plans -> render specs (phrase-timed)
  python src/episode/pipeline.py render projects/<slug> [--long|--shorts] [--preview] [--force]
  python src/episode/pipeline.py qa     projects/<slug>     # loudness, freeze, duration gates
  python src/episode/pipeline.py seo    projects/<slug>     # chapters + upload.json (NO upload)
  python src/episode/pipeline.py status projects/<slug>
"""
from __future__ import annotations

import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import unicodedata
import uuid
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
CHANNEL = json.loads((ROOT / "config" / "channel.json").read_text(encoding="utf-8"))
_LOCAL = ROOT / "config" / "local.json"  # riêng từng máy (không lên git): chrome_profile, voice.voicestudio_python...
if _LOCAL.exists():
    for _k, _v in json.loads(_LOCAL.read_text(encoding="utf-8-sig")).items():
        CHANNEL[_k] = {**CHANNEL[_k], **_v} if isinstance(_v, dict) and isinstance(CHANNEL.get(_k), dict) else _v

# ----------------------------------------------------------------------------- helpers

def jload(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def jsave(p: Path, d) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")

def dur(p: Path) -> float:
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", str(p)], text=True).strip())

def ff(*args: str) -> None:
    subprocess.run(["ffmpeg", "-y", "-v", "error", *args], check=True)

def norm(w: str) -> str:
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn").replace("đ", "d")
    return re.sub(r"[^a-z0-9]", "", w)

# ----------------------------------------------------------------------------- voice personas
# docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md — a part is either a plain string (scene/episode mood) or
# {"text": "...", "mood": "tram_bi_an"} / {"text": "...", "cast": "tham_phan"} / + optional "tempo", "speed".
_VP = ROOT / "config" / "voice_personas.json"
PERSONAS = json.loads(_VP.read_text(encoding="utf-8")) if _VP.exists() else {"moods": {}, "cast": {}, "personas": {}}

def ptext(p) -> str:
    return p["text"] if isinstance(p, dict) else p

def part_voice(ep: dict, sc: dict | None, p, v: dict) -> dict:
    """Resolve ref/instruct/speed/tempo for one part: part > scene > persona default > channel."""
    d = p if isinstance(p, dict) else {}
    persona = PERSONAS["personas"].get(ep.get("persona", ""), {})
    out = {"ref": v["reference"], "instruct": None, "speed": v.get("speed", 1.0), "tempo": v.get("tempo_long", 1.0),
           "mood": None, "cast": None}
    if d.get("cast"):
        c = PERSONAS["cast"][d["cast"]]
        out.update(ref=c.get("ref"), instruct=c.get("instruct"), speed=c.get("speed", 1.0),
                   tempo=c.get("tempo", v.get("tempo_long", 1.0)), cast=d["cast"])
    else:
        mood = d.get("mood") or (sc or {}).get("mood") or ep.get("default_mood") or persona.get("default_mood")
        if mood:
            m = PERSONAS["moods"][mood]
            out.update(ref=m.get("ref", v["reference"]), instruct=m.get("instruct"), speed=m.get("speed", out["speed"]),
                       tempo=m.get("tempo", out["tempo"]), mood=mood)
    for k in ("speed", "tempo", "instruct"):
        if k in d:
            out[k] = d[k]
    return out

def voicestudio() -> tuple[Path, Path]:
    """(python.exe of VoiceStudio's venv, reference clip). Exits with a clear message if missing."""
    import os
    v = CHANNEL["voice"]
    py = Path(os.path.expandvars(v["voicestudio_python"]))
    ref = ROOT / v["reference"]
    if not py.exists():
        raise SystemExit(f"VoiceStudio not found: {py}\nInstall VoiceStudio (https://voicestudio.sh), open it once, "
                         "download the OmniVoice model, then fix config/channel.json > voice.voicestudio_python")
    if not ref.exists() or not ref.with_suffix(".txt").exists():
        raise SystemExit(f"Missing voice reference {ref} (+ .txt transcript) — see assets/voice_refs/")
    return py, ref

def fmt_ts(s: float) -> str:
    s = int(s)
    return f"{s // 60:02d}:{s % 60:02d}"

# ----------------------------------------------------------------------------- init

TEMPLATE = ROOT / "templates" / "episode"

def cmd_init(P: Path, argv: list[str]) -> None:
    no = int(argv[argv.index("--no") + 1]) if "--no" in argv else 0
    animal = argv[argv.index("--animal") + 1] if "--animal" in argv else "?"
    if (P / "episode.json").exists():
        raise SystemExit(f"{P}/episode.json already exists")
    for d in ["audio/vs", "assets/long", "assets/shorts", "assets/inbox", "specs", "renders/snapshots", "scripts"]:
        (P / d).mkdir(parents=True, exist_ok=True)
    road = {e["ep"]: e for e in jload(ROOT / "config" / "series_roadmap.json")["episodes"]}.get(no, {})
    for f in TEMPLATE.glob("*.json"):
        if f.name.endswith("_plan.json"):  # plans are generated by src/episode/build_plans.py from storyboard.json
            continue
        txt = f.read_text(encoding="utf-8").replace("{{NO}}", f"{no:02d}").replace("{{NO_INT}}", str(no)) \
            .replace("{{ANIMAL}}", animal).replace("{{SLUG}}", P.name) \
            .replace("{{FORMAT}}", road.get("format", "F?")).replace("{{PERSONA}}", road.get("persona", "?")) \
            .replace("{{ANGLE}}", road.get("angle", "").replace('"', "'").replace("\\", "")) \
            .replace("{{SHORTS_IDEA}}", road.get("shorts", "").replace('"', "'").replace("\\", ""))
        dst = (P / "specs" / f.name) if f.name == "storyboard.json" else (P / f.name)
        dst.write_text(txt, encoding="utf-8")
    print(f"initialised {P} — format {road.get('format')} / persona {road.get('persona')} (config/series_roadmap.json).\n"
          f"Next: write episode.json (script) -> pipeline.py check -> specs/storyboard.json -> src/episode/build_plans.py")

# ----------------------------------------------------------------------------- TTS

def synth(jobs: list[tuple], v: dict) -> None:
    """Run all missing clips in ONE VoiceStudio process (model loads once). Cached: existing wavs are skipped.
    jobs = (text, out) or (text, out, {"ref", "instruct", "speed"}) for persona/cameo parts."""
    py, ref = voicestudio()
    todo = []
    for j in jobs:
        t, o, pv = j[0], j[1], (j[2] if len(j) > 2 else {})
        if o.exists():
            continue
        x = {"text": t, "out": str(o)}
        if pv:
            x["ref"] = str(ROOT / pv["ref"]) if pv.get("ref") else None
            x["speed"] = pv.get("speed", v.get("speed", 1.0))
            if pv.get("instruct"):
                x["instruct"] = pv["instruct"]
        todo.append(x)
    if not todo:
        return
    secs = sum(len(x["text"]) for x in todo) / 18.0
    print(f"VoiceStudio: {len(todo)} clips ≈ {secs / 60:.1f} min audio ≈ {secs * 7 / 60:.0f} min CPU (run in background)")
    jf = ROOT / "projects" / f"_tts_jobs_{os.getpid()}_{uuid.uuid4().hex[:6]}.json"
    jf.write_text(json.dumps(todo, ensure_ascii=False), encoding="utf-8")
    subprocess.run([str(py), str(ROOT / "src/audio/omnivoice_tts.py"), "--ref", str(ref), "--jobs", str(jf),
                    "--speed", str(v.get("speed", 1.0)), "--steps", str(v.get("steps", 32))], check=True)
    jf.unlink(missing_ok=True)

def silence(p: Path, sec: float) -> Path:
    if not p.exists():
        ff("-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", f"{sec:.3f}", "-c:a", "pcm_s16le", str(p))
    return p

def cmd_tts(P: Path, argv: list[str]) -> None:
    ep = jload(P / "episode.json")
    v = {**CHANNEL["voice"], **ep.get("voice", {})}
    A, RAW = P / "audio", P / "audio" / "vs"
    RAW.mkdir(parents=True, exist_ok=True)
    only_shorts = "--shorts" in argv
    only_scene = next((argv[i + 1] for i, a in enumerate(argv) if a == "--scene" and i + 1 < len(argv)), None)
    lead_s, gap_s = v.get("gap_leadin_s", 0.4), v.get("gap_breathing_s", 0.35)
    lead, gap = silence(A / "gap_leadin.wav", lead_s), silence(A / "gap_breathing.wav", gap_s)
    tsum = tw = 0.0
    if not only_shorts:
        for sc in ep["longform"]["scenes"]:
            if only_scene and sc["id"] != only_scene:
                continue
            sc_jobs = []
            for i, p in enumerate(sc["parts"]):
                sc_jobs.append((ptext(p), RAW / f"{sc['id']}_p{i}.wav", part_voice(ep, sc, p, v)))
            synth(sc_jobs, v)
            if not all((RAW / f"{sc['id']}_p{i}.wav").exists() for i in range(len(sc["parts"]))):
                continue
            sid, lines, pd = sc["id"], [f"file '{lead.resolve().as_posix()}'"], {}
            for i, p in enumerate(sc["parts"]):
                w = RAW / f"{sid}_p{i}_48k.wav"
                pv = part_voice(ep, sc, p, v)
                ff("-i", str(RAW / f"{sid}_p{i}.wav"), "-af",
                   f"atempo={pv['tempo']},highpass=f=70,loudnorm=I=-16:TP=-1.5:LRA=7,afade=t=in:st=0:d=0.005",
                   "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(w))
                pd[f"part{i}"] = round(dur(w), 3)
                tsum += pv["tempo"] * pd[f"part{i}"]
                tw += pd[f"part{i}"]
                lines.append(f"file '{w.resolve().as_posix()}'")
                if i < len(sc["parts"]) - 1:
                    lines.append(f"file '{gap.resolve().as_posix()}'")
            lst = RAW / f"{sid}_concat.txt"
            lst.write_text("\n".join(lines), encoding="utf-8")
            ff("-f", "concat", "-safe", "0", "-i", str(lst), "-c:a", "pcm_s16le", str(A / f"{sid}.wav"))
            d = dur(A / f"{sid}.wav")
            jsave(A / f"{sid}_parts_duration.json", {"total_duration": round(d, 3), "parts": pd, "engine": v["engine"]})
            print(f"[{sid}] {d:6.2f}s", flush=True)
    # Shorts: auto tempo so the voice lands <= target (default 53 s), broadcast EQ/comp
    if not only_scene:
        sh = ep["shorts"]
        if not (RAW / "shorts.wav").exists():
            synth([(sh["text"], RAW / "shorts.wav", part_voice(ep, None, {"mood": sh.get("mood", "hao_hung")}, v))], v)
        # rebuild when missing OR when the raw voice was regenerated (stale processed file = old voice in the render)
        if (RAW / "shorts.wav").exists() and (not (A / "shorts.wav").exists()
                                              or (A / "shorts.wav").stat().st_mtime < (RAW / "shorts.wav").stat().st_mtime):
            raw = dur(RAW / "shorts.wav")
            tempo = min(1.30, max(v.get("tempo_shorts_min", 1.0), raw / ep["shorts"].get("target_s", 53.0)))
            ff("-i", str(RAW / "shorts.wav"), "-af",
               f"aresample=48000,atempo={tempo:.3f},highpass=f=75,lowpass=f=12000,loudnorm=I=-16:TP=-1.5:LRA=7",
               "-ar", "48000", "-ac", "2", str(A / "shorts.wav"))
            print(f"[shorts] raw {raw:.1f}s -> tempo {tempo:.3f} -> {dur(A / 'shorts.wav'):.2f}s", flush=True)
    if not only_shorts and not only_scene:
        ready = [s for s in ep["longform"]["scenes"] if (A / f"{s['id']}_parts_duration.json").exists()]
        if len(ready) == len(ep["longform"]["scenes"]):
            total = sum(jload(A / f"{s['id']}_parts_duration.json")["total_duration"] for s in ep["longform"]["scenes"]) + 20.05
            need = v.get("min_long_s", 510)
            avg = tsum / tw if tw else v.get("tempo_long", 1.0)
            print(f"LONG-FORM ≈ {total:.0f}s ({fmt_ts(total)}) with intro+outro at average tempo {avg:.3f} "
                  f"— minimum {fmt_ts(need)} (TASTE-61)")
            if avg < PERSONAS.get("rotation_rules", {}).get("min_avg_tempo_long", 1.10) - 0.005:
                print(f"!! average tempo {avg:.3f} < 1.10 — too many slow moods (tram_bi_an/am_ap/bi_hai); add don_dap/hao_hung parts")
            if total < need and not ep.get("mega"):
                print(f"!! TOO SHORT by {need - total:.0f}s ≈ {(need - total) * 17 * v.get('tempo_long', 1.0):.0f} chars: "
                      f"add new parts (story/funny facts) in scene02-05, NEVER lower the tempo (scripts/voice_budget.py)")

# ----------------------------------------------------------------------------- align

def whisper_words(model, wav: Path, prompt: str) -> list[dict]:
    import numpy as np
    import soundfile as sf
    data, sr = sf.read(str(wav), dtype="float32")
    if data.ndim > 1:
        data = data.mean(axis=1)
    if sr != 16000:
        idx = np.arange(0, len(data), sr / 16000.0)
        data = np.interp(idx, np.arange(len(data)), data).astype(np.float32)
    segs, _ = model.transcribe(data, language="vi", word_timestamps=True, initial_prompt=prompt)
    return [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for s in segs for w in s.words]

def script_tokens(text: str, display: dict) -> list[str]:
    # Strip VoiceStudio emotion tags like [surprise-oh], [laughter], [sigh], etc.
    text = re.sub(r"\[[a-zA-Z0-9_\-]+\]", " ", text)
    # Apply multi-word phrase replacements from display dictionary (longest keys first)
    for k in sorted(display.keys(), key=len, reverse=True):
        if " " in k or "-" in k:
            text = text.replace(k, display[k])
    out = []
    for t in text.split():
        core = t.strip(".,!?:;\"'()")
        if core in display:
            t = t.replace(core, display[core])
        out.append(t)
    return out

def align(script: list[str], wh: list[dict]) -> list[dict]:
    """Project correct script words onto Whisper timings (fixes Whisper spelling, keeps timing)."""
    wh = [w for w in wh if norm(w["w"])]
    a, b = [norm(x["w"]) for x in wh], [norm(x) for x in script]
    res: list = [None] * len(script)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal":
            for k in range(j2 - j1):
                res[j1 + k] = {"w": script[j1 + k], "s": wh[i1 + k]["s"], "e": wh[i1 + k]["e"]}
        elif op in ("replace", "insert"):
            if i2 > i1:
                t0, t1 = wh[i1]["s"], wh[i2 - 1]["e"]
            else:
                t0 = wh[i1 - 1]["e"] if i1 > 0 else 0.0
                t1 = wh[i1]["s"] if i1 < len(wh) else t0 + 0.3 * (j2 - j1)
                t1 = max(t1, t0 + 0.12 * (j2 - j1))
            lens = [max(1, len(b[j])) for j in range(j1, j2)]
            tot, acc = sum(lens), 0
            for k, j in enumerate(range(j1, j2)):
                s = t0 + (t1 - t0) * acc / tot
                acc += lens[k]
                res[j] = {"w": script[j], "s": round(s, 3), "e": round(t0 + (t1 - t0) * acc / tot, 3)}
    ratio = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
    return res, ratio

def cmd_align(P: Path, argv: list[str]) -> None:
    from faster_whisper import WhisperModel
    ep = jload(P / "episode.json")
    display = ep.get("display_fix", {})
    prompt = ep.get("whisper_prompt", ep.get("animal", ""))
    model = WhisperModel(argv[argv.index("--model") + 1] if "--model" in argv else "small", device="cpu", compute_type="int8", cpu_threads=8)
    A = P / "audio"
    only_shorts = "--shorts" in argv
    v = {**CHANNEL["voice"], **ep.get("voice", {})}
    lead_s, gap_s = v.get("gap_leadin_s", 0.4), v.get("gap_breathing_s", 0.35)
    if not only_shorts:
        raw_all, fixed = {}, {}
        for sc in ep["longform"]["scenes"]:
            cache_file = A / f"_align_{sc['id']}.json"
            if cache_file.exists() and "--force" not in argv:
                cached = jload(cache_file)
                raw_all[sc["id"]] = cached["raw"]
                fixed[sc["id"]] = cached["fixed"]
                print(f"{sc['id']}: cached ({len(cached['raw'])} whisper words, match {cached.get('match', 0.9):.2f})", flush=True)
                continue
            print(f"Transcribing {sc['id']}...", flush=True)
            # Per-part transcription (each part < ~30 s): Whisper drops words at its 30 s window boundary when fed
            # a whole scene -> script words got crammed into a gap -> subtitles 3-4 s off (EP11 scene03, LESSON-84).
            # Offsets mirror cmd_tts: lead-in + part + gap between parts.
            pd = jload(A / f"{sc['id']}_parts_duration.json")["parts"]
            parts48 = [A / "vs" / f"{sc['id']}_p{i}_48k.wav" for i in range(len(sc["parts"]))]
            if all(p.exists() for p in parts48) and len(pd) == len(parts48):
                wh, t = [], lead_s
                for i, p in enumerate(parts48):
                    for w in whisper_words(model, p, prompt):
                        wh.append({"w": w["w"], "s": round(w["s"] + t, 3), "e": round(w["e"] + t, 3)})
                    t += pd[f"part{i}"] + gap_s
            else:
                wh = whisper_words(model, A / f"{sc['id']}.wav", prompt)
            raw_all[sc["id"]] = wh
            fixed[sc["id"]], r = align(script_tokens(" ".join(ptext(x) for x in sc["parts"]), display), wh)
            jsave(cache_file, {"raw": wh, "fixed": fixed[sc["id"]], "match": r})
            jsave(A / "long_words_raw.json", raw_all)
            jsave(A / "long_words_fixed.json", fixed)
            print(f"{sc['id']}: {len(wh)} whisper words, match {r:.2f}" + ("  <-- LOW, listen to audio!" if r < 0.8 else ""), flush=True)
        jsave(A / "long_words_raw.json", raw_all)
        jsave(A / "long_words_fixed.json", fixed)
    cache_shorts = A / "_align_shorts.json"
    if cache_shorts.exists() and "--force" not in argv:
        cached = jload(cache_shorts)
        sw = cached["sw"]
        print(f"shorts: cached ({len(sw)} script words, match {cached.get('match', 0.9):.2f})", flush=True)
    else:
        print("Transcribing shorts...", flush=True)
        wh = whisper_words(model, A / "shorts.wav", prompt)
        sw, r = align(script_tokens(ep["shorts"]["text"], display), wh)
        jsave(cache_shorts, {"sw": sw, "match": r})
        print(f"shorts: {len(wh)} whisper words, match {r:.2f}", flush=True)
    jsave(A / "shorts_words.json", [{"word": w["w"], "start": w["s"], "end": w["e"]} for w in sw])

# ----------------------------------------------------------------------------- spec

def finder(words: list[dict], ks=("w", "s")):
    n = [norm(w[ks[0]]) for w in words]
    def T(phrase: str, after: float = 0.0) -> float:
        toks = [norm(x) for x in phrase.split() if norm(x)]
        for i in range(len(words) - len(toks) + 1):
            if words[i][ks[1]] >= after and n[i:i + len(toks)] == toks:
                return words[i][ks[1]]
        raise SystemExit(f"phrase not found (after {after:.1f}s): {phrase!r} — copy it EXACTLY from the narration")
    return T

def cmd_spec(P: Path, argv: list[str]) -> None:
    ep = jload(P / "episode.json")
    slug = P.name
    A = P / "audio"
    errors = []
    only_shorts = "--shorts" in argv
    # ---- long-form
    if not only_shorts:
        plan = jload(P / "specs" / "longform_plan.json")
        words = jload(A / "long_words_fixed.json")
        targets = plan.get("targets", {})
        titles = {s["id"]: s for s in ep["longform"]["scenes"]}
        scenes = []
        for sid, pl in plan["scenes"].items():
            T = finder(words[sid])
            D = jload(A / f"{sid}_parts_duration.json")["total_duration"]
            beats = []
            for k, bp in enumerate(pl["beats"]):
                st = 0.0 if bp["at"] in (0, "0", "") else max(0.0, round(T(bp["at"]) - 0.30, 2))
                b = {"id": f"{sid}_b{k + 1:02d}", "start_s": st, "image": bp["image"], "entrance": "draw", "stickers": [], "impacts": []}
                for s in bp.get("stickers", []):
                    d = {"t": round(T(s["at"], st - 0.5), 2), "side": s["side"], "y": s.get("y", 420),
                         "value": s["value"], "label": s["label"]}
                    tg = s.get("target")
                    if tg:
                        d["target"] = list(targets[tg]) if isinstance(tg, str) else list(tg)
                    b["stickers"].append(d)
                b["impacts"] = [round(T(x, st - 0.5), 2) for x in bp.get("impacts", [])]
                beats.append(b)
            # TASTE-58: every picture is hand-drawn; short holds use the faster pen
            for i, b in enumerate(beats):
                nxt = beats[i + 1]["start_s"] if i + 1 < len(beats) else D
                hold = nxt - b["start_s"]
                b["entrance"] = "draw" if hold >= 5.0 else "draw_fast"
                if hold > 15.0:
                    errors.append(f"{b['id']} holds {hold:.1f}s > 15s (TASTE-47) -> add a beat inside {b['start_s']:.1f}-{nxt:.1f}s")
                if hold < 2.0:
                    errors.append(f"{b['id']} holds only {hold:.1f}s (<2s) -> merge with neighbour")
                if not (P / b["image"]).exists():
                    errors.append(f"{b['id']} missing image {b['image']}")
            st = titles.get(sid, {})
            # TASTE-62: AI-drawn chapter header bar if present (src/episode/prep_banners.py)
            hdr = f"assets/banners/chapter_{pl['chapter_no']:02d}.png"
            scenes.append({"id": sid, "voice": f"audio/{sid}.wav", "duration_s": D, "chapter_no": pl["chapter_no"],
                           **({"badge": pl["badge"]} if pl.get("badge") else {}),
                           **({"header_image": hdr} if (P / hdr).exists() else {}),
                           "title": pl.get("title", st.get("chapter_title", "")), "card_hook": pl.get("hook", st.get("hook", "")),
                           "chapter_card": pl.get("card", pl["chapter_no"] != 1), "card_s": 1.8, "beats": beats})
        jsave(P / "specs" / "longform_spec.json", {
            "episode": slug, "words": "audio/long_words_fixed.json", "n_chapters": len(scenes),
            "bgm": CHANNEL["bgm"], "intro": CHANNEL["intro"], "outro": CHANNEL["outro"], "intro_mode": "full_first",
            "output": f"renders/{slug}_long.mp4", "scenes": scenes})
        print(f"long-form: {sum(len(s['beats']) for s in scenes)} beats / {len(scenes)} chapters")

    # ---- shorts
    sp = jload(P / "specs" / "shorts_plan.json")
    sw = jload(A / "shorts_words.json")
    T = finder(sw, ("word", "start"))
    vd = dur(A / "shorts.wav")
    sbeats = []
    for k, bp in enumerate(sp["beats"]):
        st = float(bp["at_s"]) if "at_s" in bp else (0.0 if bp["at"] in (0, "0", "") else max(0.0, round(T(bp["at"]) - 0.25, 2)))
        b = {"id": f"s{k + 1:02d}", "start_s": st, "draw_s": bp.get("draw_s", 1.1), "image": bp["image"], "stickers": [], "captions": []}
        if k == 0:
            b["start_progress"] = 0.35  # TASTE-49: never open on blank paper
        for s in bp.get("stickers", []):
            d = {"t": float(s["at_s"]) if "at_s" in s else round(T(s["at"], st - 0.5), 2),
                 "side": s["side"], "y": s.get("y", 540), "value": s["value"], "label": s["label"]}
            if s.get("target"):
                d["target"] = list(s["target"])
            b["stickers"].append(d)
        sbeats.append(b)
    for i, b in enumerate(sbeats):
        end = sbeats[i + 1]["start_s"] if i + 1 < len(sbeats) else vd + 1
        ws = [w for w in sw if b["start_s"] - 0.05 <= w["start"] < end - 0.05] if i else [w for w in sw if w["start"] < end - 0.05]
        ws = [w for w in ws if not (w["word"].startswith("[") and w["word"].endswith("]"))]
        manual = sp["beats"][i].get("captions")
        if manual:  # explicit phrase groups (best quality): ["Chỉ một con", "ốc sên nhỏ bé", ...]
            k = 0
            for ph in manual:
                n = len(ph.split())
                if k < len(ws):
                    b["captions"].append({"t": ws[k]["start"], "text": ph})
                k += n
        else:  # auto: 2-4 words, break on punctuation or a voice pause (keeps compounds like "ốc sên" together)
            grp: list[dict] = []
            for j, w in enumerate(ws):
                grp.append(w)
                nxt_w = ws[j + 1] if j + 1 < len(ws) else None
                pause = nxt_w is not None and nxt_w["start"] - w["end"] > 0.12
                punct = re.search(r"[.,!?:;]$", w["word"])
                if len(grp) >= 4 or (len(grp) >= 2 and (punct or pause)) or (len(grp) == 3 and nxt_w and len(ws) - j - 1 > 1):
                    b["captions"].append({"t": grp[0]["start"], "text": " ".join(x["word"] for x in grp)}); grp = []
            if grp:
                if b["captions"] and len(grp) == 1 and len(b["captions"][-1]["text"].split()) < 5:
                    b["captions"][-1]["text"] += " " + grp[0]["word"]
                else:
                    b["captions"].append({"t": grp[0]["start"], "text": " ".join(x["word"] for x in grp)})
        hold = end - b["start_s"]
        if hold > 7.0:
            errors.append(f"shorts {b['id']} holds {hold:.1f}s > 7s -> one picture per sentence (TASTE-56)")
        if not (P / b["image"]).exists():
            errors.append(f"shorts {b['id']} missing image {b['image']}")
    jsave(P / "specs" / "shorts_spec.json", {
        "episode": slug, "title_lines": sp["title_lines"], "voice": "audio/shorts.wav", "words": "audio/shorts_words.json",
        **({"title_image": "assets/banners/shorts_title.png"} if (P / "assets/banners/shorts_title.png").exists() else {}),
        "voice_end_s": round(vd, 2), "outro_buffer_s": 1.5, "bgm": CHANNEL["bgm"], "output": f"renders/{slug}_shorts.mp4",
        "image_box": [560, 835], "preview_times": [round(b["start_s"] + b["draw_s"] + 0.8, 2) for b in sbeats], "beats": sbeats})
    print(f"shorts: {len(sbeats)} beats, voice {vd:.1f}s")
    if errors:
        print("\nSPEC PROBLEMS (fix the plan, re-run spec):")
        for e in errors:
            print("  -", e)
        raise SystemExit(1)
    print("spec OK")

# ----------------------------------------------------------------------------- render / qa

def cmd_render(P: Path, argv: list[str]) -> None:
    extra = [a for a in argv if a in ("--preview", "--force")]
    if "--shorts" not in argv:
        subprocess.run([sys.executable, str(ROOT / "src/render/longform_v2_renderer.py"), str(P / "specs/longform_spec.json"), *extra], check=True)
    if "--long" not in argv:
        subprocess.run([sys.executable, str(ROOT / "src/render/shorts_v4_renderer.py"), str(P / "specs/shorts_spec.json"),
                        *[a for a in extra if a == "--preview"]], check=True)

def loudness(p: Path) -> tuple[float, float]:
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(p), "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True, text=True, encoding="utf-8", errors="ignore").stderr
    i = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1])
    tp = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", out)[-1])
    return i, tp

def cmd_qa(P: Path, argv: list[str]) -> None:
    ep = jload(P / "episode.json")
    v = {**CHANNEL["voice"], **ep.get("voice", {})}
    slug, ok = P.name, True
    # long-form is mastered to -14 LUFS; the approved EP06 Shorts measured -18.8 LUFS (accepted range -20..-13)
    # long-form must be >= 8:30 (TASTE-61, owner rule 2026-11-08); mega/special is 60-80m (3600-4800s)
    min_long = v.get("min_long_s", 510)
    max_long = v.get("max_long_s", 5400 if (ep.get("mega") or ep.get("special")) else 660)
    for kind, lo, hi, lmin, lmax in (("long", min_long, max_long, -15.5, -12.5), ("shorts", 40, 59.5, -20.0, -13.0)):
        f = P / "renders" / f"{slug}_{kind}.mp4"
        if not f.exists():
            print(f"[{kind}] MISSING {f}"); ok = False; continue
        d = dur(f)
        i, tp = loudness(f)
        good = lo <= d <= hi and lmin <= i <= lmax and tp <= -1.0
        ok &= good
        print(f"[{kind}] {d:.1f}s ({fmt_ts(d)})  {i:.1f} LUFS  TP {tp:.1f}  -> {'PASS' if good else 'FAIL'}")
        subprocess.run([sys.executable, str(ROOT / "src/qa/retention_audit.py"), str(f)])
    print("QA", "PASS" if ok else "FAIL — fix before publishing")

# ----------------------------------------------------------------------------- seo

HASHTAG_BRAND = "#VẽChuyệnHoangDã"


def seo_hashtags(ep: dict) -> list[str]:
    """TASTE-68: exactly 3 Vietnamese hashtags WITH diacritics, broad -> specific -> brand.
    (seo.hashtag_broad overrides '#độngvật', seo.hashtag_animal overrides the animal tag)."""
    seo = ep["seo"]
    animal = seo.get("hashtag_animal") or "#" + re.sub(r"[^\w]", "", ep.get("animal", "").lower())
    out = []
    for h in (seo.get("hashtag_broad", "#độngvật"), animal, HASHTAG_BRAND):
        if len(h) > 1 and h.lower() not in (x.lower() for x in out):
            out.append(h)
    return out


def format_long_title(t: str, ep_no: int | None = None) -> str:
    """Format title with '| Tập N' suffix as in Episode 20 (chủ kênh yêu cầu 16/11/2026)."""
    base = re.sub(r"\s*[|\-–]\s*Tập\s*\d+\s*$", "", t).strip()
    if ep_no:
        return f"{base} | Tập {ep_no}"
    return base


def clean_title(t: str) -> str:
    return format_long_title(t)


def clean_shorts_title(t: str, tags: list[str]) -> str:
    """TASTE-68: Shorts title ends with max 2 diacritic hashtags (broad + animal), no '#shorts'."""
    base = re.sub(r"(\s*#\S+)+\s*$", "", t).strip()
    return f"{base} {' '.join(tags[:2])}"


def cmd_seo(P: Path, argv: list[str]) -> None:
    ep = jload(P / "episode.json")
    seo, slug = dict(ep["seo"]), P.name
    tags3 = seo_hashtags(ep)
    seo["hashtags"] = tags3
    ep_no = ep.get("episode_no")
    seo["title"] = format_long_title(seo["title"], ep_no)
    seo["shorts_title"] = clean_shorts_title(seo["shorts_title"], tags3)
    t = dur(ROOT / CHANNEL["intro"])
    chapters = ["00:00 Intro"]
    for sc in ep["longform"]["scenes"]:
        chapters.append(f"{fmt_ts(t)} {sc['chapter_title']}")
        pj = jload(P / "audio" / f"{sc['id']}_parts_duration.json") if (P / "audio" / f"{sc['id']}_parts_duration.json").exists() else {}
        t += pj["total_duration"] if isinstance(pj, dict) and "total_duration" in pj else sum(pj) if isinstance(pj, list) else 0.0
    chapters.append(f"{fmt_ts(t)} Kết thúc")
    prev = "\n".join(f"👉 {x}" for x in CHANNEL.get("previous_episodes", [])[::-1])
    label = ep.get("series_label") or f"Tập {ep['episode_no']}"  # tập đặc biệt (mega nội dung mới) đặt nhãn riêng
    nxt = ep.get("next_label") or f"tập {ep['episode_no'] + 1}"
    desc = (f"{seo['hook_paragraph']}\n\n{label} series {CHANNEL['name']} — kể chuyện động vật bằng tranh vẽ tay "
            f"bảng trắng (whiteboard animation).\n\n⏱️ MỤC LỤC:\n" + "\n".join(chapters) +
            "\n\n🔥 Trong video:\n" + "\n".join(f"• {b}" for b in seo["bullets"]) +
            (f"\n\n🎬 Xem tiếp các tập trước:\n{prev}" if prev else "") +
            f"\n\n💬 {seo['question']}\n🔔 Đăng ký kênh {CHANNEL['name']} để xem {nxt}: {seo.get('next_teaser', '')}"
            f"\n\n{' '.join(seo['hashtags'])}")
    long_mp4 = P / "renders" / f"{slug}_long.mp4"
    minutes = int(round(dur(long_mp4) / 60)) if long_mp4.exists() else 0
    long_title = format_long_title(seo["title"].replace("{MINUTES}", str(minutes)), ep_no)
    up = {
        "long": {"file": str(P / "renders" / f"{slug}_long.mp4"), "thumb": str(P / "renders" / f"{slug}_thumbnail.jpg"),
                 "title": long_title, "desc": desc, "tags": ", ".join(seo["tags"]), "pinned_comment": seo["question"]},
        "shorts": {"file": str(P / "renders" / f"{slug}_shorts.mp4"), "title": seo["shorts_title"],
                   "desc": seo["shorts_desc"] + "\n\n" + " ".join(seo["hashtags"]),
                   "tags": ", ".join(seo["shorts_tags"])},
    }
    # English title/description (TASTE-42, LESSON-86): seo.en_title + seo.en_hook [+ seo.en_chapters, one per scene]
    if seo.get("en_title"):
        en_ch = seo.get("en_chapters") or []
        en_lines = ["00:00 Intro"] + [
            f"{c.split(' ', 1)[0]} {en_ch[i] if i < len(en_ch) else c.split(' ', 1)[1]}"
            for i, c in enumerate(chapters[1:-1])] + [f"{chapters[-1].split(' ', 1)[0]} Ending"]
        en_desc = (f"{seo.get('en_hook', '')}\n\nCHAPTERS:\n" + "\n".join(en_lines) +
                   "\n\nWild Tales Sketch (Vẽ Chuyện Hoang Dã) explains real, fact-checked animal science with funny "
                   "hand-drawn whiteboard animation. Narration is in Vietnamese: turn on CC and choose Auto-translate "
                   "for subtitles in your language.\n\n#WildTalesSketch #AnimalFacts #WhiteboardAnimation #FunnyAnimals")
        en_title = seo["en_title"].replace("{MINUTES}", str(minutes))
        assert len(en_title) <= 100, "en_title > 100 chars"
        up["long"].update(en_title=en_title, en_desc=en_desc)
        if seo.get("en_shorts_title"):
            up["shorts"].update(en_title=seo["en_shorts_title"], en_desc=seo.get("en_hook", "") + "\n\n#shorts #AnimalFacts")
    else:
        print("!! seo.en_title missing in episode.json — no English translation will be added on upload (TASTE-42)")
    for k, s_val, n in (("title", long_title, 100), ("shorts_title", seo["shorts_title"], 100)):
        assert len(s_val) <= n, f"{k} > {n} chars"
    assert len(up["long"]["tags"]) <= 480, "tags > 500 chars"
    jsave(P / "upload.json", up)
    (P / "seo_package.md").write_text(
        f"# {long_title}\n\n## Mô tả\n```\n{desc}\n```\n\n## Tags\n{up['long']['tags']}\n\n## Ghim bình luận\n{seo['question']}\n\n"
        f"## Shorts\n**{seo['shorts_title']}**\n```\n{up['shorts']['desc']}\n```\n", encoding="utf-8")
    print("\n".join(chapters))
    print("-> upload.json + seo_package.md written. Upload ONLY when the owner says so:")
    print(f"   node src/episode/upload_youtube.cjs {P.as_posix()} --date YYYY-MM-DD --time HH:MM")

# ----------------------------------------------------------------------------- status / check

def cmd_status(P: Path, argv: list[str]) -> None:
    slug = P.name
    items = [("episode.json", P / "episode.json"), ("longform_plan", P / "specs/longform_plan.json"),
             ("shorts_plan", P / "specs/shorts_plan.json"), ("voice scene01", P / "audio/scene01.wav"),
             ("voice shorts", P / "audio/shorts.wav"), ("words", P / "audio/long_words_fixed.json"),
             ("longform_spec", P / "specs/longform_spec.json"), ("shorts_spec", P / "specs/shorts_spec.json"),
             ("long mp4", P / f"renders/{slug}_long.mp4"), ("shorts mp4", P / f"renders/{slug}_shorts.mp4"),
             ("thumbnail", P / f"renders/{slug}_thumbnail.jpg"), ("upload.json", P / "upload.json"),
             ("uploaded", P / "upload_result.json")]
    for n, p in items:
        print(f"  [{'x' if p.exists() else ' '}] {n:15s} {p.relative_to(ROOT) if p.is_relative_to(ROOT) else p}")

def voice_diversity(ep: dict, v: dict) -> None:
    """Rules of docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md: format/persona rotation, >= 3 moods, cameo lines, avg tempo."""
    R = PERSONAS.get("rotation_rules", {})
    fmt, persona = ep.get("format"), ep.get("persona")
    rm = ROOT / "config" / "series_roadmap.json"
    road = {e["ep"]: e for e in jload(rm)["episodes"]} if rm.exists() else {}
    no = ep.get("episode_no", 0)
    prev, plan = road.get(no - 1, {}), road.get(no, {})
    warn = []
    if not fmt or not persona:
        warn.append(f"episode.json thiếu 'format'/'persona' — lộ trình gợi ý: {plan.get('format')} / {plan.get('persona')} "
                    "(docs/strategy/FORMAT_KE_CHUYEN.md)")
    elif prev and (prev.get("format") == fmt or prev.get("persona") == persona):
        warn.append(f"format/persona trùng tập liền trước (Tập {no - 1}: {prev.get('format')}/{prev.get('persona')})")
    elif fmt not in PERSONAS["personas"].get(persona, {}).get("format", fmt):
        warn.append(f"persona {persona} không thuộc format {fmt}")
    chars: dict = {}
    cast_chars = tot = tsum = 0.0
    for sc in ep["longform"]["scenes"]:
        for p in sc["parts"]:
            pv = part_voice(ep, sc, p, v)
            n = len(re.sub(r"\[[^\]]+\]", "", ptext(p)))
            tot += n
            tsum += n * pv["tempo"]
            if pv["cast"]:
                cast_chars += n
            else:
                chars[pv["mood"] or "hao_hung"] = chars.get(pv["mood"] or "hao_hung", 0) + n
    mix = " ".join(f"{k} {100 * c / tot:.0f}%" for k, c in sorted(chars.items(), key=lambda x: -x[1]))
    ncast = sum(1 for sc in ep["longform"]["scenes"] for p in sc["parts"] if isinstance(p, dict) and p.get("cast"))
    avg = tsum / tot if tot else 0
    print(f"voice: format {fmt} | persona {persona} | moods: {mix} | cameo parts {ncast} ({100 * cast_chars / max(tot, 1):.0f}%) "
          f"| avg tempo {avg:.3f}")
    if len(chars) < R.get("min_distinct_moods_per_episode", 3):
        warn.append(f"chỉ {len(chars)} mood — cần ≥ {R.get('min_distinct_moods_per_episode', 3)} (giọng một màu)")
    if chars and max(chars.values()) / tot > R.get("max_share_of_one_mood", 0.5):
        warn.append("1 mood chiếm > 50% lời — đổi mood vài part theo tình huống")
    if ncast < R.get("min_cast_lines_long", 2):
        warn.append(f"cần ≥ {R.get('min_cast_lines_long', 2)} part cameo ('cast') — lời thoại nhân vật phụ")
    if cast_chars / max(tot, 1) > R.get("max_cast_share_long", 0.08):
        warn.append("cameo > 8% lời — giọng chính phải dẫn dắt")
    if avg and avg < R.get("min_avg_tempo_long", 1.10) - 0.005:
        warn.append(f"tempo trung bình {avg:.3f} < 1.10 (TASTE-61)")
    for w_ in warn:
        print(f"  !! voice-diversity: {w_}")

NUM_WORDS = ("không một hai ba bốn năm sáu bảy tám chín mười mươi lăm lẻ linh trăm ngàn nghìn triệu tỷ rưỡi").split()

def script_lint(ep: dict) -> None:
    """Pre-TTS checks that caught real bugs (EP07-EP09): numbers without display_fix, long parts, nickname count,
    unknown tags, structure words. Prints '!! script:' lines — fix them before running tts."""
    warn = []
    display = ep.get("display_fix", {})
    parts = [(sc["id"], i, ptext(p)) for sc in ep["longform"]["scenes"] for i, p in enumerate(sc["parts"])]
    parts.append(("shorts", 0, ep["shorts"]["text"]))
    allowed = {"laughter", "sigh", "surprise-oh", "surprise-ah", "surprise-wa", "question-ah", "question-oh", "dissatisfaction-hnn"}
    nw = "|".join(NUM_WORDS)
    for sid, i, t in parts:
        clean = re.sub(r"\[[^\]]+\]", "", t)
        if sid != "shorts" and len(clean) > 1300:
            warn.append(f"{sid}_p{i}: {len(clean)} ký tự > 1300 — tách part")
        for tag in re.findall(r"\[([^\]]+)\]", t):
            if tag not in allowed:
                warn.append(f"{sid}_p{i}: tag [{tag}] không hỗ trợ (chỉ {', '.join(sorted(allowed))})")
        fixed = clean
        for k in sorted(display, key=len, reverse=True):
            fixed = fixed.replace(k, " ")
        for m in re.finditer(rf"(?<![\wÀ-ỹ])((?:{nw})(?:[ -](?:{nw}))+)(?![\wÀ-ỹ])", fixed, flags=re.IGNORECASE):
            warn.append(f"{sid}_p{i}: số đọc bằng chữ chưa có display_fix: '{m.group(1)}' (luật 6)")
        if re.search(r"\d", clean):
            warn.append(f"{sid}_p{i}: có chữ số trong lời đọc — viết số bằng chữ + display_fix (VoiceStudio đọc sai số)")
        if re.search(r"phần tiếp theo|ở phần này|chương tiếp|hơ hơ|haha", clean, re.IGNORECASE):
            warn.append(f"{sid}_p{i}: câu lộ cấu trúc / cười viết ra chữ (TASTE-52)")
    # TASTE-66 (09/11/2026): regular episodes' Shorts tell a complete story — no funnel, no dangling end.
    # Mega/special compilations (format F_SPECIAL, "mega" or "special") KEEP the old funnel Shorts (TASTE-33/49).
    is_mega = ep.get("format") == "F_SPECIAL" or ep.get("mega") or ep.get("special")
    sh = re.sub(r"\[[^\]]+\]", "", ep["shorts"]["text"]).strip()
    for pat, why in () if is_mega else ((r"video dài|bấm vào kênh|bấm xem|xem trọn|xem ngay|bản full|link (bên )?dưới|video bên dưới",
                      "Shorts còn câu kéo sang video dài/kênh"),
                     (r"(\.\.\.|…)\s*$", "Shorts kết bằng câu cắt lửng (nối vòng)"),
                     (r"\?\s*$", "Shorts kết bằng câu hỏi bỏ lửng")):
        if re.search(pat, sh, re.IGNORECASE):
            warn.append(f"shorts: {why} — Shorts phải kể trọn vẹn, kết bằng câu chốt trả lời hook (TASTE-66)")
    nick = ep.get("nickname")
    if nick:
        c = sum(t.count(nick) for _, _, t in parts[:-1])
        if c < 4:
            warn.append(f"biệt danh '{nick}' chỉ xuất hiện {c} lần trong video dài (cần ≥ 4)")
    else:
        warn.append("episode.json thiếu 'nickname' (biệt danh nhân vật, humor-voice A1)")
    if not ep.get("sources"):
        warn.append("episode.json thiếu 'sources' (nguồn kiểm chứng số liệu)")
    t_seo = ep.get("seo", {}).get("title", "")
    if re.search(r"(\{MINUTES\}|\d+)\s*phút", t_seo, re.IGNORECASE):
        warn.append("seo.title chứa số phút (TASTE-70) — bỏ số phút để không bị cắt cụt trên di động/Studio")
    for w_ in dict.fromkeys(warn):
        print(f"  !! script: {w_}")
    if not warn:
        print("script lint OK (số có display_fix, tag hợp lệ, biệt danh ≥ 4, part ≤ 1300)")

def cmd_check(P: Path, argv: list[str]) -> None:
    cmd_status(P, argv)
    py, ref = voicestudio()
    print(f"VoiceStudio OK: {py.parent.parent.parent.name} | reference {ref.name}")
    ep = jload(P / "episode.json")
    v = {**CHANNEL["voice"], **ep.get("voice", {})}
    n = sum(len(re.sub(r"\[[^\]]+\]", "", ptext(t))) for s in ep["longform"]["scenes"] for t in s["parts"])
    # calibrated on EP09 (multi-mood, cameo parts, 0.35 s gaps): 9489 chars -> 480 s body = 17.6 chars/s at tempo 1.0.
    # (EP07's 17.0 over-estimated EP09 by 28 s.) Per-part tempo from the mood/cast.
    body = sum(len(re.sub(r"\[[^\]]+\]", "", ptext(t))) / (17.6 * part_voice(ep, s, t, v)["tempo"])
               for s in ep["longform"]["scenes"] for t in s["parts"])
    est = body + 20.05
    need = v.get("min_long_s", 510)
    short = est < need + 15  # 15 s safety margin: OmniVoice speed varies ±3 % per run
    if ep.get("mega"):  # Mega Compilation: scenes = new opening/bridges only; length is checked by src/mega/assemble.py check
        need, short = 0, False
        print(f"MEGA: bridges ≈ {fmt_ts(body)} of new narration (total length -> python src/mega/assemble.py check {P.as_posix()})")
    print(f"long-form chars: {n} (≈ {fmt_ts(est)} incl. intro/outro; minimum {fmt_ts(need)}"
          f"{f' — TOO SHORT: write ~{(need + 15 - est) * 17.6 * 1.12:.0f} more chars (new parts in scene02-05)' if short else ''}) "
          f"| shorts chars: {len(ep['shorts']['text'])}")
    narration = " ".join([ptext(t) for s in ep["longform"]["scenes"] for t in s["parts"]] + [ep["shorts"]["text"]])
    tags = sorted(set(re.findall(r"\[[a-z-]+\]", narration)))
    print(f"emotion tags used: {' '.join(tags) or 'NONE — add [laughter]/[surprise-oh]... (humor-voice skill)'}")
    voice_diversity(ep, v)
    script_lint(ep)
    for plan in ("longform_plan.json", "shorts_plan.json"):
        p = P / "specs" / plan
        if p.exists():
            imgs = set(re.findall(r'"image"\s*:\s*"([^"]+)"', p.read_text(encoding="utf-8")))
            miss = sorted(i for i in imgs if not (P / i).exists())
            print(f"{plan}: {len(imgs)} images, missing {len(miss)}: {', '.join(Path(m).stem for m in miss[:40])}")
    prompt_file = P / "specs" / "image_prompts.json"
    if prompt_file.exists():
        from prompt_sanitizer import audit_prompts_file
        pdict = json.loads(prompt_file.read_text(encoding="utf-8"))
        risks = audit_prompts_file(pdict)
        if risks:
            print(f"  !! CẢNH BÁO AN TOÀN PROMPT: phát hiện {len(risks)} từ khóa rủi ro vi phạm chính sách:")
            for r in risks[:5]:
                print(f"     - {r}")
        else:
            print(f"Prompt safety OK: {len(pdict)} prompts đã kiểm duyệt an toàn (ZERO rủi ro chính sách)")

STAGES = {"init": cmd_init, "check": cmd_check, "tts": cmd_tts, "align": cmd_align, "spec": cmd_spec,
          "render": cmd_render, "qa": cmd_qa, "seo": cmd_seo, "status": cmd_status}

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in STAGES:
        print(__doc__); raise SystemExit(1)
    STAGES[sys.argv[1]](Path(sys.argv[2]).resolve(), sys.argv[3:])
