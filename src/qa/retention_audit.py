"""Retention audit for a finished long-form video (objective metrics only).

Measures per-second visual change (mean abs frame diff on a 160x90 proxy), finds
"frozen" stretches where almost nothing moves, detects audio silences and loudness.

Usage: python src/qa/retention_audit.py <video.mp4> [--freeze-thr 0.6] [--min-freeze 6]
"""
import json
import re
import subprocess
import sys

import numpy as np


def visual_activity(path: str, fps: int = 2) -> np.ndarray:
    w, h = 160, 90
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={fps},scale={w}:{h},format=gray",
           "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    frames = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)
    diff = np.abs(np.diff(frames, axis=0)).mean(axis=(1, 2))
    per_sec = diff[: len(diff) // fps * fps].reshape(-1, fps).max(axis=1)
    return per_sec


def silences(path: str, noise="-38dB", d=0.8):
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", path, "-af", f"silencedetect=n={noise}:d={d}",
                        "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="ignore")
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    du = [float(x) for x in re.findall(r"silence_duration: ([\d.]+)", r.stderr)]
    return list(zip(st, du))


def loudness(path: str):
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", path, "-af", "loudnorm=print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="ignore")
    js = r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1]
    return json.loads(js)


def main():
    path = sys.argv[1]
    thr = float(sys.argv[sys.argv.index("--freeze-thr") + 1]) if "--freeze-thr" in sys.argv else 0.6
    min_f = int(sys.argv[sys.argv.index("--min-freeze") + 1]) if "--min-freeze" in sys.argv else 6
    act = visual_activity(path)
    n = len(act)
    print(f"duration≈{n}s  mean activity={act.mean():.2f}  median={np.median(act):.2f}")
    print("activity per 10s window (avg):")
    for i in range(0, n, 10):
        seg = act[i:i + 10]
        bar = "#" * int(min(40, seg.mean() * 8))
        print(f"  {i // 60:02d}:{i % 60:02d}  {seg.mean():5.2f} {bar}")
    frozen, run = [], 0
    for i, a in enumerate(list(act) + [99]):
        if a < thr:
            run += 1
        else:
            if run >= min_f:
                frozen.append((i - run, run))
            run = 0
    tot = sum(r for _, r in frozen)
    print(f"\nFROZEN stretches (activity<{thr} for ≥{min_f}s): {len(frozen)}, total {tot}s ({100 * tot / n:.0f}%)")
    for s, r in frozen:
        print(f"  {s // 60:02d}:{s % 60:02d} -> {(s + r) // 60:02d}:{(s + r) % 60:02d}  ({r}s)")
    sil = silences(path)
    print(f"\nSILENCES ≥0.8s: {len(sil)}")
    for s, d in sil:
        print(f"  {int(s) // 60:02d}:{s % 60:05.2f}  {d:.2f}s")
    ld = loudness(path)
    print(f"\nLOUDNESS: I={ld['input_i']} LUFS  TP={ld['input_tp']} dBTP  LRA={ld['input_lra']}")


if __name__ == "__main__":
    main()
