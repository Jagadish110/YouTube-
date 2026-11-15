"""Render a feed-style preview of a LinkedIn post (text + card) for Jagadish to approve.

    python3 tools/linkedin_preview.py posts/linkedin/YYYY-MM-DD "Page name"

Reads post.md (the text between the two '---' lines) and card.png in that folder,
writes preview.png beside them. A dashed line marks roughly where the feed cuts to "…see more".
"""
import base64, html, os, sys
from playwright.sync_api import sync_playwright

folder, page_name = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "Your page name")
text = open(os.path.join(folder, "post.md")).read().split("\n---\n")[1].strip()
card = base64.b64encode(open(os.path.join(folder, "card.png"), "rb").read()).decode()

FOLD = 210  # characters LinkedIn usually shows before "…see more" on desktop (approximate)
cut = text.rfind("\n", 0, FOLD)
cut = cut if cut > 40 else FOLD
above, below = text[:cut], text[cut:]
e = lambda s: html.escape(s).replace("\n", "<br>")
initials = "".join(w[0] for w in page_name.split()[:2]).upper()

page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#f4f2ee;font-family:Inter,'Noto Color Emoji',sans-serif;color:#1f1f1f;padding:28px}}
.post{{width:555px;background:#fff;border-radius:10px;box-shadow:0 0 0 1px rgba(0,0,0,.08);overflow:hidden}}
.hd{{display:flex;gap:10px;padding:14px 16px 6px}}
.av{{width:48px;height:48px;border-radius:6px;background:#0b0a12;color:#8b3dff;font-weight:900;display:flex;align-items:center;justify-content:center;font-size:18px}}
.nm{{font-weight:700;font-size:14px}} .meta{{font-size:12px;color:#666;line-height:1.4}}
.tx{{padding:4px 16px 10px;font-size:14px;line-height:1.45;overflow-wrap:anywhere}}
.fold{{border-top:2px dashed #e5383b;margin:8px 0;position:relative}}
.fold span{{position:absolute;right:0;top:-10px;background:#fff;color:#e5383b;font-size:11px;font-weight:700;padding:0 4px}}
img{{display:block;width:555px;height:555px}}
.ft{{display:flex;justify-content:space-around;border-top:1px solid #eee;padding:10px 0;font-size:13px;color:#555;font-weight:600}}
.note{{width:555px;font-size:12px;color:#666;margin-top:10px}}
</style></head><body>
<div class="post"><div class="hd"><div class="av">{html.escape(initials)}</div><div>
<div class="nm">{html.escape(page_name)}</div><div class="meta">Company page · followers<br>now · 🌐</div></div></div>
<div class="tx">{e(above)}<div class="fold"><span>feed shows "…see more" about here</span></div>{e(below)}</div>
<img src="data:image/png;base64,{card}"><div class="ft"><span>Like</span><span>Comment</span><span>Repost</span><span>Send</span></div></div>
<div class="note">Preview only, approximate layout. Nothing has been posted.</div>
</body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 611, "height": 900}, device_scale_factor=2)
    pg.set_content(page)
    pg.wait_for_timeout(400)
    pg.screenshot(path=os.path.join(folder, "preview.png"), full_page=True)
    b.close()
print("preview", os.path.join(folder, "preview.png"))
