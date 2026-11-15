"""Trendsplain brand intro + subscribe/share outro (re-usable in every video).

    python3 build_brand.py      # writes intro/project and outro/project, then render each with ../../render.sh
Colours: navy #1B2240, red #FF4A4F, white. Fonts: Outfit 800 / Plus Jakarta Sans.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import scenelib as sl
from scenelib import C, L

N, R, W = "#1B2240", "#FF4A4F", "#FFFFFF"
SHAPE = open(os.path.join(HERE, "..", "..", "channel", "v2", "shape.txt")).read()
THEME = dict(ground=N, ink=W, quiet="#C9CFEA", up=R, down=R, panel="#252D55", line="#2E3766",
             head="'Outfit', 'Inter', sans-serif", head_weight=800, body="'Plus Jakarta Sans', 'Inter', sans-serif",
             fonts=[("Outfit", 800, "assets/fonts/outfit-latin-800-normal.woff2"),
                    ("Plus Jakarta Sans", 500, "assets/fonts/plus-jakarta-sans-latin-500-normal.woff2"),
                    ("Plus Jakarta Sans", 700, "assets/fonts/plus-jakarta-sans-latin-700-normal.woff2")],
             bg="background-image: radial-gradient(circle at 50% 38%, rgba(255,74,79,0.18) 0, rgba(255,74,79,0) 45%), linear-gradient(rgba(255,255,255,.035) 2px, transparent 2px), linear-gradient(90deg, rgba(255,255,255,.035) 2px, transparent 2px); background-size: auto, 80px 80px, 80px 80px;")


def mark(prefix):
    # split the T into three parts so they can animate separately
    parts = SHAPE.split("/>")[:3]
    ids = ["bar", "fold", "stem"]
    body = "".join(p.replace("<path ", f'<path id="{prefix}-{i}" ') + "/>" for p, i in zip(parts, ids))
    return f'<svg width="300" height="320" viewBox="150 130 230 245">{body}</svg>'


# ---------------- intro ----------------
sl.EVENTS.clear()
sl.setup(os.path.join(HERE, "intro", "vo_marks.json"), 6.3)
sl.theme(**THEME)
s = sl.Scene("intro", 0)
s.E("glow", f'<svg width="900" height="900" viewBox="0 0 900 900"><circle id="intro-ring1" cx="450" cy="450" r="200" fill="none" stroke="{R}" stroke-width="6" opacity=".6"/><circle id="intro-ring2" cx="450" cy="450" r="200" fill="none" stroke="{W}" stroke-width="4" opacity=".35"/></svg>', L(510, -110, 10), 0.4, "fade")
s.J('tl.fromTo("#intro-ring1",{scale:0.4,opacity:.8,transformOrigin:"50% 50%"},{scale:1.8,opacity:0,duration:1.4,ease:"power2.out"},0.55);')
s.J('tl.fromTo("#intro-ring2",{scale:0.4,opacity:.6,transformOrigin:"50% 50%"},{scale:2.2,opacity:0,duration:1.6,ease:"power2.out"},0.7);')
s.E("mark", mark("intro-m"), L(810, 150, 10), 0.05, "fade")
s.J('tl.fromTo("#intro-m-bar",{scaleX:0,transformOrigin:"0% 50%"},{scaleX:1,duration:0.45,ease:"power3.out"},0.1);')
s.J('tl.fromTo("#intro-m-fold",{opacity:0,y:-40},{opacity:1,y:0,duration:0.35,ease:"back.out(2)"},0.4);')
s.J('tl.fromTo("#intro-m-stem",{opacity:0,y:-140},{opacity:1,y:0,duration:0.5,ease:"bounce.out"},0.5);')
s.E("k", "WELCOME TO", C(500, 48), s.P("Welcome"), "fade", cls="kick q")
s.E("w", f"Trend<span style='color:{R}'>splain</span>", C(560, 190), s.P("Trendsplain"), "pop", cls="hero")
s.E("t", "Viral topics, explained in <span style='color:#FF4A4F'>plain words.</span>", C(800, 60), s.P("We take"), "wipe")
s.E("u", "", L(760, 900, 10, f"width:400px;height:10px;border-radius:5px;background:{R};"), s.P("plain words"), "wipe")
sl.EVENTS.append(dict(t=0.45, kind="chime", n=0))
sl.write_project(os.path.join(HERE, "intro", "project"), [s], audio_dur=6.0)

# ---------------- outro ----------------
sl.EVENTS.clear()
sl.setup(os.path.join(HERE, "outro", "vo_marks.json"), 7.0)
sl.theme(**THEME)
s = sl.Scene("outro", 0)
t_sub, t_share = s.P("subscribe", off=0.0), s.P("share it", off=0.0)
s.E("k", "IF THIS MADE SENSE…", C(170, 52), 0.1, "fade", cls="kick q")
pill = "height:170px;border-radius:85px;display:flex;align-items:center;justify-content:center;gap:28px;font-size:72px;"
bell = f'<svg width="70" height="76" viewBox="0 0 70 76"><path d="M10 56 Q10 12 35 12 Q60 12 60 56 Z" fill="{W}"/><rect x="4" y="54" width="62" height="10" rx="5" fill="{W}"/><circle cx="35" cy="70" r="7" fill="{W}"/></svg>'
share = f'<svg width="70" height="70" viewBox="0 0 70 70"><circle cx="54" cy="14" r="11" fill="{N}"/><circle cx="16" cy="35" r="11" fill="{N}"/><circle cx="54" cy="56" r="11" fill="{N}"/><path d="M54 14 L16 35 L54 56" stroke="{N}" stroke-width="7" fill="none"/></svg>'
s.E("sub", f'<span class="hero">SUBSCRIBE</span>', L(250, 380, 10, pill + f"width:680px;background:{R};"), 0.3, "pop", attrs="data-layout-allow-overlap data-layout-allow-occlusion")
s.E("subd", f'<span class="hero" style="color:#C9CFEA">SUBSCRIBED ✓</span>', L(250, 380, 10, pill + "width:680px;background:#3A4270;"), round(t_sub + 0.12, 2), "fade", attrs="data-layout-allow-overlap data-layout-allow-occlusion")
s.E("bell", bell, L(960, 425, 10), round(t_sub + 0.2, 2), "pop")
s.J(f'tl.to("#outro-bell",{{rotation:18,transformOrigin:"50% 10%",duration:0.1,yoyo:true,repeat:7}},{round(t_sub + 0.5, 2)});')
s.E("sh", f'{share}<span class="hero" style="color:{N}">SHARE</span>', L(1100, 380, 10, pill + f"width:570px;background:{W};"), 0.45, "pop")
plane = f'<svg width="90" height="90" viewBox="0 0 90 90"><path d="M5 45 L85 8 L60 85 L44 52 Z" fill="{R}"/><path d="M44 52 L85 8" stroke="{N}" stroke-width="4"/></svg>'
s.E("pl", plane, L(1600, 410, 10), round(t_share + 0.25, 2), "pop")
s.J(f'tl.to("#outro-pl",{{x:260,y:-260,rotation:10,opacity:0,duration:0.9,ease:"power2.in"}},{round(t_share + 0.6, 2)});')
cursor = f'<svg width="80" height="100" viewBox="0 0 80 100"><path d="M8 4 L8 78 L28 60 L42 94 L56 88 L42 55 L70 55 Z" fill="{W}" stroke="{N}" stroke-width="6" stroke-linejoin="round"/></svg>'
s.E("cur", cursor, L(1500, 820, 10), 0.6, "fade")
s.J(f'tl.to("#outro-cur",{{x:-850,y:-330,duration:0.6,ease:"power2.inOut"}},{round(t_sub - 0.65, 2)});')
s.J(f'tl.to("#outro-cur",{{scale:0.85,duration:0.08,yoyo:true,repeat:1}},{round(t_sub - 0.02, 2)});')
s.J(f'tl.to("#outro-sub",{{scale:0.94,duration:0.08,yoyo:true,repeat:1}},{round(t_sub - 0.02, 2)});')
s.J(f'tl.to("#outro-cur",{{x:-120,y:-330,duration:0.55,ease:"power2.inOut"}},{round(t_share - 0.6, 2)});')
s.J(f'tl.to("#outro-cur",{{scale:0.85,duration:0.08,yoyo:true,repeat:1}},{round(t_share - 0.02, 2)});')
s.J(f'tl.to("#outro-sh",{{scale:0.94,duration:0.08,yoyo:true,repeat:1}},{round(t_share - 0.02, 2)});')
s.E("m", mark("outro-m").replace('width="300" height="320"', 'width="90" height="96"'), L(780, 790, 10), 1.0, "fade")
s.E("h", "@Trendsplain", L(890, 805, 56, "width:600px;"), 1.0, "fade", cls="hero")
sl.EVENTS.append(dict(t=round(t_sub, 2), kind="click", n=0))
sl.EVENTS.append(dict(t=round(t_share, 2), kind="click", n=0))
sl.write_project(os.path.join(HERE, "outro", "project"), [s], audio_dur=5.0)
