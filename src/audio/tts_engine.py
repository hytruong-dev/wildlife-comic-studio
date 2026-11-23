import asyncio
import json
import argparse
import subprocess
from pathlib import Path
import edge_tts

async def generate_voice_with_word_timings(text: str, voice: str, rate: str, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    temp_audio_path = out_dir / "temp_narration.mp3"
    audio_path = out_dir / "narration.wav"
    words_path = out_dir / "words_timeline.json"

    communicate = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
    words_timeline = []

    with open(temp_audio_path, "wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                # offset và duration của edge_tts tính bằng đơn vị 100 nanoseconds (10^-7 s)
                start_ms = int(chunk["offset"] / 10000)
                duration_ms = int(chunk["duration"] / 10000)
                words_timeline.append({
                    "word": chunk["text"],
                    "startMs": start_ms,
                    "endMs": start_ms + duration_ms,
                    "durationMs": duration_ms
                })

    # Convert to standard 44.1kHz 16-bit PCM WAV for perfect audio sync & FFmpeg compatibility
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", str(temp_audio_path),
        "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le",
        str(audio_path)
    ]
    res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
    if res.returncode == 0 and temp_audio_path.exists():
        temp_audio_path.unlink()

    # Determine total audio length via ffprobe or last word
    total_duration_ms = (words_timeline[-1]["endMs"] + 600) if words_timeline else 1000
    try:
        probe_cmd = [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path)
        ]
        probe_res = subprocess.run(probe_cmd, capture_output=True, text=True)
        if probe_res.returncode == 0:
            total_duration_ms = int(float(probe_res.stdout.strip()) * 1000)
    except Exception:
        pass

    timeline_data = {
        "voice": voice,
        "fullText": text,
        "totalDurationMs": total_duration_ms,
        "words": words_timeline
    }

    with open(words_path, "w", encoding="utf-8") as f:
        json.dump(timeline_data, f, ensure_ascii=False, indent=2)

    print(f"[OK] Đã tạo audio: {audio_path} ({len(words_timeline)} từ đã đồng bộ timestamp, {total_duration_ms}ms)")
    return timeline_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Edge-TTS Local Word-Sync Generator")
    parser.add_argument("--text", type=str, help="Nội dung văn bản")
    parser.add_argument("--input", type=str, help="Đường dẫn file script.txt")
    parser.add_argument("--voice", type=str, default="vi-VN-NamMinhNeural")
    parser.add_argument("--rate", type=str, default="+0%")
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    content = args.text if args.text else Path(args.input).read_text(encoding="utf-8").strip()
    asyncio.run(generate_voice_with_word_timings(content, args.voice, args.rate, Path(args.output)))
