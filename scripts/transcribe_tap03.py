import json
from pathlib import Path
import numpy as np
import soundfile as sf
from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")

ep3_script = {}
for i in range(1, 7):
    sid = f"scene0{i}"
    wav_path = Path(f"projects/tap-03-ca-heo/audio/{sid}.wav")
    if wav_path.exists():
        data, sr = sf.read(str(wav_path), dtype="float32")
        if data.ndim > 1:
            data = data.mean(axis=1)
        if sr != 16000:
            idx = np.arange(0, len(data), sr / 16000.0)
            data = np.interp(idx, np.arange(len(data)), data).astype(np.float32)
        segs, _ = model.transcribe(data, language="vi", initial_prompt="Cá Heo, Delphinidae, cá voi, cá mập, cá nóc, Pelorus Jack")
        text = " ".join([s.text.strip() for s in segs])
        ep3_script[sid] = text
        print(f"=== {sid} ({len(text)} chars) ===")
        print(text[:150] + "...")

with open("projects/tap-03-ca-heo/transcribed_script.json", "w", encoding="utf-8") as f:
    json.dump(ep3_script, f, ensure_ascii=False, indent=2)

print("Transcription saved to projects/tap-03-ca-heo/transcribed_script.json")
