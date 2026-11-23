import subprocess
import soundfile as sf
import numpy as np
from pathlib import Path
from faster_whisper import WhisperModel
import json

mp3_p = Path('projects/tap-06-gau-nuoc/audio/shorts_v3_perfect.mp3')
wav_p = Path('projects/tap-06-gau-nuoc/audio/shorts_v3_perfect.wav')

# Apply atempo=1.16 to bring 61.04s down to ~52.6s
# Also apply highpass/lowpass broadcast mastering
filter_str = "atempo=1.16,highpass=f=75,lowpass=f=12000,acompressor=threshold=-16dB:ratio=3:attack=5:release=50"
cmd = [
    "ffmpeg", "-y",
    "-i", str(mp3_p),
    "-filter:a", filter_str,
    "-ar", "48000",
    "-ac", "2",
    str(wav_p)
]
subprocess.run(cmd, check=True)

# Read with soundfile
data, sr = sf.read(str(wav_p))
if len(data.shape) > 1:
    mono = data.mean(axis=1)
else:
    mono = data
mono = mono.astype(np.float32)

dur_s = len(mono) / sr
print(f"Processed shorts_v3_perfect.wav duration: {dur_s:.2f}s")

# Extract word timestamps
model = WhisperModel('base', device='cpu', compute_type='int8')
segments, info = model.transcribe(mono, language='vi', word_timestamps=True)

words_data = []
all_segs = []
for seg in segments:
    all_segs.append({"start": round(seg.start, 2), "end": round(seg.end, 2), "text": seg.text})
    for w in seg.words:
        words_data.append({
            "word": w.word.strip(),
            "start": round(w.start, 2),
            "end": round(w.end, 2)
        })

print(f"Total transcribed words: {len(words_data)}")
for s in all_segs:
    print(f"[{s['start']}s -> {s['end']}s]: {s['text']}")

out_json = Path('projects/tap-06-gau-nuoc/audio/shorts_v3_perfect_words.json')
out_json.write_text(json.dumps(words_data, ensure_ascii=False, indent=2), encoding='utf-8')
print("Saved words to", out_json)
