"""Video 005: Trendsplain Daily 2026-11-20. One sl.Scene per line of vo_script.txt (data in content.py).

Look: the fixed navy "Trendsplain signature" (CHANNEL.md): ground #0B1026, cards #102046, Anton headlines with one accent word,
Sora 800 body, ghost outlined number behind the headline, one drawn icon in a rounded card, source line at the bottom.
Run from this folder:  python3 build.py
"""
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenelib as sl
import content as ct

HERE = os.path.dirname(os.path.abspath(__file__))
import json
_m = json.load(open(os.path.join(HERE, "vo_marks.json")))
TOTAL = round(_m[-1]["end"] + 0.6, 2)
sl.setup(os.path.join(HERE, "vo_marks.json"), TOTAL)
sl.theme(
    ground="#0B1026", ink="#FFFFFF", quiet="#B8C1E6", up="#FF4A4F", down="#FF4A4F",
    panel="#102046", line="#24315F",
    head="'Anton', 'Inter', sans-serif", head_weight=400, head_case="uppercase",
    body="'Sora', 'Inter', sans-serif",
    fonts=[("Anton", 400, "assets/fonts/anton-latin-400-normal.woff2"),
           ("Sora", 800, "assets/fonts/sora-latin-800-normal.woff2"),
           ("Sora", 600, "assets/fonts/sora-latin-600-normal.woff2")],
    bg="background-image: linear-gradient(rgba(255,255,255,.035) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.035) 1px, transparent 1px); background-size: 80px 80px;",
)
W, MUTED, PANEL, NAVY = "#FFFFFF", "#B8C1E6", "#102046", "#0B1026"


# ---------- drawn icons (flat SVG, 400x400, no faces, no logos) ----------
def icon(kind, a):
    s = '<svg width="400" height="400" viewBox="0 0 400 400">'
    if kind == "globe":
        s += (f'<circle cx="200" cy="200" r="150" fill="#1B2D63" stroke="{a}" stroke-width="12"/>'
              f'<path d="M50 200 H350 M200 50 C120 120 120 280 200 350 C280 280 280 120 200 50 M80 120 H320 M80 280 H320" stroke="{MUTED}" stroke-width="8" fill="none"/>'
              f'<circle cx="270" cy="150" r="22" fill="{a}"/><circle cx="140" cy="250" r="16" fill="{W}"/>')
    elif kind == "gavel":
        s += (f'<g transform="rotate(-30 200 180)"><rect x="90" y="90" width="150" height="90" rx="18" fill="{a}"/><rect x="215" y="120" width="130" height="30" rx="10" fill="{MUTED}"/></g>'
              f'<rect x="90" y="300" width="230" height="40" rx="12" fill="{W}"/><rect x="130" y="260" width="150" height="40" rx="10" fill="{MUTED}"/>')
    elif kind == "handshake":
        s += (f'<circle cx="95" cy="200" r="50" fill="{a}"/><circle cx="305" cy="200" r="50" fill="{W}"/>'
              f'<circle cx="200" cy="95" r="50" fill="{MUTED}"/><circle cx="200" cy="305" r="50" fill="{a}" opacity="0.6"/>'
              f'<path d="M120 200 H280 M200 120 V280" stroke="{W}" stroke-width="10" stroke-dasharray="16 12" opacity="0.7"/>')
    elif kind == "tanker":
        s += (f'<path d="M0 290 C60 310 140 270 200 290 C260 310 340 270 400 290 V400 H0 Z" fill="#1B2D63"/>'
              f'<path d="M40 230 H360 L320 290 H80 Z" fill="{a}"/><rect x="90" y="180" width="60" height="50" fill="{W}"/>'
              f'<ellipse cx="230" cy="215" rx="110" ry="30" fill="{MUTED}"/><rect x="300" y="150" width="30" height="80" fill="{W}"/>'
              f'<path d="M200 90 q30 -40 0 -70 q-30 30 0 70" fill="{a}"/>')
    elif kind == "coal":
        s += (f'<path d="M20 340 L130 160 L200 260 L270 120 L380 340 Z" fill="#1B2D63" stroke="{MUTED}" stroke-width="8" stroke-linejoin="round"/>'
              f'<path d="M110 340 L170 270 L230 340 Z" fill="#05081a"/><circle cx="300" cy="90" r="38" fill="{a}"/>'
              f'<rect x="150" y="300" width="100" height="40" fill="{a}"/><path d="M150 300 L200 260 L250 300" stroke="{W}" stroke-width="8" fill="none"/>')
    elif kind == "cyclone":
        s += (f'<g fill="none" stroke="{a}" stroke-linecap="round" stroke-width="22"><path d="M200 200 m-150 0 a150 150 0 1 1 150 150"/>'
              f'<path d="M200 200 m-100 0 a100 100 0 1 1 100 100"/><path d="M200 200 m-50 0 a50 50 0 1 1 50 50"/></g>'
              f'<circle cx="200" cy="200" r="14" fill="{W}"/>')
    elif kind == "ballot":
        s += (f'<rect x="60" y="170" width="280" height="190" rx="22" fill="{a}"/><rect x="150" y="150" width="100" height="20" rx="8" fill="#05081a"/>'
              f'<g transform="rotate(-8 200 90)"><rect x="130" y="30" width="140" height="150" rx="10" fill="{W}"/><path d="M155 100 l25 28 l50 -56" stroke="{NAVY}" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>')
    elif kind == "mountain":
        s += (f'<path d="M0 360 L120 140 L190 250 L270 90 L400 360 Z" fill="#1B2D63" stroke="{MUTED}" stroke-width="8" stroke-linejoin="round"/>'
              f'<path d="M232 150 L270 90 L308 150 L270 134 Z" fill="{W}"/><path d="M95 180 L120 140 L145 182 L120 170 Z" fill="{W}"/><circle cx="330" cy="70" r="30" fill="{a}"/>'
              f'<path d="M0 360 H400" stroke="{a}" stroke-width="10"/>')
    elif kind == "drought":
        s += (f'<circle cx="300" cy="90" r="55" fill="{a}"/><path d="M0 330 H400 V400 H0 Z" fill="#6b4a2a"/>'
              f'<path d="M20 330 L60 290 L90 345 L140 290 L175 345 L225 295 L260 345 L310 292 L345 345 L385 300" stroke="#05081a" stroke-width="8" fill="none"/>'
              f'<path d="M150 330 C150 250 150 200 150 170 M150 250 C120 240 110 220 110 200 M150 220 C180 210 190 190 190 170" stroke="{MUTED}" stroke-width="12" fill="none" stroke-linecap="round"/>')
    elif kind == "field":
        s += (f'<path d="M0 300 H400 V400 H0 Z" fill="#1B5E4F"/>' +
              "".join(f'<g transform="translate({40 + n * 62} 0)"><path d="M0 300 V170" stroke="{a}" stroke-width="9"/>'
                      f'<ellipse cx="-8" cy="190" rx="9" ry="22" fill="{a}"/><ellipse cx="8" cy="170" rx="9" ry="22" fill="{a}"/><ellipse cx="-8" cy="150" rx="9" ry="22" fill="{a}"/></g>' for n in range(6)) +
              f'<circle cx="320" cy="70" r="44" fill="#FFD23F"/>')
    elif kind == "probe":
        s += (f'<circle cx="200" cy="200" r="22" fill="{a}"/><g stroke="{MUTED}" stroke-width="6" fill="none"><circle cx="200" cy="200" r="70"/><circle cx="200" cy="200" r="115" stroke-dasharray="10 12"/><circle cx="200" cy="200" r="160" stroke-dasharray="4 14"/></g>'
              f'<g transform="translate(300 90) rotate(35)"><rect x="-26" y="-16" width="52" height="32" rx="6" fill="{W}"/><path d="M-26 0 H-70 M26 0 H70" stroke="{a}" stroke-width="14"/><rect x="-100" y="-14" width="34" height="28" fill="{a}"/><rect x="66" y="-14" width="34" height="28" fill="{a}"/></g>')
    elif kind == "solar":
        s += (f'<circle cx="310" cy="80" r="50" fill="#FFD23F"/><path d="M60 330 L110 160 H350 L300 330 Z" fill="#1B3FA0" stroke="{W}" stroke-width="8" stroke-linejoin="round"/>'
              f'<path d="M80 245 H325 M200 160 L180 330 M270 160 L240 330 M135 160 L120 330" stroke="{W}" stroke-width="6"/><path d="M190 330 V380 M120 380 H270" stroke="{MUTED}" stroke-width="12"/>')
    elif kind == "drops":
        s += (f'<path d="M200 40 C200 40 90 170 90 250 a110 110 0 0 0 220 0 C310 170 200 40 200 40 Z" fill="{a}"/>'
              f'<path d="M150 260 a50 50 0 0 0 50 50" stroke="{W}" stroke-width="12" fill="none" stroke-linecap="round" opacity="0.8"/>'
              f'<path d="M330 120 C330 120 290 170 290 200 a40 40 0 0 0 80 0 C370 170 330 120 330 120 Z" fill="{W}" opacity="0.8"/>')
    return s + "</svg>"


def headline_html(h, a):
    return re.sub(r"\*(.+?)\*", lambda m: f'<span style="color:{a}">{m.group(1)}</span>', h)


def numfmt(prefix, suffix, dec):
    return f'(v)=>"{prefix}"+Number(v.toFixed({dec})).toLocaleString("en-US",{{minimumFractionDigits:{dec},maximumFractionDigits:{dec}}})+"{suffix}"'


def big_size(text):
    n = len(text)
    return 128 if n <= 12 else (100 if n <= 18 else (82 if n <= 26 else 66))


STORY = {k: (lab, ic, src) for k, lab, ic, src in ct.STORIES}
order = {}
for k, *_ in ct.LINES:
    pass
S = []
ghost_idx = {}
for n, (k, *_r) in enumerate(ct.STORIES):
    ghost_idx[k] = str(n).zfill(2) if k not in ("intro", "outro") else ("★" if k == "outro" else "14")
ghost_idx.update({"q1": "+1", "q2": "+2", "q3": "+3", "q4": "+4"})
# ghost number = story number for the ten stories
for n, k in enumerate(["summit", "icj", "quad", "tara", "mahanadi", "akvan", "uproll", "ladakh", "maha", "khet"], 1):
    ghost_idx[k] = str(n).zfill(2)

for i, (key, spoken, head, card) in enumerate(ct.LINES):
    a = ct.ACCENTS[key]
    label, ic, src = STORY[key]
    s = sl.Scene(f"s{i:02d}", i)
    s.E("ghost", ghost_idx[key], sl.C(40, 560, f"font-family:'Anton';color:transparent;-webkit-text-stroke:4px {a};opacity:0.07;line-height:1;"), 0.0, anim="fade", cls="hero", attrs="data-layout-allow-occlusion")
    s.E("kick", label, sl.C(52, 32, f"color:{a};letter-spacing:0.16em;font-weight:800;"), 0.05, anim="blur")
    s.E("head", headline_html(head, a), sl.C(118, 104, f"color:{W};padding:0 120px;"), 0.15, anim="blur", cls="hero")
    s.E("card", "", f"left:192px;top:340px;width:1536px;height:580px;border-radius:26px;background:{PANEL};border:3px solid {a}55;", 0.3, anim="fade")
    kind = card[0]
    if kind == "title":
        s.E("big", card[1], sl.C(430, 260, f"color:{a};"), 0.5, anim="pop", cls="hero")
        s.E("small", card[2], sl.C(760, 44, f"color:{MUTED};font-weight:600;"), 1.0, anim="blur")
    else:
        s.E("icon", icon(ic, a), "left:232px;top:430px;width:400px;height:400px;", 0.45, anim="pop")
        if kind == "num":
            _, to, pre, suf, dec, small = card
            ln = len(f"{pre}{to:,.{dec}f}{suf}")
            nsz = 150 if ln <= 7 else (120 if ln <= 10 else (98 if ln <= 14 else 80))
            s.E("big", f"{pre}0{suf}", f"left:680px;width:1000px;text-align:center;top:{500 if nsz > 100 else 520}px;font-size:{nsz}px;color:{a};white-space:nowrap;font-weight:800;",
                0.6, anim=("count", to, numfmt(pre, suf, dec), 1.4), cls="tnum")
            s.E("small", small, f"left:700px;width:960px;text-align:center;top:690px;font-size:40px;color:{MUTED};font-weight:600;", 1.2, anim="blur")
        else:
            _, big, small = card
            sz = big_size(big)
            s.E("big", big, f"left:680px;width:1000px;text-align:center;top:{470 if sz > 100 else 440}px;font-size:{sz}px;line-height:1.12;color:{W};font-weight:800;", 0.6, anim="blur")
            s.E("small", small, f"left:680px;width:1000px;text-align:center;top:720px;font-size:40px;color:{a};font-weight:600;", 1.1, anim="blur")
    s.E("src", src, "left:96px;bottom:60px;font-size:28px;font-weight:600;color:#B8C1E6;opacity:0.85;", 0.3, anim="fade", cls="src")
    S.append(s)

sl.write_project(os.path.join(HERE, "project"), S)
print("scenes", len(S), "total", TOTAL)
