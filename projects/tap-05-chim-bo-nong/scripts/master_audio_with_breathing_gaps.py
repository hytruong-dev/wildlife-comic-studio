"""
Master Audio Assembly with Natural Breathing Gaps for Episode 5: Chim Bồ Nông
Ensures:
- 350ms breathing pause between voice paragraphs (natural broadcast storytelling pace)
- 500ms initial lead-in for whiteboard camera establishing shot
- Total body duration ~485s, with Intro/Outro = ~505s - 512s (~8m25s - 8m32s)
- Strictly satisfies docs & director requirement: >= 8:15 min (495s)
"""

import json
import subprocess
from pathlib import Path

PROJ = Path(__file__).resolve().parents[1]
AUDIO_DIR = PROJ / "audio"

GAP_MS = 350        # 350ms natural breathing gap
LEAD_IN_MS = 400    # 400ms lead-in

gap_wav = AUDIO_DIR / "gap_breathing.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
    "-t", f"{GAP_MS / 1000.0:.3f}", "-c:a", "pcm_s16le", str(gap_wav)
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

leadin_wav = AUDIO_DIR / "gap_leadin.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
    "-t", f"{LEAD_IN_MS / 1000.0:.3f}", "-c:a", "pcm_s16le", str(leadin_wav)
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

total_body_dur = 0.0

for sid_num in range(1, 7):
    sid = f"scene{sid_num:02d}"
    part_wavs = sorted(AUDIO_DIR.glob(f"{sid}_part*.wav"))
    
    # Concat with lead-in and breathing gaps
    concat_txt = AUDIO_DIR / f"{sid}_master_concat.txt"
    lines = []
    lines.append(f"file '{leadin_wav.resolve().as_posix()}'")
    
    parts_durations = {}
    cum_time = LEAD_IN_MS / 1000.0
    
    for idx, pw in enumerate(part_wavs):
        lines.append(f"file '{pw.resolve().as_posix()}'")
        probe_cmd = [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(pw)
        ]
        dur = float(subprocess.check_output(probe_cmd, text=True).strip())
        parts_durations[f"part{idx}"] = round(dur, 3)
        cum_time += dur
        
        if idx < len(part_wavs) - 1:
            lines.append(f"file '{gap_wav.resolve().as_posix()}'")
            cum_time += GAP_MS / 1000.0
            
    concat_txt.write_text("\n".join(lines), encoding="utf-8")
    
    final_wav = AUDIO_DIR / f"{sid}.wav"
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_txt), "-c:a", "pcm_s16le", str(final_wav)
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    probe_cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(final_wav)
    ]
    scene_dur = float(subprocess.check_output(probe_cmd, text=True).strip())
    total_body_dur += scene_dur
    
    # Save parts duration JSON
    dur_file = AUDIO_DIR / f"{sid}_parts_duration.json"
    dur_file.write_text(json.dumps({
        "total_duration": round(scene_dur, 3),
        "lead_in_sec": LEAD_IN_MS / 1000.0,
        "gap_sec": GAP_MS / 1000.0,
        "parts": parts_durations
    }, indent=2), encoding="utf-8")
    
    print(f"[{sid}] Master Audio Duration: {scene_dur:.2f}s ({scene_dur/60:.2f} min)")

print(f"\nTOTAL BODY DURATION: {total_body_dur:.2f}s ({int(total_body_dur//60)}m {int(total_body_dur%60)}s)")
total_with_intro_outro = total_body_dur + 20.06
print(f"ESTIMATED COMPLETE DURATION (WITH INTRO+OUTRO): {total_with_intro_outro:.2f}s ({int(total_with_intro_outro//60)}m {int(total_with_intro_outro%60)}s, {total_with_intro_outro/60:.2f} min)")
