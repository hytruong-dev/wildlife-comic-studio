"""Voice length budget: current long-form duration per scene and what it becomes at faster tempos.
usage: python scripts/voice_budget.py projects/<slug> [min_total_s=510]"""
import json, re, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else "projects/tap-07-tom-tit")
need = float(sys.argv[2]) if len(sys.argv) > 2 else 510.0
ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
CH = json.loads((Path(__file__).resolve().parents[1] / "config/channel.json").read_text(encoding="utf-8"))
tempo_now = ep.get("voice", {}).get("tempo_long", CH["voice"].get("tempo_long", 1.1))  # per-mood tempos average ~1.12
tot = chars = 0
for s in ep["longform"]["scenes"]:
    d = json.loads((P / f"audio/{s['id']}_parts_duration.json").read_text())["total_duration"]
    c = sum(len(re.sub(r"\[[^\]]+\]", "", p["text"] if isinstance(p, dict) else p)) for p in s["parts"])
    tot += d; chars += c
    print(f"{s['id']}  {d:6.1f}s  {c:5d} chars")
raw = tot * tempo_now  # duration at tempo 1.0
print(f"body {tot:.1f}s at tempo {tempo_now}, {chars} chars, {chars / tot:.1f} chars/s; final with intro/outro {tot + 20.05:.1f}s")
for t in (1.0, 1.08, 1.10, 1.12, 1.15):
    body = raw / t
    extra = max(0.0, need - 20.05 - body) * (chars / raw) * t
    print(f"tempo {t:.2f}: final {body + 20.05:6.1f}s ({int((body + 20.05) // 60)}:{(body + 20.05) % 60:04.1f})"
          f"  -> extra narration needed for {need:.0f}s: ~{extra:.0f} chars")
