import subprocess
import json
from pathlib import Path

AUDIO_DIR = Path("projects/tap-05-chim-bo-nong/audio")
tempo = 1.15

def master_audio(in_file: Path, out_file: Path, tempo: float = 1.15):
    af_chain = (
        f"rubberband=tempo={tempo},"
        "highpass=f=70,lowpass=f=14000,"
        "equalizer=f=140:width_type=o:w=1.0:g=2.2,"
        "equalizer=f=3400:width_type=o:w=1.0:g=2.0,"
        "acompressor=threshold=-15dB:ratio=3:attack=5:release=50,"
        "volume=1.25"
    )
    cmd = [
        "ffmpeg", "-y", "-i", str(in_file),
        "-filter:a", af_chain,
        "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
        str(out_file)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

# Master all 6 parts
part_durs = {}
for i in range(6):
    raw_mp3 = AUDIO_DIR / f"shorts_part{i}_raw.mp3"
    wav_p = AUDIO_DIR / f"shorts_part{i}.wav"
    master_audio(raw_mp3, wav_p, tempo=tempo)
    probe_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(wav_p)]
    dur = float(subprocess.check_output(probe_cmd, text=True).strip())
    part_durs[f"part{i}"] = round(dur, 3)
    print(f"Part {i}: {dur:.3f}s")

# Concat all 6 parts with 120ms gap
gap_wav = AUDIO_DIR / "shorts_gap_120ms.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
    "-t", "0.120", "-c:a", "pcm_s16le", str(gap_wav)
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

concat_lines = []
for i in range(6):
    wav_p = AUDIO_DIR / f"shorts_part{i}.wav"
    concat_lines.append(f"file '{wav_p.resolve().as_posix()}'")
    if i < 5:
        concat_lines.append(f"file '{gap_wav.resolve().as_posix()}'")

concat_file = AUDIO_DIR / "shorts_concat.txt"
concat_file.write_text("\n".join(concat_lines), encoding="utf-8")

final_wav = AUDIO_DIR / "shorts.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", str(concat_file), "-c:a", "pcm_s16le", str(final_wav)
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

probe_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(final_wav)]
total_dur = float(subprocess.check_output(probe_cmd, text=True).strip())
print(f"TOTAL SHORTS AUDIO DURATION: {total_dur:.3f}s")

dur_json = AUDIO_DIR / "shorts_parts_duration.json"
dur_json.write_text(json.dumps({"total_duration": round(total_dur, 3), "gap_sec": 0.12, "parts": part_durs}, indent=2), encoding="utf-8")
print("Saved:", dur_json.name)
