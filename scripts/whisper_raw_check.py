"""Raw Whisper transcript of a wav (what the voice REALLY says): python scripts/whisper_raw_check.py <wav> [prompt]"""
import sys
from faster_whisper import WhisperModel

wav = sys.argv[1]
prompt = sys.argv[2] if len(sys.argv) > 2 else None
m = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=8)
import numpy as np, soundfile as sf
data, sr = sf.read(wav, dtype="float32")
if data.ndim > 1:
    data = data.mean(axis=1)
data = np.interp(np.arange(0, len(data), sr / 16000.0), np.arange(len(data)), data).astype(np.float32)
segs, _ = m.transcribe(data, language="vi", initial_prompt=prompt)
for s in segs:
    print(f"{s.start:6.2f}-{s.end:6.2f}  {s.text.strip()}")
