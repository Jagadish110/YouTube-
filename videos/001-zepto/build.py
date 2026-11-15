"""Video 001: How Zepto Got So Big So Fast. Scene specs timed to vo_marks.json.

Run from this folder:  python3 build.py
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
import scenelib as sl
from scenelib import C, L, draw, fin

HERE = os.path.dirname(os.path.abspath(__file__))
sl.setup(os.path.join(HERE, "vo_marks.json"), 234.5)
# v2 look: Zepto brand colours (deep purple + pink). Growth = Zepto pink, drops = amber.
sl.theme(
    ground="#2E0854", ink="#ffffff", quiet="#CDBBEA", up="#FF4F9A", down="#FFB238",
    panel="#3D0C6E", line="#4A1C80",
    head="'Outfit', 'Inter', sans-serif", head_weight=800,
    body="'Plus Jakarta Sans', 'Inter', sans-serif",
    fonts=[("Outfit", 800, "assets/fonts/outfit-latin-800-normal.woff2"),
           ("Plus Jakarta Sans", 500, "assets/fonts/plus-jakarta-sans-latin-500-normal.woff2"),
           ("Plus Jakarta Sans", 700, "assets/fonts/plus-jakarta-sans-latin-700-normal.woff2")],
    bg="background-image: radial-gradient(circle at 85% 10%, rgba(255,79,154,0.22) 0, rgba(255,79,154,0) 40%), radial-gradient(circle at 8% 95%, rgba(127,209,255,0.14) 0, rgba(127,209,255,0) 45%);",
)

S = []

# ---- 2: the kids
s = sl.Scene("kids", 2); S.append(s)
s.E("yr", "2020", C(110, 150), 0.1, cls="hero up")
s.E("n1", "AADIT PALICHA", L(110, 390, 68, "width:850px;text-align:center;white-space:nowrap;"), s.P("Aadit"), cls="hero")
s.E("n2", "KAIVALYA VOHRA", L(960, 390, 68, "width:850px;text-align:center;white-space:nowrap;"), s.P("Kaivalya"), cls="hero")
s.E("fr", "Childhood friends · grew up in Dubai", C(520, 48), s.P("childhood"), "fade", cls="q")
svg = ('<svg width="1920" height="300" viewBox="0 0 1920 300"><circle id="kids-d1" cx="460" cy="110" r="18" fill="#CDBBEA"/>'
       '<path id="kids-ln" d="M478 110 H1442" stroke="#FF4F9A" stroke-width="8" fill="none" pathLength="1" stroke-dasharray="1"/>'
       '<circle id="kids-d2" cx="1460" cy="110" r="22" fill="#FF4F9A"/></svg>')
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
s.E("ar", '<svg width="1920" height="60" viewBox="0 0 1920 60"><path id="kirana-a1" d="M622 30 H728" stroke="#CDBBEA" stroke-width="8" pathLength="1" stroke-dasharray="1"/><path id="kirana-a2" d="M1192 30 H1298" stroke="#CDBBEA" stroke-width="8" pathLength="1" stroke-dasharray="1"/></svg>', L(0, 695, 10), s.P("Partner"), "fade")
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
            blocks.append(f'<rect x="{x}" y="{y}" width="150" height="104" rx="14" fill="#4A1C80"/><rect id="dark-{dark[(c, r)]}" x="{x}" y="{y}" width="150" height="104" rx="14" fill="#FF4F9A"/>')
        else:
            blocks.append(f'<rect x="{x}" y="{y}" width="150" height="104" rx="14" fill="#4A1C80"/>')
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
       '<circle id="radius-c" cx="450" cy="450" r="330" stroke="#FF4F9A" stroke-width="6" fill="rgba(255,79,154,0.10)" pathLength="1" stroke-dasharray="1"/>'
       '<line id="radius-l" x1="450" y1="450" x2="780" y2="450" stroke="#CDBBEA" stroke-width="5" stroke-dasharray="14 12"/>'
       '<rect x="418" y="418" width="64" height="64" rx="12" fill="#FF4F9A"/>'
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
segs = "".join(f'<path id="chart-s{n}" d="M{xy[n][0]} {xy[n][1]} L{xy[n + 1][0]} {xy[n + 1][1]}" stroke="#FF4F9A" stroke-width="10" stroke-linecap="round" fill="none" pathLength="1" stroke-dasharray="1"/>' for n in range(3))
dots = "".join(f'<circle id="chart-p{n}" cx="{x}" cy="{y}" r="18" fill="#FF4F9A" stroke="#2E0854" stroke-width="6"/>' for n, (x, y) in enumerate(xy))
grid = "".join(f'<line x1="260" x2="1700" y1="{Y(v)}" y2="{Y(v)}" stroke="#3F1470" stroke-width="2"/><text x="236" y="{Y(v) + 10}" text-anchor="end" font-size="28" fill="#CDBBEA" font-family="Plus Jakarta Sans" font-weight="700">${v}B</text>' for v in (2, 4, 6, 8))
ticks = "".join(f'<text x="{X(m)}" y="940" text-anchor="middle" font-size="28" fill="#CDBBEA" font-family="Plus Jakarta Sans" font-weight="700">{lb}</text>' for m, lb in ((0, "Aug 2023"), (11, "Mid 2024"), (26, "Oct 2025")))
s.E("ch", f'<svg width="1920" height="1080" viewBox="0 0 1920 1080">{grid}<line x1="260" x2="1700" y1="880" y2="880" stroke="#CDBBEA" stroke-width="3"/>{ticks}{segs}{dots}</svg>', L(0, 0, 10), 0.12, "fade")
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
ln = (f'<svg width="1920" height="120" viewBox="0 0 1920 120"><path id="ipo-l1" d="M{xs[0]} 60 H{xs[1]}" stroke="#FF4F9A" stroke-width="8" pathLength="1" stroke-dasharray="1"/>'
      f'<path id="ipo-l2" d="M{xs[1]} 60 H{xs[2]}" stroke="#FF4F9A" stroke-width="8" pathLength="1" stroke-dasharray="1" /></svg>')
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
s.E("z", f'<div class="hero" style="font-size:72px">ZEPTO</div>{bar("Quick commerce", "#FF4F9A")}', L(190, 330, 10, card), s.P("Zepto only"), cls="box")
s.E("o", f'<div class="hero" style="font-size:56px">SWIGGY · ETERNAL</div>{bar("Quick commerce", "#FF4F9A")}{bar("Food delivery", "#7FD1FF")}', L(1030, 330, 10, card), s.P("like Swiggy"), cls="box")
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
grid2 = "".join(f'<line x1="260" x2="1700" y1="{Y(v)}" y2="{Y(v)}" stroke="#3F1470" stroke-width="2"/><text x="236" y="{Y(v) + 10}" text-anchor="end" font-size="28" fill="#CDBBEA" font-family="Plus Jakarta Sans" font-weight="700">${v}B</text>' for v in (2, 4, 6, 8))
ticks2 = "".join(f'<text x="{X2(m)}" y="940" text-anchor="middle" font-size="28" fill="#CDBBEA" font-family="Plus Jakarta Sans" font-weight="700">{lb}</text>' for m, lb in ((0, "Aug 2023"), (26, "Oct 2025"), (35, "Jul 2026")))
s.E("ch", f'<svg width="1920" height="1080" viewBox="0 0 1920 1080">{grid2}<line x1="260" x2="1700" y1="880" y2="880" stroke="#CDBBEA" stroke-width="3"/>{ticks2}'
    f'<path d="{old}" stroke="#FF4F9A" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
    f'<path id="drop-s" d="M{q[3][0]} {q[3][1]} L{q[4][0]} {q[4][1]}" stroke="#FFB238" stroke-width="12" stroke-linecap="round" fill="none" pathLength="1" stroke-dasharray="1"/>'
    f'<circle cx="{q[3][0]}" cy="{q[3][1]}" r="18" fill="#FF4F9A" stroke="#2E0854" stroke-width="6"/><circle id="drop-p" cx="{q[4][0]}" cy="{q[4][1]}" r="20" fill="#FFB238" stroke="#2E0854" stroke-width="6"/></svg>', L(0, 0, 10), 0.12, "fade")
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
s.E("dv", "", L(958, 330, 10, "width:4px;height:520px;background:#4A1C80;"), s.P("Private"), "fade")
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


# ======================= v3: drawn illustrations in every scene =======================
# Flat SVG drawings in Zepto colours, placed in each scene's empty space. No faces, no logos.
ZP, ZA, ZB, ZK, ZW, ZL, ZPAN = "#FF4F9A", "#FFB238", "#7FD1FF", "#14002B", "#ffffff", "#CDBBEA", "#3D0C6E"
SC = {s_.name: s_ for s_ in S}


def svg(w, h, body, vb=None):
    return f'<svg width="{w}" height="{h}" viewBox="{vb or f"0 0 {w} {h}"}">{body}</svg>'


def bounce(s, sel, t, dy=40):
    s.J(f'tl.fromTo("{sel}",{{y:{dy}}},{{y:0,duration:0.55,ease:"back.out(1.8)"}},{t});')


def pops(s, ids, t0, step=0.08):
    for n, i in enumerate(ids):
        s.J(f'tl.fromTo("#{i}",{{opacity:0,scale:0.4,transformOrigin:"50% 50%"}},{{opacity:1,scale:1,duration:0.35,ease:"back.out(2)"}},{round(t0 + n * step, 2)});')


def scooter_svg(sid, body=ZP, box=ZW, w=460):
    return svg(w, round(w * 320 / 460), f'<g id="{sid}"><circle cx="110" cy="240" r="48" fill="{ZK}" stroke="{ZL}" stroke-width="6"/><circle cx="370" cy="240" r="48" fill="{ZK}" stroke="{ZL}" stroke-width="6"/>'
               f'<path d="M64 232 Q74 160 160 160 L310 160 Q338 160 356 140 L392 84 L414 92 L384 160 Q374 232 318 232 Z" fill="{body}"/>'
               f'<rect x="96" y="40" width="160" height="128" rx="18" fill="{box}" stroke="{ZK}" stroke-width="8"/>'
               f'<path d="M262 160 L286 74 Q293 44 322 44 L330 44 L316 160 Z" fill="{ZL}"/><circle cx="314" cy="22" r="32" fill="{ZA}"/></g>', "0 -20 460 320")


# kids: plane flies Dubai -> Stanford, cap over Stanford
s = SC["kids"]
plane = svg(120, 80, f'<path d="M10 40 L110 30 Q120 40 110 50 L10 40 Z" fill="{ZW}"/><path d="M50 38 L30 6 L48 6 L74 36 Z M50 42 L30 74 L48 74 L74 44 Z" fill="{ZW}"/><path d="M12 40 L4 22 L16 22 L26 38 Z" fill="{ZW}"/>')
s.E("pl", plane, L(470, 728, 10), s.P("They've"), "fade")
s.J(f'tl.fromTo("#kids-pl",{{x:0}},{{x:880,duration:1.4,ease:"power2.inOut"}},{round(s.P("They\'ve") + 0.2, 2)});')
s.J(f'tl.to("#kids-pl",{{opacity:0,duration:0.2}},{round(s.P("They\'ve") + 1.6, 2)});')
cap = svg(200, 130, f'<path d="M100 10 L190 50 L100 90 L10 50 Z" fill="{ZP}" stroke="{ZK}" stroke-width="6"/><path d="M50 70 L50 110 Q100 130 150 110 L150 70" fill="{ZPAN}" stroke="{ZK}" stroke-width="6"/><path d="M170 58 L170 100" stroke="{ZA}" stroke-width="6"/><circle cx="170" cy="104" r="9" fill="{ZA}"/>')
s.E("cap", cap, L(1360, 600, 10), s.P("Stanford"), "pop")

# pandemic: house + phone with no delivery
s = SC["pandemic"]
house = (f'<g id="pandemic-h"><path d="M60 120 L200 20 L340 120 Z" fill="{ZP}"/><rect x="90" y="120" width="220" height="150" fill="{ZW}"/>'
         f'<rect x="170" y="180" width="60" height="90" rx="6" fill="{ZK}"/><rect x="110" y="150" width="44" height="40" rx="6" fill="{ZB}"/><rect x="246" y="150" width="44" height="40" rx="6" fill="{ZB}"/>'
         f'<rect x="100" y="200" width="200" height="16" rx="6" fill="{ZA}" transform="rotate(-8 200 208)"/><rect x="100" y="200" width="200" height="16" rx="6" fill="{ZA}" transform="rotate(8 200 208)"/></g>'
         f'<g id="pandemic-p" transform="translate(520 0)"><rect x="0" y="10" width="150" height="260" rx="26" fill="{ZK}" stroke="{ZL}" stroke-width="6"/><rect x="14" y="36" width="122" height="206" rx="16" fill="{ZPAN}"/>'
         f'<rect x="30" y="60" width="90" height="34" rx="8" fill="{ZL}" opacity=".5"/><rect x="30" y="104" width="90" height="34" rx="8" fill="{ZL}" opacity=".5"/>'
         f'<circle cx="75" cy="190" r="34" fill="none" stroke="{ZA}" stroke-width="10"/><path d="M52 167 L98 213" stroke="{ZA}" stroke-width="10"/></g>'
         f'<g id="pandemic-b" transform="translate(760 70)"><path d="M10 60 H170 L150 200 H30 Z" fill="{ZL}" opacity=".85"/><path d="M50 60 Q50 10 90 10 Q130 10 130 60" stroke="{ZL}" stroke-width="10" fill="none"/>'
         f'<text x="90" y="160" text-anchor="middle" font-family="Outfit" font-weight="800" font-size="60" fill="{ZPAN}">0</text></g>')
s.E("ill", svg(960, 280, house), L(480, 790, 10), s.P("and they can't"), "fade")
pops(s, ["pandemic-h", "pandemic-p", "pandemic-b"], s.P("and they can't"), 0.15)

# kirana: shop, scooter, home icons above the three boxes
s = SC["kirana"]
shop = svg(220, 190, f'<rect x="20" y="70" width="180" height="110" fill="{ZW}"/>' + "".join(f'<rect x="{20 + n * 36}" y="40" width="36" height="44" fill="{ZP if n % 2 == 0 else ZW}"/>' for n in range(5)) + f'<rect x="10" y="30" width="200" height="14" rx="6" fill="{ZK}"/><rect x="84" y="110" width="52" height="70" fill="{ZPAN}"/><rect x="34" y="100" width="36" height="30" rx="4" fill="{ZB}"/><rect x="150" y="100" width="36" height="30" rx="4" fill="{ZB}"/>')
home = svg(220, 190, f'<path d="M20 90 L110 20 L200 90 Z" fill="{ZP}"/><rect x="40" y="90" width="140" height="90" fill="{ZW}"/><rect x="92" y="120" width="36" height="60" rx="4" fill="{ZK}"/><circle cx="160" cy="40" r="22" fill="{ZA}"/>')
s.E("i1", shop, L(280, 420, 10), s.P("Partner"), "pop")
s.E("i2", scooter_svg("kirana-sc", w=240), L(840, 425, 10), s.P("deliver"), "pop")
s.E("i3", home, L(1420, 420, 10), s.P("to your door"), "pop")

# fail: broken phone on the left
s = SC["fail"]
broken = (f'<rect x="20" y="10" width="280" height="420" rx="44" fill="{ZK}" stroke="{ZL}" stroke-width="8"/><rect x="42" y="44" width="236" height="352" rx="28" fill="{ZPAN}"/>'
          f'<path d="M80 60 L150 170 L120 200 L200 300 L170 330 L240 390" stroke="{ZW}" stroke-width="6" fill="none"/>'
          f'<rect x="70" y="250" width="180" height="90" rx="18" fill="{ZA}"/><text x="160" y="310" text-anchor="middle" font-family="Outfit" font-weight="800" font-size="48" fill="{ZK}">ERROR</text>')
s.E("ph", svg(320, 440, broken), L(110, 450, 10), s.P("Local"), "pop")
s.J(f'tl.to("#fail-ph",{{rotation:4,duration:0.07,yoyo:true,repeat:5}},{round(s.P("Local") + 0.4, 2)});')

# deal: graduation cap crossed out (left) + signed term sheet (right)
s = SC["deal"]
s.E("cap", svg(260, 200, f'<path d="M130 20 L250 74 L130 128 L10 74 Z" fill="{ZL}" stroke="{ZK}" stroke-width="6"/><path d="M60 100 L60 150 Q130 176 200 150 L200 100" fill="{ZPAN}" stroke="{ZK}" stroke-width="6"/><path d="M20 180 L240 20" stroke="{ZA}" stroke-width="16" stroke-linecap="round"/>'), L(80, 420, 10), s.P("don't go back"), "pop")
doc = (f'<rect x="10" y="10" width="240" height="300" rx="16" fill="{ZW}"/>' + "".join(f'<rect x="40" y="{50 + n * 34}" width="{180 - (n % 3) * 30}" height="14" rx="7" fill="#d6cbe8"/>' for n in range(5)) +
       f'<path id="deal-sig" d="M40 260 Q70 220 90 262 T150 250 T210 240" stroke="{ZP}" stroke-width="8" fill="none" stroke-linecap="round" pathLength="1" stroke-dasharray="1"/>')
s.E("doc", svg(260, 320, doc), L(1590, 400, 10), s.P("An investor"), "pop")
s.J(draw("#deal-sig", s.P("They take"), 0.6))

# born: grocery bag (left) + stopwatch (right)
s = SC["born"]
bag = (f'<path d="M60 60 Q60 10 110 10 Q160 10 160 60" stroke="{ZW}" stroke-width="12" fill="none"/><path d="M20 60 H200 L186 300 H34 Z" fill="{ZW}"/>'
       f'<rect x="40" y="20" width="44" height="60" rx="8" fill="{ZB}"/><rect x="120" y="10" width="50" height="70" rx="8" fill="{ZA}"/><rect x="60" y="140" width="100" height="80" rx="14" fill="{ZP}"/>')
s.E("bag", svg(220, 310, bag), L(140, 300, 10), s.P("Zepto."), "pop")
watch = (f'<rect x="100" y="0" width="40" height="30" rx="6" fill="{ZW}"/><circle cx="120" cy="150" r="110" fill="{ZW}"/>'
         f'<circle id="born-arc" cx="120" cy="150" r="86" fill="none" stroke="{ZP}" stroke-width="20" pathLength="1" stroke-dasharray="1" transform="rotate(-90 120 150)"/>'
         f'<text x="120" y="172" text-anchor="middle" font-family="Outfit" font-weight="800" font-size="66" fill="{ZK}">10</text>')
s.E("w", svg(240, 270, watch), L(1560, 300, 10), s.P("groceries"), "pop")
s.J(draw("#born-arc", s.P("groceries"), 1.2))

# stock: product drawings under the four pills
s = SC["stock"]
prods = [
    f'<path d="M40 40 L60 10 H120 L140 40 V200 H40 Z" fill="{ZW}"/><path d="M40 40 H140" stroke="{ZK}" stroke-width="6"/><rect x="40" y="90" width="100" height="60" fill="{ZB}"/>',
    f'<path d="M20 120 Q20 40 90 40 Q160 40 160 120 V190 H20 Z" fill="{ZA}"/><path d="M50 90 L60 160 M90 80 V170 M130 90 L120 160" stroke="#c98a1f" stroke-width="8" stroke-linecap="round"/>',
    f'<path d="M30 20 L150 20 L140 40 L150 190 L30 190 L40 40 Z" fill="{ZP}"/><circle cx="90" cy="110" r="36" fill="{ZA}"/><path d="M30 20 L150 20" stroke="{ZW}" stroke-width="8" stroke-dasharray="10 8"/>',
    f'<rect x="50" y="60" width="80" height="100" rx="16" fill="{ZW}"/><path d="M72 60 V20 M108 60 V20" stroke="{ZW}" stroke-width="12" stroke-linecap="round"/><path d="M90 160 V200 Q90 210 110 210 H160" stroke="{ZW}" stroke-width="10" fill="none"/><path d="M90 92 L80 112 H100 L88 132" stroke="{ZK}" stroke-width="6" fill="none"/>',
]
for n, (w, body) in enumerate(zip(["Milk", "bread", "chips", "chargers"], prods)):
    s.E(f"pr{n}", svg(180, 220, body), L(96 + n * 435 + 120, 720, 10), round(s.P(w) + 0.15, 2), "pop")

# unicorn: horn + sparkles
s = SC["unicorn"]
horn = (f'<path d="M100 300 L150 20 L200 300 Z" fill="{ZW}"/><path d="M112 250 L188 230 M122 190 L180 172 M134 130 L170 116 M144 76 L162 68" stroke="{ZP}" stroke-width="10" stroke-linecap="round"/>'
        + "".join(f'<path id="unicorn-st{n}" d="M{x} {y - 22} L{x + 7} {y - 7} L{x + 22} {y} L{x + 7} {y + 7} L{x} {y + 22} L{x - 7} {y + 7} L{x - 22} {y} L{x - 7} {y - 7} Z" fill="{ZA}"/>' for n, (x, y) in enumerate([(40, 80), (260, 60), (250, 220), (30, 240)])))
s.E("hn", svg(300, 320, horn), L(1560, 90, 10), s.P("India's first"), "pop")
pops(s, [f"unicorn-st{n}" for n in range(4)], round(s.P("India's first") + 0.3, 2), 0.1)
s.E("hn2", svg(300, 320, horn.replace("unicorn-st", "unicorn-su")), L(60, 90, 10, "transform:scaleX(-1);"), s.P("India's first"), "pop")

# scale: store (left) + rider (right)
s = SC["scale"]
store = (f'<rect x="20" y="90" width="260" height="190" rx="8" fill="{ZW}"/>' + "".join(f'<rect x="{20 + n * 52}" y="50" width="52" height="56" fill="{ZP if n % 2 == 0 else ZW}"/>' for n in range(5)) +
         f'<rect x="10" y="40" width="280" height="16" rx="8" fill="{ZK}"/><rect x="60" y="150" width="180" height="130" fill="#b9add0"/>' + "".join(f'<line x1="60" x2="240" y1="{165 + n * 22}" y2="{165 + n * 22}" stroke="#9a8db5" stroke-width="5"/>' for n in range(5)))
s.E("st", svg(300, 290, store), L(70, 330, 10), s.P("It ran"), "pop")
s.E("rd", scooter_svg("scale-sc"), L(1420, 360, 10, "transform:scale(0.95);transform-origin:left top;"), s.P("Nearly"), "pop")
s.J(f'tl.to("#scale-sc",{{y:-6,duration:0.25,yoyo:true,repeat:20,ease:"sine.inOut"}},{round(s.P("Nearly") + 0.4, 2)});')

# orders: conveyor of boxes
s = SC["orders"]
belt = f'<rect x="0" y="150" width="1500" height="26" rx="13" fill="{ZL}"/>' + "".join(f'<circle cx="{40 + n * 120}" cy="190" r="16" fill="{ZPAN}" stroke="{ZL}" stroke-width="5"/>' for n in range(13))
boxes_ = "".join(f'<g class="orders-bx"><rect x="{n * 190}" y="40" width="130" height="110" rx="10" fill="{[ZP, ZA, ZB, ZW][n % 4]}"/><rect x="{n * 190 + 52}" y="40" width="26" height="110" fill="{ZK}" opacity=".18"/></g>' for n in range(9))
s.E("cv", svg(1500, 220, f'{belt}<g id="orders-row">{boxes_}</g>'), L(210, 790, 10), 0.2, "fade")
s.J('tl.fromTo("#orders-row",{x:-380},{x:0,duration:4,ease:"none"},0.2);')

# why: stock-exchange board with Zepto missing
s = SC["why"]
board = (f'<rect x="0" y="0" width="1100" height="200" rx="20" fill="{ZK}" stroke="{ZL}" stroke-width="6"/>' +
         "".join(f'<text x="{60 + n * 260}" y="80" font-family="Outfit" font-weight="800" font-size="40" fill="{ZL}">{nm}</text><text x="{60 + n * 260}" y="140" font-family="Outfit" font-weight="800" font-size="40" fill="{c}">{v}</text>' for n, (nm, v, c) in enumerate([("ETERNAL", "▲", "#57E39A"), ("SWIGGY", "▼", ZA), ("ZEPTO", "?", ZP), ("NIFTY", "▲", "#57E39A")])))
s.E("bd", svg(1100, 200, board), L(410, 680, 10), 0.3, "fade")
s.J('tl.fromTo("#why-bd",{y:40},{y:0,duration:0.5,ease:"back.out(1.6)"},0.3);')

# costs: icons above the three columns
s = SC["costs"]
bld = svg(170, 150, f'<rect x="40" y="10" width="90" height="140" fill="{ZW}"/>' + "".join(f'<rect x="{54 + (n % 3) * 22}" y="{24 + (n // 3) * 26}" width="14" height="16" fill="{ZB}"/>' for n in range(12)) + f'<text x="150" y="60" font-family="Outfit" font-weight="800" font-size="44" fill="{ZA}">₹</text>')
tag = svg(170, 150, f'<path d="M20 70 L80 10 H150 V80 L90 140 Z" fill="{ZA}"/><circle cx="125" cy="36" r="12" fill="{ZPAN}"/><text x="72" y="98" text-anchor="middle" font-family="Outfit" font-weight="800" font-size="42" fill="{ZK}" transform="rotate(-45 72 90)">%</text>')
s.E("ic0", bld, L(305, 255, 10), s.P("You pay rent"), "pop")
s.E("ic1", scooter_svg("costs-sc", w=200), L(860, 262, 10), s.P("you pay riders"), "pop")
s.E("ic2", tag, L(1445, 255, 10), s.P("you pay discounts"), "pop")

# loss: burning cash
s = SC["loss"]
notes_ = "".join(f'<rect x="{150 + n * 8}" y="{150 - n * 16}" width="300" height="130" rx="12" fill="{"#8FD9A8" if n % 2 == 0 else "#7BC795"}" stroke="{ZK}" stroke-width="5"/>' for n in range(4))
flames = (f'<path id="loss-f1" d="M260 120 Q230 60 270 10 Q280 60 310 40 Q330 90 300 120 Z" fill="{ZA}"/><path id="loss-f2" d="M340 110 Q320 60 350 20 Q360 60 390 50 Q400 90 380 110 Z" fill="{ZP}"/>'
          f'<path id="loss-f3" d="M410 120 Q400 80 430 50 Q440 80 455 75 Q465 105 450 120 Z" fill="{ZA}"/>')
s.E("fire", svg(600, 290, notes_ + flames), L(660, 740, 10), s.P("It was burning"), "fade")
s.J('tl.to(["#loss-f1","#loss-f2","#loss-f3"],{scaleY:1.18,transformOrigin:"50% 100%",duration:0.2,yoyo:true,repeat:14,ease:"sine.inOut"},' + str(s.P("It was burning")) + ');')

# ipo: icons above the three timeline points
s = SC["ipo"]
icd = svg(150, 160, f'<rect x="20" y="10" width="110" height="140" rx="10" fill="{ZW}"/>' + "".join(f'<rect x="38" y="{36 + n * 24}" width="74" height="10" rx="5" fill="#d6cbe8"/>' for n in range(4)))
ics = svg(150, 160, f'<circle cx="75" cy="80" r="64" fill="none" stroke="#57E39A" stroke-width="12"/><path d="M45 82 L68 104 L108 58" stroke="#57E39A" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
icb = svg(150, 160, f'<path d="M30 120 Q30 30 75 30 Q120 30 120 120 Z" fill="{ZA}"/><rect x="20" y="118" width="110" height="14" rx="7" fill="{ZA}"/><circle cx="75" cy="146" r="12" fill="{ZA}"/><rect x="68" y="12" width="14" height="22" rx="5" fill="{ZA}"/>')
for n, ic in enumerate([icd, ics, icb]):
    s.E(f"ic{n}", ic, L([360, 960, 1560][n] - 75, 270, 10), tp[n], "pop")

# post: calendar (left) + hourglass (right)
s = SC["post"]
cal = (f'<rect x="10" y="30" width="260" height="250" rx="18" fill="{ZW}"/><rect x="10" y="30" width="260" height="70" rx="18" fill="{ZP}"/><rect x="60" y="10" width="20" height="50" rx="8" fill="{ZK}"/><rect x="200" y="10" width="20" height="50" rx="8" fill="{ZK}"/>'
       + "".join(f'<rect x="{36 + (n % 4) * 56}" y="{122 + (n // 4) * 50}" width="40" height="34" rx="6" fill="{"#d6cbe8" if n != 6 else ZA}"/>' for n in range(12)))
s.E("cal", svg(280, 290, cal), L(100, 420, 10), s.P("pushed back"), "pop")
hg = (f'<rect x="20" y="10" width="180" height="20" rx="10" fill="{ZL}"/><rect x="20" y="290" width="180" height="20" rx="10" fill="{ZL}"/>'
      f'<path d="M40 30 H180 Q180 120 110 160 Q180 200 180 290 H40 Q40 200 110 160 Q40 120 40 30 Z" fill="none" stroke="{ZL}" stroke-width="10"/>'
      f'<path id="post-sand" d="M60 270 Q110 220 160 270 Z" fill="{ZA}"/><path d="M70 60 H150 Q140 110 110 140 Q80 110 70 60 Z" fill="{ZA}"/>')
s.E("hg", svg(220, 320, hg), L(1600, 410, 10), s.P("two to three"), "pop")
s.J(f'tl.fromTo("#post-hg",{{rotation:0}},{{rotation:180,duration:0.8,ease:"power2.inOut"}},{round(s.P("two to three") + 0.6, 2)});')

# alive: safe with coins
s = SC["alive"]
safe = (f'<rect x="20" y="20" width="300" height="300" rx="28" fill="{ZL}"/><rect x="50" y="50" width="240" height="240" rx="18" fill="{ZPAN}"/>'
        f'<circle cx="170" cy="170" r="60" fill="none" stroke="{ZL}" stroke-width="12"/><path d="M170 120 V140 M170 200 V220 M120 170 H140 M200 170 H220" stroke="{ZL}" stroke-width="10"/>'
        f'<rect x="30" y="320" width="60" height="20" rx="6" fill="{ZL}"/><rect x="250" y="320" width="60" height="20" rx="6" fill="{ZL}"/>'
        + "".join(f'<ellipse id="alive-c{n}" cx="{90 + n * 80}" cy="20" rx="34" ry="12" fill="{ZA}" stroke="{ZK}" stroke-width="4"/>' for n in range(3)))
s.E("sf", svg(340, 350, safe, "0 -20 340 370"), L(80, 470, 10), s.P("Its cash burn"), "pop")
pops(s, [f"alive-c{n}" for n in range(3)], s.P("and it still"), 0.12)

# money: crystal ball (could become) and cash register (earns)
s = SC["money"]
ball = (f'<circle cx="160" cy="130" r="110" fill="{ZB}" opacity=".35" stroke="{ZB}" stroke-width="8"/><path d="M110 100 Q130 70 160 70" stroke="{ZW}" stroke-width="10" fill="none" stroke-linecap="round"/>'
        f'<path d="M90 230 H230 L250 270 H70 Z" fill="{ZP}"/><path d="M130 150 L150 110 L170 140 L190 90" stroke="{ZA}" stroke-width="8" fill="none" stroke-linecap="round"/>')
reg = (f'<rect x="40" y="110" width="240" height="160" rx="16" fill="{ZL}"/><rect x="70" y="40" width="180" height="80" rx="10" fill="{ZPAN}" stroke="{ZL}" stroke-width="6"/>'
       f'<text x="160" y="96" text-anchor="middle" font-family="Outfit" font-weight="800" font-size="44" fill="#57E39A">₹ ₹ ₹</text>'
       + "".join(f'<rect x="{70 + (n % 4) * 48}" y="{140 + (n // 4) * 40}" width="34" height="26" rx="5" fill="{ZPAN}"/>' for n in range(8)) + f'<rect x="30" y="270" width="260" height="20" rx="8" fill="{ZA}"/>')
s.E("cb", svg(320, 290, ball), L(340, 720, 10), s.P("could become"), "pop")
s.E("cr", svg(320, 300, reg), L(1260, 710, 10), s.P("earns"), "pop")

# prove: tick badge and question badge with a stopwatch between
s = SC["prove"]
s.E("ok", svg(150, 150, f'<circle cx="75" cy="75" r="68" fill="{ZP}"/><path d="M42 78 L66 102 L110 54" stroke="{ZW}" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'), L(150, 210, 10), s.P("that Indians"), "pop")
s.E("qq", svg(150, 150, f'<circle cx="75" cy="75" r="68" fill="{ZA}"/><text x="75" y="102" text-anchor="middle" font-family="Outfit" font-weight="800" font-size="84" fill="{ZK}">?</text>'), L(150, 600, 10), s.P("is that ten"), "pop")
s.E("pw", svg(240, 270, watch.replace("born-arc", "prove-arc")), L(1580, 380, 10), s.P("is that ten"), "pop")
s.J(draw("#prove-arc", s.P("is that ten"), 1.2))

# young: two founders as silhouettes from behind + rising steps
s = SC["young"]
def back(x, c):
    return f'<circle cx="{x}" cy="60" r="44" fill="{c}"/><path d="M{x - 70} 300 Q{x - 74} 120 {x} 116 Q{x + 74} 120 {x + 70} 300 Z" fill="{c}"/>'
s.E("fd", svg(420, 300, back(130, ZL) + back(290, ZP)), L(750, 650, 10), s.P("are still"), "fade")
bounce(s, "#young-fd", s.P("are still"))

# bet: balance scale
s = SC["bet"]
bal = (f'<rect x="290" y="40" width="20" height="200" fill="{ZL}"/><rect x="200" y="230" width="200" height="20" rx="8" fill="{ZL}"/>'
       f'<g id="bet-beam"><rect x="40" y="40" width="520" height="14" rx="7" fill="{ZL}"/><path d="M60 54 L20 140 H140 Z" fill="none" stroke="{ZL}" stroke-width="5"/><path d="M20 140 Q80 175 140 140 Z" fill="{ZP}"/>'
       f'<path d="M540 54 L460 140 H580 Z" fill="none" stroke="{ZL}" stroke-width="5"/><path d="M460 140 Q520 175 580 140 Z" fill="{ZA}"/></g>')
s.E("bl", svg(600, 260, bal), L(660, 500, 10), s.P("Or the most"), "fade")
s.J('tl.fromTo("#bet-beam",{rotation:-8,transformOrigin:"50% 0%"},{rotation:8,duration:0.9,yoyo:true,repeat:3,ease:"sine.inOut"},' + str(s.P("Or the most")) + ');')

# endcard: bell + a yellow scooter teasing the Blinkit video
s = SC["endcard"]
s.E("bell", svg(160, 170, f'<path d="M30 130 Q30 30 80 30 Q130 30 130 130 Z" fill="{ZA}"/><rect x="18" y="126" width="124" height="16" rx="8" fill="{ZA}"/><circle cx="80" cy="156" r="13" fill="{ZA}"/>'), L(1610, 290, 10), s.P("subscribe"), "pop")
s.J(f'tl.to("#endcard-bell",{{rotation:14,transformOrigin:"50% 10%",duration:0.12,yoyo:true,repeat:7}},{round(s.P("subscribe") + 0.4, 2)});')
s.E("bk", scooter_svg("endcard-sc", body="#0C831F", box="#F8CB46"), L(730, 760, 10, "transform:scale(0.8);transform-origin:left top;"), s.P("I'm doing"), "fade")
s.J(f'tl.fromTo("#endcard-bk",{{x:-700}},{{x:0,duration:0.9,ease:"power3.out"}},{s.P("I\'m doing")});')

sl.write_project(os.path.join(HERE, "project"), S, first_host=("coldopen", "compositions/coldopen.html", sl.sstart(2)), audio_dur=232.87)
