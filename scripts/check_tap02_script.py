import sys
sys.path.insert(0, "projects/tap-02-rai-ca-bien/scripts")
import generate_full_duration_audio_125x as m

tot = 0
for sc in m.FULL_SCENES:
    if sc["id"] != "shorts":
        chars = sum(len(p) for p in sc["paragraphs"])
        tot += chars
        print(sc["id"], len(sc["paragraphs"]), "parts", chars, "chars")
print("Total longform chars:", tot)
