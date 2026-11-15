"""Render a YouTube thumbnail (1280x720) from an HTML file, plus a small copy to judge readability.

    python3 tools/thumbnail.py videos/NNN-slug/thumbnail/thumb.html

Writes thumb.png (1280x720, under 2 MB as YouTube requires) and thumb-small.png (320x180) beside the HTML.
Fonts: reference tools/fonts/*.woff2 with relative paths from the HTML file.
Prints any element that sticks out of the frame.
"""
import os, sys
from playwright.sync_api import sync_playwright

src = os.path.abspath(sys.argv[1])
d = os.path.dirname(src)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.goto("file://" + src)
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(400)
    bad = pg.evaluate("""[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();
        return r.width>0 && (r.left<-1||r.top<-1||r.right>1281||r.bottom>721) && !e.closest('[data-bleed]')}).map(e=>e.className||e.tagName)""")
    missing = pg.evaluate("[...document.fonts].filter(f=>f.status!=='loaded').map(f=>f.family)")
    pg.screenshot(path=os.path.join(d, "thumb.png"))
    small = b.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=0.25)
    small.goto("file://" + src); small.evaluate("document.fonts.ready"); small.wait_for_timeout(300)
    small.screenshot(path=os.path.join(d, "thumb-small.png"))
    b.close()
size = os.path.getsize(os.path.join(d, "thumb.png"))
print("thumb.png", round(size / 1024), "KB", "| off-frame:", bad or "none", "| fonts not loaded:", missing or "none")
if size > 2 * 1024 * 1024:
    print("WARNING: over 2 MB, YouTube will reject it")
