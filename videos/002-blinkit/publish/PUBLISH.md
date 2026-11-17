# 002 Blinkit — publishing pack (Mon 16 Nov 2026)

Made with the yt-package, yt-seo, yt-chapters and yt-shorts skills (.claude/skills). Nothing is uploaded;
copy each block into YouTube Studio yourself.

Final video: `output/blinkit-final-upload.mp4` (Trendsplain intro after the hook + subscribe/share outro) · Captions file: `publish/captions-final.srt` (upload as English captions)

## Title + thumbnail (yt-package)

| Rank | Title | Score (title.py, with thumbnail "FINALLY PROFITABLE?") |
|---|---|---|
| 1 | **How Blinkit Makes Money in 10 Minutes** | 100/100 · 37 chars · has a number · thumbnail says something different |
| 2 | Blinkit Made ₹184 Crore. Here's How | 100/100 · 35 chars (note: ₹184 Cr is adjusted EBITDA for one quarter) |
| 3 | Blinkit's ₹20,940 Crore Quarter, Explained | 98/100 · mobile feed may cut after "Quarter," |

**Use title 1 with `thumbnail/thumb-v2.png` ("FINALLY PROFITABLE?").** The old thumbnail ("10 MIN MAKES MONEY?")
repeated the title's words and had 4+ words; the skill's rule is different words and 3 at most.

## Description (yt-seo) — paste as is

```
How does Blinkit make money if it delivers groceries in 10 minutes? Here is Blinkit's business model, explained with real numbers: dark stores, owning its stock, ads, and whether it is finally profitable.

Every number on screen has its source, listed below.

Chapters
00:00 ₹20,940 crore in three months
00:18 From Grofers to Blinkit
00:45 The dark store trick
01:13 Blinkit now owns what it sells
01:41 Revenue is not profit
01:52 The scorecard: loss to profit
02:20 The catch
02:35 Grow faster or profit first?

Sources
Eternal Q2 FY27 results: Business Standard, Indian Startup News (Oct 2026)
Inventory model: Eternal investor call, 21 July 2025 (Informist)
Ad revenue: Storyboard18
Company history: Wikipedia (Blinkit)

This video explains a business. It is not investment advice.

#Blinkit #Zomato #BusinessExplained
```

**Tags** (disambiguation only): Blinkit, Blinkit business model, how Blinkit makes money, Blinkit profit, Eternal, Zomato, Grofers,
quick commerce India, dark store, Zepto vs Blinkit, Swiggy Instamart, Albinder Dhindsa, Indian startups, business explained

**Queries this video should win:** "how blinkit makes money" · "blinkit business model" · "is blinkit profitable".
All three sets of words appear in the title or the first two description lines.

## Chapters (yt-chapters) — validated

Starts at 00:00, 8 chapters, every chapter at least 10 seconds (shortest: 01:41 to 01:52, 11 s). Times are for the final upload file; the intro sits inside chapter 1. Already in the description above.

## Shorts (yt-shorts) — top 5 from this video

| # | Span in long video | New first line (hookscore) | On-screen text, first 2 s | Ends on |
|---|---|---|---|---|
| 1 ✅ made | 1:46–2:09 (23 s) | "You probably ordered from Blinkit this week. A year ago, it was losing ₹156 crore a quarter. Now it makes ₹184 crore. Here is why." (55, WORKABLE) | −₹156 CR → +₹184 CR | "once a store matures, it makes money." |
| 2 | 0:39–0:57 (+0:57–1:06) | "Why does your 10-minute delivery app feel so fast? It is not the rider." (to score) | NOT THE RIDER | "not from fast driving." |
| 3 | 2:09–2:29 (20 s) | "Why does your 10-minute delivery app lose money on every new store it opens?" (65, WORKABLE) | EVERY NEW STORE LOSES | "the profit disappears again." |
| 4 | 1:07–1:34 (27 s) | Rewrite needed: current options score WEAK | 79% | "now the smaller part." |
| 5 | 0:12–0:39 (27 s) | "You have used Blinkit. You have probably never heard of Grofers. Here is how one became the other." (57, WORKABLE) | GROFERS → BLINKIT | "its biggest business by far." |

Loop point for #1: the last line ("it makes money") sets up the first ("losing… now it makes…").
Vertical framing: the full 16:9 frame sits in the middle of a Blinkit-yellow 9:16 canvas with a headline above and
captions below, so nothing is cropped; the on-screen source line is repeated at the bottom in readable size.

Short #1: `publish/shorts/01-scorecard/short.mp4`. Rebuild or make more with `python3 tools/make_short.py short.json`.

---
**Ship it, or change it?**
