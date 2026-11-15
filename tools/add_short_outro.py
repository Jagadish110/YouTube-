"""Append the Trendsplain like/share end card to a Short.

    python3 tools/add_short_outro.py short.mp4 out.mp4
Build the card once with python3 videos/_brand/short_outro/build.py.
"""
import os, subprocess, sys
card = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "videos", "_brand", "short_outro", "short_outro.mp4")
f = "[0:v]fps=30,format=yuv420p,setsar=1[a];[1:v]fps=30,format=yuv420p,setsar=1[b];[a][0:a][b][1:a]concat=n=2:v=1:a=1[v][au]"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", sys.argv[1], "-i", card, "-filter_complex", f, "-map", "[v]", "-map", "[au]",
                "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", sys.argv[2]], check=True)
print("with end card:", sys.argv[2])
