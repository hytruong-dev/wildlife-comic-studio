"""Print Shorts word timings with pause gaps: python scripts/print_shorts_words.py projects/<slug>"""
import json, sys
from pathlib import Path

ws = json.loads((Path(sys.argv[1]) / "audio/shorts_words.json").read_text(encoding="utf-8"))
prev = 0.0
for w in ws:
    gap = w["start"] - prev
    mark = f"  GAP {gap:.2f}" if gap > 0.35 else ""
    print(f"{w['start']:6.2f}-{w['end']:6.2f}{mark}  {w['word']}")
    prev = w["end"]
