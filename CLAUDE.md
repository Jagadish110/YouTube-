# Faceless YouTube channel: video pipeline

This repo is the saved pipeline for Jagadish's faceless YouTube channel (Indian startup
and business breakdowns). A session that opens this repo starts with no memory of earlier
work, so everything needed is written here.

## What the pipeline makes

Motion-graphics explainer videos: dark background, white Archivo Black headlines, purple
(#8b3dff) for growth, red (#ff3b47) for drops, source lines on screen for every number.
Voiceover is the open-source Kokoro voice `am_eric`. No stock footage, no faces.

## Steps for one video

1. `./setup.sh` once per session (installs Kokoro, downloads its model from GitHub, warms the HyperFrames CLI).
2. Research the topic with web search. Every number needs a source that was opened, not a snippet.
3. Write `videos/NNN-slug/vo_script.txt`: one spoken line per text line, numbers written as words,
   hard names respelled for the voice. About 150 words a minute. Keep a `sources.md` beside it.
4. `python3 tools/voiceover.py videos/NNN-slug/vo_script.txt videos/NNN-slug` then copy
   `voiceover.mp3` to `project/assets/vo.mp3`. `vo_marks.json` holds each line's start and end.
5. Write `videos/NNN-slug/build.py` with one `sl.Scene` per script line (see `videos/001-zepto/build.py`
   and `tools/scenelib.py`). `s.P("phrase")` places an element where that phrase is spoken.
   Copy `project/assets/gsap.min.js`, `hyperframes.json`, `package.json` from video 001.
6. `python3 build.py`, then `./render.sh videos/NNN-slug/project videos/NNN-slug/output/NNN-slug-v1.mp4`.
7. Look at frames before calling it done: `npx hyperframes@0.9.45 snapshot --at t1,t2,...` inside the
   project and read the contact sheet. Fix overlaps, clipped text and anything off screen.
8. Commit the video folder (script, marks, build.py, project, output mp4) and push.

## Rules

- Text on screen is never smaller than 28 px. Keep content inside the middle 90% of the frame.
- One number at a time; a count-up runs 1.2 to 1.6 s. No pie charts, no grids of KPI cards.
- Nobody in the pipeline can hear audio. Flag names and Indian terms (crore, lakh) for a human listen.
- Never post or upload anywhere. Jagadish reviews and posts to YouTube and Instagram himself.
- Set `HYPERFRAMES_NO_TELEMETRY=1`. Use HyperFrames CLI 0.9.45 and the installed Chrome
  (`HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome`); the CLI cannot download its own.
- A 4-minute video takes about 8 minutes to render. Run it in the background and wait.
- Music: `python3 tools/music_bed.py <seconds> bed.wav` makes a plain placeholder; mix at volume 0.16 under the voice.

## Layout

- `tools/` scenelib.py (scene builder), voiceover.py, music_bed.py
- `videos/001-zepto/` the first video: script, marks, build.py, project, output
- `tests/` results of scheduled test runs
