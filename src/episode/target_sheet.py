"""Vẽ điểm target của MỌI sticker lên ảnh gốc để kiểm tra mũi tên chỉ đúng chi tiết (trước khi render).

  python src/episode/target_sheet.py projects/<slug>   -> renders/snapshots/targets_N.jpg (mỗi tấm ≤ 12 ô)

Vòng đỏ = chỗ mũi tên sẽ chỉ. Lệch -> sửa "target" trong specs/storyboard.json -> build_plans -> spec.
"""
import json
import sys
from pathlib import Path

import cv2
import numpy as np

P = Path(sys.argv[1]).resolve()
items = []
lp = json.loads((P / "specs/longform_plan.json").read_text(encoding="utf-8"))
for s in lp["scenes"].values():
    for b in s["beats"]:
        items += [(b["image"], st["value"], st.get("target")) for st in b.get("stickers", [])]
sp = json.loads((P / "specs/shorts_plan.json").read_text(encoding="utf-8"))
for b in sp["beats"]:
    items += [(b["image"], st["value"], st.get("target")) for st in b.get("stickers", [])]
H, CELL = 340, 620
tiles = []
for img, v, t in items:
    im = cv2.imread(str(P / img))
    if im is None:
        print("missing", img); continue
    im = cv2.resize(im, (int(im.shape[1] * H / im.shape[0]), H))
    w = im.shape[1]
    if t:
        x, y = int(t[0] * w), int(t[1] * H)
        cv2.circle(im, (x, y), 14, (0, 0, 255), 3)
        cv2.circle(im, (x, y), 3, (0, 0, 255), -1)
    else:
        cv2.putText(im, "NO TARGET!", (10, H // 2), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    cv2.putText(im, f"{Path(img).stem} {v}", (5, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    tiles.append(cv2.copyMakeBorder(im, 0, 0, 0, max(0, CELL - w), cv2.BORDER_CONSTANT, value=(220, 220, 220))[:, :CELL])
out_dir = P / "renders" / "snapshots"
out_dir.mkdir(parents=True, exist_ok=True)
for k in range(0, len(tiles), 12):
    chunk = tiles[k:k + 12]
    while len(chunk) % 4:
        chunk.append(np.full_like(tiles[0], 220))
    sheet = np.vstack([np.hstack(chunk[i:i + 4]) for i in range(0, len(chunk), 4)])
    f = out_dir / f"targets_{k // 12 + 1}.jpg"
    cv2.imwrite(str(f), sheet, [cv2.IMWRITE_JPEG_QUALITY, 82])
    print(f)
print(f"{len(items)} stickers")
