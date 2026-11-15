"""Review clip for video 002 (Blinkit): the opening hook, about 12 seconds.

Run from this folder:  python3 build.py
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
import scenelib as sl
from scenelib import C

HERE = os.path.dirname(os.path.abspath(__file__))
sl.setup(os.path.join(HERE, "vo_marks.json"), 12.4)

S = []

# ---- 0: hook number, then the turn to profit
s = sl.Scene("hook", 0); S.append(s)
t_turn = round(s.P("And for the first") - 0.1, 2)
s.E("k", "BLINKIT · JULY TO SEPTEMBER 2026", C(170, 40), 0.1, "fade", cls="kick q")
s.E("n", "₹0 Cr", C(300, 230), s.P("twenty-one"), ("count", 20940, '(v)=>"₹"+Math.round(v).toLocaleString("en-IN")+" Cr"', 1.5), out=t_turn, cls="hero up tnum")
s.E("c", "of orders in just 3 months", C(600, 60), round(s.P("twenty-one") + 0.4, 2), "fade", out=t_turn)
s.E("a", "And for the first time…", C(330, 64), s.P("And for the first"), "fade", cls="q")
s.E("b", "IT'S MAKING <span class='up'>MONEY</span>", C(450, 150), s.P("actually making"), "pop", cls="hero")
s.E("src", "Source: Eternal Q2 FY27 results, via Business Standard", "", s.P("twenty-one"), "fade", cls="src")

# ---- 1: the question
s = sl.Scene("question", 1); S.append(s)
s.E("a", "HOW DOES", C(260, 90), 0.1, cls="hero q")
s.E("b", "<span class='up'>10-MINUTE</span> DELIVERY", C(390, 130), s.P("ten-minute"), "pop", cls="hero")
s.E("c", "TURN A PROFIT?", C(560, 130), s.P("turn a profit"), cls="hero")
s.E("d", "Let's break it down.", C(800, 56), s.P("Let's break"), "fade", cls="q")

sl.write_project(os.path.join(HERE, "project"), S, audio_dur=12.0)
