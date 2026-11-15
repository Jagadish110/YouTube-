"""Video 002: How Blinkit Makes Money in 10 Minutes. One sl.Scene per line of vo_script.txt.

Look: Blinkit yellow #F8CB46 + green #0C831F, Bricolage Grotesque / DM Sans, drawn SVG illustrations.
Run from this folder:  python3 build.py
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
import scenelib as sl
from scenelib import C, L, draw, fin

HERE = os.path.dirname(os.path.abspath(__file__))
sl.setup(os.path.join(HERE, "vo_marks.json"), 163.0)
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
RUPEE = '(v)=>"₹"+Math.round(v).toLocaleString("en-IN")+" Cr"'

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



def stopwatch(sid, label="10"):
    return (f'<svg width="300" height="330" viewBox="0 0 300 330"><rect x="125" y="0" width="50" height="34" rx="8" fill="{INK}"/>'
            f'<circle cx="150" cy="190" r="132" fill="#ffffff" stroke="{INK}" stroke-width="14"/>'
            f'<circle id="{sid}-arc" cx="150" cy="190" r="104" fill="none" stroke="{G}" stroke-width="22" pathLength="1" stroke-dasharray="1" transform="rotate(-90 150 190)"/>'
            f'<text x="150" y="210" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="800" font-size="76" fill="{INK}">{label}</text>'
            f'<text x="150" y="255" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="30" fill="{INK}">MIN</text></svg>')


def basket():
    return (f'<svg width="360" height="300" viewBox="0 0 360 300">'
            f'<path d="M110 110 Q110 30 180 30 Q250 30 250 110" stroke="{INK}" stroke-width="14" fill="none"/>'
            f'<rect x="80" y="70" width="60" height="80" rx="10" fill="{TILE[1]}"/><rect x="150" y="50" width="56" height="100" rx="10" fill="{TILE[3]}"/><rect x="214" y="80" width="64" height="70" rx="10" fill="{TILE[0]}"/>'
            f'<path d="M30 120 H330 L300 280 H60 Z" fill="{G}" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>'
            f'<path d="M110 160 V250 M180 160 V250 M250 160 V250" stroke="{Y}" stroke-width="10" stroke-linecap="round"/></svg>')


def boxes(sid):
    out = []
    pos = [(60, 300), (240, 300), (420, 300), (150, 140), (330, 140), (240, -20)]
    for n, (x, y) in enumerate(pos):
        out.append(f'<g id="{sid}-b{n}"><rect x="{x}" y="{y + 60}" width="170" height="150" rx="10" fill="#D9A15B" stroke="{INK}" stroke-width="8"/>'
                   f'<rect x="{x + 70}" y="{y + 60}" width="30" height="150" fill="#C08744"/>'
                   f'<rect x="{x + 30}" y="{y + 150}" width="110" height="34" rx="6" fill="{G}"/>'
                   f'<text x="{x + 85}" y="{y + 176}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="24" fill="#fff">OWNED</text></g>')
    return f'<svg width="660" height="540" viewBox="0 0 660 540">{"".join(out)}</svg>'


def coins(n, color, cid):
    out = []
    for i in range(n):
        out.append(f'<g id="{cid}-{i}"><ellipse cx="110" cy="{300 - i * 30}" rx="90" ry="26" fill="{color}" stroke="{INK}" stroke-width="8"/></g>')
    return f'<svg width="220" height="360" viewBox="0 0 220 360">{"".join(out)}</svg>'


def person(x, y, c):
    return (f'<circle cx="{x}" cy="{y}" r="16" fill="{c}"/><path d="M{x - 24} {y + 56} Q{x - 24} {y + 20} {x} {y + 20} Q{x + 24} {y + 20} {x + 24} {y + 56} Z" fill="{c}"/>')


def search_phone():
    return (f'<svg width="330" height="520" viewBox="0 0 330 520"><rect x="6" y="6" width="318" height="508" rx="48" fill="{INK}"/>'
            f'<rect x="24" y="30" width="282" height="462" rx="32" fill="{CREAM}"/>'
            f'<rect x="44" y="60" width="242" height="48" rx="24" fill="#fff" stroke="#d8d4b0" stroke-width="4"/>'
            f'<text x="70" y="92" font-family="DM Sans" font-weight="700" font-size="24" fill="#8a8a6a">chips</text>'
            f'<rect x="44" y="130" width="242" height="110" rx="18" fill="#fff" stroke="{G}" stroke-width="6"/>'
            f'<rect x="60" y="146" width="78" height="78" rx="12" fill="{TILE[0]}"/>'
            f'<rect x="152" y="152" width="110" height="18" rx="9" fill="#cfcab0"/>'
            f'<rect x="152" y="186" width="92" height="30" rx="8" fill="{G}"/><text x="198" y="208" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="20" fill="#fff">AD</text>'
            f'<rect x="44" y="258" width="242" height="96" rx="18" fill="#fff"/><rect x="60" y="272" width="68" height="68" rx="12" fill="{TILE[1]}"/><rect x="142" y="282" width="110" height="18" rx="9" fill="#e0dcc4"/>'
            f'<rect x="44" y="372" width="242" height="96" rx="18" fill="#fff"/><rect x="60" y="386" width="68" height="68" rx="12" fill="{TILE[4]}"/><rect x="142" y="396" width="110" height="18" rx="9" fill="#e0dcc4"/></svg>')


def skyline(sid):
    out = []
    xs = [(40, 220), (150, 320), (270, 260), (380, 380), (500, 290), (610, 340), (720, 240)]
    for n, (x, h) in enumerate(xs):
        out.append(f'<rect id="{sid}-k{n}" x="{x}" y="{420 - h}" width="96" height="{h}" rx="8" fill="{[G, INK, "#2E6B3F", G, INK, "#2E6B3F", G][n]}"/>')
        for r in range(int(h / 60)):
            out.append(f'<rect x="{x + 20}" y="{420 - h + 24 + r * 60}" width="20" height="24" rx="3" fill="{Y}" opacity="0.8"/><rect x="{x + 56}" y="{420 - h + 24 + r * 60}" width="20" height="24" rx="3" fill="{Y}" opacity="0.8"/>')
    return f'<svg width="840" height="440" viewBox="0 0 840 440">{"".join(out)}<rect x="0" y="420" width="840" height="14" rx="7" fill="{INK}"/></svg>'



# ---- 0: hook (phone + number, then profit)
s = sl.Scene("hook", 0); S.append(s)
t_turn = round(s.P("And for the first") - 0.1, 2)
s.E("ph", phone("hook-ph"), L(170, 140, 10), 0.05, "fade")
pop_ids(s, [f"hook-ph-t{n}" for n in range(6)], 0.2)
s.J(f'tl.fromTo("#hook-ph-bar",{{opacity:0,y:60}},{{opacity:1,y:0,duration:0.5,ease:"back.out(1.6)"}},0.75);')
s.E("k", "BLINKIT · JULY TO SEPTEMBER 2026", L(720, 250, 34, "width:1080px;"), 0.1, "fade", cls="kick q")
s.E("n", "₹0 Cr", L(712, 320, 190, "width:1100px;"), s.P("twenty-one"), ("count", 20940, RUPEE, 1.5), out=t_turn, cls="hero up tnum")
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

# ---- 2: Grofers origin
s = sl.Scene("origin", 2); S.append(s)
s.E("y", "2013", L(150, 170, 60, "width:600px;"), 0.1, "fade", cls="kick up")
s.E("g", "GROFERS", L(140, 250, 170, "width:1000px;"), s.P("as Grofers"), "pop", cls="hero")
s.E("d", "an online grocery app", L(150, 450, 56, "width:900px;"), s.P("an online grocery"), "fade", cls="q")
s.E("bk", basket(), L(1330, 200, 10), 0.3, "fade")
s.J('tl.fromTo("#origin-bk",{y:40},{y:0,duration:0.6,ease:"back.out(1.8)"},0.3);')
card = "width:640px;padding:30px 36px;"
s.E("f1", '<div class="q" style="font-size:30px;font-weight:700">FOUNDER</div><div class="hero" style="font-size:64px">Albinder Dhindsa</div>', L(150, 640, 10, card), s.P("Albinder"), cls="card")
s.E("f2", '<div class="q" style="font-size:30px;font-weight:700">FOUNDER</div><div class="hero" style="font-size:64px">Saurabh Kumar</div>', L(840, 640, 10, card), s.P("Saurabh"), cls="card")
s.E("src", "Source: Wikipedia, Blinkit", L(150, 960, 28, "width:800px;font-weight:500;"), s.P("as Grofers"), "fade", cls="q")

# ---- 3: the speed bet
s = sl.Scene("bet", 3); S.append(s)
t21 = s.P("Then in twenty")
s.E("ln", f'<svg width="1600" height="40" viewBox="0 0 1600 40"><path id="bet-l" d="M20 20 H1580" stroke="{INK}" stroke-width="10" stroke-linecap="round" pathLength="1" stroke-dasharray="1"/></svg>', L(160, 520, 10), 0.1, "fade")
s.J(draw("#bet-l", 0.2, 1.2))
s.E("d1", "", L(170, 513, 10, f"width:54px;height:54px;border-radius:50%;background:{INK};"), 0.2, "pop")
s.E("a1", "2013", L(130, 600, 56, "width:300px;"), 0.25, "fade", cls="hero")
s.E("b1", "a normal grocery app", L(130, 670, 36, "width:420px;"), 0.4, "fade", cls="q")
s.E("d2", "", L(1690, 505, 10, f"width:70px;height:70px;border-radius:50%;background:{G};"), t21, "pop")
s.E("a2", "2021", L(1380, 600, 56, "width:380px;text-align:right;"), t21, "fade", cls="hero up")
s.E("sw", stopwatch("bet-sw"), L(1440, 150, 10), s.P("ten-minute"), "pop")
s.J(draw("#bet-sw-arc", s.P("ten-minute"), 1.2))
s.E("sp", "bet everything<br>on <span class='up'>speed</span>", L(640, 180, 110, "width:760px;"), s.P("bet everything"), "pop", cls="hero")
s.E("nm", "new name: <span class='hero up' style='font-size:84px'>BLINKIT</span>", L(640, 720, 48, "width:900px;"), s.P("a new name"), "wipe")

# ---- 4: Zomato buys it
s = sl.Scene("buy", 4); S.append(s)
s.E("y", "2022", C(170, 60), 0.1, "fade", cls="kick up")
s.E("h", "Zomato buys Blinkit", C(250, 110), 0.15, cls="hero")
s.E("n", "₹0 Cr", C(420, 200), s.P("about four"), ("count", 4447, RUPEE, 1.4), cls="hero up tnum")
s.E("c", "paid in Zomato shares, not cash", C(700, 56), s.P("paid in"), "fade", cls="q")
s.E("src", "Source: Wikipedia, Blinkit · deal valued at about US$568 million", L(150, 960, 28, "width:1500px;font-weight:500;"), s.P("about four"), "fade", cls="q")

# ---- 5: Eternal, Blinkit biggest
s = sl.Scene("eternal", 5); S.append(s)
s.E("e", f'<div class="kick" style="font-size:40px;color:{Y}">ETERNAL</div><div style="font-size:30px;color:#fff;opacity:.8;font-weight:500">Zomato\'s parent company</div>', L(160, 160, 10, f"width:1600px;height:760px;background:{INK};border-radius:36px;padding:44px 56px;"), s.P("Eternal"), "fade")
s.E("z", '<div class="hero" style="font-size:52px;color:#fff">Zomato</div><div style="font-size:30px;color:#fff;opacity:.85">food delivery</div>', L(220, 400, 10, f"width:420px;height:420px;background:{RED};border-radius:28px;padding:36px;"), s.P("Eternal"), "pop")
s.E("b", f'<div class="hero" style="font-size:110px;color:{INK}">Blinkit</div><div style="font-size:40px;color:{INK};font-weight:700">biggest business by far</div>', L(700, 330, 10, f"width:1000px;height:520px;background:{Y};border-radius:28px;padding:56px;"), s.P("And Blinkit"), "pop")

# ---- 6: the dark store (exterior)
s = sl.Scene("darkstore", 6); S.append(s)
s.E("k", "THING #1", L(150, 300, 40, "width:700px;"), 0.1, "fade", cls="kick up")
s.E("h", "The<br>dark<br>store.", L(140, 370, 150, "width:700px;"), 0.35, "pop", cls="hero")
s.E("st", storefront("darkstore-st"), L(900, 240, 10), 0.1, "fade")
s.J('tl.fromTo("#darkstore-st-sign",{opacity:0,y:-30},{opacity:1,y:0,duration:0.4,ease:"back.out(2)"},' + str(s.P("the dark store")) + ');')

# ---- 7: inside the dark store
s = sl.Scene("inside", 7); S.append(s)
s.E("a", "A small warehouse <span class='up'>in your neighbourhood</span>", C(90, 72), 0.1, cls="hero")
s.E("sh", shelves("inside-sh"), L(640, 230, 10), 0.1, "fade")
pop_ids(s, [f"inside-sh-i{r}{c}" for r in range(3) for c in range(9)], 0.4, 0.05)
s.E("nc", "No<br>customers<br>walk in.", L(130, 330, 76, "width:460px;"), s.P("No customers"), "wipe", cls="hero down")
s.E("fw", "Just the few thousand things people order again and again.", L(110, 900, 44, "width:1700px;text-align:center;"), s.P("the few thousand"), "fade", cls="q")

# ---- 8: why it's fast (map)
s = sl.Scene("map", 8); S.append(s)
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

# ---- 9: store count and target
s = sl.Scene("stores", 9); S.append(s)
t_w = s.P("It wants")
s.E("k", "DARK STORES · 30 SEPTEMBER 2026", C(150, 40), 0.1, "fade", cls="kick q")
s.E("n", "0", C(230, 230), s.P("two thousand"), ("count", 2751, '(v)=>Math.round(v).toLocaleString("en-IN")', 1.5), cls="hero up tnum")
bar = lambda w, c: f"width:{w}px;height:70px;border-radius:35px;background:{c};"
s.E("b1", "", L(260, 640, 10, bar(1060, G)), round(s.P("two thousand") + 0.2, 2), "wipe")
s.E("l1", "2,751 now", L(260, 730, 40, "width:600px;"), round(s.P("two thousand") + 0.6, 2), "fade")
s.E("b2", "", L(260, 820, 10, bar(1400, INK)), t_w, "wipe")
s.E("l2", "3,500+ planned by March 2027", L(260, 910, 40, "width:1200px;"), round(t_w + 0.3, 2), "fade", cls="up")
s.E("src", "Sources: Business Standard · Indian Startup News", L(860, 980, 28, "width:980px;text-align:right;font-weight:500;"), s.P("two thousand"), "fade", cls="q")

# ---- 10: thing #2
s = sl.Scene("owns", 10); S.append(s)
s.E("k", "THING #2", L(150, 300, 40, "width:700px;"), 0.1, "fade", cls="kick up")
s.E("h", "Blinkit<br>owns what<br>it sells.", L(140, 370, 130, "width:800px;"), s.P("Blinkit now owns"), "pop", cls="hero")
s.E("bx", boxes("owns-bx"), L(1060, 260, 10), 0.1, "fade")
pop_ids(s, [f"owns-bx-b{n}" for n in range(6)], 0.3, 0.12)

# ---- 11: before / now
s = sl.Scene("model", 11); S.append(s)
t_now = s.P("So its revenue")
s.E("k", "JULY 2025: BLINKIT STARTS OWNING ITS STOCK", C(120, 40), 0.1, "fade", cls="kick q")
s.E("sm", "like a supermarket", C(190, 64), s.P("the way a supermarket"), "fade", cls="hero")
s.E("c1", f'<div class="kick q" style="font-size:34px">BEFORE</div><div class="hero" style="font-size:64px;margin-top:10px">a cut of<br>each sale</div>', L(240, 340, 10, "width:620px;height:520px;padding:44px;"), 0.4, "fade", cls="card")
s.E("k1", coins(1, Y, "model-a"), L(600, 450, 10), 0.6, "fade")
s.E("c2", f'<div class="kick" style="font-size:34px;color:{G}">NOW</div><div class="hero" style="font-size:64px;margin-top:10px">the full<br>price</div>', L(1060, 340, 10, f"width:620px;height:520px;padding:44px;border:6px solid {G};"), t_now, "pop", cls="card")
s.E("k2", coins(7, Y, "model-b"), L(1380, 480, 10), t_now, "fade")
pop_ids(s, [f"model-b-{i}" for i in range(7)], round(t_now + 0.2, 2), 0.1)
s.E("src", "Source: Eternal investor call, 21 July 2025, via Informist", L(240, 960, 28, "width:1400px;font-weight:500;"), 0.4, "fade", cls="q")

# ---- 12: revenue
s = sl.Scene("revenue", 12); S.append(s)
s.E("k", "BLINKIT REVENUE · JULY TO SEPTEMBER 2026", C(170, 40), 0.1, "fade", cls="kick q")
s.E("n", "₹0 Cr", C(260, 230), s.P("nineteen thousand"), ("count", 19152, RUPEE, 1.5), cls="hero up tnum")
s.E("p", f'<span style="display:inline-block;background:{G};color:#fff;padding:14px 40px;border-radius:999px">▲ 94% in a year</span>', C(600, 72), s.P("up ninety-four"), "pop", cls="hero")
s.E("src", "Source: Indian Startup News", L(150, 960, 28, "width:800px;font-weight:500;"), s.P("nineteen thousand"), "fade", cls="q")

# ---- 13: share of Eternal
s = sl.Scene("share", 13); S.append(s)
t_food = s.P("The food delivery")
s.E("k", "SHARE OF ETERNAL'S REVENUE", C(180, 40), 0.1, "fade", cls="kick q")
s.E("n", "0%", C(250, 220), 0.15, ("count", 79, '(v)=>Math.round(v)+"%"', 1.3), cls="hero up tnum")
s.E("bb", "", L(160, 560, 10, f"width:1600px;height:130px;border-radius:24px;background:{INK};"), 0.2, "fade")
s.E("bg", '<span class="hero" style="font-size:52px;color:#fff;padding-left:40px">Blinkit</span>', L(160, 560, 10, f"width:1264px;height:130px;border-radius:24px;background:{G};display:flex;align-items:center;"), 0.3, "wipe")
s.E("rest", "everything else", L(1440, 760, 40, "width:320px;text-align:right;"), t_food, "fade", cls="q")
s.E("fd", "Food delivery is now the <span class='down'>smaller</span> part.", C(860, 56), t_food, "fade", cls="hero")
s.E("src", "Source: Indian Startup News", L(160, 980, 28, "width:800px;font-weight:500;"), 0.2, "fade", cls="q")

# ---- 14: revenue is not profit
s = sl.Scene("notprofit", 14); S.append(s)
s.E("a", "REVENUE", C(270, 170), 0.1, "pop", cls="hero")
s.E("x", "≠", C(440, 150), s.P("isn't profit"), "pop", cls="hero down")
s.E("b", "PROFIT", C(600, 170), s.P("isn't profit"), "pop", cls="hero up")
s.E("q", "So where does the money come from?", C(860, 56), s.P("So where"), "fade", cls="q")

# ---- 15: two money sources
s = sl.Scene("sources", 15); S.append(s)
s.E("h", "Where the money comes from", C(100, 84), 0.1, cls="hero")
s.E("c1", f'<div class="kick up" style="font-size:34px">1</div><div class="hero" style="font-size:70px;margin-top:8px">Margin on<br>every product</div><div class="q" style="font-size:36px;margin-top:20px;font-weight:500">buy for less, sell for more</div>', L(160, 280, 10, "width:760px;height:600px;padding:52px;"), s.P("The margin"), "pop", cls="card")
s.E("bk", basket(), L(560, 640, 10, "transform:scale(0.8);transform-origin:left top;"), round(s.P("The margin") + 0.2, 2), "fade")
s.E("c2", f'<div class="kick up" style="font-size:34px">2</div><div class="hero" style="font-size:70px;margin-top:8px">Advertising</div><div class="q" style="font-size:36px;margin-top:20px;font-weight:500">brands pay to show<br>up first in search</div>', L(1000, 280, 10, "width:760px;height:600px;padding:52px;"), s.P("And brands"), "pop", cls="card")
s.E("ph", search_phone(), L(1470, 470, 10, "transform:scale(0.75);transform-origin:left top;"), round(s.P("And brands") + 0.2, 2), "fade")
s.E("src", "Ads source: Storyboard18 (Blinkit ad revenue up 220% in Q3 FY24)", L(160, 960, 28, "width:1500px;font-weight:500;"), s.P("And brands"), "fade", cls="q")

# ---- 16: scorecard
s = sl.Scene("score", 16); S.append(s)
t_now2 = s.P("This quarter")
s.E("k", "ADJUSTED EBITDA (PROFIT BEFORE SOME COSTS)", C(120, 36), 0.1, "fade", cls="kick q")
s.E("ax", "", L(260, 600, 10, f"width:1400px;height:6px;background:{INK};"), 0.2, "fade")
s.E("b1", "", L(480, 606, 10, f"width:300px;height:156px;background:{RED};border-radius:0 0 16px 16px;transform-origin:top;"), s.P("lost one"), "fade")
s.J(f'tl.fromTo("#score-b1",{{scaleY:0}},{{scaleY:1,duration:0.6,ease:"power3.out"}},{s.P("lost one")});')
s.E("n1", "−₹0 Cr", L(380, 800, 72, "width:500px;text-align:center;"), s.P("lost one"), ("count", 156, '(v)=>"−₹"+Math.round(v)+" Cr"', 1.2), cls="hero down tnum")
s.E("l1", "a year ago", L(380, 890, 40, "width:500px;text-align:center;"), s.P("lost one"), "fade", cls="q")
s.E("b2", "", L(1140, 412, 10, f"width:300px;height:188px;background:{G};border-radius:16px 16px 0 0;transform-origin:bottom;"), t_now2, "fade")
s.J(f'tl.fromTo("#score-b2",{{scaleY:0}},{{scaleY:1,duration:0.6,ease:"power3.out"}},{t_now2});')
s.E("n2", "+₹0 Cr", L(1040, 250, 90, "width:500px;text-align:center;"), t_now2, ("count", 184, '(v)=>"+₹"+Math.round(v)+" Cr"', 1.3), cls="hero up tnum")
s.E("l2", "July to September 2026", L(990, 640, 40, "width:600px;text-align:center;"), t_now2, "fade", cls="q")
s.E("src", "Source: Indian Startup News", L(260, 980, 28, "width:800px;font-weight:500;"), s.P("lost one"), "fade", cls="q")

# ---- 17: thin margin, improving
s = sl.Scene("thin", 17); S.append(s)
t_six = s.P("Thin")
s.E("n", "₹0.9", L(180, 230, 230, "width:900px;"), 0.15, "pop", cls="hero up")
s.E("c", "profit for every ₹100 of orders", L(190, 500, 56, "width:900px;"), 0.4, "fade")
steps = "".join(f'<rect id="thin-s{n}" x="{n * 110}" y="{380 - (n + 1) * 52}" width="86" height="{(n + 1) * 52}" rx="10" fill="{G if n == 5 else INK}"/>' for n in range(6))
s.E("st", f'<svg width="660" height="400" viewBox="0 0 660 400">{steps}</svg>', L(1120, 360, 10), t_six, "fade")
pop_ids(s, [f"thin-s{n}" for n in range(6)], round(t_six + 0.1, 2), 0.15)
s.E("l", "better for 6 quarters in a row", L(1080, 790, 44, "width:760px;text-align:center;"), s.P("six quarters"), "fade", cls="hero")
s.E("src", "0.9% of net order value · Source: Indian Startup News", L(180, 980, 28, "width:1200px;font-weight:500;"), 0.4, "fade", cls="q")

# ---- 18: mature cities
s = sl.Scene("mature", 18); S.append(s)
t_sig = s.P("That's the real")
s.E("k", "OLDEST CITIES", L(160, 200, 40, "width:700px;"), 0.1, "fade", cls="kick q")
s.E("n", "5%+", L(150, 260, 230, "width:700px;"), s.P("above five"), "pop", cls="hero up")
s.E("c", "margin, adjusted", L(160, 520, 52, "width:700px;"), round(s.P("above five") + 0.3, 2), "fade", cls="q")
s.E("sk", skyline("mature-sk"), L(920, 380, 10), 0.1, "fade")
pop_ids(s, [f"mature-sk-k{n}" for n in range(7)], 0.2, 0.08)
s.E("t", "Once a store matures, <span class='up'>it makes money.</span>", C(880, 60), t_sig, "wipe", cls="hero")
s.E("src", "Source: Indian Startup News", L(160, 980, 28, "width:800px;font-weight:500;"), s.P("above five"), "fade", cls="q")

# ---- 19: customers
s = sl.Scene("people", 19); S.append(s)
s.E("n", "0M", C(180, 240), 0.1, ("count", 37, '(v)=>Math.round(v)+" million"', 1.3), cls="hero up tnum")
s.E("c", "people order from Blinkit every month", C(470, 56), 0.4, "fade")
crowd = "".join(person(60 + (n % 20) * 90, 40 + (n // 20) * 100, [G, INK, "#2E6B3F"][n % 3]) for n in range(60))
s.E("cr", f'<svg width="1860" height="320" viewBox="0 0 1860 320">{crowd}</svg>', L(30, 600, 10), 0.5, "fade")
s.J('tl.fromTo("#people-cr",{y:40},{y:0,duration:0.8,ease:"power3.out"},0.5);')
s.E("src", "Monthly transacting customers · Source: Indian Startup News", L(150, 980, 28, "width:1200px;font-weight:500;"), 0.4, "fade", cls="q")

# ---- 20: the catch
s = sl.Scene("catch", 20); S.append(s)
t_riv = s.P("while Swiggy")
s.E("h", "The catch", C(110, 110), 0.1, cls="hero down")
s.E("a", "Every new store <span class='down'>loses money</span> at first.", C(260, 64), s.P("Every new store"), "fade", cls="hero")
mini = "".join(f'<g id="catch-m{n}"><rect x="{n * 150}" y="40" width="120" height="100" rx="12" fill="#ffffff" stroke="{INK}" stroke-width="6"/><rect x="{n * 150}" y="40" width="120" height="26" rx="8" fill="{G}"/><text x="{n * 150 + 60}" y="125" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="40" fill="{RED}">−</text></g>' for n in range(10))
s.E("ms", f'<svg width="1500" height="160" viewBox="0 0 1500 160">{mini}</svg>', L(230, 380, 10), s.P("opening hundreds"), "fade")
pop_ids(s, [f"catch-m{n}" for n in range(10)], s.P("opening hundreds"), 0.08)
pill = f"display:inline-block;background:{INK};color:#fff;padding:18px 40px;border-radius:999px;margin:0 14px;"
s.E("r", f'<span style="{pill}">Swiggy Instamart</span><span style="{pill}">Zepto</span><span style="{pill}">and others</span>', C(660, 52), t_riv, "pop", cls="hero")
s.E("f", "all fighting for the same customers", C(820, 48), s.P("fight for"), "fade", cls="q")

# ---- 21: two futures
s = sl.Scene("futures", 21); S.append(s)
t_no = s.P("If they don't")
s.E("o", "", L(880, 500, 10, f"width:160px;height:160px;border-radius:50%;background:{INK};"), 0.1, "pop")
paths = (f'<svg width="1920" height="1080" viewBox="0 0 1920 1080"><path id="futures-up" d="M1040 560 Q1300 560 1500 300" stroke="{G}" stroke-width="16" fill="none" stroke-linecap="round" pathLength="1" stroke-dasharray="1"/>'
         f'<path id="futures-dn" d="M880 620 Q620 640 420 820" stroke="{RED}" stroke-width="16" fill="none" stroke-linecap="round" pathLength="1" stroke-dasharray="1"/></svg>')
s.E("p", paths, L(0, 0, 10), 0.1, "fade")
s.J(draw("#futures-up", s.P("If the new"), 1.0))
s.J(draw("#futures-dn", t_no, 1.0))
s.E("u", "new stores mature<br><span class='up'>→ a retail giant</span>", L(1180, 120, 64, "width:700px;"), s.P("becomes a retail"), "pop", cls="hero")
s.E("d", "they don't<br><span class='down'>→ profit disappears</span>", L(120, 860, 64, "width:900px;"), t_no, "pop", cls="hero")

# ---- 22: question for comments
s = sl.Scene("ask", 22); S.append(s)
btn = lambda c, fg: f"width:640px;height:220px;border-radius:40px;background:{c};color:{fg};display:flex;align-items:center;justify-content:center;font-size:84px;"
s.E("a", "GROW FASTER", L(220, 330, 10, btn(G, "#fff")), 0.1, "pop", cls="hero")
s.E("or", "or", C(400, 64), s.P("or make"), "fade", cls="q")
s.E("b", "PROFIT FIRST", L(1060, 330, 10, btn(INK, Y)), s.P("or make"), "pop", cls="hero")
s.E("c", "Tell me in the comments", C(720, 64), s.P("Tell me"), "wipe", cls="hero")

# ---- 23: subscribe + next
s = sl.Scene("endcard", 23); S.append(s)
s.E("s", "SUBSCRIBE", C(150, 200), s.P("Subscribe"), "pop", cls="hero up")
nx = f"width:1200px;padding:44px 56px;border-radius:32px;background:#E4002B;color:#fff;"
s.E("n", '<div style="font-size:36px;font-weight:700;opacity:.9">NEXT · WEDNESDAY</div><div class="hero" style="font-size:72px;margin-top:10px">India\'s biggest Coca-Cola bottler wants to go public</div>', L(360, 470, 10, nx), s.P("On Wednesday"), "pop")
s.E("t", "Revenue is falling. That isn't the whole story.", C(900, 48), s.P("I'll explain"), "fade", cls="q")

sl.write_project(os.path.join(HERE, "project"), S, audio_dur=162.6)
