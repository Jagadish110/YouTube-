"""Instagram carousel (1080x1350, 4:5): top 10 world stories, one slide each + cover + closing slide.

    python3 build_carousel.py     -> output/slide-00.png ... slide-11.png (and output/html/*.html)
Every slide has its own accent colour, a big ghost number, a headline, one drawn or photo visual, three facts and a source line.
Facts come from sources.md (all opened on 19 Nov 2026). Photos in assets/ were supplied by Jagadish.
"""
import base64, os, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
NAVY = "#0B1026"


def font(name, fam, w):
    b = base64.b64encode(open(os.path.join(ROOT, "tools/fonts", name), "rb").read()).decode()
    return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}"


def img(name):
    mime = "image/png" if name.endswith("png") else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(open(os.path.join(HERE, "assets", name), "rb").read()).decode()


LEADERS, DRONE, WAREHOUSE, HUANG, LOGO = (img(x) for x in ("leaders.jpg", "drone.png", "warehouse.jpg", "huang.jpg", "nvidia_logo.png"))


def photo(src, label, pos="50% 50%", h=330):
    return (f'<div class="ph" style="height:{h}px"><img src="{src}" style="object-position:{pos}"><span class="tag">{label}</span></div>')


def flag_fr(): return '<svg width="170" height="113" viewBox="0 0 3 2"><rect width="1" height="2" fill="#0055A4"/><rect x="1" width="1" height="2" fill="#fff"/><rect x="2" width="1" height="2" fill="#EF4135"/></svg>'
def flag_ua(): return '<svg width="170" height="113" viewBox="0 0 3 2"><rect width="3" height="1" fill="#0057B7"/><rect y="1" width="3" height="1" fill="#FFD700"/></svg>'


V = {}
V[1] = photo(LEADERS, "File photo · Putin, Trump, Xi", "50% 30%")
V[2] = lambda a: f'''<div class="row" style="height:330px;gap:26px"><div class="ph" style="width:330px;height:330px;flex:none"><img src="{HUANG}"><span class="tag">Jensen Huang</span></div>
 <div style="flex:1;display:flex;flex-direction:column;justify-content:space-between"><div style="background:#fff;border-radius:22px;padding:18px 26px"><img src="{LOGO}" style="height:76px;display:block"></div>
 <div class="an" style="font-size:150px;color:{a};line-height:1">$115.8B</div><div class="sm">REVENUE · UP 103% IN A QUARTER</div></div></div>'''
V[3] = lambda a: f'''<svg width="960" height="330" viewBox="0 0 960 330"><rect width="960" height="330" rx="26" fill="#102046"/>
 <path d="M0 0 H960 V92 C820 80 700 120 560 100 C430 84 300 110 0 96 Z" fill="#2c3c6e"/><path d="M0 330 V250 C170 262 300 232 470 250 C640 266 800 240 960 262 V330 Z" fill="#2c3c6e"/>
 <text x="40" y="60" fill="#c9d3f5" font-family="Sora" font-weight="800" font-size="30">IRAN</text><text x="40" y="312" fill="#c9d3f5" font-family="Sora" font-weight="800" font-size="30">BAHRAIN · GULF STATES</text>
 <circle cx="640" cy="108" r="26" fill="none" stroke="{a}" stroke-width="7"/><circle cx="640" cy="108" r="11" fill="{a}"/><text x="680" y="100" fill="{a}" font-family="Sora" font-weight="800" font-size="30">QESHM ISLAND</text>
 <path d="M260 255 C300 190 360 140 430 120" stroke="#FFB020" stroke-width="7" stroke-dasharray="14 12" fill="none"/><text x="250" y="206" fill="#FFB020" font-family="Sora" font-weight="800" font-size="26" transform="rotate(-22 250 206)">DRONES</text>
 <path d="M740 140 C700 170 660 190 600 214" stroke="{a}" stroke-width="9" fill="none" stroke-linecap="round"/><text x="700" y="196" fill="#fff" font-family="Sora" font-weight="800" font-size="26">US STRIKE</text>
 <text x="480" y="170" fill="#8fa0d6" font-family="Sora" font-weight="700" font-size="24" text-anchor="middle">STRAIT OF HORMUZ</text></svg>'''
V[4] = lambda a: f'''<svg width="960" height="330" viewBox="0 0 960 330"><rect width="960" height="330" rx="26" fill="#102046"/>
 <path d="M960 0 V330 H700 C720 260 760 220 740 160 C725 110 760 60 800 0 Z" fill="#2c3c6e"/><text x="835" y="300" fill="#c9d3f5" font-family="Sora" font-weight="800" font-size="30" text-anchor="middle">INDIA</text>
 <g fill="none" stroke="{a}" stroke-linecap="round"><path d="M290 165 m-110 0 a110 110 0 1 1 110 110" stroke-width="14"/><path d="M290 165 m-70 0 a70 70 0 1 1 70 70" stroke-width="14"/><path d="M290 165 m-30 0 a30 30 0 1 1 30 30" stroke-width="14"/></g>
 <path d="M420 165 H720" stroke="{a}" stroke-width="8" stroke-dasharray="16 12"/><path d="M702 148 L728 165 L702 182" fill="none" stroke="{a}" stroke-width="8" stroke-linecap="round"/>
 <circle cx="735" cy="165" r="14" fill="#FF5A5F"/><text x="520" y="132" fill="#fff" font-family="Sora" font-weight="800" font-size="30">LANDFALL ~NOON, 20 NOV</text><text x="520" y="216" fill="{a}" font-family="Sora" font-weight="800" font-size="30">NELLORE – TUNI</text></svg>'''
V[5] = lambda a: '<div class="row" style="flex-wrap:wrap;gap:16px;height:330px;align-content:center">' + "".join(
    f'<span class="pill" style="border-color:{a}"><i style="background:#FF5A5F"></i>{n}</span>' for n in ("APPLE", "MARRIOTT", "NSA NET", "UNITED", "FAA", "JPMORGAN CHASE", "MICROSOFT")) + "</div>"
V[6] = lambda a: f'''<svg width="960" height="330" viewBox="0 0 960 330"><rect width="960" height="330" rx="26" fill="#102046"/>
 <path d="M60 280 H900" stroke="#555a80" stroke-width="3"/>
 <rect x="140" y="{280 - 117 * 1.1}" width="250" height="{117 * 1.1}" rx="12" fill="#4a5385"/><rect x="560" y="{280 - 190 * 1.1}" width="250" height="{190 * 1.1}" rx="12" fill="{a}"/>
 <text x="265" y="{280 - 117 * 1.1 - 14}" text-anchor="middle" fill="#fff" font-family="Anton" font-size="56">$117M</text><text x="685" y="{280 - 190 * 1.1 - 14}" text-anchor="middle" fill="{a}" font-family="Anton" font-size="56">~$190M</text>
 <text x="265" y="316" text-anchor="middle" fill="#b8c1e6" font-family="Sora" font-weight="800" font-size="24">OLD RECORD · 2022</text><text x="685" y="316" text-anchor="middle" fill="#fff" font-family="Sora" font-weight="800" font-size="24">THIS WEEK · REPORTED</text></svg>'''
V[7] = lambda a: f'''<div class="row" style="height:330px;justify-content:space-around"><div style="text-align:center">{flag_fr()}<div class="sm" style="margin-top:14px">FRANCE</div></div>
 <div style="text-align:center"><svg width="260" height="60" viewBox="0 0 260 60"><path d="M10 30 H220" stroke="{a}" stroke-width="9" stroke-dasharray="18 12"/><path d="M200 8 L240 30 L200 52" fill="none" stroke="{a}" stroke-width="9" stroke-linecap="round"/></svg><div class="sm" style="color:{a}">TRAINING · MAINTENANCE</div></div>
 <div style="text-align:center">{flag_ua()}<div class="sm" style="margin-top:14px">UKRAINE</div></div></div>'''
V[8] = lambda a: f'''<div class="row" style="height:330px;gap:30px"><div style="flex:1;background:#102046;border-radius:26px;height:100%;padding:26px 30px"><div class="an" style="font-size:190px;color:{a};line-height:1">18</div><div class="sm">PAGE DRAFT TEXT</div></div>
 <div style="flex:1;background:#102046;border-radius:26px;height:100%;padding:26px 30px"><div class="an" style="font-size:190px;color:#fff;line-height:1">2030</div><div class="sm">NET ZERO · WEALTHY NATIONS</div></div></div>'''
V[9] = lambda a: f'<div class="ph" style="height:330px"><img src="{DRONE}" style="object-position:50% 45%"><span class="tag">Illustration · a camera drone</span><span class="big" style="background:{a}">128 COUNTRIES</span></div>'
V[10] = lambda a: f'<div class="ph" style="height:330px"><img src="{WAREHOUSE}" style="object-position:50% 60%"><span class="tag">File photo · Wildberries warehouse fire</span><span class="big" style="background:{a}">145 SANCTIONED</span></div>'

S = [
    ("DIPLOMACY", "#5CC8FF", "TRUMP, XI AND PUTIN <em>MEET TODAY</em>",
     ["Shenzhen, China, on the sidelines of the APEC summit", "Trump–Xi lunch at 12:45, three-way talks at 14:30 (local time)", "A senior US official: “We do not expect to get to any kind of agreement”"],
     "Source: Newsquawk, 19 Nov"),
    ("TECH", "#76B900", "NVIDIA'S BOARD SAYS <em>NO TO HUANG</em>",
     ["Revenue $115.8 billion, up 103% in one quarter", "Huang offered to return; the board “does not intend to reinstate” him", "Colette Kress stays interim CEO while the search continues"],
     "Sources: Nvidia results (SEC) · The Next Web"),
    ("WAR", "#FF5A5F", "US STRIKES IRAN'S <em>QESHM ISLAND</em>",
     ["US warplanes hit an IRGC missile launch site, calling it self-defence", "It followed Iran's third attack on Bahrain in under a week", "Centcom: no US injuries. Iran's media: no casualties on Qeshm"],
     "Source: The National, 17 Nov"),
    ("INDIA", "#FFD23F", "CYCLONE <em>AKVAN</em> HEADS FOR ANDHRA",
     ["Forecast to cross Andhra Pradesh around noon on 20 Nov", "Winds 120–130 km/h, gusting to 145. Odisha has 74 rescue teams out", "The third cyclone over the Bay of Bengal in three weeks"],
     "Source: PTI via ThePrint (forecast as of 16 Nov)"),
    ("TECH", "#FF9F1C", "7 US OUTAGES, <em>NO ATTACK FOUND</em>",
     ["Banking, airlines, hotels, Microsoft 365, Apple and the NSA's NSA Net", "Chase, United and Microsoft each said there was no sign of a cyberattack", "Apple blamed an internal update"],
     "Source: AP via The Philadelphia Inquirer, 17 Nov"),
    ("ART", "#C77DFF", "A VAN GOGH <em>BREAKS THE RECORD</em>",
     ["“Blossoming Chestnut Trees” (1890), sold at Sotheby's New York on 18 Nov", "Estimated at $180 million. The old record is $117 million, from 2022", "The heirs of a past owner disputed its 1936 sale; both families settled"],
     "Sources: The Art Newspaper · Ocula. Final price as reported"),
    ("EUROPE", "#4D9DE0", "FRANCE'S <em>SECRET MISSION</em> IN UKRAINE",
     ["RFI: small French teams in Ukraine since at least summer 2026", "Their jobs: training and maintaining Caesar guns and Mirage 2000 jets", "Russia: “direct participation”. France: “not co-belligerents”"],
     "Source: Euronews (French), 17 Nov"),
    ("CLIMATE", "#2EC4B6", "COP31 DRAFT: <em>PHASE OUT</em> FOSSIL FUELS",
     ["Co-host Australia published the draft at the talks in Antalya, Türkiye", "It asks wealthy nations for net zero by 2030", "EU envoy: it could make talks “untenable”. Talks end Friday"],
     "Source: Al Jazeera, 17 Nov"),
    ("AI", "#FF70A6", "KILLER-ROBOT <em>TALKS</em> IN GENEVA",
     ["128 countries at a UN weapons-convention review, running to 20 Nov", "Human Rights Watch counts 76 states backing negotiations", "The US proposes five more years toward a non-binding text"],
     "Source: Tech Times, 16 Nov"),
    ("BUSINESS", "#F4A261", "EU SANCTIONS <em>WILDBERRIES</em> BOSS",
     ["Tatyana Kim was added on 16 Nov, in a package of 145 names", "EU draft: Wildberries acts as “a supply network for the Russian military”", "Wildberries says it has no assets or operations in the EU"],
     "Source: Meduza, 16 Nov"),
]

CSS = f'''{font("anton-latin-400-normal.woff2", "Anton", 400)}{font("sora-latin-800-normal.woff2", "Sora", 800)}{font("sora-latin-600-normal.woff2", "Sora", 600)}
*{{box-sizing:border-box}} html,body{{margin:0;width:1080px;height:1350px;overflow:hidden;background:{NAVY};color:#fff;font-family:Sora}}
.bg{{position:absolute;inset:0}} .abs{{position:absolute}} .an{{font-family:Anton;text-transform:uppercase}}
.row{{display:flex;align-items:center}} .sm{{font:800 26px Sora;letter-spacing:3px;color:#b8c1e6}}
.ph{{position:relative;width:100%;border-radius:26px;overflow:hidden;border:5px solid var(--a)}} .ph img{{width:100%;height:100%;object-fit:cover;display:block}}
.tag{{position:absolute;left:16px;bottom:14px;padding:6px 14px;border-radius:12px;background:rgba(0,0,0,.68);font:800 24px Sora}}
.big{{position:absolute;right:16px;top:16px;padding:10px 22px;border-radius:14px;color:{NAVY};font:400 56px Anton;letter-spacing:1px}}
.pill{{display:inline-flex;align-items:center;gap:12px;padding:14px 26px;border:3px solid;border-radius:40px;background:#13204a;font:800 36px Sora}} .pill i{{width:16px;height:16px;border-radius:50%;display:inline-block}}
.fact{{display:flex;gap:22px;align-items:flex-start;margin-bottom:20px;font:600 35px/1.22 Sora}} .fact b{{flex:none;width:52px;height:52px;border-radius:50%;background:var(--a);color:{NAVY};font:800 28px/52px Sora;text-align:center}}
em{{font-style:normal;color:var(--a)}}
'''


def slide(n):
    cat, a, head, facts, src = S[n - 1]
    vis = V[n]; vis = vis(a) if callable(vis) else vis
    dots = "".join(f'<i style="width:{34 if i == n else 14}px;height:14px;border-radius:8px;background:{a if i == n else "#3a4372"};display:inline-block;margin-right:10px"></i>' for i in range(1, 11))
    fl = "".join(f"<div class='fact'><b>{i + 1}</b><div>{t}</div></div>" for i, t in enumerate(facts))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS} :root{{--a:{a}}}</style></head><body>
<div class="bg" style="background:radial-gradient(800px 600px at 85% 0%,{a}44,transparent 70%),radial-gradient(700px 500px at 0% 100%,{a}22,transparent 70%)"></div>
<div class="bg" style="background-image:linear-gradient(rgba(255,255,255,.04) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.04) 2px,transparent 2px);background-size:60px 60px"></div>
<div class="abs an" style="right:30px;top:-30px;font-size:420px;line-height:1;color:transparent;-webkit-text-stroke:3px {a}55">{n:02d}</div>
<div class="abs" style="left:60px;top:56px;display:flex;gap:16px;align-items:center"><span style="background:{a};color:{NAVY};font:800 28px Sora;padding:10px 24px;border-radius:30px;letter-spacing:3px">{cat}</span><span style="font:800 28px Sora;color:#b8c1e6;letter-spacing:3px">{n} / 10</span></div>
<div class="abs an" style="left:60px;top:140px;width:900px;font-size:116px;line-height:1.02">{head}</div>
<div class="abs" style="left:60px;top:470px;width:960px">{vis}</div>
<div class="abs" style="left:60px;top:830px;width:960px">{fl}</div>
<div class="abs" style="left:60px;top:1235px;width:960px;font:600 26px Sora;color:#9ba6d6">{src}</div>
<div class="abs" style="left:60px;top:1288px">{dots}</div>
<div class="abs" style="right:60px;top:1272px;font:800 30px Sora;color:{a};letter-spacing:3px">{"SWIPE  →" if n < 10 else "ONE MORE  →"}</div>
</body></html>'''


def cover():
    chips = "".join(f'<span class="pill" style="border-color:{c}"><i style="background:{c}"></i>{t}</span>' for c, t in
                    (("#5CC8FF", "TRUMP · XI · PUTIN"), ("#76B900", "NVIDIA"), ("#FF5A5F", "IRAN"), ("#FFD23F", "CYCLONE AKVAN"), ("#C77DFF", "VAN GOGH"), ("#2EC4B6", "COP31")))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS} :root{{--a:#FFD23F}}</style></head><body>
<div class="bg" style="background:radial-gradient(900px 700px at 80% 20%,#FFD23F55,transparent 70%),radial-gradient(800px 600px at 0% 90%,#5CC8FF44,transparent 70%)"></div>
<div class="bg" style="background-image:linear-gradient(rgba(255,255,255,.05) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.05) 2px,transparent 2px);background-size:60px 60px"></div>
<div class="abs" style="left:60px;top:70px;font:800 32px Sora;letter-spacing:6px;color:#FFD23F">THURSDAY · 19 NOVEMBER 2026</div>
<div class="abs an" style="left:50px;top:120px;font-size:700px;line-height:1;color:#FFD23F">10</div>
<div class="abs an" style="left:60px;top:780px;font-size:150px;line-height:1">STORIES<br><span style="color:#FFD23F">GOING VIRAL</span></div>
<div class="abs row" style="left:60px;top:1100px;width:960px;flex-wrap:wrap;gap:14px;font-size:30px">{chips}</div>
<div class="abs" style="left:60px;top:1268px;font:800 32px Sora;color:#fff">@trendsplain</div>
<div class="abs" style="right:60px;top:1268px;font:800 32px Sora;color:#FFD23F;letter-spacing:3px">SWIPE  →</div></body></html>'''


def closing():
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS} :root{{--a:#FF4A4F}}</style></head><body>
<div class="bg" style="background:radial-gradient(800px 700px at 50% 35%,#FF4A4F44,transparent 70%)"></div>
<div class="bg" style="background-image:linear-gradient(rgba(255,255,255,.04) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.04) 2px,transparent 2px);background-size:60px 60px"></div>
<div class="abs" style="left:0;width:1080px;top:150px;text-align:center"><svg width="380" height="380" viewBox="150 132 230 243"><path d="M160 142 H322 V151 H167 V195 H318 V201 H160 Z" fill="#FF4A4F"/><path d="M160 201 L215 262 V201 Z" fill="#FF4A4F"/><path d="M318 142 H322 L370 188 V250 H320 V365 L268 318 V201 H318 Z" fill="#FF4A4F"/></svg></div>
<div class="abs an" style="left:0;width:1080px;top:560px;text-align:center;font-size:150px;line-height:1">Trend<span style="color:#FF4A4F">splain</span></div>
<div class="abs" style="left:0;width:1080px;top:740px;text-align:center;font:600 40px Sora;color:#c9cfe6">Viral topics, explained in plain words.</div>
<div class="abs row" style="left:130px;top:850px;gap:40px"><span class="pill" style="border-color:#FF4A4F;font-size:44px;padding:22px 44px">SAVE</span><span class="pill" style="border-color:#fff;font-size:44px;padding:22px 44px">SHARE</span><span class="pill" style="border-color:#FFD23F;font-size:44px;padding:22px 44px">FOLLOW</span></div>
<div class="abs" style="left:60px;width:960px;top:1060px;text-align:center;font:600 30px/1.4 Sora;color:#9ba6d6">Every fact was checked against the source named on its slide.<br>Reported claims are marked as reported.</div>
<div class="abs" style="left:0;width:1080px;top:1230px;text-align:center;font:800 46px Sora;color:#FFD23F">@trendsplain</div></body></html>'''


def main():
    os.makedirs(os.path.join(HERE, "output", "html"), exist_ok=True)
    pages = [("slide-00", cover())] + [(f"slide-{n:02d}", slide(n)) for n in range(1, 11)] + [("slide-11", closing())]
    for name, h in pages:
        open(os.path.join(HERE, "output", "html", name + ".html"), "w").write(h)
    if len(sys.argv) > 1 and sys.argv[1] == "html":
        return
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for name, _ in pages:
            pg.goto("file://" + os.path.join(HERE, "output", "html", name + ".html")); pg.evaluate("document.fonts.ready.then(()=>1)")
            pg.screenshot(path=os.path.join(HERE, "output", name + ".png"))
        b.close()
    print("slides:", len(pages))


main()
