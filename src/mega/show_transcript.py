"""Print a source transcript with timestamps — used to pick/verify cut points (in/out) for mega.json.

  python src/mega/show_transcript.py projects/<mega> <slug> [--head 60] [--tail 150] [--all]
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")


def main():
    proj, slug = Path(sys.argv[1]), sys.argv[2]
    if "@" in slug:  # several probes in one call: slug@seconds slug@seconds ...
        for arg in sys.argv[2:]:
            if "@" not in arg:
                continue
            s, t = arg.split("@")
            d = json.loads((proj / "sources" / f"{s}.words.json").read_text(encoding="utf-8"))
            ws = [w for seg in d["segments"] for w in seg["words"] if float(t) - 7 <= w["s"] <= float(t) + 7]
            print(f"==== {s} @ {t}\n   " + " ".join(f"[{w['s']:.2f}]{w['w']}" for w in ws))
        return
    d = json.loads((proj / "sources" / f"{slug}.words.json").read_text(encoding="utf-8"))
    D = d["duration_s"]
    head = float(sys.argv[sys.argv.index("--head") + 1]) if "--head" in sys.argv else 60
    tail = float(sys.argv[sys.argv.index("--tail") + 1]) if "--tail" in sys.argv else 150
    print(f"# {slug}  duration {D:.2f}s")
    if "--around" in sys.argv:  # word-level stamps ±6 s around a time: pick exact in/out points
        t = float(sys.argv[sys.argv.index("--around") + 1])
        for w in (w for s in d["segments"] for w in s["words"] if t - 6 <= w["s"] <= t + 6):
            print(f"   {w['s']:7.2f}-{w['e']:7.2f} {w['w']}")
        return
    for s in d["segments"]:
        if "--all" in sys.argv or s["s"] < head or s["e"] > D - tail:
            print(f"{s['s']:7.2f}-{s['e']:7.2f} | {s['text']}")


if __name__ == "__main__":
    main()
