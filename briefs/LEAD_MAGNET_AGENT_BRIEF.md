# Shared brief: 4 new Viral Bangers lead magnets (2026-10-29)

You are building ONE lead magnet guide end to end (research, outline, images, full copy, .docx build, render check). Do NOT upload to Google Drive; the main session does that.

## Who it's for and who it's from
- Author voice: **Bryan Ng** (@boomerrbryan, 23, co-founder of Viral Bangers, a done-for-you YouTube agency for business owners who sell something). First person, plain, conversational, specific, short words, like explaining to a founder over coffee. Load the bryan-voice skill files for real lines/stories: `~/bryan-os/skills/bryan-voice/` (or `~/.claude/skills/bryan-voice/`). Never invent biography, stories, client results or numbers.
- Reader: a business owner or would-be creator reading on a phone. Assume they don't know the jargon. Define any term once.

## Research tools (use them heavily)
- **Subscribr admin Strategy Search**: `mcp__0c0a1be6-3bbe-4cb9-888e-7678009a31ea__Strategy_Search` (load with ToolSearch "select:mcp__0c0a1be6-3bbe-4cb9-888e-7678009a31ea__Strategy_Search"). Run MANY specific queries (aim 20+), limit 10-20 each. Save every useful excerpt with its source (creator + video id) into `work/RESEARCH.md`. Attribute advice to the creator by name in the guide when you use it ("Noah Morris checks saturation by...") rather than "experts say".
- **Nexlev MCP** (`mcp__a4b1ff15-12ce-4fe9-a499-bc586c1cb887__*`, load via ToolSearch): youtube_search, youtube_video_details, get_video_transcript, get_niche_finder_categories, search_niche_finder_channels, get_niche_overview, faceless_outliers_videos, get_video_rpm, youtube_channel_videos, etc. Use real numbers from it and say where they came from and the date (2026-10-29).
- vidIQ MCP (`mcp__b34e36f6-bd82-45dd-a3ad-c0e9dd5b1332__*`) is also available for keyword/search data.
- Transcripts: Nexlev get_video_transcript (big results get saved to a file; parse with python).

## Images (make it fully visual, like the CLAUDE guide: 25-50 images)
- Pull real frames from YouTube videos: `yt-dlp -f "bv*[height<=1080][ext=mp4]" -o work/v_<id>.mp4 <url>` (video only, no audio needed; NEVER play audio), then `ffmpeg -ss <t> -i file -frames:v 1 -q:v 2 out.jpg`. Note: to locate moments, make contact sheets (`ffmpeg -vf "fps=1/5,scale=480:-1"` then tile with PIL) and READ them; when picking a time from an fps-filter sheet, the real moment is about +2s later than the sheet label, so re-extract and check.
- Good sources: Bryan's own channel @boomerrbryan (find via Nexlev search / youtube_channel_videos), and videos from creators in the Strategy Search results that show the thing on screen (YouTube Studio screens, analytics graphs, niche tools). Crop to the useful part with PIL.
- You can also render clean charts/tables as images with matplotlib from Nexlev data (white background, simple, readable on phone, Arial-like font, no title clichés).
- Combine images: `python3 ~/.claude/skills/lead-magnet-doc/scripts/images.py row OUT.jpg HEIGHT a.jpg b.jpg --labels "A|B" [--cols 3]` (run from a bash script file, not zsh inline). Compress to <=1600px JPEG. Name files by what they show.
- Who We Are proof collage: use `~/lead_magnets/shared/clients.jpg` (the main session is building it now; copy it into your img/ at build time; if not there yet, leave the img() call in and continue).
- READ every image you use (contact sheet) to confirm it shows what the caption says.

## The builder
- API (Python content file, executed top to bottom): `title_page(title, [(text, is_blue), ...], hero='hero.jpg')`, `toc_page(levels=1)`, `h1(text)`, `h2(text)`, `para(text)`, `img(name, width_in, caption='(...)')`, `bullets([...], numbered=False)`, `checklist([...])`, `table(rows, widths_in, bold_rows=(0,))`, `cta_link(label, url)` (prints "Go to " + link, so label is just the domain text). Inline: `**bold**`, `*italic*`, `[[label|url]]`. Example to match in structure: `~/bryan-os/skills/lead-magnet-doc/references/examples/LM2_edit/content.py` (if present) and `~/.claude/skills/lead-magnet-doc/references/example-content-rp-profits.py`. Format spec: `~/.claude/skills/lead-magnet-doc/references/format-spec.md`.
- Build: `python3 ~/.claude/skills/lead-magnet-doc/scripts/docbuilder.py content.py "<Title>.docx" --img-dir img`
- Render check: `bash ~/.claude/skills/lead-magnet-doc/scripts/render_check.sh "<abs path to docx>" "<abs path>/work/render"` then READ the contact sheets; fix broken images, huge gaps, tables too wide.

## Required structure
1. Title page: the headline given to you (exact), subtitle with one blue word, hero collage.
2. toc_page(levels=1)
3. TL;DR
4. Who We Are (Bryan intro, short): "My name is Bryan, and I run Viral Bangers with my co-founder Mauricio. We're a YouTube agency for business owners who sell something..." then these cleared one-liners ONLY (no other client numbers):
   - Chamath Palihapitiya: we edit all of his long-form videos.
   - Jordan Welch: we scripted "getting rich is easy, actually", which has 923,571 views.
   - Inayah McMillan: our very first video together did 1,185,797 views.
   - Ethan Garland: we worked on two of his top three videos, including one with 539,000 views.
   - Scott Taylor: his views went from about 3,600 a video to 15,000, and YouTube now brings in around $40,000 a month.
   - Fiction Profits Academy: 7,000 to 15,000 subscribers, and they're the top result for "how to start a KDP business".
   - Clover Trading: average views went from about 1,000 a video to 8,000.
   then img clients.jpg (6.5in).
5. The guide itself: step by step, every step with a concrete example and images, "Try this:" action steps, real numbers with sources.
6. A section on how a business owner uses this (the reader may sell a service).
7. The Checklist (checklist()).
8. CTA, last H1 "Want Us To Do This For You?" Short paragraph, then `para("**Book your 30-minute strategy call here:** [[viralbangers.com/book|https://www.viralbangers.com/book]]")`. Also put one mid-guide soft CTA paragraph pointing to the same booking link.

Headings: plain, the way a person says it ("How To Check A Niche Is Still Empty", "What 1,000 Views Pays In Each Niche"). No clever labels.

## Writing rules (ZERO AI tells, Bryan's order)
Read and obey `~/bryan-os/skills/humanizer/references/DEAI_RULES.md` (zero tolerance) plus `~/.claude/skills/humanizer/SKILL.md`. Key ones:
- No "It's not X, it's Y" / "X, not Y" reveals / "not because X but Y". No "Not X. Not Y. Just Z." No "The X? Y." No "Here's the thing/what/how/why". No false suspense, no "Imagine", "Think of it as", "Let's dive/break down".
- Banned words: quietly, deeply, fundamentally, remarkably, arguably, genuinely, truly, incredibly, certainly, utilize, leverage, robust, streamline, harness, delve, unlock, elevate, seamless, game-changer, landscape, tapestry, paradigm, synergy, ecosystem, journey, serves as, stands as, secret sauce, revolutionary, crucial, pivotal, "in today's".
- Max one rule-of-three in the whole doc. No 3+ sentences starting the same way. No one-line fragment paragraphs for emphasis; paragraphs of 2-4 related sentences. No fake-deep aphorisms, no grandiose stakes, no summary line restating the section. No invented concept labels.
- No em dashes, no en dashes as dashes, no arrows (→ or ->), straight quotes only. Bold only for step labels like "**Step 1.**" / "**Try this:**" and the booking line; no bold-first bullets.
- Numbers in full: 539,000 not 539K; "$1.2 million" spelled. Exact numbers beat rounded.
- Before finishing, grep content.py for: `—|–|→|->|[“”‘’]|Here's|isn't just|not just|delve|leverage|quietly|genuinely|truly|robust|unlock|landscape|journey|Imagine|Think of|crucial|\b[0-9]+[KkMm]\b` and fix every hit (code/URLs excepted). Then reread the whole thing once more as a hostile editor hunting reframes and fragment runs.

## Deliverables (in your folder)
- `work/RESEARCH.md` (every Strategy Search / Nexlev finding with source), `OUTLINE.md`, `img/`, `content.py`, the built `.docx`, `work/render/` contact sheets checked.
- Final reply (under 400 words): folder path, docx path, page count, image count, section list, the 5 most interesting findings, and FLAGS (any claim you couldn't verify, any third-party creator content shown, anything Bryan must confirm).
