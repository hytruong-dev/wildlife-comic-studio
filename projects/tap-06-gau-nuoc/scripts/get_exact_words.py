import soundfile as sf
import numpy as np
from faster_whisper import WhisperModel
import json

data, sr = sf.read('projects/tap-06-gau-nuoc/audio/shorts_16k.wav')
model = WhisperModel('base', device='cpu', compute_type='int8')
segs, info = model.transcribe(
    data.astype(np.float32),
    language='vi',
    initial_prompt='Gấu Nước Tardigrade bất tử tuyệt chủng ốc sên Mặt Trăng',
    word_timestamps=True
)

words_list = []
for s in segs:
    for w in s.words:
        words_list.append({
            "word": w.word.strip(),
            "start": round(w.start, 2),
            "end": round(w.end, 2)
        })

print("Total words:", len(words_list))
with open('projects/tap-06-gau-nuoc/audio/shorts_v3_exact_words.json', 'w', encoding='utf-8') as f:
    json.dump(words_list, f, ensure_ascii=False, indent=2)

for i in range(0, len(words_list), 10):
    chunk = words_list[i:i+10]
    txt = " ".join([w["word"] for w in chunk])
    t0 = chunk[0]["start"]
    t1 = chunk[-1]["end"]
    print(f"[{t0:.2f}s - {t1:.2f}s]: {txt}")
