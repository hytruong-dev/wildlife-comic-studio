import base64
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("usage: python save_thumb.py <project_path>")
    sys.exit(1)

p = Path(sys.argv[1])
slug = p.name
t = p / "assets/inbox/T01.txt"
if t.exists():
    raw = t.read_text(encoding="utf-8").strip().strip('"')
    if "," in raw:
        raw = raw.split(",", 1)[1]
    data = base64.b64decode(raw)
    out = p / f"renders/{slug}_thumbnail.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    print(f"Decoded thumbnail -> {out} ({len(data)} bytes)")
else:
    print(f"T01.txt not found in {t}")

