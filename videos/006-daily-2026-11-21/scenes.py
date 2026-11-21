"""Full-screen drawn backdrops (1920x1080 SVG, no faces, no logos, no real flags) for video 005.
scene(key, accent) -> svg string. Headline sits at y 100-300 and the card band at y 690-950, so the art lives mostly in y 280-700.
"""
import random

W, MUTED, NAVY = "#FFFFFF", "#B8C1E6", "#0B1026"


def _bg(top, bot, extra=""):
    return (f'<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bot}"/></linearGradient></defs>'
            f'<rect width="1920" height="1080" fill="url(#g)"/>' + extra)


def _stars(n=70, seed=1, y1=700):
    r = random.Random(seed)
    return "".join(f'<circle cx="{r.randint(0, 1920)}" cy="{r.randint(0, y1)}" r="{r.choice([1.5, 2, 3])}" fill="#fff" opacity="{r.choice([.4, .6, .9])}"/>' for _ in range(n))


def _sea(y, col1="#16306b", col2="#0d1f4a", a="#5CC8FF"):
    s = f'<rect x="0" y="{y}" width="1920" height="{1080 - y}" fill="{col2}"/>'
    for k in range(7):
        yy = y + 20 + k * 38
        s += f'<path d="M0 {yy} q60 -22 120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 V1080 H0Z" fill="{col1}" opacity="{0.55 - k * 0.05}"/>'
        s += f'<path d="M{30 + k * 40} {yy} q60 -22 120 0" stroke="{a}" stroke-width="4" fill="none" opacity="0.35"/>'
    return s


def _globe(cx, cy, r, a):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#1B2D63" stroke="{a}" stroke-width="10"/>'
            f'<g stroke="{MUTED}" stroke-width="6" fill="none" opacity="0.7"><ellipse cx="{cx}" cy="{cy}" rx="{r * .45}" ry="{r}"/><ellipse cx="{cx}" cy="{cy}" rx="{r * .8}" ry="{r}"/>'
            f'<path d="M{cx - r} {cy} H{cx + r} M{cx - r * .86} {cy - r * .5} H{cx + r * .86} M{cx - r * .86} {cy + r * .5} H{cx + r * .86}"/></g>'
            f'<ellipse cx="{cx}" cy="{cy}" rx="{r * 1.35}" ry="{r * .35}" stroke="{a}" stroke-width="6" fill="none" transform="rotate(-18 {cx} {cy})" opacity="0.8"/>'
            f'<circle cx="{cx + r * .55}" cy="{cy - r * .3}" r="{r * .09}" fill="{a}"/><circle cx="{cx - r * .4}" cy="{cy + r * .35}" r="{r * .06}" fill="{W}"/>')


def _skyline(y, col="#0a1330", seed=3, n=20, a=None):
    r = random.Random(seed)
    s, x = "", 0
    while x < 1920:
        w, h = r.randint(70, 150), r.randint(80, 300)
        s += f'<rect x="{x}" y="{y - h}" width="{w}" height="{h + 400}" fill="{col}"/>'
        if a:
            for k in range(r.randint(1, 4)):
                s += f'<rect x="{x + 14 + (k % 2) * 40}" y="{y - h + 24 + (k // 2) * 40}" width="16" height="22" fill="{a}" opacity="0.6"/>'
        x += w + r.randint(6, 24)
    return s


def _mountains(y, col, seed=2, hmin=140, hmax=340, snow=False):
    r = random.Random(seed)
    pts, x = [(0, y)], 0
    while x < 1920:
        x += r.randint(140, 260)
        pts.append((x, y - r.randint(hmin, hmax)))
        x += r.randint(120, 220)
        pts.append((x, y - r.randint(40, 110)))
    pts.append((1920, y)); pts.append((1920, 1080)); pts.append((0, 1080))
    s = f'<polygon points="{" ".join(f"{p[0]},{p[1]}" for p in pts)}" fill="{col}"/>'
    if snow:
        for i in range(1, len(pts) - 3, 2):
            px, py = pts[i]
            s += f'<polygon points="{px - 70},{py + 90} {px},{py} {px + 70},{py + 90} {px + 30},{py + 74} {px},{py + 100} {px - 30},{py + 72}" fill="#fff" opacity="0.92"/>'
    return s


def intro(a, outro=False):
    return (_bg("#0B1026", "#1a2a66") + _stars(60, 5, 600) + _globe(1330, 440, 250, a) +
            _skyline(980, "#0a1330", 4, a="#FFD23F") + f'<path d="M0 990 H1920" stroke="{a}" stroke-width="6"/>' +
            f'<g fill="none" stroke="{a}" stroke-width="5" opacity="0.5"><path d="M120 560 C400 380 700 380 1000 470" stroke-dasharray="14 14"/></g>')


def w1(a):  # Kyiv bridges under missile trails
    s = _bg("#120a1e", "#3a1a2a") + _stars(60, 7, 400) + _skyline(560, "#0a0f26", 11, 20, "#FFD23F")
    s += '<rect x="0" y="690" width="1920" height="390" fill="#0a1330"/>'
    for k in range(3):
        x = 300 + k * 520
        s += f'<path d="M{x} 600 H{x + 440}" stroke="{W}" stroke-width="14"/><path d="M{x + 40} 600 V690 M{x + 400} 600 V690" stroke="{MUTED}" stroke-width="12"/><path d="M{x + 40} 600 Q{x + 220} 470 {x + 400} 600" stroke="{a}" stroke-width="8" fill="none"/>'
        s += f'<circle cx="{x + 220}" cy="595" r="26" fill="{a}" opacity="0.85"/>'
    for k in range(7):
        x = 150 + k * 260
        s += f'<path d="M{x} 130 L{x + 120} 470" stroke="{a}" stroke-width="5" stroke-dasharray="2 14" stroke-linecap="round"/><polygon points="{x + 120},470 {x + 108},440 {x + 134},443" fill="{W}"/>'
    s += f'<path d="M0 710 q120 -24 240 0 t240 0 t240 0 t240 0 t240 0 t240 0 t240 0 t240 0" stroke="{MUTED}" stroke-width="5" fill="none" opacity="0.4"/>'
    return s


def w2(a):  # two missiles and a drone crossing a border line
    s = _bg("#0a1128", "#14244f") + _stars(70, 9, 450)
    s += '<path d="M0 640 Q500 600 960 650 T1920 620 V1080 H0Z" fill="#12306b"/><path d="M960 330 V1080" stroke="#FFD23F" stroke-width="8" stroke-dasharray="26 16"/>'
    for k, (x, y) in enumerate(((300, 420), (620, 330), (1000, 440))):
        s += f'<g transform="translate({x} {y}) rotate(12)"><rect x="0" y="-14" width="230" height="28" rx="14" fill="{W}"/><polygon points="230,-14 290,0 230,14" fill="{a}"/><polygon points="20,-14 -20,-50 40,-14" fill="{a}"/><polygon points="20,14 -20,50 40,14" fill="{a}"/><path d="M-10 0 H-260" stroke="{a}" stroke-width="8" stroke-dasharray="3 14" opacity="0.7"/></g>'
    s += f'<g transform="translate(1450 400)"><rect x="-50" y="-10" width="100" height="20" rx="10" fill="{MUTED}"/><path d="M-60 -22 H60 M-30 -22 V-6 M30 -22 V-6" stroke="{W}" stroke-width="6"/></g>'
    s += f'<g transform="translate(1250 600)"><path d="M0 60 V-40 H80 V60Z" fill="#0a1330"/><polygon points="-10,-40 40,-90 90,-40" fill="{a}"/></g>'
    s += f'<circle cx="1520" cy="640" r="70" fill="{a}" opacity="0.25"/><circle cx="1520" cy="640" r="34" fill="{a}" opacity="0.5"/>'
    return s


def n1(a):  # parliament dome + seat arcs
    s = _bg("#0B1026", "#1b2a5c") + _stars(40, 3, 300)
    s += f'<path d="M560 640 V470 Q960 150 1360 470 V640Z" fill="#17285a" stroke="{a}" stroke-width="8"/><rect x="520" y="640" width="880" height="40" fill="{MUTED}"/><rect x="480" y="680" width="960" height="36" fill="{W}" opacity="0.85"/>'
    for k in range(7):
        s += f'<rect x="{610 + k * 105}" y="500" width="34" height="140" fill="{MUTED}" opacity="0.8"/>'
    s += f'<path d="M960 130 V220" stroke="{W}" stroke-width="8"/><polygon points="960,130 1030,150 960,170" fill="{a}"/>'
    for r_ in (150, 210, 270):
        s += f'<path d="M{960 - r_} 640 A{r_} {r_} 0 0 1 {960 + r_} 640" stroke="{a}" stroke-width="5" stroke-dasharray="3 12" fill="none" opacity="0.6"/>'
    s += f'<path d="M0 716 H1920 V1080 H0Z" fill="#0a1330"/>'
    return s


def n2(a):  # bullet train on viaduct
    s = _bg("#0B1026", "#2a4a8a") + f'<circle cx="1500" cy="250" r="90" fill="#FFD23F" opacity="0.9"/>' + _mountains(620, "#14244f", 5, 100, 260)
    s += '<rect x="0" y="660" width="1920" height="30" fill="#c9d1ee"/>'
    for k in range(10):
        s += f'<rect x="{80 + k * 200}" y="690" width="40" height="390" fill="#a9b4d8"/>'
    s += f'<path d="M260 650 H1500 Q1640 650 1700 600 L1660 560 Q1600 540 1500 540 H260 Q200 540 200 600 Q200 650 260 650Z" fill="{W}"/><path d="M200 600 H1690" stroke="{a}" stroke-width="22"/>'
    for k in range(10):
        s += f'<rect x="{330 + k * 115}" y="560" width="62" height="34" rx="8" fill="#12306b"/>'
    s += f'<path d="M1500 540 Q1620 548 1700 600" stroke="#12306b" stroke-width="18" fill="none"/><path d="M0 560 H1920" stroke="{MUTED}" stroke-width="3" opacity="0.4"/>'
    return s


def n3(a):  # hill with a lit lamp and pillar
    s = _bg("#1a1038", "#3a2250") + _stars(110, 21, 520)
    s += '<polygon points="0,780 520,360 960,560 1380,300 1920,780 1920,1080 0,1080" fill="#0f1a3d"/>'
    s += f'<rect x="1370" y="330" width="40" height="150" fill="{MUTED}"/><rect x="1352" y="316" width="76" height="22" rx="6" fill="{W}"/>'
    s += f'<path d="M1390 260 q40 -50 0 -110 q-40 60 0 110z" fill="{a}"/><path d="M1390 252 q16 -26 0 -56 q-16 30 0 56z" fill="#FFD23F"/><circle cx="1390" cy="230" r="120" fill="{a}" opacity="0.18"/>'
    for k in range(9):
        s += f'<g transform="translate({150 + k * 190} {820 + (k % 2) * 40})"><ellipse cx="0" cy="0" rx="34" ry="12" fill="#c77a2a"/><path d="M-26 -4 H26" stroke="#0a1330" stroke-width="3"/><path d="M0 -8 q8 -20 0 -34 q-8 14 0 34z" fill="#FFD23F"/></g>'
    s += f'<rect x="620" y="600" width="170" height="90" fill="#17285a" stroke="{MUTED}" stroke-width="4"/><path d="M620 600 Q705 540 790 600" fill="{W}" opacity="0.9"/>'
    return s


def s1(a):  # village with ballot box and sign
    s = _bg("#13204a", "#c77dff") + f'<circle cx="400" cy="260" r="100" fill="#FFD23F" opacity="0.9"/>' + '<rect x="0" y="700" width="1920" height="380" fill="#2a5a40"/>'
    for k, x in enumerate((300, 640, 1500, 1740)):
        s += f'<rect x="{x}" y="560" width="190" height="140" fill="#d9b779"/><polygon points="{x - 20},560 {x + 95},470 {x + 210},560" fill="#8a3a2a"/><rect x="{x + 70}" y="620" width="50" height="80" fill="#4a2a1a"/>'
    s += f'<rect x="780" y="520" width="360" height="260" rx="22" fill="{a}"/><rect x="900" y="490" width="120" height="26" rx="8" fill="#05081a"/>'
    s += f'<g transform="rotate(-8 960 420)"><rect x="880" y="320" width="160" height="170" rx="10" fill="{W}"/><path d="M910 410 l28 30 l56 -64" stroke="#0B1026" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>'
    return s


def s2(a):  # city smoke and crackers
    s = _bg("#201018", "#5a2a2a") + _skyline(640, "#150a14", 13, 20, "#FFD23F")
    for k, (x, y, c) in enumerate(((420, 300, a), (900, 250, "#FFD23F"), (1400, 330, "#FF4A4F"), (1700, 240, "#5CC8FF"))):
        for ang in range(0, 360, 30):
            import math
            dx, dy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
            s += f'<path d="M{x + dx * 40} {y + dy * 40} L{x + dx * 110} {y + dy * 110}" stroke="{c}" stroke-width="7" stroke-linecap="round"/><circle cx="{x + dx * 130}" cy="{y + dy * 130}" r="7" fill="{c}"/>'
    s += f'<path d="M0 560 Q300 470 600 540 T1200 520 T1920 500 V640 H0Z" fill="#6b5a5a" opacity="0.55"/>'
    s += '<rect x="0" y="640" width="1920" height="440" fill="#150a14"/>'
    return s


def s3(a):  # runway and airplane
    s = _bg("#0B1026", "#3a6aa8") + '<rect x="0" y="640" width="1920" height="440" fill="#1c2748"/><path d="M0 640 H1920" stroke="#c9d1ee" stroke-width="6"/>'
    s += '<polygon points="760,1080 1160,1080 1040,640 880,640" fill="#2a3560"/>' + "".join(f'<rect x="{950 - 6}" y="{660 + k * 80}" width="12" height="{30 + k * 8}" fill="#fff"/>' for k in range(5))
    s += f'<g transform="translate(560 380) rotate(-12)"><path d="M0 0 Q120 -50 520 -20 L600 0 L520 22 Q120 50 0 0Z" fill="{W}"/><polygon points="250,-20 120,-150 190,-150 340,-20" fill="{MUTED}"/><polygon points="250,10 120,140 190,140 340,10" fill="{MUTED}"/><polygon points="40,-8 0,-90 50,-90 90,-8" fill="{a}"/>' + "".join(f'<circle cx="{200 + k * 50}" cy="-8" r="6" fill="#12306b"/>' for k in range(7)) + '</g>'
    s += f'<g stroke="{a}" stroke-width="6" stroke-dasharray="14 12" fill="none"><rect x="1200" y="520" width="560" height="120" rx="12"/></g><path d="M1220 580 H1740" stroke="{a}" stroke-width="4" opacity="0.6"/>'
    return s


def v1(a):  # dry cracked field with sparse wheat
    s = _bg("#2a1a3a", "#e8a24a") + f'<circle cx="1480" cy="300" r="140" fill="#FFD23F"/><rect x="0" y="600" width="1920" height="480" fill="#7a5230"/>'
    for k in range(14):
        x = 60 + k * 140
        s += f'<path d="M{x} 640 L{x + 40} 700 L{x - 10} 780 L{x + 50} 860 M{x + 40} 700 L{x + 110} 720" stroke="#2a1a10" stroke-width="5" fill="none"/>'
    for k in range(10):
        x = 140 + k * 180
        s += f'<g transform="translate({x} 600)"><path d="M0 0 V-130" stroke="{a}" stroke-width="7"/>' + "".join(f'<ellipse cx="{(-9 if j % 2 else 9)}" cy="{-150 + j * 18}" rx="8" ry="20" fill="{a}"/>' for j in range(5)) + '</g>'
    return s


def v2(a):  # paddy field with sacks and weighing scale
    s = _bg("#103a4a", "#bfe9d0") + f'<circle cx="360" cy="240" r="90" fill="#FFD23F"/><rect x="0" y="560" width="1920" height="520" fill="#2a7a4a"/>'
    for r_ in range(5):
        y = 590 + r_ * 60
        s += f'<path d="M0 {y} H1920" stroke="#1a5a38" stroke-width="10" opacity="0.6"/>' + "".join(f'<path d="M{x} {y} q10 -50 30 -60" stroke="#e8d36a" stroke-width="6" fill="none" stroke-linecap="round"/>' for x in range(30, 1900, 70))
    for k in range(5):
        x = 1100 + (k % 3) * 200
        y = 660 - (k // 3) * 90
        s += f'<path d="M{x} {y} q-10 -90 40 -100 h70 q50 10 40 100z" fill="#d9b779" stroke="#8a6a3a" stroke-width="5"/><path d="M{x + 20} {y - 100} h110" stroke="#8a6a3a" stroke-width="6"/>'
    s += f'<rect x="420" y="640" width="360" height="40" fill="{MUTED}"/><rect x="560" y="520" width="80" height="120" fill="{W}"/><circle cx="600" cy="500" r="64" fill="{W}" stroke="{a}" stroke-width="10"/><path d="M600 500 L630 470" stroke="#0B1026" stroke-width="8"/>'
    return s


def q1(a):  # border barrier with a closed gate
    s = _bg("#0B1026", "#3a5a8a") + _stars(60, 5, 400) + '<rect x="0" y="640" width="1920" height="440" fill="#1c2748"/>'
    s += '<path d="M0 720 H1920" stroke="#c9d1ee" stroke-width="6" stroke-dasharray="30 20"/>'
    s += f'<rect x="760" y="470" width="30" height="230" fill="{MUTED}"/><rect x="1130" y="470" width="30" height="230" fill="{MUTED}"/><rect x="760" y="560" width="400" height="30" fill="{a}"/>'
    for k in range(6):
        s += f'<polygon points="{778 + k * 64},560 {800 + k * 64},560 {770 + k * 64},590 {748 + k * 64},590" fill="{W}"/>'
    s += f'<rect x="1180" y="430" width="120" height="100" rx="10" fill="#12306b" stroke="{W}" stroke-width="5"/><path d="M1240 450 V510 M1210 480 H1270" stroke="{a}" stroke-width="8"/>'
    s += f'<circle cx="960" cy="330" r="64" fill="none" stroke="{a}" stroke-width="12"/><path d="M915 285 L1005 375" stroke="{a}" stroke-width="12"/>'
    return s


def q2(a):  # ships and target ranges
    s = _bg("#0B1026", "#1b3a73") + _sea(560, "#16306b", "#0d2250", a)
    s += f'<path d="M420 540 H1100 L1040 600 H480 Z" fill="{MUTED}"/><rect x="620" y="480" width="200" height="60" fill="{W}"/><rect x="680" y="440" width="60" height="40" fill="{a}"/><path d="M700 440 V380" stroke="{W}" stroke-width="6"/>'
    s += f'<g transform="translate(1250 500)"><circle r="120" fill="none" stroke="{a}" stroke-width="8"/><circle r="70" fill="none" stroke="{W}" stroke-width="8"/><circle r="22" fill="{a}"/></g>'
    s += f'<path d="M800 430 Q1000 220 1250 480" stroke="{a}" stroke-width="6" stroke-dasharray="3 16" fill="none" stroke-linecap="round"/>'
    return s


def q3(a):  # capsule above Earth
    s = _bg("#05081a", "#10204a") + _stars(160, 31, 800)
    s += f'<circle cx="960" cy="1080" r="560" fill="#1B3FA0"/><circle cx="960" cy="1080" r="560" fill="none" stroke="#5CC8FF" stroke-width="10" opacity="0.7"/><path d="M620 700 q80 -60 170 -20 q30 50 -30 80 q-80 20 -140 -60z" fill="#2EC4B6"/>'
    s += f'<g transform="translate(1100 330) rotate(25)"><path d="M-60 40 L-30 -90 H30 L60 40Z" fill="{W}"/><rect x="-60" y="40" width="120" height="30" rx="8" fill="{MUTED}"/><circle cx="0" cy="-30" r="14" fill="{a}"/><path d="M-70 90 L-40 120 M0 90 V140 M70 90 L40 120" stroke="{a}" stroke-width="8" stroke-linecap="round"/></g>'
    s += f'<path d="M520 480 Q800 380 1060 330" stroke="{a}" stroke-width="5" stroke-dasharray="3 16" fill="none" stroke-linecap="round"/>'
    return s


def q4(a):  # cricket stadium: stumps, bat, ball
    s = _bg("#0B1026", "#1b5a4a") + _stars(40, 4, 300) + '<ellipse cx="960" cy="700" rx="1100" ry="260" fill="#2a8a5a"/><ellipse cx="960" cy="700" rx="700" ry="150" fill="#35a06a"/><rect x="900" y="620" width="120" height="150" fill="#d9b779" opacity="0.8"/>'
    for k in range(3):
        s += f'<rect x="{918 + k * 40}" y="480" width="10" height="160" fill="{W}"/>'
    s += f'<rect x="914" y="474" width="82" height="8" fill="{a}"/>'
    s += f'<g transform="translate(1180 520) rotate(28)"><rect x="-26" y="-190" width="52" height="260" rx="16" fill="#d9b779"/><rect x="-10" y="70" width="20" height="100" rx="8" fill="#3a2a1a"/></g>'
    s += f'<circle cx="760" cy="420" r="30" fill="#FF4A4F"/><path d="M742 408 q18 12 36 0" stroke="{W}" stroke-width="3" fill="none"/>'
    for k in range(18):
        s += f'<circle cx="{100 + k * 100}" cy="{400 + (k % 3) * 20}" r="12" fill="{MUTED}" opacity="0.4"/>'
    return s


def q5(a):  # exchange building and rising bars
    s = _bg("#0B1026", "#1b2a5c") + _stars(40, 8, 300)
    s += f'<polygon points="420,500 960,330 1500,500" fill="{MUTED}"/><rect x="450" y="500" width="1020" height="40" fill="{W}"/>'
    s += "".join(f'<rect x="{500 + k * 140}" y="540" width="60" height="200" fill="{W}" opacity="0.85"/>' for k in range(7))
    s += f'<rect x="420" y="740" width="1080" height="40" fill="{MUTED}"/>'
    for k in range(5):
        h = 80 + k * 55
        s += f'<rect x="{1560 + k * 70}" y="{780 - h}" width="48" height="{h}" fill="{a}" opacity="{0.55 + k * 0.1}"/>'
    s += f'<path d="M1540 600 L1650 520 L1740 560 L1880 400" stroke="{W}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    s += f'<path d="M0 780 H1920 V1080 H0Z" fill="#0a1330"/>'
    return s


BUILD = {"intro": intro, "outro": lambda a: intro(a, True), "w1": w1, "w2": w2, "n1": n1, "n2": n2, "n3": n3, "s1": s1, "s2": s2, "s3": s3,
         "v1": v1, "v2": v2, "q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5}


def scene(key, a):
    return f'<svg width="1920" height="1080" viewBox="0 0 1920 1080" preserveAspectRatio="none">{BUILD[key](a)}</svg>'
