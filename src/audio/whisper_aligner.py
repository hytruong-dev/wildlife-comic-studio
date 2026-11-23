import json
import argparse
import subprocess
import numpy as np
from pathlib import Path
from faster_whisper import WhisperModel

def load_audio_16k_mono(audio_path: str) -> tuple[np.ndarray, float]:
    """
    Decodes audio directly to 16kHz mono float32 numpy array via FFmpeg.
    This guarantees 100% compatibility across Python versions and avoids PyAV av.open() bugs.
    """
    # Probe duration
    probe_cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", audio_path
    ]
    probe_res = subprocess.run(probe_cmd, capture_output=True, text=True)
    duration_s = float(probe_res.stdout.strip()) if probe_res.returncode == 0 and probe_res.stdout.strip() else 0.0

    # Stream raw float32 samples at 16000Hz mono
    cmd = [
        "ffmpeg", "-y", "-i", audio_path,
        "-f", "f32le", "-ac", "1", "-ar", "16000", "-"
    ]
    proc = subprocess.run(cmd, capture_output=True, check=True)
    audio_data = np.frombuffer(proc.stdout, dtype=np.float32)
    if duration_s == 0.0:
        duration_s = len(audio_data) / 16000.0

    return audio_data, duration_s

def align_audio_with_whisper(audio_path: str, out_dir: str, model_size: str = "base", language: str = "vi"):
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    words_path = out_path / "words_timeline.json"

    print(f"[INFO] Giải mã âm thanh chuẩn 16kHz qua FFmpeg: {audio_path}...")
    audio_data, file_duration_s = load_audio_16k_mono(audio_path)

    print(f"[INFO] Khởi tạo mô hình faster-whisper ({model_size}) trên CPU...")
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    print(f"[INFO] Đang trích xuất Word-level Timestamps từ {audio_path}...")
    segments, info = model.transcribe(audio_data, language=language, word_timestamps=True)

    words_timeline = []
    full_text_parts = []

    for segment in segments:
        full_text_parts.append(segment.text.strip())
        if segment.words:
            for w in segment.words:
                start_ms = int(w.start * 1000)
                end_ms = int(w.end * 1000)
                words_timeline.append({
                    "word": w.word.strip(),
                    "startMs": start_ms,
                    "endMs": end_ms,
                    "durationMs": max(1, end_ms - start_ms),
                    "probability": round(float(w.probability), 3)
                })

    full_text = " ".join(full_text_parts)
    total_duration_ms = int(file_duration_s * 1000) if file_duration_s > 0 else (words_timeline[-1]["endMs"] + 400 if words_timeline else 1000)

    timeline_data = {
        "source": "faster-whisper",
        "audioFile": audio_path,
        "language": language,
        "fullText": full_text,
        "totalDurationMs": total_duration_ms,
        "words": words_timeline
    }

    with open(words_path, "w", encoding="utf-8") as f:
        json.dump(timeline_data, f, ensure_ascii=False, indent=2)

    print(f"[OK] Whisper hoàn tất: {len(words_timeline)} từ đã đồng bộ -> {words_path}")
    return timeline_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Faster-Whisper Word Alignment Tool")
    parser.add_argument("--audio", type=str, required=True, help="Đường dẫn file âm thanh đầu vào")
    parser.add_argument("--output", type=str, required=True, help="Thư mục xuất file words_timeline.json")
    parser.add_argument("--model", type=str, default="base", help="Model size: tiny, base, small")
    parser.add_argument("--lang", type=str, default="vi", help="Ngôn ngữ nhận diện")
    args = parser.parse_args()

    align_audio_with_whisper(args.audio, args.output, args.model, args.lang)
