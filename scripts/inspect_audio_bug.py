import subprocess
from pathlib import Path

# Let's inspect assets/sfx/marker-scribble-loop.wav
scrib = Path("assets/sfx/marker-scribble-loop.wav")
print("marker-scribble-loop exists:", scrib.exists())

# Let's extract the audio from tap-07-tom-tit_shorts.mp4 to a wav
shorts_mp4 = Path("projects/tap-07-tom-tit/renders/tap-07-tom-tit_shorts.mp4")
subprocess.run(["ffmpeg", "-y", "-i", str(shorts_mp4), "-vn", "temp_shorts_audio.wav"], capture_output=True)

# Also check projects/tap-06-gau-nuoc/renders/tap-06-gau-nuoc_shorts.mp4
ep06_shorts = Path("projects/tap-06-gau-nuoc/renders/tap-06-gau-nuoc_shorts.mp4")
if ep06_shorts.exists():
    print("ep06 shorts exists!")
    subprocess.run(["ffmpeg", "-y", "-i", str(ep06_shorts), "-vn", "temp_ep06_shorts_audio.wav"], capture_output=True)
