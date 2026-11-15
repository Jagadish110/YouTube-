"""Vertical end card for Shorts (1080x1920, about 3.4 s): T mark, Trendsplain, LIKE + SHARE, voice line.

    python3 build.py            -> short_outro.mp4
Append it to a Short with tools/add_short_outro.py.
"""
import base64, json, os, subprocess, sys
import numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", ".."); sys.path.insert(0, os.path.join(ROOT, "tools"))
subprocess.run(["python3", os.path.join(ROOT, "tools/voiceover.py"), os.path.join(HERE, "vo_script.txt"), HERE], check=True, capture_output=True)
VO = json.load(open(os.path.join(HERE, "vo_marks.json")))[0]["end"]; D0 = 0.55; TOTAL = round(D0 + VO + 0.7, 2); FPS = 30
def font(name, fam, w):
    b = base64.b64encode(open(os.path.join(ROOT, "tools/fonts", name), "rb").read()).decode()
    return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}"
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{font("outfit-latin-800-normal.woff2", "Outfit", 800)}{font("plus-jakarta-sans-latin-700-normal.woff2", "PJS", 700)}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#1B2240;font-family:Outfit;color:#fff}}
#glow{{position:absolute;inset:0;background:radial-gradient(700px 700px at 50% 36%,rgba(255,74,79,.30),transparent 70%)}}
.c{{position:absolute;left:0;width:1080px;text-align:center}}
.btn{{position:absolute;top:1090px;width:400px;height:150px;border-radius:80px;display:flex;align-items:center;justify-content:center;gap:22px;font:800 64px Outfit}}
#like{{left:110px;background:#FF4A4F}} #share{{left:570px;background:#fff;color:#1B2240}}
</style></head><body><div id="glow"></div>
<div class="c" id="mark" style="top:330px"><svg width="420" height="420" viewBox="150 132 230 243"><path d="M160 142 H322 V151 H167 V195 H318 V201 H160 Z" fill="#FF4A4F"/><path d="M160 201 L215 262 V201 Z" fill="#FF4A4F"/><path d="M318 142 H322 L370 188 V250 H320 V365 L268 318 V201 H318 Z" fill="#FF4A4F"/></svg></div>
<div class="c" id="name" style="top:790px;font-size:150px">Trend<span style="color:#FF4A4F">splain</span></div>
<div class="c" id="tag" style="top:975px;font:700 44px PJS;color:#c9cfe6">Viral topics, explained in plain words.</div>
<div class="btn" id="like"><svg width="70" height="70" viewBox="0 0 24 24"><path id="heart" fill="#fff" d="M12 21s-8-5.3-8-11a4.6 4.6 0 0 1 8-3 4.6 4.6 0 0 1 8 3c0 5.7-8 11-8 11z"/></svg>LIKE</div>
<div class="btn" id="share"><svg width="70" height="70" viewBox="0 0 24 24"><path fill="#1B2240" d="M2 21 23 12 2 3v7l15 2-15 2z"/></svg>SHARE</div>
<div class="c" id="fol" style="top:1320px;font:700 46px PJS;color:#c9cfe6">Full video on the channel</div>
<script>{open(os.path.join(ROOT, "videos/001-zepto/project/assets/gsap.min.js")).read()}</script><script>
const tl=gsap.timeline({{paused:true}});window.tl=tl;
tl.from("#mark",{{scale:0,rotation:-25,duration:.4,ease:"back.out(2)"}},.05).from("#name",{{y:60,opacity:0,duration:.3}},.3).from("#tag",{{opacity:0,duration:.3}},.5)
 .from("#like",{{x:-600,duration:.35,ease:"back.out(1.4)"}},{D0}).from("#share",{{x:600,duration:.35,ease:"back.out(1.4)"}},{D0 + .45})
 .to("#like",{{scale:1.14,duration:.12,yoyo:true,repeat:1}},{D0 + .95}).to("#share",{{scale:1.14,duration:.12,yoyo:true,repeat:1}},{D0 + 1.35}).from("#fol",{{opacity:0,y:30,duration:.3}},{D0 + 1.5});
</script></body></html>'''
open(os.path.join(HERE, "outro.html"), "w").write(html)
from playwright.sync_api import sync_playwright
raw = os.path.join(HERE, "raw.mp4")
ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-", "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p", raw], stdin=subprocess.PIPE)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920}); pg.goto("file://" + os.path.join(HERE, "outro.html")); pg.evaluate("document.fonts.ready.then(()=>1)")
    for f in range(int(TOTAL * FPS)):
        pg.evaluate(f"void tl.seek({f / FPS}, false)"); ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
    b.close()
ff.stdin.close(); ff.wait()
import sfx
SR = sfx.SR; fx = np.zeros(int((TOTAL + .3) * SR))
def put(x, t, g=1.0):
    s = int(t * SR); x = x[:len(fx) - s]; fx[s:s + len(x)] += x * g
put(sfx.swoosh(0.3, .4), 0); put(sfx.pop(True), .1); put(sfx.pop(), D0 + .05); put(sfx.pop(), D0 + .5); put(sfx.mouse_click(), D0 + .95); put(sfx.mouse_click(), D0 + 1.35); put(sfx.chime(), D0 + 1.4, .35)
sf.write(os.path.join(HERE, "fx.wav"), np.stack([fx, fx], 1) * .6, SR)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-i", os.path.join(HERE, "voiceover.wav"), "-i", os.path.join(HERE, "fx.wav"), "-filter_complex",
                f"[1:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={int(D0 * 1000)}|{int(D0 * 1000)}[v];[v][2:a]amix=inputs=2:duration=longest:normalize=0[a]",
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", str(TOTAL), os.path.join(HERE, "short_outro.mp4")], check=True)
os.remove(raw); print("short outro:", TOTAL, "s")
