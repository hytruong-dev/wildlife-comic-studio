"""Print each long-form beat with the exact narration spoken while its image is on screen."""
import json, sys
from collections import Counter
from pathlib import Path

proj = Path(sys.argv[1] if len(sys.argv) > 1 else "projects/tap-07-tom-tit")
spec = json.loads((proj / "specs/longform_spec.json").read_text(encoding="utf-8"))
words = json.loads((proj / "audio/long_words_fixed.json").read_text(encoding="utf-8"))
use = Counter()
out = []
for sc in spec["scenes"]:
    ws = words[sc["id"]]
    beats = sc["beats"]
    for i, b in enumerate(beats):
        s = b["start_s"]
        e = beats[i + 1]["start_s"] if i + 1 < len(beats) else sc["duration_s"]
        txt = " ".join(w["w"] for w in ws if s - 0.05 <= w["s"] < e - 0.05)
        img = Path(b["image"]).stem
        use[img] += 1
        st = "; ".join(f'{x["value"]}@{x["t"]:.1f}' for x in b.get("stickers", []))
        out.append(f'{b["id"]} [{s:6.1f}-{e:6.1f} {e-s:4.1f}s] {img}  | {st}\n    "{txt}"')
print("\n".join(out))
print("\nImage reuse:", {k: v for k, v in sorted(use.items()) if v > 1})
