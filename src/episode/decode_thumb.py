# -*- coding: utf-8 -*-
import base64
from pathlib import Path

p = Path("projects/tap-35-ca-voi-sat-thu")
t = p / "assets/inbox/T01.txt"
if t.exists():
    raw = t.read_text(encoding="utf-8").strip().strip('"')
    data = base64.b64decode(raw.split(",", 1)[1])
    out = p / "renders/tap-35-ca-voi-sat-thu_thumbnail.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    print(f"Decoded thumbnail -> {out} ({len(data)} bytes)")
else:
    print("T01.txt not found in inbox")

