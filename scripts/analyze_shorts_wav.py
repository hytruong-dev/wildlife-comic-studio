import numpy as np
import scipy.io.wavfile as wavfile
from pathlib import Path

def analyze_wav(p):
    sr, data = wavfile.read(p)
    if data.ndim > 1:
        data = data.mean(axis=1)
    # Check silent parts
    print(f"File {p}: sr={sr}, dur={len(data)/sr:.2f}s, max={np.max(np.abs(data))}, mean_abs={np.mean(np.abs(data))}")

analyze_wav("projects/tap-07-tom-tit/audio/shorts.wav")
analyze_wav("temp_shorts_audio.wav")
analyze_wav("assets/sfx/marker-scribble-loop.wav")
