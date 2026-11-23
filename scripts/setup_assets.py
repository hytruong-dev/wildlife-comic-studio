import os
import math
import wave
import struct
from pathlib import Path

def create_doodles():
    doodles_dir = Path("assets/doodles")
    doodles_dir.mkdir(parents=True, exist_ok=True)

    doodles = {
        "lightbulb.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M9 18h6"/>
  <path d="M10 22h4"/>
  <path d="M12 2a7 7 0 0 0-7 7c0 2.5 1.5 4.5 3 5.5v1.5a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V14.5c1.5-1 3-3 3-5.5a7 7 0 0 0-7-7z"/>
  <line x1="12" y1="6" x2="12" y2="8"/>
</svg>""",
        "arrow-growth.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
  <polyline points="17 6 23 6 23 12"/>
</svg>""",
        "star.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
</svg>""",
        "target.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>""",
        "heart.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
</svg>""",
        "money-bag.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M11 7h2"/>
  <path d="M9 4h6"/>
  <path d="M4 10a8 8 0 0 0 16 0c0-3-2-5-4-5H8c-2 0-4 2-4 5Z"/>
  <path d="M12 10v4"/>
  <path d="M10 12h4"/>
</svg>""",
        "brain.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 4.44-5.04Z"/>
  <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-4.44-5.04Z"/>
</svg>""",
        "checkmark.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
  <polyline points="20 6 9 17 4 12"/>
</svg>"""
    }

    for name, content in doodles.items():
        p = doodles_dir / name
        p.write_text(content.strip(), encoding="utf-8")
        print(f"[OK] Doodles created: {p}")

def create_calm_bgm():
    bgm_dir = Path("assets/bgm")
    bgm_dir.mkdir(parents=True, exist_ok=True)
    out_wav = bgm_dir / "calm-acoustic.wav"
    out_mp3 = bgm_dir / "calm-acoustic.mp3"

    # Generate a soft, gentle acoustic guitar / Rhodes piano harmonic chord progression (16 seconds loop)
    sr = 44100
    duration_s = 16.0
    total_samples = int(sr * duration_s)

    # Chords: Cmaj7 - Am7 - Fmaj7 - G7 (gentle warm frequencies)
    chord_freqs = [
        [261.63, 329.63, 392.00, 493.88], # Cmaj7
        [220.00, 261.63, 329.63, 392.00], # Am7
        [174.61, 220.00, 261.63, 329.63], # Fmaj7
        [196.00, 246.94, 293.66, 349.23], # G7
    ]

    samples = [0.0] * total_samples
    samples_per_chord = total_samples // len(chord_freqs)

    for c_idx, chord in enumerate(chord_freqs):
        start_samp = c_idx * samples_per_chord
        for n_idx, f in enumerate(chord):
            # Arpeggiated fingerpicking pattern
            note_offset = int((n_idx * 0.35) * sr)
            note_start = start_samp + note_offset
            for s in range(note_start, min(total_samples, start_samp + samples_per_chord)):
                t = (s - note_start) / sr
                envelope = math.exp(-2.5 * t)
                # Harmonic richness with soft timbre
                val = 0.08 * envelope * (
                    math.sin(2 * math.pi * f * t) +
                    0.4 * math.sin(2 * math.pi * 2 * f * t) +
                    0.15 * math.sin(2 * math.pi * 3 * f * t)
                )
                samples[s] += val

    # Write WAV
    with wave.open(str(out_wav), "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        packed_frames = bytearray()
        for s in samples:
            clamped = max(-0.95, min(0.95, s))
            int_val = int(clamped * 32767)
            frame = struct.pack("<hh", int_val, int_val)
            packed_frames.extend(frame)
        wf.writeframes(packed_frames)

    # Convert to MP3 via ffmpeg
    os.system(f'ffmpeg -y -i "{out_wav}" -b:a 192k "{out_mp3}" >nul 2>&1')
    print(f"[OK] BGM Track created: {out_mp3}")

if __name__ == "__main__":
    create_doodles()
    create_calm_bgm()
