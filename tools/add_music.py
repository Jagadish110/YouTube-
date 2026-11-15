"""Mix a background song under a finished video's voiceover.

    python3 tools/add_music.py video.mp4 song.mp3 out.mp4 [volume=0.16] [start_seconds=0]

- Loops the song if it is shorter than the video, trims it if longer.
- Fades the song in (1.5 s) and out (3 s at the end).
- Ducks the song automatically while the voice speaks (sidechain compression), so words stay clear.
- Copies the video stream untouched; only the audio is re-encoded (AAC 192k).
Keep the song file in the video folder as music/<name> and note its licence in sources.md.
"""
import json, subprocess, sys

video, song, out = sys.argv[1], sys.argv[2], sys.argv[3]
vol = float(sys.argv[4]) if len(sys.argv) > 4 else 0.16
start = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0

dur = float(json.loads(subprocess.run(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", video],
    capture_output=True, text=True, check=True).stdout)["format"]["duration"])
fade_out_at = max(0.0, dur - 3.0)

filt = (
    f"[1:a]atrim=start={start},asetpts=PTS-STARTPTS,atrim=0:{dur:.3f},"
    f"afade=t=in:st=0:d=1.5,afade=t=out:st={fade_out_at:.3f}:d=3,volume={vol},"
    f"aformat=sample_rates=48000:channel_layouts=stereo[m];"
    f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit=2[v][vkey];"
    f"[m][vkey]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
    f"[v][md]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[a]"
)
subprocess.run([
    "ffmpeg", "-v", "error", "-y", "-i", video, "-stream_loop", "-1", "-i", song,
    "-filter_complex", filt, "-map", "0:v", "-map", "[a]",
    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", out,
], check=True)
print("music added:", out, f"(volume {vol}, {dur:.1f} s)")
