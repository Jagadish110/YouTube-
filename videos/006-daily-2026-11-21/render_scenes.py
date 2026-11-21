"""Renders scenes.py drawings to project/assets/scenes/<key>.jpg (1920x1080)."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import scenes, content
out = os.path.join(HERE, "project/assets/scenes"); os.makedirs(out, exist_ok=True)
for k, a in content.ACCENTS.items():
    svg = os.path.join(out, k + ".svg"); open(svg, "w").write(scenes.scene(k, a))
    subprocess.run(["rsvg-convert", "-w", "1920", "-h", "1080", "-o", os.path.join(out, k + ".png"), svg], check=True)
    subprocess.run(["convert", os.path.join(out, k + ".png"), "-quality", "90", os.path.join(out, k + ".jpg")], check=True)
    os.remove(svg); os.remove(os.path.join(out, k + ".png"))
print("ok", len(content.ACCENTS))
