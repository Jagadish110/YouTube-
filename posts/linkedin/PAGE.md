# LinkedIn company page and daily AI post workflow

Status: page copy is a DRAFT for Jagadish to pick from. He creates the page himself on LinkedIn.

## Page name options (pick one, or give your own)

1. **AI Brief India**: plain and searchable; matches the "AI BRIEF" label on the cards.
2. **The Daily Prompt**: friendly; AI-native wordplay.
3. **Signal over Noise AI**: positions the page as the filter for AI hype.

## Tagline (max 120 characters)

Daily AI news in 2 minutes: what happened, why it matters, with sources. Built for Indian professionals.

## About

Every morning we pick the 3 to 5 AI stories that matter most, from global labs to India's own AI
push, and explain each in plain words: what happened, why it matters for your work, and where
it came from. Every claim links to its source. No hype, no investment advice.

Industry: Online Audio and Video Media (or Technology, Information and Media). Size: 1 employee.
Logo/banner: use the same dark #0b0a12 background and #8b3dff purple as the video channel.

## Daily post rules (each scheduled run follows these)

- Window: news from the last 24 hours (up to 48 on Mondays). 3 to 5 stories; at least 1 about India when there is real news.
- Open every source. Prefer primary sources (company filings, official blogs, government releases), then major outlets.
  Never use an AI-written news roundup as a source; use it only to find leads.
- Shape: hook line, numbered stories each with one "Why it matters" line, one takeaway, a question,
  sources list, 3 to 5 hashtags. 150 to 260 words. Plain English, short sentences.
- Leave out rumours, unproven allegations and private life. No buy/sell talk.
- Card: write card.json and run `python3 tools/linkedin_card.py card.json card.png`. Headline + accent under
  about 24 characters, red accent for bad news, purple for growth. Look at card.png before finishing.
- Save to `posts/linkedin/YYYY-MM-DD/` (post.md, card.json, card.png). Status starts as `draft`.
- Never post to LinkedIn. Jagadish copies the post and uploads the card himself.
