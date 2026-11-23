import subprocess, os

for i in range(1, 7):
    f = f"projects/tap-02-rai-ca-bien/audio/scene0{i}.wav"
    if os.path.exists(f):
        dur = subprocess.check_output(f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{f}"', shell=True).decode().strip()
        print(f"Scene {i}: {float(dur):.2f}s")
