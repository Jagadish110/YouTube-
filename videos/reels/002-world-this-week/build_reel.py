"""Instagram Reel 002 (1080x1920): four world stories this week, one scene each.

    python3 build_reel.py        -> output/reel-world-this-week.mp4
Look: Trendsplain navy + yellow + coral + sky (news-desk style), drawn maps and icons, numbered chips 01-04.
Optional photos: drop files into assets/ (s1.jpg ... s4.jpg) and they replace the drawn icon of that story.
"""
import base64, json, os, subprocess, sys
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
M = json.load(open(os.path.join(HERE, "vo_marks.json")))
TOTAL = round(M[-1]["end"] + 1.4, 2); FPS = 30
NAVY, Y, C, SKY = "#0B1026", "#FFD23F", "#FF5A5F", "#5CC8FF"
S = [m["start"] for m in M]; E = [m["end"] for m in M]


def at(i, phrase):
    t = M[i]["text"]; return round(M[i]["start"] + (M[i]["end"] - M[i]["start"]) * t.index(phrase) / len(t), 2)


def font(name, fam, w):
    b = base64.b64encode(open(os.path.join(ROOT, "tools/fonts", name), "rb").read()).decode()
    return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}"


def photo(i, w, h, label="", pos="50% 50%"):
    """User-supplied photo assets/s{i}.jpg|png as a framed box; None if missing."""
    for ext, mime in (("jpg", "image/jpeg"), ("png", "image/png")):
        p = os.path.join(HERE, "assets", f"s{i}.{ext}")
        if os.path.exists(p):
            b = base64.b64encode(open(p, "rb").read()).decode()
            tag = f'<div style="position:absolute;left:18px;bottom:16px;padding:6px 16px;border-radius:12px;background:rgba(0,0,0,.65);font:800 26px Sora;color:#fff">{label}</div>' if label else ""
            return (f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:30px;overflow:hidden;border:6px solid {Y}">'
                    f'<img src="data:{mime};base64,{b}" style="width:100%;height:100%;object-fit:cover;object-position:{pos};display:block">{tag}</div>')
    return None


# ---- captions: 3-word chunks timed by character share
HI = {"four", "one.", "two.", "three.", "four.", "quad", "xi", "putin", "twelve", "percent", "houthis", "hundred", "twenty-eight",
      "human.", "non-binding", "sanctioned", "military.", "no"}
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

# ---- drawings
globe = f'''<svg width="560" height="560" viewBox="0 0 200 200"><circle cx="100" cy="100" r="92" fill="#13204a" stroke="{SKY}" stroke-width="4"/>
 <g fill="none" stroke="{SKY}" stroke-width="3" opacity=".8"><ellipse cx="100" cy="100" rx="40" ry="92"/><ellipse cx="100" cy="100" rx="75" ry="92"/>
 <path d="M8 100 H192 M20 55 H180 M20 145 H180"/></g>
</svg>'''
flag_us = '<svg width="150" height="100" viewBox="0 0 15 10"><rect width="15" height="10" fill="#fff"/><g fill="#B22234">' + "".join(f'<rect y="{i * 10 / 7}" width="15" height="{10 / 13}"/>' for i in range(7)) + '</g><rect width="6.5" height="5.4" fill="#3C3B6E"/></svg>'
flag_cn = '<svg width="150" height="100" viewBox="0 0 30 20"><rect width="30" height="20" fill="#DE2910"/><path d="M5 2.5 L6.18 6.1 L2.6 3.9 H7.4 L3.82 6.1 Z" fill="#FFDE00"/></svg>'
flag_ru = '<svg width="150" height="100" viewBox="0 0 9 6"><rect width="9" height="2" fill="#fff"/><rect y="2" width="9" height="2" fill="#0039A6"/><rect y="4" width="9" height="2" fill="#D52B1E"/></svg>'
seamap = f'''<svg width="900" height="560" viewBox="0 0 900 560">
 <rect width="900" height="560" rx="36" fill="#13204a"/>
 <path d="M0 0 H330 L470 240 L520 330 L560 360 L560 560 H0 Z" fill="#2a3a6e"/>
 <path d="M420 0 H900 V300 L700 330 L610 360 L585 345 L520 200 Z" fill="#2a3a6e"/>
 <path d="M560 360 L585 345 L610 360 L700 330 L900 300 V560 H560 Z" fill="#13204a"/>
 <text x="120" y="300" fill="#c9d3f5" font-family="Sora" font-weight="800" font-size="40">AFRICA</text>
 <text x="660" y="190" fill="#c9d3f5" font-family="Sora" font-weight="800" font-size="40">YEMEN</text>
 <text x="355" y="90" fill="{SKY}" font-family="Sora" font-weight="800" font-size="30" transform="rotate(58 355 90)">RED SEA</text>
 <circle id="pulse" cx="572" cy="352" r="30" fill="none" stroke="{C}" stroke-width="8"/><circle cx="572" cy="352" r="14" fill="{C}"/>
 <text x="572" y="425" text-anchor="middle" fill="{Y}" font-family="Sora" font-weight="800" font-size="34">BAB AL-MANDAB</text>
 <path id="gov" d="M700 250 C760 300 800 330 840 360" stroke="{Y}" stroke-width="10" fill="none" stroke-linecap="round" marker-end="url(#ar)"/>
 <defs><marker id="ar" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="{Y}"/></marker></defs>
 <text x="760" y="430" fill="{Y}" font-family="Sora" font-weight="800" font-size="26">TO ADEN</text></svg>'''
drone = f'''<svg width="520" height="420" viewBox="0 0 260 210"><g stroke="{SKY}" stroke-width="6" fill="none">
 <circle cx="130" cy="105" r="80" stroke-dasharray="12 10"/><path d="M130 10 V45 M130 165 V200 M35 105 H70 M190 105 H225"/></g>
 <g fill="#e8ecff"><rect x="105" y="92" width="50" height="26" rx="10"/><rect x="60" y="100" width="140" height="8" rx="4"/>
 <ellipse cx="60" cy="96" rx="26" ry="6"/><ellipse cx="200" cy="96" rx="26" ry="6"/></g><circle cx="130" cy="124" r="7" fill="{C}"/></svg>'''
parcel = f'''<svg width="520" height="440" viewBox="0 0 260 220"><path d="M130 20 L230 65 V160 L130 205 L30 160 V65 Z" fill="#c98a4b"/>
 <path d="M30 65 L130 110 L230 65 M130 110 V205" stroke="#8a5a2b" stroke-width="5" fill="none"/>
 <path d="M80 42 L180 88 V120 L160 112 V96 L60 50 Z" fill="#e8b578"/>
 <rect x="40" y="120" width="180" height="46" rx="8" fill="{C}" transform="rotate(-12 130 143)"/>
 <text x="130" y="152" text-anchor="middle" fill="#fff" font-family="Anton" font-size="34" transform="rotate(-12 130 143)">SANCTIONED</text></svg>'''


def chip(n):
    return f'<div class="num">0{n}<span>/04</span></div>'


p = {1: photo(1, 900, 420, pos="50% 35%"), 2: photo(2, 900, 560, "File photo · container ship"),
     3: photo(3, 900, 260, "Illustration · a camera drone", "50% 45%"), 4: photo(4, 900, 300, "File photo · Wildberries warehouse fire", "50% 60%")}
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{font("anton-latin-400-normal.woff2", "Anton", 400)}{font("sora-latin-800-normal.woff2", "Sora", 800)}{font("sora-latin-600-normal.woff2", "Sora", 600)}
*{{box-sizing:border-box}} html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:{NAVY};color:#fff;font-family:Sora}}
#bg{{position:absolute;inset:0;background:radial-gradient(900px 800px at 50% 30%,rgba(92,200,255,.18),transparent 70%),linear-gradient({NAVY},#070a1a)}}
#ticker{{position:absolute;left:0;top:1830px;width:1080px;height:90px;background:{Y};color:{NAVY};font:800 36px Sora;white-space:nowrap;overflow:hidden;line-height:90px}}
#tick{{position:absolute;left:0}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0}}
.sc{{position:absolute;left:0;top:150px;width:1080px;height:1060px;opacity:0}}
.abs{{position:absolute}} .ctr{{left:0;width:1080px;text-align:center}}
.an{{font-family:Anton;text-transform:uppercase;line-height:1.0}}
.num{{position:absolute;left:90px;top:0;font:400 120px/1 Anton;color:{Y}}} .num span{{font-size:54px;color:#8f9bc7}}
.hd{{position:absolute;left:90px;top:135px;width:900px;font:400 112px/1.02 Anton;text-transform:uppercase}}
.card{{position:absolute;left:90px;width:900px;border-radius:28px;padding:30px 38px;background:#141d40;border:3px solid rgba(92,200,255,.5);font:600 44px/1.25 Sora}}
.card small{{display:block;font:800 28px Sora;letter-spacing:4px;color:{SKY};margin-bottom:8px}}
.pill{{display:inline-block;margin:0 10px 14px 0;padding:12px 26px;border-radius:40px;background:#1d2a5c;font:800 38px Sora}}
#caps{{position:absolute;left:60px;top:1300px;width:960px;height:280px}}
.cap{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;opacity:0;font:400 100px/1.08 Anton;text-transform:uppercase;text-shadow:0 6px 0 #000,0 0 40px rgba(0,0,0,.9)}}
.cap b{{font-weight:400;color:{Y}}}
.src{{position:absolute;left:60px;top:1620px;width:960px;text-align:center;font:600 28px Sora;color:#9aa6d4;opacity:0}}
#at{{position:absolute;left:0;top:1700px;width:1080px;text-align:center;font:800 44px Sora;color:{Y};opacity:0}}
</style></head><body><div id="bg"></div>

<div class="sc" id="s0">
 <div class="abs" id="g0" style="left:260px;top:0">{globe}</div>
 <div class="abs ctr an" id="h1" style="top:560px;font-size:230px;color:{Y}">4 STORIES</div>
 <div class="abs ctr an" id="h2" style="top:790px;font-size:96px">THE WORLD THIS WEEK</div>
 <div class="abs ctr" id="h3" style="top:930px;font:800 34px Sora;color:#9aa6d4">17 NOVEMBER 2026</div>
</div>

<div class="sc" id="s1">{chip(1)}<div class="hd" id="t1">Trump in <span style="color:{Y}">Asia</span></div>
 <div class="card" id="m1" style="top:290px"><small>MANILA · FIRST IN 2 YEARS</small>Quad leaders meet<div style="margin-top:16px"><span class="pill">🇺🇸 US</span><span class="pill">🇯🇵 Japan</span><span class="pill">🇦🇺 Australia</span><span class="pill" style="background:{Y};color:{NAVY}">🇮🇳 India</span></div></div>
 <div class="abs" id="ph1" style="left:90px;top:640px">{p[1] or ""}</div>
 <div class="card" id="m2" style="top:{960 if p[1] else 660}px;border-color:{Y}"><small style="color:{Y}">THURSDAY · SHENZHEN, CHINA</small>Trump, Xi Jinping and Vladimir Putin meet together</div>
 <div class="abs" id="fl" style="left:150px;top:900px;display:{"none" if p[1] else "flex"};gap:90px">{flag_us}{flag_cn}{flag_ru}</div>
</div>

<div class="sc" id="s2">{chip(2)}<div class="hd" id="t2">The <span style="color:{C}">Red Sea</span> gate</div>
 <div class="abs" id="map" style="left:90px;top:290px">{seamap}</div>
 <div class="abs" id="ph2" style="left:90px;top:290px">{p[2] or ""}</div>
 <div class="abs an" id="pc" style="left:90px;top:870px;font-size:190px;color:{Y}"><span id="n12">0</span>%</div>
 <div class="abs" id="pt" style="left:500px;top:915px;font:800 44px/1.2 Sora">of world trade<br><span style="color:#9aa6d4;font-size:34px">goes through it</span></div>
</div>

<div class="sc" id="s3">{chip(3)}<div class="hd" id="t3">Killer <span style="color:{SKY}">robots</span></div>
 <div class="abs" id="dr" style="left:{90 if p[3] else 500}px;top:{260 if p[3] else 240}px;{"" if p[3] else "transform:scale(.8);transform-origin:0 0"}">{p[3] or drone}</div>
 <div class="abs an" id="n128w" style="left:90px;top:{540 if p[3] else 300}px;font-size:{170 if p[3] else 230}px;color:{Y}"><span id="n128">0</span></div>
 <div class="abs" id="ct" style="left:{420 if p[3] else 96}px;top:{575 if p[3] else 540}px;font:800 46px/1.2 Sora">countries<br><span style="color:#9aa6d4;font-size:34px">Geneva · 16 to 20 Nov</span></div>
 <div class="card" id="w1" style="top:{705 if p[3] else 720}px"><small>THE TOPIC</small>Weapons that choose targets without a human</div>
 <div class="card" id="w2" style="top:{935 if p[3] else 930}px;border-color:{C}"><small style="color:{C}">THE US POSITION</small>Non-binding guidelines, not a treaty</div>
</div>

<div class="sc" id="s4">{chip(4)}<div class="hd" id="t4">EU hits <span style="color:{C}">Wildberries</span></div>
 <div class="abs" id="pk" style="left:{90 if p[4] else 280}px;top:250px;{"" if p[4] else "transform:scale(.8);transform-origin:50% 0"}">{p[4] or parcel}</div>
 <div class="card" id="u1" style="top:560px"><small>SANCTIONED · 16 NOV</small>Tatyana Kim, founder of Russia's online marketplace Wildberries</div>
 <div class="card" id="u2" style="top:790px;border-color:{C}"><small style="color:{C}">THE EU SAYS</small>The company helps supply the Russian military</div>
 <div class="card" id="u3" style="top:1000px"><small>WILDBERRIES SAYS</small>It has no business in the EU</div>
</div>

<div id="caps">{cap_html}</div>
<div class="src" id="r0">Source: 10 Things Global News</div>
<div class="src" id="r1">Source: DD News</div>
<div class="src" id="r2">Sources: Al Jazeera · NewsBytes</div>
<div class="src" id="r3">Source: Tech Times</div>
<div class="src" id="r4">Source: Meduza</div>
<div id="at">@trendsplain</div>
<div id="flash"></div>
<script>{open(os.path.join(ROOT, "videos/001-zepto/project/assets/gsap.min.js")).read()}</script>
<script>
const tl=gsap.timeline({{paused:true}});window.tl=tl;const S={json.dumps(S)},E={json.dumps(E)},T={TOTAL};
[0,1,2,3,4].forEach(i=>{{const a=i?S[i]-.12:0,b=i<4?S[i+1]-.12:T;
 tl.set("#s"+i,{{opacity:1}},a).set("#r"+i,{{opacity:1}},a).fromTo("#s"+i,{{x:i?1080:0}},{{x:0,duration:i?.32:.01,ease:"power3.out"}},a);
 if(i<4)tl.to("#s"+i,{{x:-1080,duration:.3,ease:"power3.in"}},b-.3).set("#s"+i,{{opacity:0}},b).set("#r"+i,{{opacity:0}},b);
 if(i)tl.from("#s"+i+" .num",{{scale:2.5,opacity:0,duration:.25,ease:"back.out(2)"}},a+.25).from("#t"+i,{{y:60,opacity:0,duration:.3}},a+.4);}});
const cnt=(id,v,t,d)=>{{const o={{v:0}};tl.to(o,{{v:v,duration:d,ease:"power2.out",onUpdate:()=>document.getElementById(id).textContent=Math.round(o.v)}},t)}};
tl.from("#g0",{{scale:0,rotation:-120,duration:.5,ease:"back.out(1.6)"}},.05).to("#g0",{{rotation:20,duration:2.6,ease:"none"}},.5)
 .from("#h1",{{scale:3,opacity:0,duration:.2,ease:"power4.in"}},.25).fromTo("#flash",{{opacity:.5}},{{opacity:0,duration:.3,immediateRender:false}},.45)
 .from("#h2",{{y:50,opacity:0,duration:.3}},{at(0, "watching")}).from("#h3",{{opacity:0,duration:.3}},{at(0, "watching")}+.3);
tl.from("#m1",{{x:-1000,duration:.35,ease:"power3.out"}},{at(1, "Trump")}).from("#m1 .pill",{{scale:0,stagger:.12,duration:.2,ease:"back.out(2)"}},{at(1, "with Japan")})
 .from("#ph1",{{opacity:0,scale:1.1,duration:.4}},{at(1, "On Thursday")}-.1).from("#m2",{{x:1000,duration:.35,ease:"power3.out"}},{at(1, "On Thursday")}).from("#fl svg",{{y:60,opacity:0,stagger:.25,duration:.25,ease:"back.out(2)"}},{at(1, "Xi")}-.1);
tl.from("#map",{{opacity:0,scale:.9,duration:.35}},{at(2, "Yemen")}).fromTo("#pulse",{{attr:{{r:16}},opacity:1}},{{attr:{{r:60}},opacity:0,duration:.9,repeat:7,ease:"power1.out"}},{at(2, "Bab")})
 .from("#gov",{{opacity:0,duration:.3}},{at(2, "pulled")}).from("#ph2",{{opacity:0,duration:.4}},{at(2, "a route")}).from("#pc",{{y:60,opacity:0,duration:.25}},{at(2, "twelve")}-.2).from("#pt",{{opacity:0,duration:.3}},{at(2, "of world")});
cnt("n12",12,{at(2, "twelve")}-.2,1.2);
tl.from("#n128w",{{y:60,opacity:0,duration:.25}},{at(3, "A hundred")}).from("#ct",{{opacity:0,duration:.3}},{at(3, "countries")}).from("#dr",{{scale:.6,opacity:0,duration:.4,ease:"back.out(2)"}},S[3]+.3)
 .from("#w1",{{x:-1000,duration:.35,ease:"power3.out"}},{at(3, "weapons")}).from("#w2",{{x:1000,duration:.35,ease:"power3.out"}},{at(3, "The US")});
cnt("n128",128,{at(3, "A hundred")},1.4);
tl.from("#pk",{{y:-300,opacity:0,duration:.4,ease:"bounce.out"}},{at(4, "The EU")}).from("#u1",{{x:-1000,duration:.35,ease:"power3.out"}},{at(4, "Tatyana")})
 .from("#u2",{{x:1000,duration:.35,ease:"power3.out"}},{at(4, "It says")}).from("#u3",{{x:-1000,duration:.35,ease:"power3.out"}},{at(4, "Wildberries says")})
 .to("#at",{{opacity:1,duration:.25}},E[4]+.1);
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

# ---- sound: news stingers on each number, whooshes on cards, ticks on count-ups, light pulse bed
SR = 48000; rng = np.random.default_rng(5); n = int((TOTAL + .5) * SR); fx = np.zeros(n)
def put(x, t, g=1.0):
    s = max(0, int(t * SR)); x = x[:n - s]; fx[s:s + len(x)] += x * g
def tone(f, d, dec):
    t = np.arange(int(d * SR)) / SR; return np.sin(2 * np.pi * f * t) * np.exp(-t / dec) * np.minimum(1, t / .004)
def sting():
    return np.concatenate([tone(880, .12, .06), tone(1318.5, .35, .14)]) * .5
def hit(d=.6):
    t = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * (45 * t + 50 * .08 * (1 - np.exp(-t / .08)))) * np.exp(-t / .2) + rng.standard_normal(len(t)) * np.exp(-t / .01) * .4
def whoosh(d=.32):
    t = np.arange(int(d * SR)) / SR; x = np.convolve(rng.standard_normal(len(t)), np.ones(26) / 26, "same"); return x * np.sin(np.pi * t / d) ** 2 * 2.2
def tick():
    t = np.arange(int(.025 * SR)) / SR; return np.sin(2 * np.pi * 2200 * t) * np.exp(-t / .005) * .3
put(hit(.9), .25, 1.0); put(sting(), .45, .9)
for i in (1, 2, 3, 4):
    put(whoosh(), S[i] - .3, .8); put(sting(), S[i] + .25, .9); put(hit(.5), S[i] + .25, .5)
for i, ph in ((1, "Trump"), (1, "On Thursday"), (3, "weapons"), (3, "The US"), (4, "Tatyana"), (4, "It says"), (4, "Wildberries says")):
    put(whoosh(.28), at(i, ph) - .05, .6)
for i, ph, k in ((2, "twelve", 16), (3, "A hundred", 19)):
    for j in range(k): put(tick(), at(i, ph) - .2 + j * .075, .8)
for a, _, _ in caps: put(tick(), a, .25)
t = np.arange(n) / SR
bed = np.sin(2 * np.pi * 65.4 * t) * (0.5 + 0.5 * np.sin(2 * np.pi * (110 / 60) * t)) ** 6 * .09 + np.sin(2 * np.pi * 130.8 * t) * .015
fade = np.minimum(1, np.minimum(t / .5, (t[-1] - t) / 1.0)); fx = np.tanh((fx * .55 + bed * fade) * 1.3) * .75
sf.write(os.path.join(HERE, "output", "fx.wav"), np.stack([fx, fx], 1), SR)
out = os.path.join(HERE, "output", "reel-world-this-week.mp4")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-i", os.path.join(HERE, "voiceover.wav"), "-i", os.path.join(HERE, "output", "fx.wav"),
                "-filter_complex", "[1:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=1.5,asplit=2[v][k];"
                "[2:a][k]sidechaincompress=threshold=0.04:ratio=3:attack=10:release=220[f];[v][f]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.9[a]",
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", str(TOTAL), out], check=True)
os.remove(raw); os.remove(os.path.join(HERE, "output", "fx.wav"))
print("reel:", out, TOTAL, "s")
