"""Test run: automated pipeline check. Three scenes timed to vo_marks.json.

Run from this folder:  python3 build.py
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
import scenelib as sl
from scenelib import C, L

HERE = os.path.dirname(os.path.abspath(__file__))
sl.setup(os.path.join(HERE, "vo_marks.json"), 14.2)

S = []

# ---- 0: what this is
s = sl.Scene("intro", 0); S.append(s)
s.E("k", "AUTOMATED TEST", C(240, 44), 0.1, "fade", cls="kick q")
s.E("h", "CHANNEL <span class='up'>PIPELINE</span>", C(330, 150), s.P("automated"), "pop", cls="hero")
s.E("c", "Running on a schedule · nobody watching", C(640, 56), s.P("running on"), "fade", cls="q")

# ---- 1: the three steps
s = sl.Scene("steps", 1); S.append(s)
bx = "width:500px;height:200px;font-size:52px;"
s.E("b1", "SCRIPT → VOICE", L(110, 440, 52, bx), s.P("a short script"), cls="box")
s.E("b2", "GRAPHICS", L(710, 440, 52, bx), s.P("builds the"), cls="box")
s.E("b3", "VIDEO", L(1310, 440, 52, bx + "border-color:var(--up);"), s.P("renders"), "pop", cls="box up")
s.E("h", "HOW IT WORKS", C(220, 72), 0.1, cls="hero")

# ---- 2: it works
s = sl.Scene("works", 2); S.append(s)
s.E("a", "If you can see and hear this", C(330, 60), 0.1, "fade", cls="q")
s.E("b", "IT WORKS <span class='up'>END TO END</span>", C(450, 130), s.P("the pipeline"), "pop", cls="hero")

sl.write_project(os.path.join(HERE, "project"), S, audio_dur=13.8)
