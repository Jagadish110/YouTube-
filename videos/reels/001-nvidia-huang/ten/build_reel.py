"""Instagram Reel (1080x1920, native vertical): Nvidia CEO resignation, explained.

    python3 build_reel.py            # writes reel.html, renders frames with Playwright, adds sound -> output/reel.mp4
    python3 build_reel.py html       # only write reel.html

Style is different from the YouTube videos/Shorts: black + Nvidia green, full-screen kinetic captions,
bass hits / risers / glitch ticks instead of typing and pops. No photos, no logos (drawn silhouette only).
"""
import base64, json, os, subprocess, sys
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..", "..")
M = json.load(open(os.path.join(HERE, "vo_marks.json")))
TOTAL = round(M[-1]["end"] + 1.6, 2); FPS = 30
G = "#76B900"


def font(name, fam, w):
    b = base64.b64encode(open(os.path.join(ROOT, "tools/fonts", name), "rb").read()).decode()
    return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}"


# ---- captions: chunks of about 3 words, timed by character share of each spoken line
HI = {"quit.", "spy", "affair", "resigned.", "billion", "open.", "denies", "without", "him?"}
caps = []
for m in M:
    w = m["text"].split(); n = sum(len(x) + 1 for x in w); t = m["start"]; d = m["end"] - m["start"]
    for i in range(0, len(w), 2):
        ch = w[i:i + 2]; dt = d * sum(len(x) + 1 for x in ch) / n
        caps.append((round(t, 3), round(t + dt, 3), " ".join(f'<b>{x}</b>' if x.lower() in HI else x for x in ch)))
        t += dt
cap_html = "".join(f'<div class="cap" id="c{i}"><span>{x}</span></div>' for i, (_, _, x) in enumerate(caps))
cap_js = "".join(f'tl.set("#c{i}",{{opacity:1}},{a}).fromTo("#c{i}",{{scale:.86,y:18}},{{scale:1,y:0,duration:.16,ease:"back.out(2.5)"}},{a}).set("#c{i}",{{opacity:0}},{b});'
                 for i, (a, b, _) in enumerate(caps))

S = [m["start"] for m in M]; E = [m["end"] for m in M]
CUTS = S[1:]                                   # scene changes
person = f'''<svg viewBox="0 0 600 640" width="600" height="640">
 <ellipse cx="300" cy="600" rx="250" ry="26" fill="{G}" opacity=".18"/>
 <path d="M70 640 C70 430 150 350 235 330 L300 372 L365 330 C450 350 530 430 530 640 Z" fill="#0d0f0d" stroke="{G}" stroke-width="5"/>
 <path d="M235 330 L262 300 L300 372 Z M365 330 L338 300 L300 372 Z" fill="#161a16" stroke="{G}" stroke-width="4"/>
 <path d="M300 372 V640" stroke="{G}" stroke-width="3" stroke-dasharray="10 12" opacity=".7"/>
 <circle cx="300" cy="205" r="104" fill="#0d0f0d" stroke="{G}" stroke-width="5"/>
 <path d="M200 185 C205 105 395 105 400 185 C380 150 340 138 300 138 C260 138 220 150 200 185 Z" fill="#cfd6cf"/>
</svg>'''
chip = f'''<svg viewBox="0 0 300 300" width="300" height="300"><g stroke="{G}" stroke-width="8" stroke-linecap="round">
 {"".join(f'<path d="M{70 + i * 40} 20 V60 M{70 + i * 40} 240 V280 M20 {70 + i * 40} H60 M240 {70 + i * 40} H280"/>' for i in range(5))}</g>
 <rect x="60" y="60" width="180" height="180" rx="18" fill="#0d0f0d" stroke="{G}" stroke-width="8"/>
 <rect x="105" y="105" width="90" height="90" rx="8" fill="{G}"/></svg>'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{font("anton-latin-400-normal.woff2", "Anton", 400)}{font("sora-latin-800-normal.woff2", "Sora", 800)}{font("sora-latin-600-normal.woff2", "Sora", 600)}
*{{box-sizing:border-box}} html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#040604;color:#fff;font-family:Sora}}
#bg{{position:absolute;inset:0;background:radial-gradient(900px 700px at 50% 34%,rgba(118,185,0,.26),transparent 70%),linear-gradient(#040604,#070b05)}}
#grid{{position:absolute;inset:-80px;background-image:linear-gradient(rgba(118,185,0,.10) 2px,transparent 2px),linear-gradient(90deg,rgba(118,185,0,.10) 2px,transparent 2px);background-size:90px 90px;transform:perspective(900px) rotateX(58deg) translateY(520px);transform-origin:50% 100%}}
#flash{{position:absolute;inset:0;background:{G};opacity:0}}
#bar{{position:absolute;left:60px;top:150px;width:960px;height:8px;background:rgba(255,255,255,.16);border-radius:8px}} #barf{{height:8px;width:0;background:{G};border-radius:8px}}
#tag{{position:absolute;left:60px;top:182px;font:800 30px Sora;letter-spacing:5px;color:{G}}}
#tag2{{position:absolute;right:60px;top:182px;font:600 30px Sora;color:#b9c2b9}}
.sc{{position:absolute;left:0;top:250px;width:1080px;height:960px;opacity:0}}
.abs{{position:absolute}} .ctr{{left:0;width:1080px;text-align:center}}
.an{{font-family:Anton;text-transform:uppercase;line-height:1.0}}
.card{{position:absolute;left:90px;width:900px;border-radius:28px;padding:34px 40px;background:#0e130c;border:3px solid rgba(118,185,0,.55);font:600 46px/1.25 Sora}}
.card small{{display:block;font:800 30px Sora;letter-spacing:4px;color:{G};margin-bottom:10px}}
.date{{position:absolute;left:340px;width:400px;border-radius:30px;overflow:hidden;background:#fff;color:#0a0d0a;text-align:center}}
.date i{{display:block;font:800 44px Sora;font-style:normal;background:{G};padding:14px 0;letter-spacing:6px}} .date span{{display:block;font:400 230px/1.1 Anton;padding-bottom:14px}}
#stamp{{position:absolute;left:150px;top:560px;width:780px;text-align:center;font:400 170px/1.15 Anton;color:#ff3b30;border:14px solid #ff3b30;border-radius:26px;transform:rotate(-9deg)}}
#caps{{position:absolute;left:60px;top:1250px;width:960px;height:300px}}
.cap{{position:absolute;left:0;top:0;width:960px;height:300px;display:flex;align-items:center;justify-content:center;text-align:center;opacity:0;font:400 104px/1.08 Anton;text-transform:uppercase;letter-spacing:1px;text-shadow:0 6px 0 #000,0 0 40px rgba(0,0,0,.9)}}
.cap b{{font-weight:400;color:{G}}}
#src{{position:absolute;left:60px;top:1640px;width:960px;text-align:center;font:600 28px Sora;color:#aab3aa}}
</style></head><body>
<div id="bg"></div><div id="grid"></div>
<div class="sc" id="s0">
 <div class="abs" id="p0" style="left:240px;top:330px;opacity:.55">{person}</div>
 <div class="abs ctr an" id="h1" style="top:60px;font-size:190px">NVIDIA'S CEO</div>
 <div class="abs ctr an" id="h2" style="top:270px;font-size:300px;color:{G}">JUST QUIT</div>
</div>
<div class="sc" id="s1">
 <div class="abs ctr an" id="a1" style="top:40px;font-size:150px">CHINESE</div>
 <div class="abs ctr an" id="a2" style="top:210px;font-size:240px;white-space:nowrap;color:{G}">SPY LINK?</div>
 <div class="abs ctr" id="a3" style="top:540px"><span style="display:inline-block;font:800 46px Sora;letter-spacing:4px;color:#ff3b30;border:6px solid #ff3b30;border-radius:18px;padding:14px 30px">REPORTED · NOT PROVEN</span></div>
 <div class="abs ctr" id="a4" style="top:700px;font:600 38px Sora;color:#b9c2b9">New York Times report, October · China denies it</div>
</div>
<div class="sc" id="s2">
 <div class="date" id="d8" style="top:10px"><i>NOVEMBER</i><span>8</span></div>
 <div class="card" id="k1" style="top:470px"><small>HIS LETTER TO STAFF</small>Says he was not faithful to his wife</div>
</div>
<div class="sc" id="s3">
 <div class="date" id="d12" style="top:10px"><i>NOVEMBER</i><span>12</span></div>
 <div id="stamp">RESIGNED</div>
</div>
<div class="sc" id="s4">
 <svg class="abs" style="left:60px;top:0" width="960" height="560" viewBox="0 0 960 560">
  <path d="M0 520 H960" stroke="rgba(255,255,255,.25)" stroke-width="3"/>
  <path id="ln" d="M20 150 L150 120 L280 160 L400 110 L500 130 L520 440 L640 380 L760 300 L940 215" fill="none" stroke="#ff3b30" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1900" stroke-dashoffset="1900"/>
 </svg>
 <div class="abs an" id="bn" style="left:80px;top:540px;font-size:230px;color:#ff3b30;line-height:.95">−$<span id="n546">0</span><br>BILLION</div>
 <div class="abs" id="pl" style="left:660px;top:580px;font:800 40px/1.25 Sora">−14% at<br>the open,<br>12 Nov</div>
 <div class="abs" id="cl" style="left:84px;top:1000px;font:800 38px Sora;color:{G};white-space:nowrap">Closed −4.3% that day</div>
</div>
<div class="sc" id="s5">
 <div class="abs ctr an" id="e1" style="top:60px;font-size:150px">CAN NVIDIA<br>STAY NVIDIA</div>
 <div class="abs ctr an" id="e2" style="top:410px;font-size:176px;white-space:nowrap;color:{G}">WITHOUT HIM?</div>
 <div class="abs ctr" id="e3" style="top:670px;font:800 44px Sora">Comment your answer 👇</div>
</div>
<div id="at" style="position:absolute;left:0;top:1568px;width:1080px;text-align:center;font:800 44px Sora;color:{G};opacity:0">@trendsplain</div>
<div id="caps">{cap_html}</div>
<div id="src">Sources: Al Jazeera · Yahoo Finance</div>
<div id="flash"></div>
<script>{open(os.path.join(ROOT, "videos/001-zepto/project/assets/gsap.min.js")).read()}</script>
<script>
const tl=gsap.timeline({{paused:true}}); window.tl=tl; const S={json.dumps(S)},E={json.dumps(E)},T={TOTAL};
tl.fromTo("#grid",{{backgroundPosition:"0px 0px"}},{{backgroundPosition:"0px 400px",duration:T,ease:"none"}},0);
[0,1,2,3,4,5].forEach(i=>{{const a=i?S[i]-.08:0,b=i<5?S[i+1]-.08:T;
  tl.set("#s"+i,{{opacity:1}},a).fromTo("#s"+i,{{scale:1.12}},{{scale:1,duration:.28,ease:"power3.out"}},a);
  if(i){{tl.fromTo("#flash",{{opacity:.5}},{{opacity:0,duration:.22,immediateRender:false}},a)}} if(i<5)tl.set("#s"+i,{{opacity:0}},b);}});
tl.from("#h1",{{y:-220,opacity:0,duration:.2,ease:"power4.out"}},.03).from("#h2",{{scale:3,opacity:0,duration:.18,ease:"power4.in"}},1.0)
  .fromTo("#s0",{{x:-14}},{{x:14,duration:.05,repeat:5,yoyo:true,ease:"none"}},1.18).set("#s0",{{x:0}},1.5).fromTo("#flash",{{opacity:.7}},{{opacity:0,duration:.3,immediateRender:false}},1.18);
tl.from("#a1",{{y:-150,opacity:0,duration:.2}},S[1]+.05).from("#a2",{{scale:2.5,opacity:0,duration:.18,ease:"power4.in"}},S[1]+1.1).from("#a3",{{scale:0,duration:.25,ease:"back.out(2.5)"}},S[1]+.45).from("#a4",{{opacity:0,duration:.25}},S[1]+1.4);
tl.from("#d8",{{y:-300,opacity:0,duration:.25,ease:"back.out(1.6)"}},S[2]+.03).from("#k1",{{x:-1000,duration:.3,ease:"power3.out"}},S[2]+.6);
tl.from("#d12",{{y:-300,opacity:0,duration:.25,ease:"back.out(1.6)"}},S[3]+.03).from("#stamp",{{scale:4,opacity:0,duration:.16,ease:"power4.in"}},E[3]-.7)
  .fromTo("#s3",{{x:-12}},{{x:12,duration:.05,repeat:5,yoyo:true,ease:"none"}},E[3]-.54).set("#s3",{{x:0}},E[3]-.2);
const o={{c:0}}; tl.to("#ln",{{strokeDashoffset:880,duration:.5,ease:"none"}},S[4]).to("#ln",{{strokeDashoffset:560,duration:.2,ease:"power2.in"}},S[4]+.5)
  .from("#bn",{{y:60,opacity:0,duration:.2}},S[4]+.4).to(o,{{c:546,duration:1.3,ease:"power2.out",onUpdate:()=>document.getElementById("n546").textContent=Math.round(o.c)}},S[4]+.4)
  .from("#pl",{{opacity:0,duration:.25}},S[4]+2.4).to("#ln",{{strokeDashoffset:0,duration:.8,ease:"power1.out"}},E[4]-.9).from("#cl",{{opacity:0,x:40,duration:.25}},E[4]-.7)
  .from("#e1",{{y:-100,opacity:0,duration:.25}},S[5]+.1).from("#e2",{{scale:2.6,opacity:0,duration:.2,ease:"power4.in"}},E[5]-.9)
  .fromTo("#flash",{{opacity:.6}},{{opacity:0,duration:.3,immediateRender:false}},E[5]-.7).from("#e3",{{y:40,opacity:0,duration:.3}},E[5]-.2).to("#at",{{opacity:1,duration:.25}},E[5]);
{cap_js}
</script></body></html>'''
open(os.path.join(HERE, "reel.html"), "w").write(html)
if len(sys.argv) > 1 and sys.argv[1] == "html":
    sys.exit()

# ---- render frames
from playwright.sync_api import sync_playwright
os.makedirs(os.path.join(HERE, "output"), exist_ok=True)
raw = os.path.join(HERE, "output", "reel-raw.mp4")
ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                       "-c:v", "libx264", "-preset", "fast", "-crf", "17", "-pix_fmt", "yuv420p", raw], stdin=subprocess.PIPE)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto("file://" + os.path.join(HERE, "reel.html")); pg.evaluate("document.fonts.ready.then(()=>1)")
    for f in range(int(TOTAL * FPS)):
        pg.evaluate(f"void tl.seek({f / FPS}, false)")
        ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
    b.close()
ff.stdin.close(); ff.wait()

# ---- sound: sub-bass hits, risers, glitch ticks, low pulse bed (all synthesised)
SR = 48000; rng = np.random.default_rng(11); n = int((TOTAL + 0.5) * SR); fx = np.zeros(n)
def put(x, t, g=1.0):
    s = max(0, int(t * SR)); x = x[:n - s]; fx[s:s + len(x)] += x * g
def hit(d=0.7):
    t = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * (38 * t + 55 * 0.09 * (1 - np.exp(-t / 0.09)))) * np.exp(-t / 0.22) + rng.standard_normal(len(t)) * np.exp(-t / 0.012) * 0.5
def riser(d=0.8):
    t = np.arange(int(d * SR)) / SR; x = rng.standard_normal(len(t)); k = np.ones(24) / 24
    return (x - np.convolve(x, k, "same")) * (t / d) ** 3 * 0.5 + np.sin(2 * np.pi * (200 * t + 500 * t * t / d)) * (t / d) ** 2 * 0.25
def tick():
    t = np.arange(int(0.03 * SR)) / SR
    return np.sign(np.sin(2 * np.pi * rng.choice([1400, 1900, 2600]) * t)) * np.exp(-t / 0.006) * 0.25
def whoosh(d=0.3):
    t = np.arange(int(d * SR)) / SR; x = np.convolve(rng.standard_normal(len(t)), np.ones(30) / 30, "same")
    return x * np.sin(np.pi * t / d) ** 2 * 2.2
put(hit(), 0.03, .8); put(riser(0.6), .5, .8); put(hit(0.9), 1.18, 1.0)
for c in CUTS: put(whoosh(), c - 0.2, .7); put(hit(0.5), c - 0.06, .55)
for a, _, _ in caps: put(tick(), a, .5)
put(hit(0.8), S[1] + 1.28, .9); put(whoosh(), S[2] + .6); put(hit(0.9), E[3] - .54, 1.0)
for i in range(17): put(tick(), S[4] + .4 + i * 0.075, .7)
put(hit(0.9), S[4] + .7, .9); put(riser(0.7), E[5] - 1.4, .8); put(hit(1.0), E[5] - .7, 1.0)
t = np.arange(n) / SR                                                    # dark pulse bed, 100 bpm
bed = np.sin(2 * np.pi * 55 * t) * (0.5 + 0.5 * np.sin(2 * np.pi * (120 / 60) * t)) ** 4 * 0.10 + np.sin(2 * np.pi * 110.3 * t) * 0.02
fade = np.minimum(1, np.minimum(t / 0.5, (t[-1] - t) / 0.6)); fx = np.tanh((fx * 0.55 + bed * fade) * 1.3) * 0.75
sf.write(os.path.join(HERE, "output", "fx.wav"), np.stack([fx, fx], 1), SR)
out = os.path.join(HERE, "output", "reel-nvidia-short.mp4")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-i", os.path.join(HERE, "voiceover.wav"), "-i", os.path.join(HERE, "output", "fx.wav"),
                "-filter_complex", "[1:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=1.5,asplit=2[v][k];"
                "[2:a][k]sidechaincompress=threshold=0.04:ratio=3:attack=10:release=220[f];[v][f]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.9[a]",
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", str(TOTAL), out], check=True)
print("reel:", out, TOTAL, "s")
