"""Sound design: synthesise effects for every on-screen moment and mix them under the voice.

    python3 tools/sfx.py videos/NNN-slug/sfx_events.json in.mp4 out.mp4 [level=1.0] [until_seconds]

sfx_events.json is written by scenelib.write_project (one cue per element, drawing and scene change).
Every sound is generated here with numpy (no samples, no copyright):
  text appears  -> soft keyboard typing (more letters = more clicks, capped)
  number counts -> fast ticks rising in pitch for the count's length, then a bright "ding"
  pop / drawing -> short bubbly pop        wipe -> swoosh        stamp -> low thump
  line drawn    -> quiet shimmer           scene change -> airy whoosh
The effects are ducked under the voice so words stay clear.
"""
import json, os, subprocess, sys, tempfile
import numpy as np, soundfile as sf

SR = 48000
rng = np.random.default_rng(7)


def env(n, a=0.002, d=0.05):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)


def tone(f0, f1, dur, a=0.002, d=0.08, shape="sine"):
    n = int(dur * SR); t = np.arange(n) / SR
    f = np.linspace(f0, f1, n)
    ph = 2 * np.pi * np.cumsum(f) / SR
    w = np.sin(ph) if shape == "sine" else np.sign(np.sin(ph)) * 0.6
    return w * env(n, a, d)


def lowpass(x, k):
    k = max(1, int(k))
    return np.convolve(x, np.ones(k) / k, mode="same")


def click():
    n = int(0.018 * SR)
    noise = rng.standard_normal(n)
    hp = noise - lowpass(noise, 6)                        # bright tick
    body = tone(1800 + rng.uniform(-300, 300), 1200, 0.018, d=0.006) * 0.5
    return (hp * env(n, 0.0005, 0.004) * 0.6 + body) * rng.uniform(0.6, 1.0)


def typing(nchars):
    k = int(np.clip(nchars / 3, 3, 12))
    out = np.zeros(int((k * 0.045 + 0.05) * SR))
    for i in range(k):
        s = int((i * 0.045 + rng.uniform(-0.008, 0.008)) * SR); c = click()
        s = max(0, s); out[s:s + len(c)] += c[:len(out) - s]
    return out * 0.55


def ticker(dur):
    out = np.zeros(int((dur + 0.9) * SR)); t = 0.0; i = 0
    while t < dur:
        p = t / dur
        f = 900 + 1100 * p
        b = tone(f, f * 0.9, 0.03, d=0.01) * (0.35 + 0.25 * p)
        s = int(t * SR); out[s:s + len(b)] += b
        t += 0.075 - 0.035 * p; i += 1
    s = int(dur * SR)
    ding = (tone(1568, 1568, 0.8, d=0.25) + 0.5 * tone(2352, 2352, 0.8, d=0.18) + 0.25 * tone(3136, 3136, 0.8, d=0.1)) * 0.5
    out[s:s + len(ding)] += ding[:len(out) - s]
    return out


def pop(big=False):
    f0, f1 = (260, 720) if big else (420, 1100)
    p = tone(f0, f1, 0.09, a=0.001, d=0.03 if not big else 0.05)
    return p * (0.75 if big else 0.5)


def swoosh(dur=0.35, bright=0.0):
    n = int(dur * SR); noise = rng.standard_normal(n)
    t = np.arange(n) / n
    e = np.sin(np.pi * t) ** 2
    a = lowpass(noise, 40); b = lowpass(noise, 8)
    mix = a * (1 - t) + b * t * (0.6 + bright)
    return mix * e * 0.5


def thump():
    out = tone(110, 45, 0.25, a=0.001, d=0.09) * 0.9
    sw = swoosh(0.12) * 0.3
    out[:len(sw)] += sw
    return out


def shimmer(dur=0.6):
    n = int(dur * SR); out = np.zeros(n)
    for f in (2093, 2637, 3136):
        out += tone(f, f * 1.01, dur, a=0.05, d=0.25)
    return out * 0.12 * np.sin(np.pi * np.arange(n) / n)


def build(events, total):
    out = np.zeros(int((total + 2) * SR))
    last = {}
    for e in events:
        t, k, n = e["t"], e["kind"], e.get("n", 0)
        if t > total:
            continue
        group = "pop" if k in ("pop", "draw") else k
        if t - last.get(group, -9) < (0.05 if group == "pop" else 0.12):
            continue  # merge cues that land together
        last[group] = t
        if k in ("fade", "blur"):
            snd = typing(n) if n > 0 else pop()
        elif k == "count":
            snd = ticker(e.get("dur", 1.4))
        elif k == "pop":
            snd = pop(big=n > 0)
        elif k == "draw":
            snd = shimmer() if n == 0 else typing(n)
        elif k == "wipe":
            snd = swoosh(0.3, bright=0.4)
        elif k == "stamp":
            snd = thump()
        elif k == "scene":
            snd = swoosh(0.45) * 0.8
            t = max(0, t - 0.15)
        else:
            continue
        s = int(t * SR); out[s:s + len(snd)] += snd[:len(out) - s]
    peak = np.max(np.abs(out)) or 1
    return np.tanh(out / peak * 1.2) * 0.7


def main():
    ev_path, vin, vout = sys.argv[1], sys.argv[2], sys.argv[3]
    level = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
    until = float(sys.argv[5]) if len(sys.argv) > 5 else None
    dur = float(json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", vin],
                                          capture_output=True, text=True, check=True).stdout)["format"]["duration"])
    total = min(dur, until) if until else dur
    fx = build(json.load(open(ev_path)), total)
    tmp = os.path.join(tempfile.gettempdir(), "sfx_track.wav")
    sf.write(tmp, np.stack([fx, fx], 1), SR)
    filt = (f"[1:a]volume={0.85 * level},aformat=sample_rates=48000:channel_layouts=stereo[fx];"
            f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit=2[v][k];"
            f"[fx][k]sidechaincompress=threshold=0.05:ratio=2:attack=10:release=200[fxd];"
            f"[v][fxd]amix=inputs=2:duration=first:normalize=0[a]")
    cmd = ["ffmpeg", "-v", "error", "-y"] + (["-t", str(total)] if until else []) + ["-i", vin, "-i", tmp,
           "-filter_complex", filt, "-map", "0:v", "-map", "[a]", "-c:v", "libx264" if until else "copy"] + \
          (["-preset", "fast", "-crf", "18"] if until else []) + ["-c:a", "aac", "-b:a", "192k", vout]
    subprocess.run(cmd, check=True)
    print("sound design added:", vout, f"({total:.1f} s)")


if __name__ == "__main__":
    main()
