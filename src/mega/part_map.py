"""Exact time of every narration part inside a published long video (pipeline episodes Tập 7+).

Video = intro (10.03 s) + scene01..N; scene audio = 0.4 s lead-in + part0 + 0.35 s gap + part1 ...
Use it to cut whole parts (clean sentence boundaries) out of a source body.

  python src/mega/part_map.py projects/tap-10-gau-koala
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]


def main():
    P = Path(sys.argv[1]).resolve()
    ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
    t = 10.03  # branded intro (assets/branding/intro_ve_chuyen_hoang_da.mp4, intro_mode full_first)
    for sc in ep["longform"]["scenes"]:
        pd = json.loads((P / "audio" / f"{sc['id']}_parts_duration.json").read_text(encoding="utf-8"))
        print(f"== {sc['id']} {t:7.2f}s  {sc.get('chapter_title', '')}")
        p0 = t + 0.4
        for i, p in enumerate(sc["parts"]):
            d = pd["parts"][f"part{i}"]
            txt = p["text"] if isinstance(p, dict) else p
            who = p.get("cast", "") if isinstance(p, dict) else ""
            print(f"   p{i} {p0:7.2f}-{p0 + d:7.2f} ({d:5.1f}s) {who:10s} {txt[:90]}")
            p0 += d + 0.35
        t += pd["total_duration"]
    print(f"== end of body {t:.2f}s (outro after)")


if __name__ == "__main__":
    main()
