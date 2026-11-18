"""Instagram Reel 003 (1080x1920): Nvidia earnings + board rules out Huang's return. Earnings-terminal look:
black, Nvidia green, big count-up numbers, bar charts, amber for 'reported' items, red stamp for the board's decision.

    python3 build_reel.py        -> output/reel-nvidia-earnings.mp4   (NOBED=1 -> -for-music version without the pulse bed)
Photos: assets/huang.jpg and assets/logo.png were supplied by Jagadish (17 Nov). Swap in more as assets/*.jpg.
"""
import base64, json, os, subprocess, sys
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
M = json.load(open(os.path.join(HERE, "vo_marks.json")))
TOTAL = round(M[-1]["end"] + 1.5, 2); FPS = 30
G, AM, RD, BK = "#76B900", "#FFB020", "#FF3B30", "#050806"
S = [m["start"] for m in M]; E = [m["end"] for m in M]


def at(i, phrase):
    t = M[i]["text"]; return round(M[i]["start"] + (M[i]["end"] - M[i]["start"]) * t.index(phrase) / len(t), 2)


def font(name, fam, w):
    b = base64.b64encode(open(os.path.join(ROOT, "tools/fonts", name), "rb").read()).decode()
    return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}"


def img(name, mime):
    return f"data:{mime};base64," + base64.b64encode(open(os.path.join(HERE, "assets", name), "rb").read()).decode()


HUANG, LOGO = img("huang.jpg", "image/jpeg"), img("logo.png", "image/png")

HI = {"doubled", "revenue.", "not", "coming", "back.", "billion", "percent.", "billion.", "offered", "reinstate", "interim", "ceo", "five", "sec", "probing"}
caps = []
for m in M:
    w = m["text"].split(); n = sum(len(x) + 1 for x in w); t = m["start"]; d = m["end"] - m["start"]
    for i in range(0, len(w), 3):
        ch = w[i:i + 3]; dt = d * sum(len(x) + 1 for x in ch) / n
        caps.append((round(t, 3), round(t + dt, 3), " ".join(f"<b>{x}</b>" if x.lower().strip(",") in HI else x for x in ch)))
        t += dt
cap_html = "".join(f'<div class="cap" id="c{i}"><span>{x}</span></div>' for i, (_, _, x) in enumerate(caps))
cap_js = "".join(f'tl.set("#c{i}",{{opacity:1}},{a}).fromTo("#c{i}",{{scale:.86,y:18}},{{scale:1,y:0,duration:.16,ease:"back.out(2.5)"}},{a}).set("#c{i}",{{opacity:0}},{b});'
                 for i, (a, b, _) in enumerate(caps))

person = f'''<svg width="240" height="260" viewBox="0 0 240 260"><circle cx="120" cy="80" r="52" fill="#0e140c" stroke="{G}" stroke-width="5"/>
 <path d="M20 260 C20 170 70 140 120 140 C170 140 220 170 220 260 Z" fill="#0e140c" stroke="{G}" stroke-width="5"/>
 <path d="M70 70 C74 30 166 30 170 70 C150 50 90 50 70 70 Z" fill="#cfd6cf"/></svg>'''
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{font("anton-latin-400-normal.woff2", "Anton", 400)}{font("sora-latin-800-normal.woff2", "Sora", 800)}{font("sora-latin-600-normal.woff2", "Sora", 600)}
*{{box-sizing:border-box}} html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:{BK};color:#fff;font-family:Sora}}
#bg{{position:absolute;inset:0;background:radial-gradient(900px 700px at 50% 32%,rgba(118,185,0,.24),transparent 70%),linear-gradient({BK},#081006)}}
#grid{{position:absolute;inset:-80px;background-image:linear-gradient(rgba(118,185,0,.09) 2px,transparent 2px),linear-gradient(90deg,rgba(118,185,0,.09) 2px,transparent 2px);background-size:90px 90px;transform:perspective(900px) rotateX(58deg) translateY(520px);transform-origin:50% 100%}}
#flash{{position:absolute;inset:0;background:{G};opacity:0}}
.sc{{position:absolute;left:0;top:130px;width:1080px;height:1100px;opacity:0}}
.abs{{position:absolute}} .ctr{{left:0;width:1080px;text-align:center}}
.an{{font-family:Anton;text-transform:uppercase;line-height:1.0}}
.lab{{position:absolute;left:90px;font:800 34px Sora;letter-spacing:6px;color:#b9c2b9}}
.card{{position:absolute;left:90px;width:900px;border-radius:28px;padding:30px 38px;background:#0e130c;border:3px solid rgba(118,185,0,.55);font:600 44px/1.25 Sora}}
.card small{{display:block;font:800 28px Sora;letter-spacing:4px;color:{G};margin-bottom:8px}}
.stamp{{position:absolute;text-align:center;font:400 120px/1.15 Anton;color:{RD};border:12px solid {RD};border-radius:24px;transform:rotate(-8deg);background:rgba(5,8,6,.8)}}
#caps{{position:absolute;left:60px;top:1300px;width:960px;height:280px}}
.cap{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;opacity:0;font:400 100px/1.08 Anton;text-transform:uppercase;text-shadow:0 6px 0 #000,0 0 40px rgba(0,0,0,.9)}}
.cap b{{font-weight:400;color:{G}}}
.src{{position:absolute;left:60px;top:1630px;width:960px;text-align:center;font:600 28px Sora;color:#aab3aa;opacity:0}}
#at{{position:absolute;left:0;top:1715px;width:1080px;text-align:center;font:800 44px Sora;color:{G};opacity:0}}
</style></head><body><div id="bg"></div><div id="grid"></div>

<div class="sc" id="s0">
 <div class="abs" id="lg" style="left:250px;top:0;background:#fff;border-radius:28px;padding:24px 40px"><img src="{LOGO}" style="display:block;height:120px"></div>
 <div class="abs ctr an" id="a1" style="top:250px;font-size:150px">REVENUE</div>
 <div class="abs ctr an" id="a2" style="top:400px;font-size:300px;color:{G}">DOUBLED</div>
 <div class="abs ctr" id="a3" style="top:790px"><span style="display:inline-block;font:800 40px Sora;letter-spacing:3px;border:5px solid {AM};color:{AM};border-radius:18px;padding:14px 30px">BOARD: HUANG IS NOT COMING BACK</span></div>
</div>

<div class="sc" id="s1">
 <div class="lab" id="l1" style="top:0">QUARTER ENDED 25 OCTOBER</div>
 <div class="abs an" id="v1" style="left:84px;top:60px;font-size:250px;color:{G};white-space:nowrap">$<span id="n1">0.0</span>B</div>
 <svg class="abs" id="ch1" style="left:90px;top:370px" width="900" height="640" viewBox="0 0 900 640">
  <rect id="b0" x="120" y="400" width="230" height="200" rx="14" fill="#3a443a"/><rect id="b1" x="520" y="193" width="230" height="407" rx="14" fill="{G}"/>
  <path d="M60 600 H840" stroke="#555" stroke-width="3"/>
  <text x="235" y="640" text-anchor="middle" fill="#b9c2b9" font-family="Sora" font-weight="800" font-size="30">A YEAR AGO</text>
  <text x="635" y="640" text-anchor="middle" fill="#fff" font-family="Sora" font-weight="800" font-size="30">NOW</text>
  <text id="up" x="635" y="150" text-anchor="middle" fill="{G}" font-family="Anton" font-size="110">+103%</text></svg>
</div>

<div class="sc" id="s2">
 <div class="lab" id="l2" style="top:0">DATA CENTRES</div>
 <div class="abs an" id="v2" style="left:84px;top:60px;font-size:250px;color:{G};white-space:nowrap">$<span id="n2">0.0</span>B</div>
 <div class="abs" id="bar" style="left:90px;top:400px;width:900px;height:130px;border-radius:24px;background:#2a322a;overflow:hidden"><div id="barf" style="height:130px;width:0;background:{G}"></div></div>
 <div class="abs" id="bl" style="left:96px;top:555px;font:800 34px Sora;color:#b9c2b9">of $115.8B total revenue</div>
 <div class="abs an" id="g2" style="left:90px;top:680px;font-size:190px">+110%</div>
 <div class="abs" id="g2l" style="left:600px;top:780px;font:800 44px/1.2 Sora;color:{G}">year on year</div>
</div>

<div class="sc" id="s3">
 <div class="lab" id="l3" style="top:0">NEXT QUARTER · OUTLOOK</div>
 <div class="abs an" id="v3" style="left:84px;top:60px;font-size:250px;color:{G};white-space:nowrap">≈$<span id="n3">0</span>B</div>
 <div class="abs" id="pm" style="left:90px;top:360px"><span style="display:inline-block;font:800 40px Sora;border:5px solid {G};border-radius:40px;padding:10px 30px">plus or minus 3%</span></div>
 <svg class="abs" style="left:90px;top:470px" width="900" height="520" viewBox="0 0 900 520"><path id="ln" d="M10 480 L160 420 L300 440 L450 330 L600 300 L760 170 L870 60" fill="none" stroke="{G}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1500" stroke-dashoffset="1500"/><circle id="dt" cx="870" cy="60" r="24" fill="{G}" opacity="0"/></svg>
</div>

<div class="sc" id="s4">
 <div class="abs" id="ph" style="left:90px;top:0;width:420px;height:420px;border-radius:30px;overflow:hidden;border:6px solid {AM}"><img src="{HUANG}" style="width:100%;height:100%;object-fit:cover"></div>
 <div class="abs an" id="of" style="left:550px;top:20px;font-size:100px;color:{AM};line-height:1.05">HUANG<br>OFFERED<br>TO RETURN</div>
 <div class="card" id="q" style="top:470px;border-color:{G}"><small>BOARD CHAIR HARVEY JONES</small>The board accepted his resignation and “does not intend to reinstate Jensen as CEO”</div>
 <div class="stamp" id="st" style="left:250px;top:850px;width:580px;font-size:90px">NOT REINSTATED</div>
</div>

<div class="sc" id="s5">
 <div class="abs" id="pe" style="left:90px;top:0">{person}</div>
 <div class="abs an" id="ic" style="left:380px;top:20px;font-size:90px;color:{G}">INTERIM CEO</div>
 <div class="abs an" id="kr" style="left:380px;top:130px;font-size:120px;line-height:1.02">COLETTE<br>KRESS</div>
 <div class="card" id="se" style="top:440px"><small>STILL OPEN</small>The search for a permanent CEO continues</div>
</div>

<div class="sc" id="s6">
 <svg class="abs" style="left:90px;top:0" width="300" height="300" viewBox="0 0 300 300"><path id="ar" d="M150 270 V60 M60 150 L150 50 L240 150" fill="none" stroke="{G}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/></svg>
 <div class="abs an" id="pc" style="left:420px;top:10px;font-size:230px;color:{G}">+<span id="n6">0</span>%</div>
 <div class="abs" id="pl" style="left:426px;top:250px;font:800 44px/1.2 Sora">about, after hours</div>
 <div class="card" id="sec" style="top:420px;border-color:{AM}"><small style="color:{AM}">REPORTED · WALL STREET JOURNAL</small>The SEC is probing Nvidia's disclosures</div>
</div>

<div id="caps">{cap_html}</div>
<div class="src" id="r0">Source: Nvidia results · The Next Web</div>
<div class="src" id="r1">Source: Nvidia results (SEC filing)</div>
<div class="src" id="r2">Source: Nvidia results (SEC filing)</div>
<div class="src" id="r3">Source: Nvidia results (SEC filing)</div>
<div class="src" id="r4">Source: The Next Web</div>
<div class="src" id="r5">Source: Nvidia results (SEC filing)</div>
<div class="src" id="r6">Sources: The Next Web · WSJ via TNW</div>
<div id="at">@trendsplain</div><div id="flash"></div>
<script>{open(os.path.join(ROOT, "videos/001-zepto/project/assets/gsap.min.js")).read()}</script>
<script>
const tl=gsap.timeline({{paused:true}});window.tl=tl;const S={json.dumps(S)},E={json.dumps(E)},T={TOTAL};
tl.fromTo("#grid",{{backgroundPosition:"0px 0px"}},{{backgroundPosition:"0px 600px",duration:T,ease:"none"}},0);
[0,1,2,3,4,5,6].forEach(i=>{{const a=i?S[i]-.1:0,b=i<6?S[i+1]-.1:T;
 tl.set("#s"+i,{{opacity:1}},a).set("#r"+i,{{opacity:1}},a).fromTo("#s"+i,{{y:i?120:0,opacity:i?0:1}},{{y:0,opacity:1,duration:i?.3:.01,ease:"power3.out"}},a);
 if(i)tl.fromTo("#flash",{{opacity:.45}},{{opacity:0,duration:.22,immediateRender:false}},a);
 if(i<6)tl.to("#s"+i,{{y:-100,opacity:0,duration:.22}},b-.22).set("#s"+i,{{opacity:0}},b).set("#r"+i,{{opacity:0}},b);}});
const cnt=(id,v,dp,t,d)=>{{const o={{v:0}};tl.to(o,{{v:v,duration:d,ease:"power2.out",onUpdate:()=>document.getElementById(id).textContent=o.v.toFixed(dp)}},t)}};
// 0 hook
tl.from("#lg",{{y:-250,opacity:0,duration:.3,ease:"back.out(1.6)"}},.05).from("#a1",{{x:-300,opacity:0,duration:.25}},.35)
 .from("#a2",{{scale:3,opacity:0,duration:.2,ease:"power4.in"}},.7).fromTo("#flash",{{opacity:.6}},{{opacity:0,duration:.3,immediateRender:false}},.9)
 .fromTo("#s0",{{x:-12}},{{x:12,duration:.05,repeat:5,yoyo:true,ease:"none"}},.9).set("#s0",{{x:0}},1.25)
 .from("#a3",{{scale:0,duration:.3,ease:"back.out(2)"}},{at(0, "And the board")});
// 1 revenue
tl.from("#l1",{{opacity:0,duration:.3}},S[1]).from("#v1",{{y:60,opacity:0,duration:.25}},S[1]+.1);
cnt("n1",115.8,1,S[1]+.1,1.4);
tl.from("#b0",{{attr:{{height:0,y:600}},duration:.5,ease:"power2.out"}},S[1]+.3).from("#b1",{{attr:{{height:0,y:600}},duration:.9,ease:"power2.out"}},S[1]+.6)
 .from("#up",{{scale:0,transformOrigin:"center",duration:.3,ease:"back.out(2.5)"}},{at(1, "up one")});
// 2 data centres
tl.from("#l2",{{opacity:0,duration:.3}},S[2]).from("#v2",{{y:60,opacity:0,duration:.25}},S[2]+.1);
cnt("n2",107.6,1,S[2]+.1,1.3);
tl.from("#bar",{{opacity:0,duration:.2}},S[2]+.4).to("#barf",{{width:"93%",duration:1.1,ease:"power2.out"}},S[2]+.5).from("#bl",{{opacity:0,duration:.3}},S[2]+.9)
 .from("#g2",{{x:-80,opacity:0,duration:.25}},S[2]+1.6).from("#g2l",{{opacity:0,duration:.3}},S[2]+1.9);
// 3 outlook
tl.from("#l3",{{opacity:0,duration:.3}},S[3]).from("#v3",{{y:60,opacity:0,duration:.25}},S[3]+.1);
cnt("n3",130,0,S[3]+.1,1.3);
tl.from("#pm",{{scale:0,duration:.3,ease:"back.out(2)"}},S[3]+1.1).to("#ln",{{strokeDashoffset:0,duration:1.3,ease:"power2.out"}},S[3]+.5).set("#dt",{{opacity:1}},S[3]+1.8);
// 4 board
tl.from("#ph",{{scale:1.3,opacity:0,duration:.35,ease:"power3.out"}},S[4]).from("#of",{{x:80,opacity:0,duration:.3}},S[4]+.2)
 .from("#q",{{x:1000,duration:.35,ease:"power3.out"}},{at(4, "The board")}).from("#st",{{scale:4,opacity:0,duration:.16,ease:"power4.in"}},{at(4, "does not")})
 .fromTo("#s4",{{x:-12}},{{x:12,duration:.05,repeat:5,yoyo:true,ease:"none"}},{at(4, "does not")}+.16).set("#s4",{{x:0}},{at(4, "does not")}+.5);
// 5 interim
tl.from("#pe",{{x:-300,opacity:0,duration:.35,ease:"power3.out"}},S[5]).from("#ic",{{x:80,opacity:0,duration:.25}},S[5]+.2).from("#kr",{{x:80,opacity:0,duration:.25}},S[5]+.5)
 .from("#se",{{y:80,opacity:0,duration:.3}},{at(5, "while")});
// 6 shares
tl.from("#ar",{{y:200,opacity:0,duration:.4,ease:"back.out(2)"}},S[6]).from("#pc",{{scale:.4,opacity:0,duration:.25}},S[6]+.1);
cnt("n6",5,0,S[6]+.1,.9);
tl.from("#pl",{{opacity:0,duration:.3}},S[6]+.9).from("#sec",{{x:1000,duration:.35,ease:"power3.out"}},{at(6, "The Wall")}).to("#at",{{opacity:1,duration:.25}},E[6]+.1);
{cap_js}
</script></body></html>'''
open(os.path.join(HERE, "reel.html"), "w").write(html)
if len(sys.argv) > 1 and sys.argv[1] == "html":
    sys.exit()

from playwright.sync_api import sync_playwright
os.makedirs(os.path.join(HERE, "output"), exist_ok=True)
raw = os.path.join(HERE, "output", "reel-raw.mp4")
ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                       "-c:v", "libx264", "-preset", "fast", "-crf", "17", "-pix_fmt", "yuv420p", raw], stdin=subprocess.PIPE)
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto("file://" + os.path.join(HERE, "reel.html")); pg.evaluate("document.fonts.ready.then(()=>1)")
    for f in range(int(TOTAL * FPS)):
        pg.evaluate(f"void tl.seek({f / FPS}, false)"); ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
    b.close()
ff.stdin.close(); ff.wait()

SR = 48000; rng = np.random.default_rng(9); n = int((TOTAL + .5) * SR); fx = np.zeros(n)
def put(x, t, g=1.0):
    s = max(0, int(t * SR)); x = x[:n - s]; fx[s:s + len(x)] += x * g
def hit(d=.6):
    t = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * (40 * t + 55 * .09 * (1 - np.exp(-t / .09)))) * np.exp(-t / .22) + rng.standard_normal(len(t)) * np.exp(-t / .012) * .45
def whoosh(d=.3):
    t = np.arange(int(d * SR)) / SR; x = np.convolve(rng.standard_normal(len(t)), np.ones(28) / 28, "same"); return x * np.sin(np.pi * t / d) ** 2 * 2.2
def riser(d=.7):
    t = np.arange(int(d * SR)) / SR; x = rng.standard_normal(len(t)); k = np.ones(24) / 24
    return (x - np.convolve(x, k, "same")) * (t / d) ** 3 * .5 + np.sin(2 * np.pi * (200 * t + 500 * t * t / d)) * (t / d) ** 2 * .25
def tick():
    t = np.arange(int(.03 * SR)) / SR; return np.sign(np.sin(2 * np.pi * rng.choice([1400, 1900, 2600]) * t)) * np.exp(-t / .006) * .25
def ding():
    t = np.arange(int(.6 * SR)) / SR; return (np.sin(2 * np.pi * 1568 * t) + .5 * np.sin(2 * np.pi * 2352 * t)) * np.exp(-t / .2) * .3
put(riser(.6), .1, .8); put(hit(.9), .7, 1.0)
for i in range(1, 7): put(whoosh(), S[i] - .25, .7); put(hit(.5), S[i] - .08, .5)
for i, k, d0 in ((1, 18, .1), (2, 17, .1), (3, 17, .1), (6, 12, .1)):
    for j in range(k): put(tick(), S[i] + d0 + j * .075, .7)
    put(ding(), S[i] + d0 + k * .075, .8)
put(hit(.9), at(4, "does not") + .16, 1.0); put(riser(.5), at(4, "does not") - .5, .7)
for a, _, _ in caps: put(tick(), a, .22)
t = np.arange(n) / SR
bed = np.sin(2 * np.pi * 55 * t) * (.5 + .5 * np.sin(2 * np.pi * (104 / 60) * t)) ** 4 * .10 + np.sin(2 * np.pi * 110.3 * t) * .02
fade = np.minimum(1, np.minimum(t / .5, (t[-1] - t) / .8)); NOBED = os.environ.get("NOBED") == "1"
fx = np.tanh((fx * .55 + (0 if NOBED else bed * fade)) * 1.3) * .75
sf.write(os.path.join(HERE, "output", "fx.wav"), np.stack([fx, fx], 1), SR)
out = os.path.join(HERE, "output", "reel-nvidia-earnings" + ("-for-music" if NOBED else "") + ".mp4")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-i", os.path.join(HERE, "voiceover.wav"), "-i", os.path.join(HERE, "output", "fx.wav"),
                "-filter_complex", "[1:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=1.5,asplit=2[v][k];"
                "[2:a][k]sidechaincompress=threshold=0.04:ratio=3:attack=10:release=220[f];[v][f]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.9[a]",
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", str(TOTAL), out], check=True)
os.remove(raw); os.remove(os.path.join(HERE, "output", "fx.wav"))
print("reel:", out, TOTAL, "s")
