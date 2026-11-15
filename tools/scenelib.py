"""Scene library: builds HyperFrames scene files timed to voiceover marks.

Usage in a per-video build script:
    import scenelib as sl
    sl.setup("vo_marks.json", total_seconds)
    s = sl.Scene("intro", 0); s.E("t", "TITLE", sl.C(400, 120), 0.1, cls="hero"); ...
    sl.write_project("project", [s, ...])
"""
import json, os

MARKS, LEAD, TOTAL = [], 0.2, 0.0

# Per-video look. Every video sets its own THEME with sl.theme(...) so videos never share one design.
# Defaults = video 001's dark/purple look.
THEME = dict(
    ground="#0b0a12", ink="#ffffff", quiet="#a7a3b8", up="#8b3dff", down="#ff3b47",
    panel="#16141f", line="#2a2740",
    head="'Archivo Black', sans-serif", head_weight=400, head_case="none",
    body="'Inter', sans-serif",
    fonts=[],          # [(family, weight, "assets/fonts/file.woff2"), ...] copied into the project
    bg="",             # extra CSS for #bg (gradients, patterns)
)


def theme(**kw):
    THEME.update(kw)


def setup(marks_path, total, lead=0.2):
    global MARKS, LEAD, TOTAL
    MARKS, LEAD, TOTAL = json.load(open(marks_path)), lead, total


def sstart(i):
    return 0.0 if i == 0 else round(MARKS[i]["start"] - LEAD, 2)


def C(top, size, extra=""):
    return f"left:0;width:1920px;text-align:center;top:{top}px;font-size:{size}px;{extra}"


def L(left, top, size, extra=""):
    return f"left:{left}px;top:{top}px;font-size:{size}px;{extra}"


class Scene:
    def __init__(self, name, i, j=None):
        self.name, self.i, self.j = name, i, (j if j is not None else i)
        self.start = sstart(i)
        self.end = sstart(self.j + 1) if self.j + 1 < len(MARKS) else TOTAL
        self.dur = round(self.end - self.start, 2)
        self.els, self.js, self.css = [], [], []

    def P(self, phrase, line=None, off=-0.1):
        m = MARKS[line if line is not None else self.i]
        k = m["text"].index(phrase)
        t = m["start"] + (k / len(m["text"])) * (m["end"] - m["start"])
        return round(max(0.05, t - self.start + off), 2)

    def E(self, eid, html, style, at, anim="blur", out=None, cls="", tag="div", attrs=""):
        self.els.append(dict(id=f"{self.name}-{eid}", html=html, style=style, at=round(at, 2), anim=anim, out=out, cls=cls, tag=tag, attrs=attrs))
        return f"#{self.name}-{eid}"

    def J(self, code):
        self.js.append(code)

    def render(self):
        css = [
            "#root{position:absolute;inset:0;overflow:hidden;color:var(--ink);font-family:var(--body);font-weight:700;}",
            f".hero{{font-family:var(--head);font-weight:{THEME['head_weight']};letter-spacing:-0.02em;line-height:1.05;text-transform:{THEME['head_case']};}}",
            ".q{color:var(--quiet);}.up{color:var(--up);}.down{color:var(--down);}",
            ".kick{letter-spacing:0.14em;font-weight:900;}",
            ".el{position:absolute;}",
            ".pill{display:inline-block;padding:20px 40px;border:4px solid var(--up);border-radius:999px;}",
            ".img{display:block;}.card{background:var(--panel);border-radius:28px;}",
            ".box{border:4px solid var(--quiet);border-radius:24px;display:flex;align-items:center;justify-content:center;text-align:center;}",
            ".src{left:96px;bottom:64px;font-size:28px;font-weight:400;color:var(--quiet);opacity:0.75;}",
            ".tnum{font-variant-numeric:tabular-nums;}",
        ] + self.css
        body, js = [], ["const tl = gsap.timeline({ paused: true });"]
        for n, e in enumerate(self.els):
            end = (e["out"] + 0.2) if e["out"] else self.dur
            d = round(end - e["at"], 2)
            css.append(f"#{e['id']}{{{e['style']}}}")
            body.append(
                f"<{e['tag']} id=\"{e['id']}\" class=\"el clip {e['cls']}\" data-start=\"{e['at']}\" data-duration=\"{d}\" data-track-index=\"{n + 1}\" {e['attrs']}>{e['html']}</{e['tag']}>"
            )
            s, at, a = f"#{e['id']}", e["at"], e["anim"]
            if a == "blur":
                js.append(f'tl.fromTo("{s}",{{opacity:0,filter:"blur(10px)"}},{{opacity:1,filter:"blur(0px)",duration:0.22,ease:"power4.out"}},{at});')
            elif a == "fade":
                js.append(f'tl.fromTo("{s}",{{opacity:0}},{{opacity:1,duration:0.3,ease:"power2.out"}},{at});')
            elif a == "pop":
                js.append(f'tl.fromTo("{s}",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:0.35,ease:"expo.out"}},{at});')
            elif a == "stamp":
                js.append(f'tl.fromTo("{s}",{{opacity:0,scale:2.2,rotation:-9}},{{opacity:1,scale:1,rotation:-9,duration:0.24,ease:"power3.in"}},{at});')
            elif a == "wipe":
                js.append(f'tl.fromTo("{s}",{{clipPath:"inset(0 100% 0 0)"}},{{clipPath:"inset(0 0% 0 0)",duration:0.5,ease:"power3.out"}},{at});')
            elif isinstance(a, tuple) and a[0] == "count":
                _, to, fmt, cdur = a
                v = f"o{n}"
                js.append(f'const {v}={{v:0}}, el{n}=document.querySelector("{s}"), f{n}={fmt};')
                js.append(f'tl.fromTo("{s}",{{opacity:0,scale:0.94}},{{opacity:1,scale:1,duration:0.3,ease:"expo.out"}},{at});')
                js.append(f'tl.fromTo({v},{{v:0}},{{v:{to},duration:{cdur},ease:"power3.out",onUpdate:()=>{{el{n}.textContent=f{n}({v}.v);}}}},{at});')
            xt = e["out"] if e["out"] else round(self.dur - 0.22, 2)
            js.append(f'tl.to("{s}",{{opacity:0,filter:"blur(8px)",duration:0.18,ease:"power3.in"}},{xt});')
        js += self.js
        js.append(f'window.__timelines["{self.name}"] = tl;')
        return (
            "<template>\n<style>\n" + "\n".join(css) + "\n</style>\n"
            f'<div id="root" data-composition-id="{self.name}" data-width="1920" data-height="1080">\n'
            + "\n".join(body) + "\n</div>\n<script>\n" + "\n".join(js) + "\n</script>\n</template>\n"
        )


def draw(sel, t, d=0.8):
    return f'tl.fromTo("{sel}",{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:{d},ease:"power2.inOut"}},{t});'


def fin(sel, t, d=0.3):
    return f'tl.fromTo("{sel}",{{opacity:0}},{{opacity:1,duration:{d},ease:"power2.out"}},{t});'


def write_project(out, scenes, first_host=None, audio="assets/vo.mp3", audio_dur=None):
    """first_host: optional (id, src, end_seconds) for a hand-written opening scene."""
    os.makedirs(f"{out}/compositions", exist_ok=True)
    hosts = []
    if first_host:
        hid, hsrc, hend = first_host
        hosts.append(f'<div id="{hid}" data-composition-id="{hid}" data-composition-src="{hsrc}" data-start="0" data-duration="{hend}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>')
    for sc in scenes:
        open(f"{out}/compositions/{sc.name}.html", "w").write(sc.render())
        hosts.append(f'<div id="{sc.name}" data-composition-id="{sc.name}" data-composition-src="compositions/{sc.name}.html" data-start="{sc.start}" data-duration="{sc.dur}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>')
    adur = audio_dur if audio_dur else round(MARKS[-1]["end"] + 0.4, 2)
    T = THEME
    fontfaces = " ".join(f"@font-face {{ font-family: '{fam}'; font-weight: {w}; src: url('{src}') format('woff2'); }}" for fam, w, src in T["fonts"])
    index = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="assets/gsap.min.js"></script>
    <style>
      {fontfaces}
      :root {{ --ground: {T['ground']}; --ink: {T['ink']}; --quiet: {T['quiet']}; --up: {T['up']}; --down: {T['down']}; --panel: {T['panel']}; --line: {T['line']}; --head: {T['head']}; --body: {T['body']}; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: var(--ground); }}
      #bg {{ position: absolute; inset: 0; background: var(--ground); {T['bg']} }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
      <div id="bg"></div>
      {chr(10).join(hosts)}
      <audio id="vo" class="clip" src="{audio}" data-start="0" data-duration="{adur}" data-track-index="2" data-volume="1"></audio>
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
    open(f"{out}/index.html", "w").write(index)
    for sc in scenes:
        print(f"{sc.name:10s} {sc.start:7.2f} {sc.dur:6.2f}")
