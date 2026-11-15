"""Sample for video 002 (Blinkit): new per-video look + drawn illustrations. About 31 s.

Look: sunny yellow ground, deep green ink, Bricolage Grotesque headlines, DM Sans text.
Images are flat illustrations drawn in SVG (no stock photos, no faces, no logos).
Run from this folder:  python3 build.py
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
import scenelib as sl
from scenelib import C, L, draw, fin

HERE = os.path.dirname(os.path.abspath(__file__))
sl.setup(os.path.join(HERE, "vo_marks.json"), 31.0)
sl.theme(
    ground="#F8CB46", ink="#0F2A1A", quiet="#5A4F1E", up="#0C831F", down="#E5383B",
    panel="#FFF1A8", line="#E9C232",
    head="'Bricolage Grotesque', 'Inter', sans-serif", head_weight=800,
    body="'DM Sans', 'Inter', sans-serif",
    fonts=[("Bricolage Grotesque", 800, "assets/fonts/bricolage-grotesque-latin-800-normal.woff2"),
           ("DM Sans", 500, "assets/fonts/dm-sans-latin-500-normal.woff2"),
           ("DM Sans", 700, "assets/fonts/dm-sans-latin-700-normal.woff2")],
    bg="background-image: radial-gradient(circle at 88% 12%, #FFE98A 0, rgba(255,233,138,0) 38%), radial-gradient(circle at 6% 94%, #FFC83A 0, rgba(255,200,58,0) 42%);",
)
G, Y, INK, RED, CREAM = "#0C831F", "#F8CB46", "#0F2A1A", "#E5383B", "#FFF8DC"
TILE = ["#FF8A3D", "#3DB2FF", "#7BD389", "#FF5C8A", "#B48CFF", "#FFC23D"]

S = []


# ---------- illustrations ----------
def phone(pid):
    tiles = "".join(
        f'<rect id="{pid}-t{n}" x="{58 + (n % 3) * 106}" y="{190 + (n // 3) * 120}" width="92" height="104" rx="18" fill="{TILE[n]}"/>'
        f'<rect x="{78 + (n % 3) * 106}" y="{214 + (n // 3) * 120}" width="52" height="40" rx="8" fill="#ffffff" opacity="0.55"/>'
        for n in range(6))
    return (f'<svg width="440" height="800" viewBox="0 0 440 800">'
            f'<rect x="10" y="10" width="420" height="780" rx="64" fill="{INK}"/>'
            f'<rect x="34" y="40" width="372" height="720" rx="44" fill="{CREAM}"/>'
            f'<rect x="170" y="56" width="100" height="18" rx="9" fill="{INK}"/>'
            f'<rect x="58" y="110" width="324" height="52" rx="26" fill="#ffffff"/>'
            f'<circle cx="88" cy="136" r="10" fill="none" stroke="#9a9a7a" stroke-width="4"/>'
            f'<rect x="112" y="128" width="150" height="16" rx="8" fill="#d8d4b0"/>{tiles}'
            f'<g id="{pid}-bar"><rect x="58" y="460" width="324" height="150" rx="26" fill="{G}"/>'
            f'<text x="84" y="520" font-family="DM Sans" font-weight="700" font-size="30" fill="#ffffff">Arriving in</text>'
            f'<text x="84" y="584" font-family="Bricolage Grotesque" font-weight="800" font-size="60" fill="{Y}">9 min</text>'
            f'<circle cx="330" cy="535" r="34" fill="none" stroke="{Y}" stroke-width="8" stroke-dasharray="160 220" transform="rotate(-90 330 535)"/></g>'
            f'<rect x="58" y="640" width="324" height="84" rx="22" fill="{INK}"/>'
            f'<rect x="90" y="672" width="160" height="20" rx="10" fill="{Y}"/></svg>')


def scooter(sid):
    return (f'<svg width="760" height="520" viewBox="0 0 760 520">'
            f'<g id="{sid}-lines" stroke="{INK}" stroke-width="10" stroke-linecap="round" opacity="0.35">'
            f'<line x1="20" y1="260" x2="150" y2="260"/><line x1="0" y1="330" x2="170" y2="330"/><line x1="40" y1="400" x2="160" y2="400"/></g>'
            f'<g id="{sid}-body">'
            f'<ellipse cx="420" cy="500" rx="300" ry="14" fill="{INK}" opacity="0.15"/>'
            f'<circle cx="250" cy="430" r="62" fill="{INK}"/><circle cx="250" cy="430" r="26" fill="#cfc9a0"/>'
            f'<circle cx="600" cy="430" r="62" fill="{INK}"/><circle cx="600" cy="430" r="26" fill="#cfc9a0"/>'
            f'<path d="M190 420 Q200 330 320 330 L520 330 Q560 330 590 300 L640 220 L668 230 L630 330 Q620 420 540 420 Z" fill="{G}"/>'
            f'<rect x="600" y="170" width="70" height="20" rx="10" fill="{INK}"/>'
            f'<rect x="250" y="120" width="210" height="190" rx="22" fill="{Y}" stroke="{INK}" stroke-width="10"/>'
            f'<text x="355" y="238" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="800" font-size="72" fill="{INK}">10</text>'
            f'<path d="M470 330 L500 210 Q510 170 550 170 L560 170 L540 330 Z" fill="{INK}"/>'
            f'<circle cx="540" cy="130" r="48" fill="{RED}"/><rect x="500" y="118" width="80" height="18" rx="9" fill="{INK}" opacity="0.6"/>'
            f'</g></svg>')


def storefront(sid):
    stripes = "".join(f'<rect x="{150 + n * 100}" y="140" width="50" height="70" fill="{G}"/>' for n in range(6))
    shutter = "".join(f'<line x1="240" x2="660" y1="{300 + n * 26}" y2="{300 + n * 26}" stroke="#9aa39a" stroke-width="6"/>' for n in range(9))
    return (f'<svg width="800" height="620" viewBox="0 0 800 620">'
            f'<rect x="120" y="120" width="660" height="480" rx="10" fill="#ffffff"/>'
            f'<rect x="120" y="140" width="660" height="70" fill="#ffffff"/>{stripes}'
            f'<rect x="100" y="110" width="700" height="30" rx="10" fill="{INK}"/>'
            f'<rect x="240" y="280" width="420" height="320" fill="#c9d1c9"/>{shutter}'
            f'<g id="{sid}-sign"><rect x="300" y="220" width="300" height="46" rx="10" fill="{INK}"/>'
            f'<text x="450" y="254" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="30" fill="{Y}">STAFF ONLY</text></g>'
            f'<rect x="80" y="596" width="740" height="14" rx="7" fill="{INK}" opacity="0.2"/></svg>')


def shelves(sid):
    out = []
    for r in range(3):
        y = 110 + r * 170
        out.append(f'<rect x="60" y="{y + 120}" width="880" height="16" rx="8" fill="{INK}"/>')
        for c in range(9):
            col = TILE[(r * 2 + c) % 6]
            h = [90, 70, 110, 80, 100, 64, 96, 76, 104][(c + r) % 9]
            out.append(f'<rect id="{sid}-i{r}{c}" x="{80 + c * 96}" y="{y + 120 - h}" width="76" height="{h}" rx="12" fill="{col}"/>')
    return f'<svg width="1000" height="640" viewBox="0 0 1000 640">{"".join(out)}</svg>'


def citymap(mid):
    houses = []
    spots = [(150, 170), (330, 150), (690, 160), (840, 190), (130, 520), (300, 560), (720, 560), (860, 520), (140, 340), (860, 360), (520, 120), (520, 610)]
    for n, (x, y) in enumerate(spots):
        houses.append(f'<rect x="{x - 34}" y="{y - 30}" width="68" height="60" rx="12" fill="{TILE[n % 6]}"/>'
                      f'<path d="M{x - 40} {y - 28} L{x} {y - 62} L{x + 40} {y - 28} Z" fill="{INK}" opacity="0.85"/>')
    roads = (f'<path d="M0 255 H1000 M0 445 H1000 M240 0 V720 M780 0 V720" stroke="#ffffff" stroke-width="44" fill="none"/>'
             f'<path d="M0 255 H1000 M0 445 H1000 M240 0 V720 M780 0 V720" stroke="#e9c232" stroke-width="4" stroke-dasharray="18 18" fill="none"/>')
    return (f'<svg width="1000" height="720" viewBox="0 0 1000 720">'
            f'<rect width="1000" height="720" rx="40" fill="#F6E7A0"/>{roads}{"".join(houses)}'
            f'<circle id="{mid}-ring" cx="510" cy="350" r="300" fill="rgba(15,138,60,0.10)" stroke="{G}" stroke-width="8" pathLength="1" stroke-dasharray="1"/>'
            f'<rect x="460" y="300" width="100" height="100" rx="20" fill="{G}"/>'
            f'<text x="510" y="364" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="800" font-size="40" fill="{Y}">DS</text>'
            f'<path id="{mid}-route" d="M560 350 H780 V200" stroke="{RED}" stroke-width="10" stroke-linecap="round" fill="none" pathLength="1" stroke-dasharray="1"/>'
            f'<circle id="{mid}-pin" cx="840" cy="190" r="22" fill="{RED}" stroke="#ffffff" stroke-width="6"/>'
            f'<circle id="{mid}-dot" cx="560" cy="350" r="18" fill="{INK}" stroke="#ffffff" stroke-width="6"/></svg>')


def pop_ids(s, ids, t0, step=0.06):
    for n, i in enumerate(ids):
        s.J(f'tl.fromTo("#{i}",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.35,ease:"back.out(2)"}},{round(t0 + n * step, 2)});')


# ---- 0: hook (phone + number, then profit)
s = sl.Scene("hook", 0); S.append(s)
t_turn = round(s.P("And for the first") - 0.1, 2)
s.E("ph", phone("hook-ph"), L(170, 140, 10), 0.05, "fade")
pop_ids(s, [f"hook-ph-t{n}" for n in range(6)], 0.2)
s.J(f'tl.fromTo("#hook-ph-bar",{{opacity:0,y:60}},{{opacity:1,y:0,duration:0.5,ease:"back.out(1.6)"}},0.75);')
s.E("k", "BLINKIT · JULY TO SEPTEMBER 2026", L(720, 250, 34, "width:1080px;"), 0.1, "fade", cls="kick q")
s.E("n", "₹0 Cr", L(712, 320, 190, "width:1100px;"), s.P("twenty-one"), ("count", 20940, '(v)=>"₹"+Math.round(v).toLocaleString("en-IN")+" Cr"', 1.5), out=t_turn, cls="hero up tnum")
s.E("c", "in orders, in just 3 months", L(720, 560, 60, "width:1080px;"), round(s.P("twenty-one") + 0.4, 2), "fade", out=t_turn)
s.E("a", "And for the first time…", L(720, 330, 60, "width:1080px;"), s.P("And for the first"), "fade", cls="q")
s.E("b", "it's making<br><span class='up'>money.</span>", L(712, 420, 170, "width:1100px;"), s.P("actually making"), "pop", cls="hero")
s.E("src", "Source: Eternal Q2 FY27 results, via Business Standard", L(720, 960, 28, "width:1100px;font-weight:500;"), s.P("twenty-one"), "fade", cls="q")

# ---- 1: question (rider)
s = sl.Scene("question", 1); S.append(s)
s.E("a", "How does <span class='up'>10-minute</span> delivery", C(110, 100), 0.1, cls="hero")
s.E("b", "turn a profit?", C(230, 100), s.P("turn a profit"), "pop", cls="hero")
s.E("sc", scooter("question-sc"), L(580, 430, 10), 0.15, "fade")
s.J('tl.fromTo("#question-sc-body",{x:-260},{x:0,duration:0.9,ease:"power3.out"},0.15);')
s.J('tl.fromTo("#question-sc-lines",{opacity:0,x:60},{opacity:0.35,x:0,duration:0.6,ease:"power2.out"},0.6);')
s.J('tl.to("#question-sc-body",{y:-6,duration:0.25,yoyo:true,repeat:11,ease:"sine.inOut"},1.05);')
s.E("d", "Let's break<br>it down.", L(150, 560, 60, "width:420px;"), s.P("Let's break"), "fade", cls="q")

# ---- 2: the dark store (exterior)
s = sl.Scene("darkstore", 2); S.append(s)
s.E("k", "THING #1", L(150, 300, 40, "width:700px;"), 0.1, "fade", cls="kick up")
s.E("h", "The<br>dark<br>store.", L(140, 370, 150, "width:700px;"), 0.35, "pop", cls="hero")
s.E("st", storefront("darkstore-st"), L(900, 240, 10), 0.1, "fade")
s.J('tl.fromTo("#darkstore-st-sign",{opacity:0,y:-30},{opacity:1,y:0,duration:0.4,ease:"back.out(2)"},' + str(s.P("the dark store")) + ');')

# ---- 3: inside the dark store (shelves fill up)
s = sl.Scene("inside", 3); S.append(s)
s.E("a", "A small warehouse <span class='up'>in your neighbourhood</span>", C(90, 72), 0.1, cls="hero")
s.E("sh", shelves("inside-sh"), L(640, 230, 10), 0.1, "fade")
pop_ids(s, [f"inside-sh-i{r}{c}" for r in range(3) for c in range(9)], 0.4, 0.05)
s.E("nc", "No<br>customers<br>walk in.", L(130, 330, 76, "width:460px;"), s.P("No customers"), "wipe", cls="hero down")
s.E("fw", "Just the few thousand things people order again and again.", L(110, 900, 44, "width:1700px;text-align:center;"), s.P("the few thousand"), "fade", cls="q")

# ---- 4: why it's fast (map)
s = sl.Scene("map", 4); S.append(s)
t_r = s.P("the rider")
s.E("m", citymap("map-m"), L(90, 180, 10), 0.1, "fade")
s.J(draw("#map-m-ring", 0.3, 1.2))
s.J(draw("#map-m-route", t_r, 1.4))
s.J('tl.to("#map-m-dot",{x:220,duration:0.7,ease:"none"},' + str(t_r) + ');')
s.J('tl.to("#map-m-dot",{y:-150,duration:0.7,ease:"none"},' + str(round(t_r + 0.7, 2)) + ');')
s.J(fin("#map-m-pin", round(t_r + 1.3, 2)))
s.E("k", "SHORT TRIP", L(1170, 220, 40, "width:660px;"), t_r, "fade", cls="kick up")
s.E("a", "The speed comes from", L(1170, 330, 56, "width:660px;"), s.P("The speed comes"), "fade", cls="q")
s.E("b", "where the<br>store sits", L(1162, 410, 120, "width:680px;"), s.P("where the store"), "pop", cls="hero up")
s.E("c", "not from fast driving.", L(1170, 700, 56, "width:660px;"), s.P("not from fast"), "wipe", cls="hero down")

sl.write_project(os.path.join(HERE, "project"), S, audio_dur=30.8)
