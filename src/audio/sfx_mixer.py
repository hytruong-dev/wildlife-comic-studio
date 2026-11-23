import json
import os
import argparse
import subprocess
import numpy as np
from scipy.io import wavfile
from pathlib import Path

def generate_sfx_track(motion_log_path: str, total_duration_ms: int, out_wav_path: str, sfx_dir: str = "assets/sfx"):
    """
    Tạo track âm thanh SFX đồng bộ với chuyển động bàn tay:
    - Khi Z(t) == 0 và v(t) > 5 px/s: marker scribble loop (-18 dBFS)
    - 40ms fade-in / fade-out khi nhấc/đặt bút
    - Chèn page-whoosh khi có chuyển động camera lớn
    """
    sr = 44100
    total_samples = int((total_duration_ms / 1000.0) * sr)
    sfx_track = np.zeros(total_samples, dtype=np.float32)

    scribble_file = Path(sfx_dir) / "marker-scribble-loop.wav"
    whoosh_file = Path(sfx_dir) / "page-whoosh.wav"

    # Load scribble loop
    scribble_sr, scribble_data = wavfile.read(str(scribble_file))
    if scribble_data.ndim > 1:
        scribble_data = scribble_data[:, 0]
    scribble_norm = scribble_data.astype(np.float32) / 32768.0

    # Load whoosh
    whoosh_sr, whoosh_data = wavfile.read(str(whoosh_file))
    if whoosh_data.ndim > 1:
        whoosh_data = whoosh_data[:, 0]
    whoosh_norm = whoosh_data.astype(np.float32) / 32768.0

    # Read motion log
    with open(motion_log_path, "r", encoding="utf-8") as f:
        log_data = json.load(f)

    frames = log_data.get("frames", [])
    if not frames:
        wavfile.write(out_wav_path, sr, (sfx_track * 32767).astype(np.int16))
        return

    # Envelope array for scribble
    envelope = np.zeros(total_samples, dtype=np.float32)
    scribble_gain = 10.0 ** (-18.0 / 20.0) # -18 dBFS ~= 0.126

    # 40ms fade in samples
    fade_len = int(0.040 * sr)

    for i in range(len(frames)):
        cur = frames[i]
        time_ms = cur.get("timeMs", 0)
        z = cur.get("z", 1.0)
        v = cur.get("v", 0.0)
        is_drawing = cur.get("isDrawing", False)

        # Contact with paper and moving
        if (z < 0.1 and v > 5.0) or is_drawing:
            # Map time to sample range (assume frame covers ~1/30s or ~33ms)
            sample_start = int((time_ms / 1000.0) * sr)
            dt_ms = cur.get("dtMs", 33)
            sample_end = min(total_samples, int(((time_ms + dt_ms) / 1000.0) * sr))
            
            # Subtle speed dependent scaling (0.8x to 1.2x)
            v_factor = np.clip(0.8 + (v / 200.0) * 0.4, 0.7, 1.3)
            envelope[sample_start:sample_end] = scribble_gain * v_factor

        # Check for scene camera switch whoosh
        if cur.get("cameraSwitch", False):
            w_start = int((time_ms / 1000.0) * sr)
            w_len = min(len(whoosh_norm), total_samples - w_start)
            if w_len > 0:
                whoosh_gain = 10.0 ** (-22.0 / 20.0) # -22 dBFS
                sfx_track[w_start:w_start + w_len] += whoosh_norm[:w_len] * whoosh_gain

    # Smooth the scribble envelope to avoid popping (40ms moving window)
    window = np.ones(fade_len) / fade_len
    smoothed_envelope = np.convolve(envelope, window, mode="same")

    # Apply scribble loop
    loop_len = len(scribble_norm)
    for idx in range(total_samples):
        if smoothed_envelope[idx] > 0.001:
            scribble_sample = scribble_norm[idx % loop_len]
            sfx_track[idx] += scribble_sample * smoothed_envelope[idx]

    # Clip to avoid saturation
    sfx_track = np.clip(sfx_track, -0.95, 0.95)

    wavfile.write(out_wav_path, sr, (sfx_track * 32767).astype(np.int16))
    print(f"[OK] Đã tạo track SFX sột soạt bút vẽ: {out_wav_path}")

def mix_master_audio(narration_wav: str, sfx_wav: str, bgm_wav: str | None, output_wav: str, bgm_ducking_db: float = -16.0):
    """
    Trộn giọng đọc narration + SFX + BGM có sidechain ducking bằng FFmpeg
    """
    if not os.path.exists(narration_wav):
        raise FileNotFoundError(f"Không tìm thấy narration wav: {narration_wav}")

    has_sfx = sfx_wav and os.path.exists(sfx_wav)
    has_bgm = bgm_wav and os.path.exists(bgm_wav)

    if not has_sfx and not has_bgm:
        # Just copy or convert narration
        subprocess.run(["ffmpeg", "-y", "-i", narration_wav, "-c:a", "pcm_s16le", output_wav], check=True)
        return

    cmd = ["ffmpeg", "-y", "-i", narration_wav]
    input_count = 1

    if has_sfx:
        cmd.extend(["-i", sfx_wav])
        input_count += 1
    
    if has_bgm:
        cmd.extend(["-i", bgm_wav])
        input_count += 1

    # Build filtergraph
    if has_sfx and not has_bgm:
        filter_str = "[1:a]volume=0.35[sfx];[0:a][sfx]amix=inputs=2:weights=1 1:normalize=0:duration=first[aout]"
    elif has_sfx and has_bgm:
        # Sidechain ducking on BGM by narration
        filter_str = (
            f"[2:a]volume=0.18[bgm_base];"
            f"[bgm_base][0:a]sidechaincompress=threshold=0.08:ratio=4:attack=50:release=350[ducked_bgm];"
            f"[1:a]volume=0.35[sfx];"
            f"[0:a][sfx][ducked_bgm]amix=inputs=3:weights=1 1 1:normalize=0:duration=first[aout]"
        )
    elif not has_sfx and has_bgm:
        filter_str = (
            f"[1:a]volume=0.18[bgm_base];"
            f"[bgm_base][0:a]sidechaincompress=threshold=0.08:ratio=4:attack=50:release=350[ducked_bgm];"
            f"[0:a][ducked_bgm]amix=inputs=2:weights=1 1:normalize=0:duration=first[aout]"
        )

    cmd.extend([
        "-filter_complex", filter_str,
        "-map", "[aout]",
        "-c:a", "pcm_s16le",
        "-ar", "44100",
        output_wav
    ])

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("[WARN] FFmpeg complex mix failed, falling back to simple mix:", res.stderr)
        # Fallback simple amix
        simple_cmd = ["ffmpeg", "-y", "-i", narration_wav]
        if has_sfx: simple_cmd.extend(["-i", sfx_wav])
        simple_cmd.extend(["-filter_complex", f"amix=inputs={input_count}:duration=first", "-c:a", "pcm_s16le", output_wav])
        subprocess.run(simple_cmd, check=True)

    print(f"[OK] Master audio đã trộn hoàn tất: {output_wav}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SFX & Audio Mixer")
    parser.add_argument("--motion-log", type=str, help="File hand_motion_log.json")
    parser.add_argument("--duration-ms", type=float, default=10000.0)
    parser.add_argument("--narration", type=str, required=True)
    parser.add_argument("--sfx-out", type=str, default="sfx_track.wav")
    parser.add_argument("--bgm", type=str, default=None)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    dur_ms = int(round(args.duration_ms))
    if args.motion_log and os.path.exists(args.motion_log):
        generate_sfx_track(args.motion_log, dur_ms, args.sfx_out)
        mix_master_audio(args.narration, args.sfx_out, args.bgm, args.output)
    else:
        mix_master_audio(args.narration, None, args.bgm, args.output)
