"""vo_marks.json -> captions.srt (one cue per sentence, timed by character share within each line).

    python3 tools/marks_to_srt.py videos/NNN-slug/vo_marks.json videos/NNN-slug/publish/captions.srt
Upload the SRT to YouTube as English captions; the yt-chapters / yt-shorts / yt-edit skills read it too.
"""
import json, re, sys

def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)):03d}"

marks = json.load(open(sys.argv[1])); out = []; n = 1
for m in marks:
    parts = [p for p in re.split(r"(?<=[.?!:])\s+", m["text"]) if p.strip()]
    total = sum(len(p) for p in parts); t = m["start"]
    for p in parts:
        d = (m["end"] - m["start"]) * len(p) / total
        out.append(f"{n}\n{ts(t)} --> {ts(t + d)}\n{p}\n"); n += 1; t += d
open(sys.argv[2], "w").write("\n".join(out))
print(sys.argv[2], n - 1, "cues")
