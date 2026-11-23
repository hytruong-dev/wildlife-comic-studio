"""Locate colour features in shorts images so callout arrows point at the exact detail.

Prints, per image and colour class, the largest blobs (centroid + bbox) in image
fractions (0..1). Usage: python find_feature_anchors.py v5_s04 [v5_s05 ...]
"""
import sys
from pathlib import Path

import cv2
import numpy as np

DIR = Path(__file__).resolve().parents[1] / "assets" / "gemini_downloaded_shorts"

# HSV ranges (OpenCV H: 0-180)
CLASSES = {
    "ice_lightblue": [((85, 25, 170), (110, 160, 255))],
    "water_blue": [((95, 120, 120), (125, 255, 255))],
    "navy_space": [((100, 80, 20), (135, 255, 120))],
    "red": [((0, 140, 120), (8, 255, 255)), ((170, 140, 120), (180, 255, 255))],
    "orange_brown": [((8, 110, 90), (22, 255, 230))],
    "yellow": [((22, 120, 150), (35, 255, 255))],
    "green": [((36, 80, 60), (85, 255, 230))],
    "pink_body": [((0, 25, 170), (20, 110, 255)), ((165, 25, 170), (180, 110, 255))],
    "gray_moon": [((0, 0, 120), (180, 25, 215))],
    "black_ink": [((0, 0, 0), (180, 255, 45))],
}


def blobs(img: np.ndarray, rngs, top=3):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    m = np.zeros(img.shape[:2], np.uint8)
    for lo, hi in rngs:
        m |= cv2.inRange(hsv, np.array(lo), np.array(hi))
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    n, lab, st, cen = cv2.connectedComponentsWithStats(m)
    h, w = m.shape
    out = []
    for i in np.argsort(-st[1:, 4])[:top] + 1:
        x, y, bw, bh, a = st[i]
        if a < 150:
            continue
        out.append((a, cen[i][0] / w, cen[i][1] / h, x / w, y / h, (x + bw) / w, (y + bh) / h))
    return out


def main(names):
    for n in names:
        p = Path(n) if Path(n).suffix else DIR / f"{n}.png"
        if not p.exists():
            p = DIR.parent / "gemini_downloaded_long" / f"{n}.png"
        if not p.exists():
            p = DIR.parent / "gemini_downloaded" / f"{n}.png"
        img = cv2.imread(str(p))
        print(f"== {n}")
        for k, r in CLASSES.items():
            for a, cx, cy, x0, y0, x1, y1 in blobs(img, r):
                print(f"  {k:14s} area={a:6d} c=({cx:.2f},{cy:.2f}) box=({x0:.2f},{y0:.2f})-({x1:.2f},{y1:.2f})")


if __name__ == "__main__":
    main(sys.argv[1:])
