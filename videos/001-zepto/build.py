"""Video 001: How Zepto Got So Big So Fast. Scene specs timed to vo_marks.json.

Run from this folder:  python3 build.py
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
import scenelib as sl
from scenelib import C, L, draw, fin

HERE = os.path.dirname(os.path.abspath(__file__))
sl.setup(os.path.join(HERE, "vo_marks.json"), 234.5)

S = []

# ---- 2: the kids
s = sl.Scene("kids", 2); S.append(s)
s.E("yr", "2020", C(110, 150), 0.1, cls="hero up")
s.E("n1", "AADIT PALICHA", L(110, 390, 68, "width:850px;text-align:center;white-space:nowrap;"), s.P("Aadit"), cls="hero")
s.E("n2", "KAIVALYA VOHRA", L(960, 390, 68, "width:850px;text-align:center;white-space:nowrap;"), s.P("Kaivalya"), cls="hero")
s.E("fr", "Childhood friends · grew up in Dubai", C(520, 48), s.P("childhood"), "fade", cls="q")
svg = ('<svg width="1920" height="300" viewBox="0 0 1920 300"><circle id="kids-d1" cx="460" cy="110" r="18" fill="#a7a3b8"/>'
       '<path id="kids-ln" d="M478 110 H1442" stroke="#8b3dff" stroke-width="8" fill="none" pathLength="1" stroke-dasharray="1"/>'
       '<circle id="kids-d2" cx="1460" cy="110" r="22" fill="#8b3dff"/></svg>')
s.E("rt", svg, L(0, 660, 10), s.P("They've"), "fade")
s.J(draw("#kids-ln", s.P("They've") + 0.2, 1.2)); s.J(fin("#kids-d2", s.P("Stanford")))
s.E("c1", "DUBAI", L(260, 810, 44, "width:400px;text-align:center;"), s.P("They've"), "fade", cls="kick q")
s.E("c2", "STANFORD", L(1210, 810, 44, "width:500px;text-align:center;"), s.P("Stanford"), cls="kick")
s.E("c3", "Computer Science", L(1210, 874, 36, "width:500px;text-align:center;"), s.P("to study"), "fade", cls="q")

# ---- 3: pandemic
s = sl.Scene("pandemic", 3); S.append(s)
s.E("lk", "LOCKDOWN", C(250, 230), 0.12, "pop", cls="hero down")
s.E("a", "Stuck at home in Mumbai", C(560, 60), s.P("They're"), "fade", cls="q")
s.E("b", "No grocery delivery.", C(680, 84), s.P("and they can't"), cls="hero")

# ---- 4: KiranaKart
s = sl.Scene("kirana", 4); S.append(s)
s.E("k", "STILL TEENAGERS · APP #1", C(130, 40), 0.15, "fade", cls="kick q")
s.E("t", "KIRANAKART", C(210, 170), s.P("Kirana Kart"), "pop", cls="hero")
bx = "width:440px;height:170px;font-size:46px;"
s.E("b1", "KIRANA SHOP", L(170, 640, 46, bx), s.P("Partner"), cls="box")
s.E("b2", "RIDER", L(740, 640, 46, bx), s.P("deliver"), cls="box")
s.E("b3", "YOUR DOOR", L(1310, 640, 46, bx + "border-color:var(--up);"), s.P("to your door"), cls="box")
s.E("ar", '<svg width="1920" height="60" viewBox="0 0 1920 60"><path id="kirana-a1" d="M622 30 H728" stroke="#a7a3b8" stroke-width="8" pathLength="1" stroke-dasharray="1"/><path id="kirana-a2" d="M1192 30 H1298" stroke="#a7a3b8" stroke-width="8" pathLength="1" stroke-dasharray="1"/></svg>', L(0, 695, 10), s.P("Partner"), "fade")
s.J(draw("#kirana-a1", s.P("deliver") - 0.3, 0.4)); s.J(draw("#kirana-a2", s.P("to your door") - 0.3, 0.4))

# ---- 5: failure
s = sl.Scene("fail", 5); S.append(s)
s.E("t", "KIRANAKART", C(120, 120), 0.05, "fade", cls="hero q")
s.E("h", "It doesn't take off.", C(270, 64), 0.2, cls="down")
rows = [("Local", "Shops run out of stock"), ("they don't", "No inventory tracking"), ("and every", "Every order = a phone call")]
for n, (ph, tx) in enumerate(rows):
    s.E(f"r{n}", f'<span class="down hero">×</span>&nbsp;&nbsp;{tx}', L(520, 470 + n * 130, 72, "width:1300px;"), s.P(ph), "wipe")

# ---- 6: dropout deal
s = sl.Scene("deal", 6); S.append(s)
s.E("st", 'STANFORD<span id="deal-x" style="position:absolute;left:-2%;width:104%;top:46%;height:16px;background:var(--down);transform-origin:left center;"></span>', L(430, 150, 190, "width:1060px;text-align:center;"), 0.12, cls="hero")
s.J(f'tl.fromTo("#deal-x",{{scaleX:0}},{{scaleX:1,duration:0.35,ease:"power3.inOut"}},{s.P("don\'t go back")});')
s.E("c", 'Investor <span style="color:var(--ink)">CONTRARY</span> offers to back them', C(480, 60), s.P("An investor"), "fade", cls="q")
s.E("i", "…if they drop out.", C(580, 60), s.P("if they"), "fade")
s.E("d", "THEY TAKE THE DEAL.", C(740, 120), s.P("They take"), "pop", cls="hero up")

# ---- 7: Zepto is born
s = sl.Scene("born", 7); S.append(s)
t_new = s.P("New name")
s.E("y", "2021", C(130, 44), 0.12, "fade", cls="kick q")
s.E("k", "KIRANAKART", C(400, 170), 0.12, "fade", out=round(t_new - 0.1, 2), cls="hero q", attrs="data-layout-allow-overlap")
s.E("x", "CLOSED", L(610, 395, 170, "width:700px;text-align:center;border:12px solid var(--down);border-radius:20px;padding:6px 0;"), s.P("shut"), "stamp", out=round(t_new - 0.1, 2), cls="hero down", attrs="data-layout-allow-overlap data-layout-allow-occlusion")
s.E("z", "ZEPTO", C(270, 320), s.P("Zepto.") , "pop", cls="hero up")
s.E("p", "GROCERIES IN <span class='up'>10 MINUTES</span>", C(700, 84), s.P("groceries"), cls="hero")

# ---- 8: dark stores
s = sl.Scene("dark", 8); S.append(s)
s.E("k", "THE TRICK", C(90, 72), 0.12, cls="hero up")
s.E("h", "Zepto doesn't use shops.", C(190, 56), s.P("Zepto doesn't"), "fade")
blocks, cols, rows_ = [], 8, 3
dark = {(3, 1): "dk0", (0, 0): "dk1", (6, 0): "dk2", (1, 2): "dk3", (6, 2): "dk4"}
for r in range(rows_):
    for c in range(cols):
        x, y = 268 + c * 176, 20 + r * 130
        if (c, r) in dark:
            blocks.append(f'<rect x="{x}" y="{y}" width="150" height="104" rx="14" fill="#2a2740"/><rect id="dark-{dark[(c, r)]}" x="{x}" y="{y}" width="150" height="104" rx="14" fill="#8b3dff"/>')
        else:
            blocks.append(f'<rect x="{x}" y="{y}" width="150" height="104" rx="14" fill="#2a2740"/>')
s.E("g", f'<svg width="1920" height="420" viewBox="0 0 1920 420">{"".join(blocks)}</svg>', L(0, 310, 10), s.P("It builds"), "fade")
s.J(f'tl.fromTo("#dark-dk0",{{opacity:0,scale:0.6,transformOrigin:"50% 50%"}},{{opacity:1,scale:1,duration:0.4,ease:"expo.out"}},{s.P("called dark")});')
for n in range(1, 5):
    s.J(f'tl.fromTo("#dark-dk{n}",{{opacity:0,scale:0.6,transformOrigin:"50% 50%"}},{{opacity:1,scale:1,duration:0.4,ease:"expo.out"}},{round(s.P("packed") + 0.12 * n, 2)});')
s.E("lb", "DARK STORE", L(700, 715, 40, "width:520px;text-align:center;"), s.P("called dark"), "fade", out=round(s.P("No customers") - 0.1, 2), cls="kick up")
s.E("a", "No customers walk in.", C(790, 64), s.P("No customers"), cls="hero")
s.E("b", "Built only to pack orders fast.", C(890, 48), s.P("They only"), "fade", cls="q")

# ---- 9: 1.8 km radius
s = sl.Scene("radius", 9); S.append(s)
t_sw = round(s.P("The speed comes") - 0.1, 2)
svg = ('<svg width="900" height="900" viewBox="0 0 900 900">'
       '<circle id="radius-c" cx="450" cy="450" r="330" stroke="#8b3dff" stroke-width="6" fill="rgba(139,61,255,0.08)" pathLength="1" stroke-dasharray="1"/>'
       '<line id="radius-l" x1="450" y1="450" x2="780" y2="450" stroke="#a7a3b8" stroke-width="5" stroke-dasharray="14 12"/>'
       '<rect x="418" y="418" width="64" height="64" rx="12" fill="#8b3dff"/>'
       '<circle id="radius-r" cx="450" cy="450" r="20" fill="#ffffff"/></svg>')
s.E("m", svg, L(90, 90, 10), 0.12, "fade")
s.J(draw("#radius-c", s.P("covers a small"), 1.4)); s.J(fin("#radius-l", s.P("so the rider")))
s.J(f'tl.fromTo("#radius-r",{{x:0}},{{x:330,duration:2.6,ease:"power1.inOut"}},{s.P("so the rider")});')
s.E("st", "DARK STORE", L(390, 575, 30, "width:300px;text-align:center;"), 0.3, "fade", cls="kick q")
s.E("km", "1.8 km", L(1040, 250, 170, "width:780px;"), s.P("1.8"), "pop", out=t_sw, cls="hero")
s.E("mn", "in 10 minutes", L(1046, 450, 64, "width:780px;"), s.P("in ten minutes"), "fade", out=t_sw, cls="q")
s.E("sp", "= under 15 km/h", L(1040, 580, 92, "width:820px;"), s.P("means riding"), out=t_sw, cls="hero up")
s.E("w1", "Speed comes from", L(1040, 330, 60, "width:820px;"), s.P("The speed comes"), "fade", cls="q")
s.E("w2", "WHERE THE<br>STORE SITS", L(1040, 420, 120, "width:820px;"), s.P("where the store"), cls="hero up")
s.E("w3", "not how fast the rider goes", L(1046, 710, 48, "width:820px;"), s.P("not from"), "fade", cls="q")
s.E("src", "Source: Aadit Palicha, via Global Indian", "", s.P("Aadit"), "fade", out=t_sw, cls="src")

# ---- 10: narrow stock
s = sl.Scene("stock", 10); S.append(s)
s.E("h", "NARROW ON PURPOSE", C(190, 120), s.P("narrow"), cls="hero")
s.E("a", "A few thousand items people actually reorder", C(360, 50), s.P("just the few"), "fade", cls="q")
for n, w in enumerate(["Milk", "bread", "chips", "chargers"]):
    s.E(f"p{n}", f'<span class="pill hero">{w.upper()}</span>', L(96 + n * 435, 600, 52, "width:420px;text-align:center;white-space:nowrap;"), s.P(w), "pop")

# ---- 11: unicorn
s = sl.Scene("unicorn", 11); S.append(s)
s.E("b", "Backed by", C(120, 44), s.P("Zepto was backed"), "fade", cls="q")
s.E("yc", "Y COMBINATOR", C(180, 110), s.P("Y Combinator"), cls="hero")
s.E("d", "AUGUST 2023", C(430, 44), s.P("by August"), "fade", cls="kick q")
s.E("u", "UNICORN", C(490, 250), s.P("India's first"), "pop", cls="hero up")
s.E("c", "India's first unicorn of 2023", C(790, 52), s.P("unicorn of"), "fade")
s.E("src", "Source: Outlook Business", "", s.P("by August"), "fade", cls="src")

# ---- 12-13: valuation chart
s = sl.Scene("chart", 12, 13); S.append(s)
X = lambda m: round(260 + m / 26 * 1400)
Y = lambda v: round(880 - v / 8 * 620)
pts = [(0, 1.4), (10, 3.6), (12, 5.0), (26, 7.0)]
xy = [(X(m), Y(v)) for m, v in pts]
segs = "".join(f'<path id="chart-s{n}" d="M{xy[n][0]} {xy[n][1]} L{xy[n + 1][0]} {xy[n + 1][1]}" stroke="#8b3dff" stroke-width="10" stroke-linecap="round" fill="none" pathLength="1" stroke-dasharray="1"/>' for n in range(3))
dots = "".join(f'<circle id="chart-p{n}" cx="{x}" cy="{y}" r="18" fill="#8b3dff" stroke="#0b0a12" stroke-width="6"/>' for n, (x, y) in enumerate(xy))
grid = "".join(f'<line x1="260" x2="1700" y1="{Y(v)}" y2="{Y(v)}" stroke="#221f33" stroke-width="2"/><text x="236" y="{Y(v) + 10}" text-anchor="end" font-size="28" fill="#a7a3b8" font-family="Inter" font-weight="700">${v}B</text>' for v in (2, 4, 6, 8))
ticks = "".join(f'<text x="{X(m)}" y="940" text-anchor="middle" font-size="28" fill="#a7a3b8" font-family="Inter" font-weight="700">{lb}</text>' for m, lb in ((0, "Aug 2023"), (11, "Mid 2024"), (26, "Oct 2025")))
s.E("ch", f'<svg width="1920" height="1080" viewBox="0 0 1920 1080">{grid}<line x1="260" x2="1700" y1="880" y2="880" stroke="#a7a3b8" stroke-width="3"/>{ticks}{segs}{dots}</svg>', L(0, 0, 10), 0.12, "fade")
s.E("k", "ZEPTO VALUATION", L(260, 90, 40), 0.12, "fade", cls="kick q")
s.E("h", "The money came in waves", L(260, 150, 72), 0.3, cls="hero")
T = [0.5, s.P("In 2024"), s.P("A few months"), s.P("led a four", 13)]
TL = [0.6, s.P("three point six"), s.P("at five billion"), s.P("Zepto was now", 13)]
s.J(fin("#chart-p0", 0.5))
for n in range(3):
    s.J(draw(f"#chart-s{n}", T[n + 1], 0.9 if n != 1 else 0.5)); s.J(fin(f"#chart-p{n + 1}", round(T[n + 1] + (0.8 if n != 1 else 0.4), 2), 0.2))
s.E("l0", "$1B+", L(xy[0][0] + 6, xy[0][1] - 122, 52, "width:300px;"), TL[0], "fade", cls="hero q")
s.E("l1", "$3.6B", L(xy[1][0] + 40, xy[1][1] + 6, 64, "width:300px;"), TL[1], cls="hero")
s.E("l1b", "raised $665M", L(xy[1][0] + 44, xy[1][1] + 84, 30, "width:400px;font-weight:400;"), TL[1], "fade", cls="q")
s.E("l2", "$5B", L(xy[2][0] - 40, xy[2][1] - 130, 64, "width:300px;"), TL[2], cls="hero")
s.E("l2b", "raised $350M", L(xy[2][0] + 110, xy[2][1] - 98, 30, "width:400px;font-weight:400;"), TL[2], "fade", cls="q")
s.E("l3", "$7B", L(xy[3][0] - 330, xy[3][1] - 190, 150, "width:400px;text-align:right;"), TL[3], "pop", cls="hero up")
s.E("l3b", "Oct 2025 · raised $450M · led by CalPERS", L(xy[3][0] - 870, xy[3][1] - 30, 32, "width:820px;text-align:right;font-weight:400;"), s.P("a US pension", 13), "fade", cls="q")
s.E("src", "Sources: Money9 · Business Standard", "", 1.0, "fade", cls="src")
s.css.append("#chart-src{left:auto;right:96px;bottom:24px;}")

# ---- 14: scale counters
s = sl.Scene("scale", 14); S.append(s)
s.E("k", "FY26 · YEAR ENDING MARCH 2026", C(110, 40), s.P("In the year"), "fade", cls="kick q")
nums = [("twenty-two", "It ran", ("count", 22600, '(v)=>"₹"+(Math.round(v/100)*100).toLocaleString("en-IN")+" Cr"', 1.4), "₹0 Cr", "in revenue", "₹22,600 Cr", "revenue"),
        ("eleven hundred", "Nearly", ("count", 1139, '(v)=>Math.round(v).toLocaleString("en-IN")', 1.2), "0", "dark stores", "1,139", "dark stores"),
        ("forty-eight", None, ("count", 48, '(v)=>"~"+Math.round(v)+"M"', 1.2), "~0M", "people ordered at least once", "~48M", "people ordered")]
for n, (ph, nxt, anim, init, cap, rv, rc) in enumerate(nums):
    o = round(s.P(nxt) - 0.25, 2) if nxt else None
    s.E(f"n{n}", init, C(300, 230), s.P(ph), anim, out=o, cls="hero up tnum")
    s.E(f"c{n}", cap, C(570, 60), round(s.P(ph) + 0.3, 2), "fade", out=o)
    if o:
        s.E(f"r{n}", f'<div class="hero" style="font-size:64px">{rv}</div><div class="q" style="font-size:32px;margin-top:8px">{rc}</div>', L(200 + n * 520, 800, 10, "width:480px;text-align:center;"), round(o + 0.15, 2), "fade")
s.E("r2", '<div class="hero" style="font-size:64px">~48M</div><div class="q" style="font-size:32px;margin-top:8px">people ordered</div>', L(1240, 800, 10, "width:480px;text-align:center;"), round(s.P("at least once") + 0.6, 2), "fade")
s.E("src", "Sources: Free Press Journal · 5paisa", "", s.P("twenty-two"), "fade", cls="src")
s.css.append("#scale-src{bottom:24px;}")

# ---- 15: orders a day
s = sl.Scene("orders", 15); S.append(s)
s.E("k", "LAST QUARTER OF FY26", C(150, 40), 0.12, "fade", cls="kick q")
s.E("n", "0 LAKH+", C(300, 250), s.P("twenty-three"), ("count", 23, '(v)=>Math.round(v)+" LAKH+"', 1.0), cls="hero up tnum")
s.E("c", "orders a day", C(600, 72), round(s.P("twenty-three") + 0.25, 2), "fade")
s.E("c2", "(2.3 million)", C(710, 44), round(s.P("twenty-three") + 0.7, 2), "fade", cls="q")

# ---- 16: question
s = sl.Scene("why", 16); S.append(s)
s.E("q", "SO WHY ISN'T IT <span class='down'>PUBLIC?</span>", C(450, 130), 0.1, cls="hero")

# ---- 17: revenue is not profit
s = sl.Scene("costs", 17); S.append(s)
s.E("h", "REVENUE <span class='down'>IS NOT</span> PROFIT", C(130, 120), s.P("revenue isn't"), cls="hero")
cols3 = [("You pay rent", "RENT", "stores in prime locations"), ("you pay riders", "RIDERS", "on every order"), ("you pay discounts", "DISCOUNTS", "to win customers")]
for n, (ph, a, b) in enumerate(cols3):
    s.E(f"c{n}", f'<div class="hero" style="font-size:88px">{a}</div><div class="q" style="font-size:36px;margin-top:14px;font-weight:400">{b}</div>', L(120 + n * 570, 430, 10, "width:540px;text-align:center;"), s.P(ph), "pop")
s.E("v", "fighting", C(720, 40), s.P("from Blinkit"), "fade", cls="q")
s.E("r", "BLINKIT · INSTAMART · AMAZON", C(780, 76), s.P("Blinkit"), "wipe", cls="hero")

# ---- 18: losses
s = sl.Scene("loss", 18); S.append(s)
s.E("k", "THE YEAR BEFORE (FY25) · NET LOSS", C(160, 40), 0.12, "fade", cls="kick q")
s.E("n", "₹0 Cr", C(310, 240), s.P("three thousand"), ("count", 3367, '(v)=>"₹"+Math.round(v).toLocaleString("en-IN")+" Cr"', 1.4), cls="hero down tnum")
s.E("c", "Burning cash every quarter", C(640, 64), s.P("It was burning"), "fade")
s.E("src", "Source: Free Press Journal", "", s.P("three thousand"), "fade", cls="src")

# ---- 19: IPO plan timeline
s = sl.Scene("ipo", 19); S.append(s)
s.E("k", "THE IPO PLAN", C(140, 72), 0.12, cls="hero")
xs = [360, 960, 1560]
ln = (f'<svg width="1920" height="120" viewBox="0 0 1920 120"><path id="ipo-l1" d="M{xs[0]} 60 H{xs[1]}" stroke="#8b3dff" stroke-width="8" pathLength="1" stroke-dasharray="1"/>'
      f'<path id="ipo-l2" d="M{xs[1]} 60 H{xs[2]}" stroke="#8b3dff" stroke-width="8" pathLength="1" stroke-dasharray="1" /></svg>')
s.E("ln", ln, L(0, 440, 10), 0.12, "fade")
tp = [s.P("filed"), s.P("got approval"), s.P("The plan")]
s.J(draw("#ipo-l1", round(tp[1] - 0.5, 2), 0.6)); s.J(draw("#ipo-l2", round(tp[2] - 0.5, 2), 0.6))
for n, (a, b) in enumerate([("DEC 2025", "IPO filed"), ("MAY 2026", "SEBI approval"), ("JULY 2026", "Planned listing")]):
    s.E(f"d{n}", "", L(xs[n] - 26, 474, 10, "width:52px;height:52px;border-radius:50%;background:var(--up);"), tp[n], "pop")
    s.E(f"a{n}", a, L(xs[n] - 260, 570, 44, "width:520px;text-align:center;"), tp[n], "fade", cls="kick q")
    s.E(f"b{n}", b, L(xs[n] - 260, 635, 64, "width:520px;text-align:center;"), tp[n], cls="hero")
s.E("src", "Source: Kotak Neo", "", tp[0], "fade", cls="src")

# ---- 20: pure quick commerce
s = sl.Scene("push", 20); S.append(s)
s.E("h", "Fund managers pushed back", C(120, 84), 0.12, cls="hero")
card = "width:700px;height:420px;flex-direction:column;gap:26px;justify-content:flex-start;padding-top:56px;"
bar = lambda t, c: f'<div style="width:520px;padding:22px 0;border-radius:16px;background:{c};font-size:40px;color:#fff">{t}</div>'
s.E("z", f'<div class="hero" style="font-size:72px">ZEPTO</div>{bar("Quick commerce", "#8b3dff")}', L(190, 330, 10, card), s.P("Zepto only"), cls="box")
s.E("o", f'<div class="hero" style="font-size:56px">SWIGGY · ETERNAL</div>{bar("Quick commerce", "#8b3dff")}{bar("Food delivery", "#3d7bff")}', L(1030, 330, 10, card), s.P("like Swiggy"), cls="box")
s.E("nf", "No food delivery", L(280, 608, 40, "width:520px;height:92px;border:4px dashed var(--quiet);border-radius:16px;display:flex;align-items:center;justify-content:center;"), s.P("It doesn't have"), "fade", cls="q")
s.E("n", "Nothing to fall back on", L(190, 800, 52, "width:700px;text-align:center;"), s.P("to fall back"), "fade", cls="down")
s.E("src", "Source: The Week", "", s.P("Zepto only"), "fade", cls="src")
s.css.append("#push-src{bottom:24px;}")

# ---- 21: the drop
s = sl.Scene("drop", 21); S.append(s)
X2 = lambda m: round(260 + m / 35 * 1400)
p2 = [(0, 1.4), (10, 3.6), (12, 5.0), (26, 7.0), (35, 4.5)]
q = [(X2(m), Y(v)) for m, v in p2]
old = " ".join(f"{'M' if n == 0 else 'L'}{x} {y}" for n, (x, y) in enumerate(q[:4]))
grid2 = "".join(f'<line x1="260" x2="1700" y1="{Y(v)}" y2="{Y(v)}" stroke="#221f33" stroke-width="2"/><text x="236" y="{Y(v) + 10}" text-anchor="end" font-size="28" fill="#a7a3b8" font-family="Inter" font-weight="700">${v}B</text>' for v in (2, 4, 6, 8))
ticks2 = "".join(f'<text x="{X2(m)}" y="940" text-anchor="middle" font-size="28" fill="#a7a3b8" font-family="Inter" font-weight="700">{lb}</text>' for m, lb in ((0, "Aug 2023"), (26, "Oct 2025"), (35, "Jul 2026")))
s.E("ch", f'<svg width="1920" height="1080" viewBox="0 0 1920 1080">{grid2}<line x1="260" x2="1700" y1="880" y2="880" stroke="#a7a3b8" stroke-width="3"/>{ticks2}'
    f'<path d="{old}" stroke="#8b3dff" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
    f'<path id="drop-s" d="M{q[3][0]} {q[3][1]} L{q[4][0]} {q[4][1]}" stroke="#ff3b47" stroke-width="12" stroke-linecap="round" fill="none" pathLength="1" stroke-dasharray="1"/>'
    f'<circle cx="{q[3][0]}" cy="{q[3][1]}" r="18" fill="#8b3dff" stroke="#0b0a12" stroke-width="6"/><circle id="drop-p" cx="{q[4][0]}" cy="{q[4][1]}" r="20" fill="#ff3b47" stroke="#0b0a12" stroke-width="6"/></svg>', L(0, 0, 10), 0.12, "fade")
s.E("k", "JULY 2026", L(260, 66, 40), 0.12, "fade", cls="kick q")
s.E("h", "Zepto pulls the brakes", L(260, 116, 72), s.P("Zepto pulled"), cls="hero")
s.E("r", "Raised ~₹1,000 Cr privately instead of listing", L(260, 204, 36, "font-weight:400;"), s.P("it raised"), "fade", cls="q")
s.E("l7", "$7B", L(q[3][0] - 150, q[3][1] - 110, 64, "width:300px;text-align:center;"), 0.4, "fade", cls="hero up")
td = s.P("at a valuation")
s.J(draw("#drop-s", td, 1.0)); s.J(fin("#drop-p", round(td + 0.9, 2), 0.2))
s.E("l4", "$4.5B", L(q[4][0] - 420, q[4][1] + 40, 130, "width:480px;text-align:right;"), s.P("four and a half"), "pop", cls="hero down")
s.E("t", "▼ about a third below its peak", L(q[4][0] - 820, q[4][1] + 200, 44, "width:880px;text-align:right;"), s.P("That's about"), "fade", cls="down")
s.E("src", "Sources: YourStory · 5paisa", "", s.P("it raised"), "fade", cls="src")
s.css.append("#drop-src{bottom:24px;}")

# ---- 22: postponed
s = sl.Scene("post", 22); S.append(s)
s.E("i", "IPO", C(150, 240), 0.1, "fade", cls="hero q", attrs="data-layout-allow-overlap")
s.E("x", "POSTPONED", L(410, 440, 170, "width:1100px;text-align:center;border:12px solid var(--down);border-radius:20px;padding:6px 0;background:var(--ground);"), s.P("pushed back"), "stamp", cls="hero down", attrs="data-layout-allow-overlap data-layout-allow-occlusion")
s.E("c", "by 2 to 3 quarters", C(770, 64), s.P("two to three"), "fade")

# ---- 23: not failing
s = sl.Scene("alive", 23); S.append(s)
s.E("k", "WHAT MOST PEOPLE MISS", C(130, 40), 0.12, "fade", cls="kick q")
s.E("h", "ZEPTO ISN'T <span class='up'>FAILING.</span>", C(210, 120), s.P("Zepto isn't"), cls="hero")
for n, (ph, tx) in enumerate([("Its cash burn", "Cash burn came down"), ("it says it has", "No debt, the company says"), ("and it still", "Thousands of crores in the bank")]):
    s.E(f"r{n}", f'<span style="display:inline-block;width:34px;height:34px;border-radius:50%;background:var(--up);margin-right:36px;vertical-align:middle"></span>{tx}', L(470, 470 + n * 125, 64, "width:1300px;"), s.P(ph), "wipe")
s.E("src", "Sources: Outlook Business · Free Press Journal", "", s.P("Its cash burn"), "fade", cls="src")

# ---- 24: two kinds of money
s = sl.Scene("money", 24); S.append(s)
s.E("k", "TWO KINDS OF MONEY", C(130, 72), s.P("the gap"), cls="hero")
s.E("dv", "", L(958, 330, 10, "width:4px;height:520px;background:#2a2740;"), s.P("Private"), "fade")
s.E("a1", "PRIVATE INVESTORS", L(100, 360, 44, "width:800px;text-align:center;"), s.P("Private"), "fade", cls="kick q")
s.E("a2", "pay for what it", L(100, 470, 56, "width:800px;text-align:center;"), s.P("pay for what a"), "fade")
s.E("a3", "COULD BECOME", L(100, 560, 100, "width:800px;text-align:center;"), s.P("could become"), "pop", cls="hero up")
s.E("b1", "PUBLIC MARKETS", L(1020, 360, 44, "width:800px;text-align:center;"), s.P("Public"), "fade", cls="kick q")
s.E("b2", "pay for what it", L(1020, 470, 56, "width:800px;text-align:center;"), s.P("pay for what it earns"), "fade")
s.E("b3", "EARNS", L(1020, 560, 100, "width:800px;text-align:center;"), s.P("earns"), "pop", cls="hero down")

# ---- 25: proved / to prove
s = sl.Scene("prove", 25); S.append(s)
s.E("a1", "PROVED", C(170, 48), s.P("proved"), "fade", cls="kick up")
s.E("a2", "India wants groceries in 10 minutes", C(250, 84), s.P("that Indians"), cls="hero")
s.E("b1", "STILL TO PROVE", C(560, 48), s.P("What it still"), "fade", cls="kick down")
s.E("b2", "10 minutes can make money", C(640, 84), s.P("is that ten"), cls="hero")

# ---- 26: mid-twenties
s = sl.Scene("young", 26); S.append(s)
s.E("k", "THE TWO FOUNDERS", C(330, 44), 0.12, "fade", cls="kick q")
s.E("h", "Still in their <span class='up'>mid-twenties.</span>", C(430, 120), s.P("are still"), cls="hero")

# ---- 27: the bet
s = sl.Scene("bet", 27); S.append(s)
s.E("k", "IF ZEPTO LISTS IN 2027", C(130, 48), 0.12, "fade", cls="kick q")
s.E("a", "THE CHEAPEST<br>IT EVER LOOKS", L(60, 330, 88, "width:800px;text-align:center;"), s.P("cheapest"), "pop", cls="hero up")
s.E("or", "or", C(420, 64), s.P("Or the most"), "fade", cls="q")
s.E("b", "THE MOST<br>EXPENSIVE", L(1080, 330, 88, "width:760px;text-align:center;"), s.P("Or the most"), "pop", cls="hero down")
s.E("c", "Comment which one you'd bet on", C(760, 64), s.P("Tell me"), "wipe")

# ---- 28: end card
s = sl.Scene("endcard", 28); S.append(s)
s.E("s", "SUBSCRIBE", C(300, 220), s.P("subscribe"), "pop", cls="hero up")
s.E("n", "Next breakdown: <span style='color:var(--ink)'>BLINKIT</span>", C(620, 72), s.P("I'm doing"), cls="q")

sl.write_project(os.path.join(HERE, "project"), S, first_host=("coldopen", "compositions/coldopen.html", sl.sstart(2)), audio_dur=232.87)
