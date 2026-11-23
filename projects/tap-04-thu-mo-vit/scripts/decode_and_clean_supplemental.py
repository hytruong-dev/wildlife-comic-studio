"""
Decode and Clean Watermarks for 9 Supplemental Gemini Illustrations
"""

import json
import base64
import cv2
import numpy as np
from pathlib import Path

PROJ = Path(__file__).resolve().parents[1]
G = PROJ / "assets" / "gemini_downloaded"
BACKUP = G / "_raw_with_watermark_backup"
G.mkdir(parents=True, exist_ok=True)
BACKUP.mkdir(parents=True, exist_ok=True)

def clean_star_watermark_whiteboard(img_bgr: np.ndarray) -> np.ndarray:
    h, w = img_bgr.shape[:2]
    roi = img_bgr[h - 140 : h, w - 140 : w].copy()
    b, g, r = cv2.split(roi)
    yy, xx = np.mgrid[0:140, 0:140]
    star_paper_zone = (yy >= 35) & (xx >= 35) & (b >= 205) & (g >= 205) & (r >= 205)
    roi[star_paper_zone] = [255, 255, 255]
    img_bgr[h - 140 : h, w - 140 : w] = roi
    return img_bgr

candidates = [
    Path(r"C:\Users\PC\.playwright-mcp\ep04_gemini_supp9.json"),
    Path(r"C:\Users\PC\.playwright-mcp\ep04-gemini-supp9.json"),
]

json_p = None
for c in candidates:
    if c.exists():
        json_p = c
        break

if not json_p:
    raise FileNotFoundError("Could not find ep04_gemini_supp9.json")

print(f"Loading {json_p}...")
data = json.loads(json_p.read_text(encoding="utf-8"))

for fname, b64 in data.items():
    raw_bytes = base64.b64decode(b64)
    (BACKUP / fname).write_bytes(raw_bytes)
    
    arr = np.frombuffer(raw_bytes, dtype=np.uint8)
    im_bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    im_clean = clean_star_watermark_whiteboard(im_bgr)
    
    out_p = G / fname
    cv2.imwrite(str(out_p), im_clean)
    h, w = im_clean.shape[:2]
    print(f"[CLEANED & SAVED] {fname} ({w}x{h})")

print(f"Successfully processed all {len(data)} supplemental illustrations!")
