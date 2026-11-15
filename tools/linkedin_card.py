"""Make the 1200x1200 LinkedIn image card in the channel style.

    python3 tools/linkedin_card.py card.json out.png

card.json: {"date": "15 NOV 2026", "headline": "NVIDIA'S CEO", "accent": "RESIGNS",
            "accent_color": "down" | "up", "bullets": ["...", "..."]}
Headline + accent should stay under about 24 characters; at most 3 short bullets.
"""
import base64, html, json, os, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(sys.argv[1]))
out = os.path.abspath(sys.argv[2])
font = base64.b64encode(open(os.path.join(ROOT, "fonts", "archivo-black-latin-400-normal.woff2"), "rb").read()).decode()
col = "#ff3b47" if spec.get("accent_color", "up") == "down" else "#8b3dff"
e = html.escape
bul = "".join(f'<div class="l"><i>+</i> {e(b)}</div>' for b in spec.get("bullets", [])[:3])
page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo Black';src:url(data:font/woff2;base64,{font}) format('woff2');}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:1200px;background:#0b0a12;color:#fff;font-family:Inter,sans-serif;position:relative;overflow:hidden}}
.k{{position:absolute;left:96px;top:110px;font-weight:900;letter-spacing:.14em;font-size:30px;color:#a7a3b8}}
.k b{{color:#8b3dff}}
.h{{position:absolute;left:96px;top:210px;width:1010px;font-family:'Archivo Black',sans-serif;font-size:112px;line-height:1.04;letter-spacing:-.02em}}
.h span{{color:{col}}}
.foot{{position:absolute;left:96px;right:96px;bottom:90px}}
.bar{{width:120px;height:10px;background:#8b3dff;border-radius:5px;margin-bottom:44px}}
.l{{font-size:42px;font-weight:700;line-height:1.25;margin-bottom:28px}}
.l i{{font-style:normal;color:#8b3dff}}
.f{{font-size:30px;color:#a7a3b8;margin-top:36px}}
</style></head><body>
<div class="k"><b>AI BRIEF</b> · {e(spec['date'])}</div>
<div class="h">{e(spec['headline'])} <span>{e(spec.get('accent', ''))}</span></div>
<div class="foot"><div class="bar"></div>{bul}<div class="f">Daily AI news, explained · sources in post</div></div>
</body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 1200})
    pg.set_content(page)
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(300)
    over = pg.evaluate("(()=>{const h=document.querySelector('.h').getBoundingClientRect(),f=document.querySelector('.foot').getBoundingClientRect();return h.bottom>f.top-30})()")
    pg.screenshot(path=out)
    b.close()
print("card", out, "OVERLAP: shorten headline or bullets" if over else "ok")
