"""Six background sound designs (no model, numpy). One is picked at random per video.

    python3 tools/bg_beds.py <seconds> <outdir>        # writes bed-01..bed-06.wav
    python3 tools/bg_beds.py --pick <videoslug>        # prints the design chosen for that video (stable per slug)
"""
import hashlib, sys, os
import numpy as np, soundfile as sf
SR = 44100
NAMES = {1:"ambient-pad",2:"soft-plucks",3:"low-drone",4:"light-ticks",5:"warm-lofi",6:"room-air"}

def env(n, a, r):
    e = np.ones(n); na = min(int(a*SR), n//2); nr = min(int(r*SR), n//2)
    e[:na] = np.linspace(0,1,na)**2; e[-nr:] = np.linspace(1,0,nr)**2; return e

def f(m): return 440*2**((m-69)/12)

def bed(k, dur):
    n = int(dur*SR); t = np.arange(n)/SR; x = np.zeros(n)
    if k == 1:   # ambient pad, two detuned sines per note, slow swell
        for m in (57,60,64,67):
            x += 0.05*np.sin(2*np.pi*f(m)*t) + 0.04*np.sin(2*np.pi*f(m)*1.005*t)
        x *= env(n,2.0,2.0)*(1+0.2*np.sin(2*np.pi*0.2*t))
    elif k == 2: # soft plucks every half second on a pentatonic scale
        scale = [57,60,62,64,67]
        for i in range(int(dur*2)):
            p = int(i/2*SR); m = scale[(i*3)%5]+12; d = int(0.9*SR); x_ = np.arange(d)/SR
            w = (np.sin(2*np.pi*f(m)*x_)+0.3*np.sin(4*np.pi*f(m)*x_))*np.exp(-x_*6)*0.05
            e = min(d, n-p); x[p:p+e] += w[:e]
    elif k == 3: # dark low drone with slow pulse (tension)
        x = 0.08*np.sin(2*np.pi*f(33)*t) + 0.05*np.sin(2*np.pi*f(40)*t)
        x *= (0.7+0.3*np.sin(2*np.pi*0.5*t))*env(n,3,3)
    elif k == 4: # light ticks at 100 bpm, quiet
        step = int(0.3*SR)
        for p in range(0, n, step):
            d = min(int(0.04*SR), n-p); x_ = np.arange(d)/SR
            x[p:p+d] += np.random.default_rng(p).normal(0,1,d)*np.exp(-x_*120)*0.05
    elif k == 5: # warm lo-fi pad with vinyl crackle
        for m in (53,57,60):
            x += 0.05*np.sin(2*np.pi*f(m)*t)*(1+0.1*np.sin(2*np.pi*0.3*t))
        rng = np.random.default_rng(5); crackle = (rng.random(n) < 0.0008).astype(float)*0.2
        x = x*env(n,1.5,1.5) + crackle
    elif k == 6: # room air: very low hum and soft noise, almost silent
        x = 0.012*np.sin(2*np.pi*55*t) + 0.004*np.random.default_rng(6).normal(0,1,n)
        x *= env(n,2,2)
    return np.stack([x, x]) * 0.9

def pick(slug):
    h = int(hashlib.sha256(slug.encode()).hexdigest(), 16)
    return h % 6 + 1

if __name__ == "__main__":
    if sys.argv[1] == "--pick":
        k = pick(sys.argv[2]); print(k, NAMES[k])
    else:
        dur = float(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
        for k in NAMES:
            sf.write(os.path.join(out, f"bed-{k:02d}.wav"), bed(k, dur).T, SR)
            print(f"bed-{k:02d}.wav {NAMES[k]}")
