"""Script text -> voiceover WAV/MP3 + per-line timing marks (Kokoro, open source).

    python3 tools/voiceover.py script.txt outdir [voice] [speed]

One line of script.txt = one spoken line = one scene. Writes outdir/voiceover.wav,
outdir/voiceover.mp3 and outdir/vo_marks.json ([{i,start,end,text}]).
Models are downloaded by setup.sh into models/.
"""
import json, os, subprocess, sys
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
script, out = sys.argv[1], sys.argv[2]
voice = sys.argv[3] if len(sys.argv) > 3 else "am_eric"
speed = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
k = Kokoro(os.path.join(ROOT, "models/kokoro-v1.0.onnx"), os.path.join(ROOT, "models/voices-v1.0.bin"))
lines = [l.strip() for l in open(script) if l.strip()]
os.makedirs(out, exist_ok=True)
chunks, marks, t, sr = [], [], 0.0, 24000
for i, l in enumerate(lines):
    s, sr = k.create(l, voice=voice, speed=speed, lang="en-gb" if voice[0] == "b" else "en-us")
    gap = np.zeros(int(sr * 0.45), dtype=s.dtype)
    marks.append({"i": i, "start": round(t, 2), "end": round(t + len(s) / sr, 2), "text": l})
    chunks += [s, gap]; t += (len(s) + len(gap)) / sr
audio = np.concatenate(chunks)
sf.write(os.path.join(out, "voiceover.wav"), audio, sr)
json.dump(marks, open(os.path.join(out, "vo_marks.json"), "w"), indent=1)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(out, "voiceover.wav"), "-b:a", "192k", os.path.join(out, "voiceover.mp3")], check=True)
print("lines", len(lines), "total seconds", round(len(audio) / sr, 1))
