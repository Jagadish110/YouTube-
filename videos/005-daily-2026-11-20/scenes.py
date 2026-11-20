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


def summit(a):
    s = _bg("#0B1026", "#23346e") + _stars(40, 8, 400) + _skyline(700, "#0a1330", 11, a="#FFD23F")
    s += f'<ellipse cx="960" cy="640" rx="470" ry="84" fill="#102046" stroke="{a}" stroke-width="8"/><ellipse cx="960" cy="628" rx="410" ry="62" fill="#1B2D63"/>'
    for cx, col in ((470, a), (960, W), (1450, "#5CC8FF")):
        s += (f'<rect x="{cx - 70}" y="440" width="140" height="170" rx="30" fill="{col}"/><rect x="{cx - 90}" y="580" width="180" height="48" rx="16" fill="{col}" opacity="0.8"/>'
              f'<circle cx="{cx}" cy="380" r="46" fill="{col}" opacity="0.9"/>')
    for cx, col in ((220, a), (960, W), (1700, "#5CC8FF")):
        s += f'<rect x="{cx - 4}" y="300" width="8" height="330" fill="{MUTED}"/><path d="M{cx + 4} 304 h120 l-24 34 l24 34 h-120z" fill="{col}" opacity="0.85"/>'
    return s


def icj(a, scales=False):
    s = _bg("#0B1026", "#1c2f6b") + _stars(50, 12, 500)
    if scales:
        s += (f'<rect x="946" y="300" width="28" height="360" fill="{MUTED}"/><rect x="760" y="640" width="400" height="46" rx="14" fill="{W}"/>'
              f'<path d="M520 340 H1400" stroke="{a}" stroke-width="16" stroke-linecap="round"/>')
        for cx in (560, 1360):
            s += (f'<path d="M{cx} 340 L{cx - 110} 520 M{cx} 340 L{cx + 110} 520" stroke="{MUTED}" stroke-width="6"/>'
                  f'<path d="M{cx - 150} 520 H{cx + 150} q-20 90 -150 90 q-130 0 -150 -90z" fill="{a}" opacity="0.9"/>')
        s += f'<circle cx="960" cy="300" r="34" fill="{a}"/>'
        return s
    s += f'<polygon points="360,360 960,230 1560,360" fill="{W}" opacity="0.95"/><polygon points="460,350 960,256 1460,350" fill="#102046"/>'
    s += f'<rect x="340" y="364" width="1240" height="40" fill="{W}"/>'
    for i in range(7):
        x = 420 + i * 180
        s += f'<rect x="{x}" y="410" width="68" height="230" fill="{W}" opacity="0.95"/><rect x="{x - 10}" y="410" width="88" height="22" fill="{MUTED}"/>'
    s += f'<rect x="320" y="640" width="1280" height="34" fill="{MUTED}"/><rect x="280" y="674" width="1360" height="30" fill="{W}" opacity="0.8"/>'
    s += f'<circle cx="960" cy="318" r="22" fill="{a}"/>'
    return s


def quad(a):
    s = _bg("#0B1026", "#1b3a73") + _sea(560, "#16306b", "#0d2250", a) + _stars(40, 20, 380)
    pts = [(420, 420), (960, 330), (1500, 420), (960, 560)]
    s += f'<path d="M420 420 L960 330 L1500 420 L960 560 Z" stroke="{a}" stroke-width="8" stroke-dasharray="18 14" fill="none"/>'
    s += f'<path d="M420 420 L1500 420 M960 330 L960 560" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 12" opacity="0.5"/>'
    for (x, y), col in zip(pts, (a, W, "#5CC8FF", "#FF9F1C")):
        s += (f'<ellipse cx="{x}" cy="{y + 34}" rx="110" ry="30" fill="#0a1330" opacity="0.6"/><path d="M{x - 100} {y + 30} q100 -150 200 0z" fill="{col}"/>'
              f'<circle cx="{x}" cy="{y - 40}" r="14" fill="{col}"/><path d="M{x} {y - 26} V{y + 26}" stroke="{col}" stroke-width="6"/>')
    s += f'<circle cx="960" cy="445" r="52" fill="none" stroke="{a}" stroke-width="8"/><path d="M960 395 V495 M910 445 H1010" stroke="{a}" stroke-width="6"/>'
    return s


def tara(a):
    s = _bg("#1a1038", "#ff7b3a") + f'<circle cx="1480" cy="470" r="120" fill="#FFD23F" opacity="0.9"/>' + _sea(560, "#7a2d3a", "#2a1530", "#FFB86B")
    s += f'<path d="M420 520 H1380 L1300 600 H500 Z" fill="#0a1330"/><rect x="520" y="440" width="150" height="82" fill="{W}"/><rect x="545" y="410" width="100" height="32" fill="{MUTED}"/>'
    s += f'<rect x="1180" y="440" width="150" height="62" fill="#0a1330"/><rect x="740" y="478" width="380" height="44" rx="22" fill="{MUTED}"/>'
    s += f'<path d="M600 410 C560 340 640 300 590 240 C560 200 620 160 600 100" stroke="#1a1a2e" stroke-width="46" fill="none" stroke-linecap="round" opacity="0.8"/>'
    s += f'<polygon points="1180,440 1215,368 1250,440" fill="{a}"/><circle cx="1215" cy="500" r="16" fill="{a}"/>'
    return s


def mahanadi(a):
    s = _bg("#101a3f", "#3a2a1a") + f'<circle cx="1560" cy="250" r="90" fill="{a}" opacity="0.85"/>'
    cols = ["#2b2118", "#3a2c1e", "#4a3825", "#5a4430", "#6d5440"]
    for i, c in enumerate(cols):
        y = 380 + i * 62
        s += f'<path d="M{200 + i * 70} {y} H{1720 - i * 70} L{1640 - i * 70} {y + 62} H{280 + i * 70}Z" fill="{c}" stroke="#0a0805" stroke-width="3"/>'
    s += f'<path d="M0 640 H1920 V1080 H0Z" fill="#241a12"/>'
    s += f'<rect x="1180" y="560" width="170" height="70" rx="8" fill="{a}"/><rect x="1160" y="520" width="90" height="44" fill="#2a2a3a"/><circle cx="1210" cy="640" r="30" fill="#05081a"/><circle cx="1320" cy="640" r="30" fill="#05081a"/>'
    s += f'<path d="M600 520 L690 330 L780 520" stroke="{W}" stroke-width="14" fill="none"/><path d="M690 330 L980 300" stroke="{W}" stroke-width="10"/><path d="M980 300 V470" stroke="{MUTED}" stroke-width="5"/><rect x="950" y="470" width="60" height="40" fill="{a}"/>'
    s += "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r * .6}" fill="#0a0805"/>' for x, y, r in ((420, 610, 40), (500, 625, 26), (1500, 620, 36), (1600, 610, 28)))
    return s


def akvan(a):
    s = _bg("#0a1128", "#14244f") + _sea(600, "#16306b", "#0a1740", a)
    cx, cy = 960, 430
    s += f'<g transform="translate({cx} {cy})" fill="none" stroke-linecap="round">'
    for i, (r, op, w) in enumerate(((250, .25, 46), (200, .4, 40), (150, .6, 34), (100, .8, 28), (55, 1, 22))):
        s += f'<path d="M{-r} 0 A{r} {r} 0 1 1 {r * .2} {r * .98}" stroke="{a if i % 2 else W}" stroke-width="{w}" opacity="{op}" transform="rotate({i * 38})"/>'
    s += f'</g><circle cx="{cx}" cy="{cy}" r="30" fill="{NAVY}"/>'
    s += f'<path d="M1500 520 q80 -60 260 -30 L1920 520 V1080 H1500Z" fill="#2b2118"/><path d="M1500 520 q80 -60 260 -30 L1920 520" stroke="{a}" stroke-width="6" fill="none"/>'
    r = random.Random(9)
    s += "".join(f'<path d="M{x} {y} l-26 70" stroke="{MUTED}" stroke-width="4" opacity="0.5"/>' for x, y in ((r.randint(0, 1920), r.randint(260, 640)) for _ in range(60)))
    return s


def uproll(a):
    s = _bg("#0B1026", "#26316e") + _stars(30, 31, 300)
    s += f'<rect x="480" y="290" width="520" height="380" rx="20" fill="{W}" transform="rotate(-6 740 480)"/><rect x="560" y="300" width="520" height="380" rx="20" fill="{MUTED}" transform="rotate(3 820 490)"/>'
    s += f'<rect x="640" y="290" width="540" height="390" rx="20" fill="{W}"/>'
    for i in range(6):
        y = 340 + i * 54
        s += f'<rect x="690" y="{y}" width="260" height="14" rx="7" fill="#9aa4cf"/><rect x="990" y="{y}" width="130" height="14" rx="7" fill="#9aa4cf"/>'
        if i % 2 == 0:
            s += f'<path d="M1138 {y + 4} l12 14 l24 -30" stroke="{a}" stroke-width="10" fill="none" stroke-linecap="round"/>'
    s += f'<rect x="1260" y="430" width="360" height="250" rx="20" fill="{a}"/><rect x="1370" y="400" width="140" height="26" rx="10" fill="#05081a"/>'
    s += f'<g transform="rotate(-8 1440 330)"><rect x="1370" y="270" width="150" height="160" rx="10" fill="{W}"/><path d="M1396 350 l28 30 l52 -60" stroke="{NAVY}" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>'
    return s


def ladakh(a):
    s = _bg("#0a1030", "#2b4a8a") + _stars(80, 41, 420) + f'<circle cx="1500" cy="220" r="70" fill="#f2f2e8"/><circle cx="1530" cy="205" r="62" fill="#0a1030" opacity="0.18"/>'
    s += _mountains(640, "#1a2e5e", 7, 200, 380, True) + _mountains(720, "#0f1d44", 17, 90, 200)
    s += f'<path d="M180 470 Q960 580 1740 440" stroke="{MUTED}" stroke-width="4" fill="none"/>'
    for i, c in enumerate(("#FF4A4F", "#FFD23F", W, "#2EC4B6", "#5CC8FF") * 4):
        x = 190 + i * 76
        s += f'<polygon points="{x},{472 + 8 * abs(10 - i) / 3} {x + 44},{472 + 8 * abs(10 - i) / 3 + 4} {x + 22},{472 + 8 * abs(10 - i) / 3 + 46}" fill="{c}" opacity="0.9"/>'
    return s


def maha(a):
    s = _bg("#2a1a3a", "#f0803a") + f'<circle cx="960" cy="470" r="150" fill="{a}" opacity="0.9"/>' + f'<rect x="0" y="560" width="1920" height="520" fill="#6b4a2a"/>'
    s += f'<path d="M0 560 H1920" stroke="#3a2614" stroke-width="6"/>'
    r = random.Random(14)
    for i in range(22):
        x, y = r.randint(40, 1880), r.randint(590, 1000)
        s += f'<path d="M{x} {y} l{r.randint(40, 110)} {r.randint(-18, 18)} l{r.randint(-30, 30)} {r.randint(30, 60)} M{x + 50} {y} l-{r.randint(20, 60)} {r.randint(20, 50)}" stroke="#2a1a0c" stroke-width="5" fill="none"/>'
    s += f'<path d="M420 600 C430 480 420 420 410 330 M420 500 C360 470 340 430 330 390 M420 440 C480 420 500 380 500 340 M410 360 C370 350 350 330 350 300" stroke="#2a1a0c" stroke-width="14" fill="none" stroke-linecap="round"/>'
    s += f'<ellipse cx="1500" cy="640" rx="150" ry="22" fill="#2a1a0c" opacity="0.5"/><path d="M1440 640 q10 -80 40 -100 q-10 40 20 40 q30 -20 10 -80 q50 40 40 140z" fill="#a78458"/>'
    return s


def khet(a):
    s = _bg("#12306b", "#9fe3d0") + f'<circle cx="1480" cy="330" r="110" fill="#FFD23F"/>' + f'<polygon points="0,560 1920,560 1920,1080 0,1080" fill="#1B5E4F"/>'
    s += _mountains(560, "#2a6e60", 23, 40, 110)
    for i in range(11):
        xb = -200 + i * 260
        s += f'<polygon points="{xb + 100},560 {xb + 160},560 {xb + 400},1080 {xb - 60},1080" fill="{"#2f8a6c" if i % 2 else "#23705a"}"/>'
    for i in range(8):
        y = 590 + i * 62
        s += f'<path d="M0 {y} H1920" stroke="#0e3d33" stroke-width="3" opacity="0.5"/>'
    s += f'<rect x="1160" y="540" width="170" height="70" rx="8" fill="{a}"/><rect x="1230" y="490" width="100" height="56" fill="{W}"/><circle cx="1190" cy="620" r="40" fill="#05081a"/><circle cx="1310" cy="610" r="26" fill="#05081a"/>'
    return s


def q1(a):
    s = _bg("#05081a", "#10204a") + _stars(180, 51, 1000)
    s += f'<circle cx="260" cy="860" r="140" fill="#1B3FA0"/><path d="M160 820 q60 -50 130 -20 q-10 40 -60 50 q-30 20 -70 -30z" fill="#2EC4B6"/><circle cx="260" cy="860" r="140" fill="none" stroke="#5CC8FF" stroke-width="8" opacity="0.6"/>'
    s += f'<path d="M330 770 C700 620 1100 520 1480 420" stroke="{a}" stroke-width="6" stroke-dasharray="4 18" fill="none" stroke-linecap="round"/>'
    s += f'<g transform="translate(1560 380) rotate(-18)"><rect x="-44" y="-28" width="88" height="56" rx="8" fill="{W}"/><path d="M-44 0 H-150 M44 0 H150" stroke="{MUTED}" stroke-width="10"/><rect x="-190" y="-24" width="50" height="48" fill="{a}"/><rect x="140" y="-24" width="50" height="48" fill="{a}"/>'
    s += f'<path d="M0 -28 V-80" stroke="{MUTED}" stroke-width="8"/><path d="M-60 -130 Q0 -60 60 -130Z" fill="{W}"/></g>'
    s += f'<g stroke="{a}" stroke-width="5" fill="none" opacity="0.5"><circle cx="1560" cy="380" r="120"/><circle cx="1560" cy="380" r="190" stroke-dasharray="10 14"/></g>'
    return s


def q2(a):
    s = _bg("#12306b", "#bfe9ff") + f'<circle cx="400" cy="250" r="100" fill="#FFD23F"/>' + f'<rect x="0" y="560" width="1920" height="520" fill="#2a5a40"/>'
    for row in range(4):
        y = 580 + row * 90
        for col in range(9):
            x = 40 + col * 210 - row * 20
            w = 190 + row * 18
            s += f'<polygon points="{x + 20},{y} {x + w},{y} {x + w - 20},{y + 70 + row * 6} {x},{y + 70 + row * 6}" fill="#1B3FA0" stroke="{W}" stroke-width="4"/><path d="M{x + w / 2} {y} L{x + w / 2 - 10} {y + 70 + row * 6}" stroke="{W}" stroke-width="3"/>'
    for cx, sc in ((1500, 1.0), (1730, .75)):
        s += f'<path d="M{cx} 560 V250" stroke="{W}" stroke-width="{14 * sc}"/><g transform="translate({cx} 250)" stroke="{W}" stroke-width="{12 * sc}" stroke-linecap="round"><path d="M0 0 L0 -{150 * sc}"/><path d="M0 0 L{130 * sc} {75 * sc}"/><path d="M0 0 L-{130 * sc} {75 * sc}"/></g><circle cx="{cx}" cy="250" r="{14 * sc}" fill="{a}"/>'
    return s


def q3(a):
    return icj(a, scales=True)


def q4(a):
    s = _bg("#1b2a5c", "#5CC8FF") + _sea(640, "#2b7fb8", "#14507a", W)
    s += f'<path d="M280 640 q220 -170 440 0z" fill="#d9b779"/><path d="M280 640 q220 -80 440 0z" fill="#2EC4B6" opacity="0.8"/>'
    s += f'<path d="M500 560 C490 500 520 440 560 380" stroke="#5a3a1a" stroke-width="14" fill="none"/><path d="M560 380 q-90 -20 -140 40 M560 380 q60 -70 150 -40 M560 380 q-30 -80 20 -130 M560 380 q80 10 120 70" stroke="#2EC4B6" stroke-width="12" fill="none" stroke-linecap="round"/>'
    s += f'<path d="M1100 300 q-60 -10 -70 -60 q10 -70 90 -70 q40 -50 120 -20 q80 -10 100 60 q60 10 50 60 q-10 40 -60 40z" fill="#3a4a7a"/>'
    for i in range(10):
        x = 1070 + i * 34
        s += f'<path d="M{x} 350 l-18 {60 + (i % 3) * 30}" stroke="{W}" stroke-width="5" stroke-linecap="round" opacity="0.7"/>'
    for cx, cy, sc in ((1500, 560, 1.4), (1700, 500, 1.0)):
        s += f'<path d="M{cx} {cy - 70 * sc} C{cx} {cy - 70 * sc} {cx - 50 * sc} {cy} {cx - 50 * sc} {cy + 30 * sc} a{50 * sc} {50 * sc} 0 0 0 {100 * sc} 0 C{cx + 50 * sc} {cy} {cx} {cy - 70 * sc} {cx} {cy - 70 * sc}Z" fill="{a}" opacity="0.95" stroke="{W}" stroke-width="4"/>'
    return s


BUILD = {"intro": intro, "outro": lambda a: intro(a, True), "summit": summit, "icj": icj, "quad": quad, "tara": tara, "mahanadi": mahanadi,
         "akvan": akvan, "uproll": uproll, "ladakh": ladakh, "maha": maha, "khet": khet, "q1": q1, "q2": q2, "q3": q3, "q4": q4}


def scene(key, a):
    return f'<svg width="1920" height="1080" viewBox="0 0 1920 1080" preserveAspectRatio="none">{BUILD[key](a)}</svg>'
