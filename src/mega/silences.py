"""Voice pauses of every source video (ffmpeg silencedetect) — cut points must sit inside a pause, never mid-word.

  python src/mega/silences.py projects/<mega> [--only slug] [--db -32] [--min 0.15]
  -> projects/<mega>/sources/<slug>.silences.json  [[start, end], ...]
Also prints transcript holes > 8 s (Whisper skipped speech there -> forbidden-word scan is blind; probe with probe_range.py).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]


def detect(f: Path, db: float, mn: float) -> list[list[float]]:
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(f), "-vn", "-af", f"silencedetect=n={db}dB:d={mn}", "-f", "null", "-"],
                         capture_output=True, text=True, encoding="utf-8", errors="ignore").stderr
    st = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", err)]
    en = [float(x) for x in re.findall(r"silence_end: (-?[\d.]+)", err)]
    return [[round(a, 3), round(b, 3)] for a, b in zip(st, en)]


def main():
    P = Path(sys.argv[1]).resolve()
    mega = json.loads((P / "mega.json").read_text(encoding="utf-8"))
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    db = float(sys.argv[sys.argv.index("--db") + 1]) if "--db" in sys.argv else -32
    mn = float(sys.argv[sys.argv.index("--min") + 1]) if "--min" in sys.argv else 0.15
    for s in mega["sources"]:
        if only and s["slug"] != only:
            continue
        sil = detect(ROOT / s["file"], db, mn)
        (P / "sources" / f"{s['slug']}.silences.json").write_text(json.dumps(sil), encoding="utf-8")
        tr = P / "sources" / f"{s['slug']}.words.json"
        holes = []
        if tr.exists():
            segs = json.loads(tr.read_text(encoding="utf-8"))["segments"]
            holes = [(a["e"], b["s"]) for a, b in zip(segs, segs[1:]) if b["s"] - a["e"] > 8]
        print(f"{s['slug']:22s} {len(sil):4d} pauses" + (f" | transcript holes: {', '.join(f'{a:.0f}-{b:.0f}s' for a, b in holes)}" if holes else ""))


if __name__ == "__main__":
    main()
