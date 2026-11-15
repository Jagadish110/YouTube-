# Faceless YouTube channel: video pipeline

This repo is the saved pipeline for Jagadish's faceless YouTube channel (Indian business,
explained: startups, business models, IPOs and founders; see CHANNEL.md). A session that opens this repo starts with no memory of earlier
work, so everything needed is written here.

## What the pipeline makes

Motion-graphics explainer videos with drawn illustrations. Each video has its own colourful look (CHANNEL.md);
video 001 used dark + purple. Source lines on screen for every number.
Voiceover is the open-source Kokoro voice `am_eric`. No stock footage, no faces.

## Niche and topics

Read `CHANNEL.md` before picking a topic. It sets the niche (Indian business, explained), the four
pillars that rotate, the topic rules and the log. Every video run appends its row to that log.

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
8. Add sound effects: `python3 tools/sfx.py videos/NNN-slug/sfx_events.json output/NNN-slug-v1.mp4 output/NNN-slug-v1-sfx.mp4`
   (see "Sound design" in CHANNEL.md). The -sfx file is the final video.
   Then make the thumbnail (see "Thumbnails" in CHANNEL.md) and add it to the dashboard.
9. Commit the video folder (script, marks, build.py, project, output mp4, thumbnail) and push.

## Two toolkits: who does what

- **Making the video** (script, voiceover, scenes, drawings, sound effects, render, thumbnail art): ONLY this repo's
  own pipeline above (tools/scenelib.py, voiceover.py, sfx.py, thumbnail.py), as used for 001 Zepto and 002 Blinkit.
- **Everything after the video is made** uses the YouTube agent skills in `.claude/skills/yt-*` (MIT, vendored from
  github.com/Jakeschincariol/youtube-agent-skill; voice profile in `.claude/youtube/voice.md`, copied by setup.sh):
  - `/yt-package` title + thumbnail check (thumbnail words must differ from the title, 3 words max)
  - `/yt-seo` description, tags, 3 target queries · `/yt-chapters` chapters from `publish/captions.srt`
  - `/yt-shorts` picks Short spans and new first lines; render them with `tools/make_short.py short.json`
  - `/yt-viral` niche research · `/yt-plan` weekly plan · `/yt-comment` replies · `/yt-retention` retention exports · `/yt-audit` channel audit
  - `/yt-script` hook scoring only (`hookscore.py`): score the opening line of new scripts, but keep this channel's voice and research rules
- After each video: `python3 tools/marks_to_srt.py videos/NNN-slug/vo_marks.json videos/NNN-slug/publish/captions.srt`,
  then write `videos/NNN-slug/publish/PUBLISH.md` (titles, description, tags, chapters, Shorts table) and make Short #1.
  See `videos/002-blinkit/publish/` for the reference pack.

## The dashboard (keep it current after every run and every change)

The dashboard "Content Pipeline" is https://claude.ai/artifact/EQFeH3ubmGrYxGHoMNComG (a Claude Data
dashboard). It reads four CSV files from this repo. Each one is a dataset in the dashboard's store:

| Repo file | Dataset id | Who updates it |
|---|---|---|
| `tests/runs.csv` | `runs` | every health check and video run (one row per run) |
| `content/videos.csv` | `videos` | whenever a video changes status or a new week is planned |
| `content/linkedin.csv` | `linkedin` | every LinkedIn drafting run, and when a post is approved/posted |
| `content/changes.csv` | `changes` | every change Jagadish asks for (date, area, change, status) |

Video status values, in order: `Script draft`, `Script approved`, `Preview ready`, `Preview approved`,
`Rendered`, `Posted`. LinkedIn status values: `Draft`, `Approved`, `Posted`. Change status: `Done` or `Pending`.
CSV notes fields must not contain commas.

`tests/runs.csv` columns: `run_at_utc` (ISO, e.g. 2026-11-15T05:30:00Z), `kind` (`health` or `video`),
`video` (folder slug), `status` (`pass`/`fail`), `setup_s`, `voiceover_s`, `render_s`, `duration_s`, `size_kb`
(numbers, blank if the step never ran), `supabase` (`reachable`/`unreachable`/blank), `commit`, `notes`
(short; the exact error on a fail).

To push a changed CSV to the dashboard:
1. Commit and push the CSV.
2. Upload it: Artifact tool, `url` = the dashboard URL, `asset: true`, `file_path` = the CSV. It returns `/_blob/<id>`.
3. ArtifactData: `get` collection `datasets`, doc = the dataset id, then `update` it with its `version` as
   `if_version`: `source.url` = the new `/_blob/<id>`, `updated: {at: <now UTC ISO>, by: "Claude"}`,
   `edit: {via: "claude", at: <now>}`. Do not touch `files/index.html`.
4. Delete the old blob: Artifact `action: "delete"`, `url` = dashboard, `path` = old blob id (only if no dataset names it).

## Changes Jagadish asks for

When he asks for a change (voice, style, topic, schedule, LinkedIn tone), apply it in the repo so every future
run follows it (CLAUDE.md, CHANNEL.md, posts/linkedin/PAGE.md, scripts or build.py), re-render the
preview if it is affected, add a row to `content/changes.csv`, and push it to the dashboard.

## LinkedIn: daily AI news page

Rules, page copy and the card tool are in `posts/linkedin/PAGE.md` and `tools/linkedin_card.py`.
Each daily run saves `posts/linkedin/YYYY-MM-DD/` (post.md, card.json, card.png), adds a `Draft` row to
`content/linkedin.csv`, pushes it to the dashboard, and notifies Jagadish with the post text. Never post to LinkedIn.

## Rules

- Every video has its own look and uses drawn images; see "Look and images" in CHANNEL.md.
- Text on screen is never smaller than 28 px. Keep content inside the middle 90% of the frame.
- One number at a time; a count-up runs 1.2 to 1.6 s. No pie charts, no grids of KPI cards.
- Nobody in the pipeline can hear audio. Flag names and Indian terms (crore, lakh) for a human listen.
- Never post or upload anywhere. Jagadish reviews and posts to YouTube and Instagram himself.
- Set `HYPERFRAMES_NO_TELEMETRY=1`. Use HyperFrames CLI 0.9.45 and the installed Chrome
  (`HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome`); the CLI cannot download its own.
- A 4-minute video takes about 8 minutes to render. Run it in the background and wait.
- Sound: synthesised effects via tools/sfx.py on every video; no background song unless Jagadish asks (tools/add_music.py).

## Layout

- `tools/` scenelib.py (scene builder, also writes sfx_events.json), voiceover.py, sfx.py (sound effects), add_music.py, music_bed.py
- `videos/001-zepto/` the first video: script, marks, build.py, project, output
- `tests/` results of scheduled test runs (`runs.csv`)
- `content/` dashboard data: videos.csv, linkedin.csv, changes.csv
- `posts/linkedin/` daily AI news drafts and PAGE.md
- `tools/make_short.py` vertical Shorts from a long video; `tools/marks_to_srt.py` captions
- `.claude/skills/yt-*` YouTube agent skills (packaging, SEO, chapters, Shorts, viral, plan, comments, retention, audit)
- `tools/thumbnail.py` YouTube thumbnails; `tools/linkedin_card.py`, `tools/linkedin_preview.py` LinkedIn
- `tools/fonts/` woff2 fonts (all OFL, from @fontsource) used by thumbnails and cards
