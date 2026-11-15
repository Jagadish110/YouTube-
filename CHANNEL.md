# Channel niche and topic plan

**Channel name: Trendsplain** (@Trendsplain) — "Whatever's trending, explained." Branding and setup kit in `channel/`.
The channel will widen to any viral topic over time; Indian business stays the core for now.

**Niche:** Indian business, explained. One knowledgeable channel that makes Indian companies,
founders and markets easy to understand, with real numbers and sources on screen.

**Promise to the viewer:** in 3 to 5 minutes you understand how an Indian business really works,
what the numbers say and why it matters, without hype.

## Four content pillars (rotate in this order)

| # | Pillar | What a video answers | Examples |
|---|---|---|---|
| 1 | Startup rise & fall | How did it grow so fast, and what went wrong or could go wrong? | Zepto, Byju's, Dunzo, Ola Electric, Paytm |
| 2 | How brands make money | What is the business model, and where does the profit come from? | Zomato, Jio, DMart, Amul, Paper Boat, IRCTC |
| 3 | IPOs & listed companies | What is this company, what are its numbers, and what should a viewer understand before forming a view? | Recent and upcoming Indian IPOs, big market moves |
| 4 | Founder stories | Who built it, and which decisions made the difference? | Founders of Indian companies, old and new |

## Rules for picking a topic

- Take the next pillar after the last row in the log below (after 4, back to 1).
- Never repeat a company that is already in the log. A different angle on it later is fine only after 10 more videos.
- Prefer topics that are in the news now and have solid public numbers from sources that can be opened.
- If a video promises the next topic in its end card, the next video of that pillar makes it.
- Tone: calm, clear, curious. Explain any term the first time (crore, ARR, IPO, valuation, unit economics).
- Pillar 3 only: say "this is not investment advice" in the voiceover and show it on screen. Never say buy, sell or a price target.
- Pillar 4 only: stick to public facts about the person. No private life, no rumours.

## Log (each video run appends one row)

| No. | Folder | Company / person | Pillar | Made (UTC date) |
|---|---|---|---|---|
| 001 | 001-zepto | Zepto | 1 Startup rise & fall | 2026-11-14 |

## Look and images: every video is different

- Never reuse a previous video's colours, fonts or layout. Each video sets its own theme with
  `sl.theme(...)` in its build.py (ground, ink, accent colours, headline + body fonts, background CSS),
  picked to fit the subject. Fonts come from npm `@fontsource/<font>` (Google Fonts cannot be downloaded here);
  copy the .woff2 files into `project/assets/fonts/` and list them in `fonts=[...]`.
- Colourful is the default. Light or bright grounds are fine; keep text contrast strong.
- Every video uses images: flat illustrations drawn in SVG inside build.py (people only from behind or as
  silhouettes, no faces, no brand logos). See `videos/002-blinkit/sample/build.py` for phone, scooter, store,
  shelves and map examples. Real photos only if Jagadish supplies them or allows a free photo site.
- Use the company's own brand colours for the video and its thumbnail (colours only, never the logo).
  For a founder story, use the colours of the company they are known for.
- Planned looks: 002 Blinkit = Blinkit yellow #F8CB46 + green #0C831F, Bricolage Grotesque / DM Sans.
  003 Coca-Cola IPO = Coca-Cola red #E4002B + white, Anton headlines, plain bottles (never the contour bottle).
  004 Albinder Dhindsa = Zomato red #E23744 + Blinkit yellow #F8CB46 on charcoal, Sora.

## Thumbnails

- Every video gets `videos/NNN-slug/thumbnail/thumb.html`, rendered with `python3 tools/thumbnail.py <thumb.html>`
  into thumb.png (1280x720, under 2 MB) and thumb-small.png. Look at both; the small one must still read.
- Company colours, 2 to 5 big words, one drawn image, no faces, no logos. Fonts from tools/fonts.
- Make it pop: light-ray background, outlined or shadowed headline, one tilted sticker/badge, a big bold drawing.
  See the four thumbnails in videos/001 to 004 as the reference style.
- Upload thumb.png to the dashboard as an asset and put its `/_blob/<id>` in the `thumbnail` column of content/videos.csv.

| Video | Look |
|---|---|
| 001 Zepto | v3 Zepto purple #2E0854 + pink #FF4F9A, Outfit / Plus Jakarta Sans, drawn images in every scene |
| 002 Blinkit | Blinkit yellow + green, Bricolage Grotesque / DM Sans, drawn images |
| 003 Coca-Cola IPO | Coca-Cola red + white, Anton (planned) |
| 004 Albinder Dhindsa | Zomato red + Blinkit yellow on charcoal, Sora (planned) |

## Sound design (default) and background music

Every video gets synthesised sound effects instead of a song: typing on text, rising ticks + ding on
count-ups, pops on drawings, swooshes on wipes, thumps on stamps, whooshes between scenes.
`python3 build.py` writes `sfx_events.json`; after rendering run
`python3 tools/sfx.py sfx_events.json output/NNN-slug-v1.mp4 output/NNN-slug-v1-sfx.mp4`. The -sfx file is the one to post.
For a hand-written composition, add its cues to sfx_events.json in build.py (see videos/001-zepto/build.py).

Optional song (only if Jagadish asks):

Jagadish supplies the song. Save it as `videos/NNN-slug/music/<file>` and run
`python3 tools/add_music.py output/NNN-slug-v1.mp4 music/<file> output/NNN-slug-v1-music.mp4 0.16`.
It loops/trims the song, fades it, and ducks it under the voice. Note the song's licence in sources.md.
A copyrighted song without a licence will get a YouTube copyright claim; use royalty-free or licensed music.

## Instagram Reels (@trendsplain)

- Every Reel runs 15 to 45 seconds. Never shorter, never longer.
- Built vertical (1080x1920) with `videos/reels/NNN-slug/build_reel.py` (see `videos/reels/001-nvidia-huang/ten/`), not cut from a YouTube video.
- Own style, different from the Shorts: full-screen kinetic captions, bass hits / risers / ticks, colours of the subject.
- No top label and no progress line. A small "@trendsplain" appears in the last second.
- Every claim from an opened source. Reported but unproven claims are labelled "REPORTED · NOT PROVEN" on screen. No photos of real people, no logos.
