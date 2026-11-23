import subprocess
import shutil
from pathlib import Path

RENDERS_DIR = Path("projects/tap-01-lung-mat/renders")
BRAND_DIR = Path("assets/branding")

# Official Gemini AI Intro & Outro (cleaned of Gemini 4-pointed star watermark)
intro_raw = BRAND_DIR / "gemini_generated_video_105939de.mp4"
outro_raw = BRAND_DIR / "gemini_generated_video_3314fb91.mp4"

intro_mp4 = BRAND_DIR / "intro_ve_chuyen_hoang_da.mp4"
master_mp4 = RENDERS_DIR / "tap01_lung_mat_master.mp4"
outro_mp4 = BRAND_DIR / "outro_ve_chuyen_hoang_da.mp4"

# Step 1: Ensure watermark-free Intro & Outro are generated and normalized (24fps, tbn 12288, 48kHz)
print("Cleaning Gemini watermark and normalizing Intro & Outro timebase (24fps, tbn 12288, 48kHz)...")
subprocess.run(["python", "projects/tap-01-lung-mat/scripts/clean_gemini_watermarks.py"], check=True)

out_complete_intro_outro = RENDERS_DIR / "tap01_lung_mat_complete_with_intro_outro.mp4"
out_complete = RENDERS_DIR / "tap01_lung_mat_complete.mp4"

concat_list = RENDERS_DIR / "complete_concat_list.txt"
lines = [
    f"file '{intro_mp4.resolve().as_posix()}'",
    f"file '{master_mp4.resolve().as_posix()}'",
    f"file '{outro_mp4.resolve().as_posix()}'"
]
concat_list.write_text("\n".join(lines), encoding="utf-8")

# Step 2: Concat with zero frame drop and broadcast 320kbps audio
print("Concatenating Intro + Master + Outro...")
cmd = [
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0",
    "-i", str(concat_list),
    "-c:v", "libx264", "-preset", "fast", "-crf", "17",
    "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2",
    str(out_complete_intro_outro)
]
subprocess.run(cmd, check=True)

shutil.copy2(out_complete_intro_outro, out_complete)

dur_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration,size", "-of", "default=noprint_wrappers=1:nokey=1", str(out_complete_intro_outro)]
out = subprocess.check_output(dur_cmd, text=True).strip().split()
dur_sec = float(out[0])
size_mb = float(out[1]) / (1024 * 1024)
print(f"[SUCCESS] Complete Episode 1 with Official Gemini Intro & Outro created:")
print(f"  File 1: {out_complete_intro_outro}")
print(f"  File 2: {out_complete}")
print(f"  Duration: {dur_sec:.2f}s ({int(dur_sec//60)}m {int(dur_sec%60)}s, {dur_sec/60:.2f} min)")
print(f"  Size: {size_mb:.2f} MB")
