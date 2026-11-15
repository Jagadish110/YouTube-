"""Cut a vertical YouTube Short (1080x1920) out of a finished long video, with a NEW spoken first line.

    python3 tools/make_short.py short.json

short.json (one per Short, kept in videos/NNN-slug/publish/shorts/NN-name/):
{
  "video": "../../../output/002-blinkit-v1-sfx.mp4",   # the final long video (with sound effects)
  "captions": "../../captions.srt",                     # from tools/marks_to_srt.py
  "start": 106.08, "end": 129.27,                       # span in the long video (20-55 s, see yt-shorts skill)
  "replace_until": 115.26,                              # long-video audio before this is replaced by the new hook
  "hook": "You probably ordered from Blinkit this week. ...",   # new first line (numbers as words)
  "hook_captions": [[0, 3.0, "You probably ordered..."], ...],  # on-screen captions for the hook (optional)
  "kicker": "BLINKIT · EXPLAINED", "title": "HOW BLINKIT\\NTURNED A PROFIT",
  "flash": "−₹156 CR → +₹184 CR",                        # big on-screen text for the first 2 s (different words)
  "source": "Source: Eternal results via Indian Startup News",
  "bg": "F8CB46", "ink": "0F2A1A", "accent": "0C831F"    # company colours (hex RGB)
}
Writes short.mp4 beside the JSON. Fonts: Inter (system). Captions keep text >= 44 px.
"""
import json, os, subprocess, sys

cfg_path = os.path.abspath(sys.argv[1]); d = os.path.dirname(cfg_path); c = json.load(open(cfg_path))
os.chdir(d)
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
start, end, rep = c["start"], c["end"], c.get("replace_until", c["start"])
D = round(end - start, 2); H = round(rep - start, 2)


def bgr(h):
    return f"&H00{h[4:6]}{h[2:4]}{h[0:2]}"


def t(s):
    return f"{int(s // 3600)}:{int(s % 3600 // 60):02d}:{s % 60:05.2f}"


def p(x):
    h, m, s = x.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(s)


# 1. voice the new hook and fit it to the replaced span
open("hook.txt", "w").write(c["hook"] + "\n")
subprocess.run(["python3", os.path.join(ROOT, "tools", "voiceover.py"), "hook.txt", "."], check=True, capture_output=True)
hl = json.load(open("vo_marks.json"))[0]["end"]
tempo = max(0.9, min(1.15, hl / H)) if H > 0 else 1.0
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "voiceover.wav", "-af", f"atempo={tempo:.3f}", "hook_fit.wav"], check=True)

# 2. captions: hook captions + the long video's captions inside the kept span
cues = [tuple(x) for x in c.get("hook_captions", [])] or [(0, H, c["hook"])]
for b in open(c["captions"]).read().strip().split("\n\n"):
    l = b.split("\n"); a, z = l[1].split(" --> "); s0, s1 = p(a), p(z)
    if s0 >= rep - 0.05 and s1 <= end + 0.2:
        cues.append((s0 - start, min(s1, end) - start, " ".join(l[2:])))
ink, acc, bg = c.get("ink", "0F2A1A"), c.get("accent", "0C831F"), c.get("bg", "F8CB46")
ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Title,Inter Black,84,{bgr(ink)},{bgr(ink)},&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,8,60,60,190,1
Style: Kick,Inter ExtraBold,44,{bgr(acc)},{bgr(acc)},&H00000000,&H00000000,-1,0,0,0,100,100,2,0,1,0,0,8,60,60,130,1
Style: Big,Inter Black,96,&H00FFFFFF,&H00FFFFFF,{bgr(ink)},{bgr(ink)},-1,0,0,0,100,100,0,0,3,18,0,5,60,60,0,1
Style: Cap,Inter ExtraBold,62,{bgr(ink)},{bgr(ink)},&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,8,70,70,1290,1
Style: Foot,Inter Bold,32,{bgr(ink)},{bgr(ink)},&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,2,60,60,120,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = [f"Dialogue: 0,{t(0)},{t(D)},Kick,,0,0,0,,{c.get('kicker', '')}",
      f"Dialogue: 0,{t(0)},{t(D)},Title,,0,0,0,,{c.get('title', '')}",
      f"Dialogue: 0,{t(0)},{t(D)},Foot,,0,0,0,,{c.get('source', '')}\\NFull video on the channel"]
if c.get("flash"):
    ev.append(f"Dialogue: 1,{t(0.15)},{t(2.4)},Big,,0,0,0,,{{\\pos(540,1640)\\fad(120,150)}}{c['flash']}")
ev += [f"Dialogue: 0,{t(a)},{t(b)},Cap,,0,0,0,,{{\\fad(60,60)}}{x}" for a, b, x in cues]
open("short.ass", "w").write(ass + "\n".join(ev) + "\n")

# 3. compose
fc = (f"[1:v]scale=1000:-2,pad=1016:ih+16:8:8:color=0x{ink}[clip];[0:v][clip]overlay=(W-w)/2:620[bg];[bg]ass=short.ass[v];"
      f"[1:a]atrim=start={H},asetpts=PTS-STARTPTS,adelay={int(H * 1000)}|{int(H * 1000)}[rest];"
      f"[2:a]aformat=sample_rates=48000:channel_layouts=stereo[h];[h][rest]amix=inputs=2:duration=longest:normalize=0[a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=0x{bg}:s=1080x1920:r=30:d={D}",
                "-ss", str(start), "-t", str(D), "-i", c["video"], "-i", "hook_fit.wav", "-filter_complex", fc,
                "-map", "[v]", "-map", "[a]", "-t", str(D), "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "short.mp4"], check=True)
print("short:", os.path.join(d, "short.mp4"), f"{D} s, hook tempo {tempo:.3f}")
