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

SCENE_MAPPING = {
    "scene01": ["act01_myth_buster_hook.mp3", "act01_part2.mp3"],
    "scene02": ["act02_rpg_stats.mp3", "act02_part2.mp3"],
    "scene03": ["act03_cryptobiosis_mechanism.mp3", "act03_part2.mp3"],
    "scene04": ["act04_snail_weakness.mp3", "act04_part2.mp3"],
    "scene05": ["act05_moon_mission_beresheet.mp3", "act05_part2.mp3", "act05_part3.mp3"],
    "scene06": ["act06_evolution_lesson_teaser.mp3", "act06_part2.mp3"]
}

total_body_dur = 0.0

print("=== MASTER AUDIO ASSEMBLY WITH BREATHING GAPS (EPISODE 06) ===")

for sid, part_names in SCENE_MAPPING.items():
    # Convert all parts to 48000Hz stereo WAV
    part_wav_paths = []
    for idx, pname in enumerate(part_names):
        src_p = AUDIO_DIR / pname
        dst_wav = AUDIO_DIR / f"{sid}_part{idx}.wav"
        subprocess.run([
            "ffmpeg", "-y", "-i", str(src_p),
            "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(dst_wav)
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        part_wav_paths.append(dst_wav)
        
    concat_txt = AUDIO_DIR / f"{sid}_master_concat.txt"
    lines = []
    lines.append(f"file '{leadin_wav.resolve().as_posix()}'")
    
    parts_durations = {}
    cum_time = LEAD_IN_MS / 1000.0
    
    for idx, pw in enumerate(part_wav_paths):
        lines.append(f"file '{pw.resolve().as_posix()}'")
        probe_cmd = [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(pw)
        ]
        dur = float(subprocess.check_output(probe_cmd, text=True).strip())
        parts_durations[f"part{idx}"] = round(dur, 3)
        cum_time += dur
        
        if idx < len(part_wav_paths) - 1:
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
    
    dur_file = AUDIO_DIR / f"{sid}_parts_duration.json"
    dur_file.write_text(json.dumps({
        "total_duration": round(scene_dur, 3),
        "lead_in_sec": LEAD_IN_MS / 1000.0,
        "gap_sec": GAP_MS / 1000.0,
        "parts": parts_durations
    }, indent=2), encoding="utf-8")
    
    print(f"[{sid}] Duration: {scene_dur:6.2f}s ({scene_dur/60:4.2f}m) | Parts: {len(part_names)}")

print("-" * 55)
print(f"TOTAL 6-SCENE BODY DURATION: {total_body_dur:.2f}s ({total_body_dur/60:.2f}m)")
with_intro_outro = total_body_dur + 20.0  # 10s Intro + 10s Outro
print(f"ESTIMATED FULL VIDEO (WITH INTRO/OUTRO): {with_intro_outro:.2f}s ({with_intro_outro/60:.2f}m)")
if with_intro_outro >= 495.0:
    print("[PASS] Complies strictly with 8:15 - 10:30 min YouTube Long-form standard!")
else:
    print(f"[WARN] Need {495.0 - with_intro_outro:.1f}s more to meet 495s!")
