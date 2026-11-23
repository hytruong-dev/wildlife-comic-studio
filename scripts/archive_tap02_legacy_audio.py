import os, shutil

audio_dir = "projects/tap-02-rai-ca-bien/audio"
legacy_dir = os.path.join(audio_dir, "_legacy_audio")
os.makedirs(legacy_dir, exist_ok=True)

for f in os.listdir(audio_dir):
    p = os.path.join(audio_dir, f)
    if os.path.isfile(p):
        shutil.move(p, os.path.join(legacy_dir, f))
        print(f"Archived {f}")

print("Cleaned tap-02 audio directory for VoiceStudio TTS")
