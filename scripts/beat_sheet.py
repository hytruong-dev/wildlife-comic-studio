"""One frame per long-form beat (at sticker time + 0.8s, else beat midpoint) from rendered scene mkv -> grid per scene."""
import json, subprocess, sys
from pathlib import Path
import cv2, numpy as np

proj = Path(sys.argv[1] if len(sys.argv) > 1 else "projects/tap-07-tom-tit")
spec = json.loads((proj / "specs/longform_spec.json").read_text(encoding="utf-8"))
out = proj / "renders/beat_audit"; out.mkdir(parents=True, exist_ok=True)
for sc in spec["scenes"]:
    src = proj / "renders/long_v2" / f"{sc['id']}.mkv"
    beats, tiles = sc["beats"], []
    for i, b in enumerate(beats):
        e = beats[i + 1]["start_s"] if i + 1 < len(beats) else sc["duration_s"]
        st = b.get("stickers") or []
        t = min(st[-1]["t"] + 0.8, e - 0.2) if st else (b["start_s"] + e) / 2
        f = out / "tmp.jpg"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.2f}", "-i", str(src), "-frames:v", "1", str(f)], check=True)
        im = cv2.resize(cv2.imread(str(f)), (640, 360))
        cv2.putText(im, f"{b['id'][-3:]} {Path(b['image']).stem}", (8, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        tiles.append(im)
    while len(tiles) % 3: tiles.append(np.full_like(tiles[0], 255))
    grid = np.vstack([np.hstack(tiles[i:i + 3]) for i in range(0, len(tiles), 3)])
    cv2.imwrite(str(out / f"{sc['id']}.jpg"), grid, [cv2.IMWRITE_JPEG_QUALITY, 82])
    print(out / f"{sc['id']}.jpg")
