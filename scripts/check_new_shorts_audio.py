import subprocess
import numpy as np
import scipy.io.wavfile as wavfile

# Extract audio from new shorts video
subprocess.run(["ffmpeg", "-y", "-i", "projects/tap-07-tom-tit/renders/tap-07-tom-tit_shorts.mp4", "-vn", "temp_new_shorts_audio.wav"], capture_output=True)

sr, data = wavfile.read("temp_new_shorts_audio.wav")
print(f"New Shorts audio: sr={sr}, dur={len(data)/sr:.2f}s, max={np.max(np.abs(data))}")

# Check silence/pause sections (where scribble used to buzz)
# For example around 49.5s to 50.8s where voice has ended
tail_data = data[int(49.5 * sr):int(50.8 * sr)]
print(f"Tail audio (after voice ends): mean_abs={np.mean(np.abs(tail_data)):.2f}, max={np.max(np.abs(tail_data))}")
