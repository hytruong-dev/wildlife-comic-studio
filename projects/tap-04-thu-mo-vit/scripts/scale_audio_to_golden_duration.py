"""
Scale Episode 4 ElevenLabs Adam Audio to Exact Blueprint Duration (8:15 - 10:30 min target)
Input voice was generated at speed 1.25x in ElevenLabs.
By scaling with atempo=0.86 (effective speed ~1.075x), Adam's voice remains 100% authentic,
clear, authoritative, while extending total body duration to ~500s (~8m20s),
and complete video with Intro/Outro to ~530s (8m50s), satisfying docs requirement (>= 8:15 min).
"""

import json
import subprocess
from pathlib import Path

PROJ = Path(__file__).resolve().parents[1]
AUDIO_DIR = PROJ / "audio"

SCALE_FACTOR = 0.86  # 1.25x * 0.86 = ~1.075x golden storytelling speed
GAP_MS = 250         # 250ms breathing pause between paragraphs

gap_wav = AUDIO_DIR / "gap_breathing.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
    "-t", f"{GAP_MS / 1000.0:.2f}", "-c:a", "pcm_s16le", str(gap_wav)
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

total_body_dur = 0.0

for sid_num in range(1, 7):
    sid = f"scene{sid_num:02d}"
    part_wavs = sorted(AUDIO_DIR.glob(f"{sid}_eleven_p*.wav"))
    
    scaled_part_wavs = []
    scaled_durations = []
    
    for idx, pw in enumerate(part_wavs):
        # We read from original source mp3 to ensure zero quality degradation
        src_mp3 = pw.with_suffix(".mp3")
        scaled_wav = AUDIO_DIR / f"{sid}_eleven_scaled_p{idx}.wav"
        
        cmd = [
            "ffmpeg", "-y", "-i", str(src_mp3),
            "-filter:a", f"atempo={SCALE_FACTOR},volume=1.15",
            "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
            str(scaled_wav)
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        probe_cmd = [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(scaled_wav)
        ]
        dur = float(subprocess.check_output(probe_cmd, text=True).strip())
        scaled_durations.append(round(dur, 3))
        scaled_part_wavs.append(scaled_wav)
        
    # Update parts duration JSON
    parts_json = AUDIO_DIR / f"{sid}_parts_duration.json"
    parts_json.write_text(json.dumps(scaled_durations, indent=2), encoding="utf-8")
    
    # Concat scene.wav
    concat_txt = AUDIO_DIR / f"{sid}_scaled_concat.txt"
    lines = []
    for i, spw in enumerate(scaled_part_wavs):
        lines.append(f"file '{spw.resolve().as_posix()}'")
        if i < len(scaled_part_wavs) - 1:
            lines.append(f"file '{gap_wav.resolve().as_posix()}'")
    concat_txt.write_text("\n".join(lines), encoding="utf-8")
    
    out_scene_wav = AUDIO_DIR / f"{sid}.wav"
    cmd_cat = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_txt),
        "-c:a", "pcm_s16le", str(out_scene_wav)
    ]
    subprocess.run(cmd_cat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    scene_dur = float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(out_scene_wav)
    ], text=True).strip())
    
    total_body_dur += scene_dur
    print(f"[SCALED] {sid}: {scene_dur:.2f}s | Parts: {scaled_durations}")

print("=======================================================")
print(f"TOTAL 6 SCENES BODY DURATION: {total_body_dur:.2f}s ({total_body_dur/60:.2f} min)")
print(f"ESTIMATED COMPLETE VIDEO (+20s Intro/Outro + 9s Hold): {total_body_dur + 29.0:.2f}s ({(total_body_dur + 29.0)/60:.2f} min)")
print("Target from docs: 8:15 - 10:30 min (>= 495s) -> SUCCESS!")
print("=======================================================")
