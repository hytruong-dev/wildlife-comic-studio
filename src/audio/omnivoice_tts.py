"""Local Vietnamese voice-clone TTS — VoiceStudio (k2-fsa OmniVoice). The channel's ONLY voice engine.

Emotion/humour comes from the REFERENCE clip (assets/voice_refs/*.wav + same-name .txt transcript):
the new narration inherits its timbre, energy and comic timing. Inline tags the model understands:
  [laughter] [sigh] [surprise-oh] [surprise-ah] [surprise-wa] [question-ah] [question-oh] [dissatisfaction-hnn]
Any other [tag] is removed before synthesis.

Must run with VoiceStudio's own venv (torch + omnivoice). `src/episode/pipeline.py tts` does this for you.
  VS_PY = %LOCALAPPDATA%/com.debpalash.omnivoice-studio/project/.venv/Scripts/python.exe
  VS_PY src/audio/omnivoice_tts.py --ref assets/voice_refs/adam_funny_ep1.wav --text "..." --out out.wav
  VS_PY src/audio/omnivoice_tts.py --ref ... --jobs jobs.json      # [{"text": "...", "out": "a.wav"}, ...]
CPU (i5-12600K): ~7 s of compute per 1 s of audio -> a 9-min episode takes ~1 h. Run in background.
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

VS = Path(os.environ.get("VOICESTUDIO_DIR", Path(os.environ.get("LOCALAPPDATA", "")) / "com.debpalash.omnivoice-studio" / "project"))
sys.path.insert(0, str(VS))
os.environ.setdefault("HF_HUB_CACHE", str(Path(os.environ.get("LOCALAPPDATA", "")) / "OmniVoice" / "hf_cache"))
os.environ.setdefault("HF_HUB_OFFLINE", "1")

KEEP_TAGS = {"laughter", "sigh", "confirmation-en", "question-en", "question-ah", "question-oh", "question-ei",
             "question-yi", "surprise-ah", "surprise-oh", "surprise-wa", "surprise-yo", "dissatisfaction-hnn"}

def clean(text: str) -> str:
    """Drop tags OmniVoice does not know (e.g. old ElevenLabs [excited]) and tidy spaces."""
    t = re.sub(r"\[([^\]]+)\]", lambda m: m.group(0) if m.group(1).strip().lower() in KEEP_TAGS else "", text)
    return re.sub(r"\s{2,}", " ", t).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", required=True)
    ap.add_argument("--ref-text", default=None, help="transcript of ref (default: <ref>.txt)")
    ap.add_argument("--text")
    ap.add_argument("--text-file", help="one paragraph per line -> <out>_000.wav ...")
    ap.add_argument("--jobs", help='JSON list [{"text":..., "out":...}]')
    ap.add_argument("--out")
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--steps", type=int, default=32)
    ap.add_argument("--guidance", type=float, default=2.0)
    a = ap.parse_args()

    if a.jobs:
        jobs = json.loads(Path(a.jobs).read_text(encoding="utf-8"))
    else:
        texts = [a.text] if a.text else [l.strip() for l in Path(a.text_file).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        out = Path(a.out)
        jobs = [{"text": t, "out": str(out if len(texts) == 1 else out.with_name(f"{out.stem}_{i:03d}{out.suffix}"))}
                for i, t in enumerate(texts)]

    import torch
    import torchaudio
    from omnivoice.models.omnivoice import OmniVoice

    torch.set_num_threads(os.cpu_count() or 8)
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    t0 = time.time()
    model = OmniVoice.from_pretrained("k2-fsa/OmniVoice", device_map=dev,
                                      dtype=torch.float16 if dev == "cuda" else torch.float32)
    print(f"model loaded on {dev} in {time.time() - t0:.0f}s", flush=True)
    # Voice personas (docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md): every job may carry its own
    # "ref" (clone a different emotional reference clip) and/or "instruct" (OmniVoice voice design:
    # e.g. "male, elderly, low pitch"). "ref": null + "instruct" = designed cameo voice (no clone).
    prompts: dict = {}

    def clone_prompt(ref: str):
        if ref not in prompts:
            txt = a.ref_text if (ref == a.ref and a.ref_text) else \
                Path(ref).with_suffix(".txt").read_text(encoding="utf-8-sig").strip()
            prompts[ref] = model.create_voice_clone_prompt(ref_audio=ref, ref_text=txt)
        return prompts[ref]

    for i, j in enumerate(jobs):
        dst = Path(j["out"])
        dst.parent.mkdir(parents=True, exist_ok=True)
        t1 = time.time()
        ref = j.get("ref", a.ref)
        kw = {"voice_clone_prompt": clone_prompt(ref)} if ref else {}
        if j.get("instruct"):
            kw["instruct"] = j["instruct"]
        audio = model.generate(text=clean(j["text"]), language="vi", speed=j.get("speed", a.speed),
                               num_step=a.steps, guidance_scale=a.guidance, **kw)[0]
        tmp = dst.with_suffix(".tmp.wav")
        torchaudio.save(str(tmp), audio.cpu().float().reshape(1, -1), model.sampling_rate)
        tmp.replace(dst)  # atomic: a crash never leaves a half-written cache file
        sec = audio.numel() / model.sampling_rate
        print(json.dumps({"n": f"{i + 1}/{len(jobs)}", "file": str(dst), "audio_s": round(sec, 2),
                          "gen_s": round(time.time() - t1, 1)}, ensure_ascii=False), flush=True)

if __name__ == "__main__":
    main()
