"""Find a constant hum/drone: per-band energy of the voice-only track vs the rendered mix (and in voice pauses)."""
import subprocess, sys
import numpy as np

def load(path, sr=16000):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-vn", "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32), sr

def bands(x, sr, label):
    n = 1 << 15
    segs = [x[i:i + n] for i in range(0, len(x) - n, n)]
    spec = np.mean([np.abs(np.fft.rfft(s * np.hanning(n))) for s in segs], axis=0)
    f = np.fft.rfftfreq(n, 1 / sr)
    edges = [20, 60, 120, 250, 500, 1000, 2000, 4000, 8000]
    row = [20 * np.log10(spec[(f >= a) & (f < b)].mean() + 1e-9) for a, b in zip(edges, edges[1:])]
    lo = (f > 20) & (f < 1000)
    peaks = f[lo][np.argsort(spec[lo])[-5:]][::-1]
    print(f"{label:28s}", " ".join(f"{v:6.1f}" for v in row), "| top<1k Hz:", " ".join(f"{p:.0f}" for p in peaks))

def quiet_parts(x, sr, ref):
    """Samples of the mix where the voice-only track is silent."""
    w = sr // 20
    m = min(len(x), len(ref))
    rms = np.array([np.sqrt(np.mean(ref[i:i + w] ** 2)) for i in range(0, m - w, w)])
    idx = np.where(rms < 0.003)[0]
    return np.concatenate([x[i * w:(i + 1) * w] for i in idx]) if len(idx) else np.zeros(1)

print(" " * 28, "  20-60 60-120 120-250 250-500 0.5-1k  1-2k   2-4k   4-8k")
for p in sys.argv[1:]:
    x, sr = load(p); bands(x, sr, p[-28:])
if len(sys.argv) >= 3:
    # argv[1] MUST be the processed voice (audio/shorts.wav, same tempo as the render), not raw audio/vs/shorts.wav
    v, sr = load(sys.argv[1]); m, _ = load(sys.argv[2])
    q = quiet_parts(m, sr, v)
    print(f"mix during voice pauses: {len(q)/sr:.1f}s  rms={20*np.log10(np.sqrt(np.mean(q**2))+1e-9):.1f} dBFS (incl. SFX)")
    w = sr // 20
    med = np.median([np.sqrt(np.mean(q[i:i + w] ** 2)) for i in range(0, len(q) - w, w)] or [0])
    print(f"NOISE FLOOR (median of pause windows): {20*np.log10(med+1e-9):.1f} dBFS  -> {'OK' if med < 0.01 else 'HUM? listen!'} (target < -40)")
    bands(q, sr, "mix @ voice pauses")
