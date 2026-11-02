# Phase brief: Magnum Opus outline -> lead magnet guide (2026-10-30)

Bryan's course outline "Magnum Opus: YouTube Client Acquisition Course" (Google Doc 1M9v_V1m..., v4.1) is being turned into ONE long, fully visual lead-magnet guide in the Maria Wendt format. You write ONE phase of it. The main session writes the title page, TOC, TL;DR, Who We Are, final checklist and CTA, and stitches the phases together. Do NOT upload anything.

## Read first
1. `/Users/bryanng/lead_magnets/BRIEF.md` — voice, builder API, image method, writing rules (ZERO AI tells, DEAI_RULES.md), numbers in full. Follow it, EXCEPT the "Required structure" list (you only write your phase's sections) and you don't make a title page / Who We Are / CTA.
2. Your phase file: `/Users/bryanng/lead_magnets/MAGNUM/work/phase<N>.md` (the raw outline: Bryan's quotes with source tags, flags, ledger notes).
3. `/Users/bryanng/lead_magnets/MAGNUM/work/ASSETS.md` — proof images, client win screenshots, example videos and the asset map. Proof images live in `~/scripts/outline_191U/assets/proof/<client>/` and thumbnails in `~/scripts/outline_191U/assets/thumbs/`. NEVER use anything in `assets/_blocked/`.
4. Reader: a coach, consultant or service business doing about $50,000 to $100,000+ a month whose channel is inconsistent, gets no views, or gets no buyers. Promise of the whole guide: the complete system to turn YouTube into your best client acquisition channel, measured in revenue, not views.

## What to turn the outline into
- Finished, readable guide copy in Bryan's first person, written for the page (not a script, no "Beat 1", no runtime, no source tags, no editor notes, no «BRYAN» tags). Each outline section becomes an `h1` (plain human heading), with `h2`s for sub-steps where helpful.
- Every section: the idea in plain words, Bryan's real examples/stories/numbers, at least one image, and a "**Try this:**" action step. Include tables/templates/checklists where the outline has frameworks.
- LIVE segments (2.1a teardown, 2.2a hook critique, 3.7 live audits): turn into short worked examples ("Here's a thumbnail I'd fix and why") using real thumbnails/frames, or skip if there's nothing concrete. Never imply a live event in the doc.
- The 0.0 "Lead-magnet CTA" section: skip (the main session handles CTA).

## What you may and may not use (strict)
- USE: lines tagged as Bryan's own words (transcripts [SL ...], [1000H n] when not marked drafted, Kit emails, DOC notes from Bryan, Classroom), cleared proof ([LEDGER] / CLEARED), public channel data.
- Tweets marked "account line, authorship unconfirmed": you may use the idea in your own words, never as a direct quote.
- DO NOT USE: anything marked drafted / not Bryan, anything from another creator's private course, unresolved VERIFY facts, CONFIRM FIRST or NEVER items in the proof ledger, competitor names, private chats not listed as cleared.
- Where a «BRYAN: ...» decision is unanswered, leave that point out rather than guessing. List what you dropped in FLAGS.
- Never invent facts, stories or numbers. Keep exact numbers (923,571 not 923K).

## Images (aim 10-20 per phase, all READ before use)
- Prefer: cleared proof images and thumbnails from the asset folders; frames from Bryan's own videos at the timestamps the outline cites ([SL <videoId> @ m:ss] means his video id and time: `yt-dlp -f "bv*[height<=1080][ext=mp4]" --download-sections "*START-END"` a short window, then ffmpeg frames; video only, never play audio); YouTube thumbnails via i.ytimg.com/vi/<id>/maxresdefault.jpg; simple matplotlib charts or clean table images for frameworks (white background, readable on phone).
- NO text labels added under/over images (Bryan's rule). Put any explanation in the italic caption.
- Save every image you use to `/Users/bryanng/lead_magnets/MAGNUM/img/` with your prefix `p<N>_` (e.g. `p2_rp_formula_pair.jpg`), <=1600px JPEG.

## Output
- `/Users/bryanng/lead_magnets/MAGNUM/parts/phase<N>.py`: ONLY builder calls (h1/h2/para/img/bullets/table/checklist), no title_page/toc_page/cta_link. Add one soft CTA paragraph somewhere natural in your phase: `para("If you'd rather have a team build this for you, **Book your 30-minute strategy call here:** [[viralbangers.com/book|https://www.viralbangers.com/book]]")`.
- Test-build your part alone: write a tiny wrapper `work/test_p<N>.py` that does `title_page('Test', [('x',False)], hero=None); toc_page(levels=1)` then `exec(open('/Users/bryanng/lead_magnets/MAGNUM/parts/phase<N>.py').read())`, build with `python3 ~/.claude/skills/lead-magnet-doc/scripts/docbuilder.py work/test_p<N>.py work/test_p<N>.docx --img-dir /Users/bryanng/lead_magnets/MAGNUM/img`, render-check (`render_check.sh` with absolute paths, output dir `work/render_p<N>`), READ the contact sheets, fix problems.
- Run the DEAI grep from BRIEF.md on your part and fix all hits. Then reread as a hostile editor for reframes ("X, not Y"), "Here's", fragment runs, triads.
- Final reply (under 300 words): file path, h1 list, image count, 3 strongest examples used, FLAGS (what you dropped and why, third-party content shown, anything Bryan must confirm).
