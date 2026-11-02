---
name: lead-magnet-doc
description: Bryan's end-to-end lead magnet builder for Viral Bangers. Turns a client case study (PDF, Gamma, client docx), a course deck, a transcript, a YouTube video or a gear list into a Google Doc in the Maria Wendt doc format, then delivers it through a ManyChat keyword. Pipeline is intake, outline, ICP audit agent, Bryan-voice copy, humanizer, one-to-one images, .docx build, render check, upload to Drive through Chrome, native Google Doc with a dotted-leader TOC. Covers the 9 live guides (SCRIPT, SCOTT, THUMBNAILS, MILLION, ALGORITHM, IDEAS, SETUP, EDIT, CLAUDE) and five variants: case-study, video-to-guide, product-guide, line-by-line script breakdown, course-to-guide with a private source. Use when Bryan says "make the SCRIPT lead magnet like the Maria doc", "create a lead magnet for ...", "rebuild the guide", "free guide", "case study doc", "make it like the Maria Wendt doc", or asks to update a live keyword guide. Not for emails (use dfy-email-flows or email-writing), not for the opt-in pages that deliver the guide (use lead-magnet-optin-pipeline), not for ManyChat flow edits (use automation-audit-and-fix).
---

# Lead Magnet Doc

## 1. What this does and when

Builds a Viral Bangers lead magnet as a Maria Wendt format Google Doc. LM3 (the RP Profits thumbnail guide, 2026-10-06) is the reference build and its copy is `references/example-content-rp-profits.py`. Eight more guides were built the same day with this skill, so the folder `references/examples/` holds each guide's `content.py` and outlines as worked examples. The registry of the 9 live guides, their links and the promise lines for CTAs is `references/LEAD_MAGNET_GUIDES.md`.

Every guide is a Google Doc set to "anyone with the link can view". ManyChat sends the link on a comment keyword, the opt-in pages send it by email, so a link must never change once it is live. A rebuilt doc is a new link (see section 4, step 8), so rebuilds of live guides go through the in-place Apps Script path (section 5 variant F).

## 2. Load first

1. `docs/rules/GLOBAL_RULES.md` (zero AI tells, no K/M, retrieve don't invent, audience wording).
2. `docs/proof/CLAIMS_LEDGER.md` before any client number goes in. A guide's "Who We Are" block and its numbers come only from CLEARED rows.
3. Skills: `bryan-voice` (SECOND_BRAIN.md, voice-dna.md, bio-facts-and-conflicts.md) and `humanizer`. For writing in the doc, also `~/budgetdog-analysis/bryan-system/deai/RULES.md`.
4. Memory files for the guide you touch: `references/memory/project_lm*.md` (copies of the live memory), plus `feedback_manychat_keywords.md`, `feedback_number_format.md`, `project_viral_bangers_proof_rules.md`.
5. `docs/access/ACCESS_REGISTRY.md` for doc ids and Drive ids.

## 3. Fixed rules

Each rule carries its date and source.

- **Headline is Bryan's, never reworded** (Bryan 2026-10-06 "don't change the headline"). If a number in it conflicts with the body, flag it, do not fix it silently. Examples: THUMBNAILS "two years" became "14 months" only because Bryan said so; IDEAS "Gets" became "Get" because he said so; EDIT keeps "100M" in the headline though copy bans K/M, because it is his headline.
- **Headings are plain and human** (2026-10-06): "TL;DR", "Who Is RP Profits?", "He Fixed The Design, But Nothing Happened". He rejected "the short version", "stalled" and the clever stat-headline "Same Words. Wrong Package. 2,887 Views.". Details and good/bad list in `references/format-spec.md`.
- **Voice**: Bryan's written register through `bryan-voice`, then the humanizer pass, always both (2026-10-06 "I want it to be written in Brian Owens voice [sic] ... use the humanized writing skill"). Pull his real lines from the transcript or deck. Open humble about adjacent skills ("I'm personally not a huge thumbnail expert"). Paragraphs hold 2 to 3 sentences.
- **Humanizer is mandatory.** Zero em dashes, arrows, curly quotes, bold-first bullets, "The X? A Y.", "Not X. Y." countdowns, "Think of it like". Zero tolerance since 2026-10-09 (feedback_zero_ai_tells). Run `grep -nP '[\x{2014}\x{2192}\x{201C}\x{201D}]|-[>]' content.py` plus the humanizer grep before building.
- **Reader (ICP)**: a consultant or service business owner who sells something, under about 5,000 subscribers, makes thumbnails in Canva, does not know CTR, reads on a phone. Target "businesses", not "coaches".
- **Spine**: the case, beat by beat. After each beat the course lesson it proves, then one "Try this" step. A section "Make It Work For Your Business" is mandatory (a translation table works well).
- **Required sections**: TL;DR, Who We Are (100 to 300 words, 5 to 7 one-line client results from cleared proof, 1 to 2 proof image grids from `~/budgetdog-analysis/bryan-system/proof/` where `index.json` status is `public`), the case or how-to, a checklist, and the CTA.
- **CTA**: last H1 is "Want Us To Do This For You?" then bold "Go to viralbangers.com" (Bryan 2026-10-06 "The CTA at the end of the lead magnet should just be to go to viralbangers.com"). Never a keyword CTA in the doc.
- **Proof**: cleared claims only. Keep a private claims ledger (cleared / confirm first / never) and only use CLEARED lines. Chamath = "we edit his long-form".
- **Never name the tracking tool.** Write "the tracking we run for clients".
- **Other creators' frameworks become Bryan's own** (2026-10-06 SCRIPT: "remove any nate curtiss mention, oscar owen mentin, amploify views, i want to take these as things that I've said"; then "remove kallaway, hormozi, you can have blair warren and nesb"). Rewrite as "I call this ...", "My rule for endings ...". Another person's client numbers never appear as Bryan's data. Named frameworks that survive: Blair Warren, NESB, Earl Nightingale.
- **Private sources are never named or quoted** (paid courses, private PDFs, client chats). Use them only as background.
- **Pasted third-party articles are not reproduced** (SCRIPT: the tropes.fyi article became a 25-point "cut these" list in Bryan's words with a one-line credit; Bryan did not object).
- **Invented examples are flagged** (LM3 sales-consultant example) and listed in the report.
- **No K or M in copy.** Ethan's title is written "$45,000 Per Month" though the real title says "$45k"; flag it.
- **Do not trash old Drive files unless Bryan says yes.** Every report lists the leftovers.
- **Sign-off before build**: show Bryan the outline, flags and the format sample request first (skill rule from LM3 on). After the first six builds he stopped answering flags and the sessions proceeded on stated defaults; where he never replied the default stands and the item is in section 8.

## 4. Workflow

Models: Opus or Sonnet for copy; the ICP audit agent is a general-purpose subagent run in the foreground (`run_in_background: false`, SCRIPT used background true). One agent, never in parallel. Folder per magnet: `~/budgetdog-analysis/bryan-system/short_form/lead_magnets/<LMn_name>/` with `content.py`, `img/`, `OUTLINE_v1.md`, `OUTLINE_v2.md`, `work/`. Before creating a folder, `ls` the parent: on 2026-10-06 two sessions both wrote to `LM2_edit/` and had to move one to `LM2_edit_checklist/` and message each other.

1. **Intake** (by source type, see Variants).
   - PDF case study: `python3 scripts/images.py extract-pdf SRC.pdf WORK/rp`, read pages with Read `pages:`.
   - PPTX course: `python3 scripts/images.py extract-pptx SRC.pptx WORK/codex`, read `slides.txt`. Images that repeat on every slide are chrome. Diagram slides with no raw image: `python3 scripts/images.py slides-keynote SRC.pptx WORK/slides`.
   - Client docx (Offer Viral Bangers): unzip, `word/media` holds the screenshots; extract text with python-docx; note which image numbers are the client's.
   - Format sample: `references/format-spec.md` is Maria's spec. A different sample doc: `curl -L "https://docs.google.com/document/d/<ID>/export?format=docx"`, parse styles.xml, update the spec and `assets/template.docx`. The Maria sample is 46 MB, too big for the Drive tool, so use curl.
2. **Live numbers**: compare every screenshot number with the live count (Nexlev `youtube_video_details`, or vidIQ `vidiq_get_videos_by_ids`) and flag differences. Inayah 1,185,797 on the screenshot vs 1,203,773 live is the standing example. Keep the screenshot figure and flag.
3. **Outline then ICP audit**: write `OUTLINE_v1.md` (each section mapped to case beat, lesson, "try this" step, images, ending with "Cut and why" and Flags). Spawn the ICP audit agent with the prompt in `references/prompts/2026-10-06_lm3-icp-audit-agent.md` (adapt the magnet name; the other 9 files are the same prompt per magnet). It reports drop-off points, jargon, deletions, gaps where the niche does not translate, and the top 5 edits. Check its "data contradictions" yourself: scope differences are not errors. Write `OUTLINE_v2.md`.
4. **Images**: contact sheets first (`images.py contact`), look before choosing. Prefer raw media over slide renders (slide renders carry the Academy branding and a pink background). Combine with `images.py row OUT.jpg H IMG... --labels 'a|b|c'` (use `|` when a label has commas so numbers keep them). Compress to 1600 px JPEG. Name by what the image shows. Drop any image with unclear attribution.
5. **Copy**: write `content.py` with the builder API (`title_page`, `toc_page`, `h1`, `h2`, `para`, `img`, `bullets`, `table`, `checklist`, `cta_link`; inline `**bold**`, `*italic*`, `[[label|url]]`, `{AST}` for a literal asterisk). Humanizer pass, grep, fix bold-first bullets and "Go to Go to" duplicates.
6. **Build the docx**: `python3 scripts/docbuilder.py content.py "<LM folder>/<Title>.docx" --img-dir WORK/img`. The TOC is a static dotted-leader TOC (not a Word field, because Pages and Word regenerate fields and shift pages). `toc_page(levels=1)` fits one page (the all-H2 first attempt of SCRIPT was 4 pages and 75 entries with repeated "The Open Loop"). Two passes: build, `bash scripts/render_check.sh "<ABSOLUTE path to docx>" WORK/render` (needs an absolute path), `python3 scripts/toc_pages.py WORK/render/render.pdf "<docx>.headings.json" WORK/toc_pages.json`, rebuild with `--toc-pages WORK/toc_pages.json`, rerun toc_pages and confirm numbers did not move.
7. **Render check**: Read the contact sheets. Look for broken images, orphan headings (fix with page breaks), clipped diagram labels, table widths. The renderer is Pages through osascript and swaps Lora for a default font; Google Docs shows Lora.
8. **Publish**: follow `references/google-docs-upload.md` (Chrome file-input capture, Save as Google Docs, TOC). Build the upload copy with `--docs` so two empty lines wait under the TOC heading. Gotchas, all from 2026-10-06:
   - The Drive MCP may be a different Google account from the one logged into Chrome. It cannot see these docs and cannot edit text in an existing doc. Upload only through Chrome.
   - The Drive "New" menu toggles and sometimes needs a second click. Screenshot after each click.
   - File > Save as Google Docs can silently fail. LM7 v2 failed twice and worked on the third try by clicking the menu item at its coordinate. The first File menu click can also miss (LM8: retried at (72,44) then (158,176)). The File menu sits near (73,45) in a 1512-wide frame; (38,43) is the Docs home logo, do not click it.
   - Use the URL `docs.google.com/document/d/<docx id>/edit?rtpof=true&sd=true`; the plain /edit URL can hang on "Opening the file".
   - A converted doc can arrive with a TOC field showing "00" page numbers. Click inside the TOC, then its refresh icon.
   - Never type cmd+f into Docs through keystrokes; they land in the doc (LM3 undid it with cmd+z). Check the title after.
   - Pasting from one doc to another with synthetic cmd+c / cmd+v does not work, and pasting into the old doc is blocked, so every rebuild is a new Google Doc with a new link. Tell Bryan the new link.
   - Claude in Chrome "No group with id" tab-group error: SCRIPT failed 4 times and SCOTT 5 times in a row. Stop after about 3 retries, send the .docx to Bryan (`SendUserFile`), retry later. A later attempt in the same session worked.
   - TOC: Insert > Page elements > Table of contents > second thumbnail (dotted leaders). Then the TOC menu, Table of contents options, untick Heading 2 for an H1-only TOC. Coordinates in the upload reference.
   - Doc title: rename after conversion (LM8 needed it).
   - Sharing: guides that ManyChat sends must be "anyone with the link can view". The LM2 Claude guide was left private at first.
9. **Close out**: write the memory file (`project_lm<n>_<name>_doc.md`), update `LEAD_MAGNET_GUIDES.md` and its Kit tag line, report link, section list, cuts, flags, open decisions, leftover Drive files.

## 5. Variants

**A. Case-study guide (THUMBNAILS, SCOTT, MILLION, ALGORITHM).** Source = client case study (Gamma PDF or section of your internal proof doc) plus the course lesson deck. Spine = case beats with lesson and try-this. SCOTT specifics: unzip the client docx, pick the Scott images (11 of them), Nexlev `channel_resolver` then `youtube_channel_videos` to find the 9 videos and download thumbnails for a grid. Headline claim "$40,000 a month" is the cleared "about $40,000 a month tracked to YouTube", body says "thought it was dead". MILLION specifics: Inayah, spine = income claims everywhere, Step 1 unique advantage, Step 2 borrow a format (Leila Hormozi "How I Brainwashed Myself ..."), Step 3 combine, hook in 4 moves, "What We're Not Claiming" (no revenue, no floor claim, no brother clause until Bryan answers). A humanize pass (audit table first, then replace) produced v2; keep `content_v1_prehumanize.py`. ALGORITHM specifics: 9 `Strategy_Search` queries on the Subscribr admin MCP (0c0a1be6) for viewer satisfaction, TV viewership, small channels, revenue-backed titles, plateau, business channels, 2026 trends, Shorts vs long-form, upload frequency; "CTR" only means thumbnail clicks, link clicks are "link-click rate"; a second round added "YouTube Changed How It Counts Views" from 4 vidIQ videos (7Vql2c08Q9o, boxBsZRuI4I, T-tMbKuyj6g, aYdi6h3K4ls) fetched with Nexlev `get_bulk_video_transcripts`: from 27 August 2026 a view counts from the first frame, engaged views are the old count, use the "1of10" Chrome extension or Studio Advanced mode + Engaged views (install steps and price not verified).

**B. Video-to-guide (CLAUDE, EDIT video guide).** Source = a YouTube video, here Mauricio's xn3IKXrPHvw (42 min). Steps: Nexlev `youtube_video_details` and `get_video_transcript` into `work/transcript.txt`; download `video.mp4` with yt-dlp; ffmpeg `fps=1/4` frames with timestamp drawtext (631 frames), 22 contact sheets, view all, pick about 95 timestamps; extract full-resolution frames to `work/full/`; contact-sheet labels run about 2 seconds late, so extract at label + 2 s (the first set mismatched and was rebuilt as `full2/`); crop prompt text areas and check they are readable; fetch `maxresdefault` as the thumbnail; a `collages.sh` script because zsh word-splitting broke inline loops. Link the video in the doc and deep-link each section to its timestamp; transcribe every on-screen prompt as a copy-paste prompt with `[PLACEHOLDERS]` in place of the reference creators' URLs; add glossary, cost table (Claude $200 a month, desktop not phone) and chapter table. Voice = the presenter in first person: "Hey, I'm Mauricio, co-founder of Viral Bangers" (Bryan 2026-10-06 "hey, Mauricio. Mauricio is the co-founder of Viral Bangers, too."). Bryan asked for "as many images as possible" and "the most robust guide as possible", so the ICP agent's advice to cut worked examples 2 and 4 was overruled. Title = video title verbatim because Bryan gave none.

**C. Product-guide (SETUP).** Source = an old PDF plus Bryan's dictated brief (`references/prompts/2026-10-06_lm7-gear-guide-brief.md`). Three tiers (Beginner about $130, MVP about $2,400, Premium about $8,300; prices are MSRP marked "~", not verified live). Method: a research agent (`references/prompts/2026-10-06_lm7-gear-research-agent.md`) verifies each Amazon ASIN against the product title and saves `work/RESEARCH.md`; Amazon links need not be affiliate links; product-in-use photos come from the Amazon listing image galleries per ASIN, never other creators' photos; Bryan's own frames come from yt-dlp + ffmpeg on his videos (4JR47fUrz88, KbNmN8S_ZRI, Cx4VFf_ec1Y, w4L0vW8Vol4, xga0r4O5mrs, GJbXDbYHgwg) for then-vs-now shots; Tella images from tella.com/mac via Browser-pane JS `img src` extraction; diagrams drawn with PIL (light diagram, studio side view, mic placement, SM7B chain, Sony to Cam Link to Tella). AI-generated harsh-vs-soft lighting images (treg `replicate.image-gen.flux-schnell`) were rejected as fake. Cowork prompts use the OBJECTIVE / OUTPUT SCHEMA / METHODS format (the studio finder prompt is in `references/examples/LM7_recording_equipment/content.py`; Bryan's older studio prompt was never found on the Mac). Bryan facts: studios $20 an hour in Medellin (his spoken "$30 Colombia" was wrong), $100 to $200 an hour typical with gear, videographer $500 for the day, MVP mic Shure MV7+, SM7B moves to Premium, Elgato Prompter stays although his bio says teleprompters "give you the ick".

**D. Line-by-line script breakdown (SCRIPT).** Source = Bryan's Google Doc with margin comments (21 comments), exported with unzip of the .docx and `work/jw_script.txt`. Structure: intro line by line, then steps each with open loop, why, what, how, close; "For your business" lines after the intro and steps 1, 3, 4; consultant Q&A (where to pitch a $5,000 call, no rags-to-riches story, pain state without insulting business owners, small channel); jargon defined (RPM, AdSense, hook, payoff). `Strategy_Search` ran 12 queries (hooks and stakes, open loops, why-what-how, NESB, CTA and sponsor placement, belief shifting and villain, endings, personal stories and objections, make it easy, YouTube as VSL, anticipating objections, specific numbers). Intro is about 622 words (4 minutes), not 30 seconds; Digital Launchpad is co-owned with Iman Gadzhi. The pasted QA checklist (`references/prompts/2026-10-06_lm5-script-qa-checklist-paste.md`) became "Your Script Checklist": Quick Version of 10 points, the 5 phases as tick boxes, red flags, "Adjust It For Your Channel" table with 5 blank boxes. The headline "Case Study: The Script Behind Jordan Welch's 923,776-View Video, Broken Down Line By Line" was written by the assistant because Bryan gave none and was not confirmed.

**E. Course-to-guide with a private source (IDEAS, EDIT checklist).** Two subagents digest private PDFs (digest prompts kept private); the digests live only in scratchpads and are not copied. Rename every named framework as Bryan's own: IDEAS used "Buyer's Path", "Banger Score" (5 questions times 10 points), "Idea Bank", plus Bryan's own "Unique Advantage + Buyer Problem + Proven Format = banger idea" and voice-bank lines "steal with style", "flip the ratio", 100 to 20 to 5 to 1. Spine: idea = viral topic x viral format, made yours by a unique advantage (Inayah). Bryan asked for "value per word super duper high", more business examples, "massively actionable", non-obvious insights; the $275,766 Stripe shot was cut (a reader on 1,200 subscribers sees a brag). Live views refreshed with vidIQ before quoting. Tracking data unnamed. Bryan allowed the YT Master Tracker sheet (1PCJiUpGoqg7j2ire5Idh_GMvLKTGH-LwCrIndRkF_Z4) as a free resource and any outlier age if recent copies still do well. The EDIT checklist (88aa8292): authority-first TL;DR ("We edit for some of the biggest names on YouTube, including billionaire investor Chamath Palihapitiya", Bryan 2026-10-06 "not have a soft TLDR"); headline "EDITING CHECKLIST BEHIND 100M VIEWS For Business YouTube Channels"; Chamath is talking-head interviews with off-camera questions cut out; annotate frames from his videos (yt-dlp ids 0-LAT4HjWPo and J2qKVjRR12w, 11 videos on the channel); do not credit the editor; never tell readers to edit their own videos: outsource, then CTA; 13 visuals from `make_images.py`; two unverifiable claims removed (music behaviour, clinic example); the "100M views" total is unverified.

**F. De-AI pass on live docs (Apps Script).** Live docs must keep their link, so they are edited in place with Google Apps Script (project https://script.google.com/home/projects/1YWd6V4rKMsUTfcUD-JoQ0RKcZFCzgLc7_dtVtLUFherkLTRlLFQf_sjh/edit, [your-email]). Code is `assets/scripts/Code.gs` (replace only when the old text is found exactly once outside the TOC, keep run attributes, unbold labels, then scan for em dashes, arrows, "here's the", adverbs) plus `assets/scripts/full.gs` (Code.gs with `var DATA = {name: {id, pairs, unbold}}` prepended; pairs come from the Kit `.kit.json` vs `.kit.deai.json` trees; 117 KB). Status on 2026-10-09: loaded and saved, not run. It needs Bryan to click Google's OAuth Allow (do not click it for him). After it runs: read the log, refresh the TOCs, run `scanAll`. Chrome blocks localhost fetches from Google pages, so the data went in through an injected file input and Monaco `setValue`.

## 6. QA checklist

- [ ] Headline is Bryan's exact words; conflicts flagged, not fixed.
- [ ] `grep -nP '[\x{2014}\x{2192}\x{201C}\x{201D}]|-[>]' content.py` is empty; humanizer grep clean; no bold-first bullets.
- [ ] Every number traces to the source or a cleared ledger row; live counts checked; K/M absent.
- [ ] Who We Are 100 to 300 words, 5 to 7 cleared one-liners, images from `proof/` with status `public`.
- [ ] "Make It Work For Your Business" section present; checklist present; CTA block present once ("Go to viralbangers.com", no doubled "Go to").
- [ ] No tracking-tool name, no private source name, no VTC claims, no uncleared client claims.
- [ ] Contact sheets read: no broken images, no orphan headings, no clipped labels, TOC numbers stable after pass two.
- [ ] Google Doc: converted, TOC real (not "00"), H1-only if intended, title renamed, sharing set to anyone-with-link, first page opens.
- [ ] LEAD_MAGNET_GUIDES.md, memory file and access registry updated; leftover Drive ids listed; invented examples listed.

## 7. Outputs and where they go

- Local: `~/budgetdog-analysis/bryan-system/short_form/lead_magnets/<LMn>/` (docx, content.py, img/).
- Google Doc link into `references/LEAD_MAGNET_GUIDES.md` and the registry (`docs/access/ACCESS_REGISTRY.md`, Google Docs table).
- Memory: `project_lm<n>_*_doc.md` plus one line in MEMORY.md.
- Report to Bryan: link, section list, cuts and additions, flags, open decisions, leftovers.

## 8. Open questions

- «BRYAN: which EDIT magnet does the keyword EDIT send, the checklist doc (1-qo8fv...) or Mauricio's Claude video guide (1VxLy8...)? Until answered LEAD_MAGNET_GUIDES.md sends the checklist for EDIT and the Claude guide for CLAUDE.»
- «BRYAN: confirm the CLAUDE keyword (proposed by Claude 2026-10-06, never confirmed).»
- «BRYAN: SCRIPT headline (assistant-written) and the three Claude-drafted Q&A answers.»
- «BRYAN: MILLION headline count 1,185,797 vs live 1,203,786; floor claim 10,000 to 50,000; brother clause; leave out "2 million first video" (proof doc) vs 882,000.»
- «BRYAN: "40+ clients use this setup" (SETUP, dropped); Elgato Prompter vs the "ick" line.»
- «BRYAN: Mauricio's "1,500+ long-form videos edited" and "100+ videos a month", and whether to keep Kallaway, Leila Hormozi, Amplify Views, Daniel Priestley screenshots in the CLAUDE guide; "I run white to view" caption meaning.»
- «BRYAN: "100M views" total for the EDIT headline.»
- «BRYAN: trash the leftover Drive files? THUMBNAILS v1 1Vuu51..., v2 1TB1kaxx..., .docx 1BN_EAKp..., 1RQPnIk_..., 1qKWZbgJ...; MILLION v1 1CDGXoWz..., .docx 12PcUaZn..., 1Bss6e1v...; SCRIPT 1_vxn4pyh..., .docx 1O2Whm7f...; ALGORITHM v1 1fYxY8ij..., bad 1f7tmKEW..., .docx 1f6ikcj0...; SCOTT .docx 1qnZngAi...; SETUP v1 1x4C5hN9..., .docx 1iiH4pSJ..., 1ZfOcuXx...; IDEAS .docx 1XgDYnnW...; EDIT .docx 1T7MjLUA...; CLAUDE .docx 1RfWK5qn...»
- «BRYAN: click Allow on the Apps Script OAuth so the 9 live docs get their de-AI pass.»
- «BRYAN: non-trading real client formula for the THUMBNAILS sales-consultant example; SCOTT "If You Understand Math" video labelled reach, check.»

## 9. Files

| File | What it is |
|---|---|
| `scripts/docbuilder.py` | .docx builder in Maria format (TOC, `--docs`, `--toc-pages`) |
| `scripts/images.py` | PDF/PPTX extraction, Keynote renders, contact sheets, collages (`--labels 'a|b'`) |
| `scripts/render_check.sh` | Pages to PDF to contact sheets (absolute path) |
| `scripts/toc_pages.py` | reads the render PDF, writes TOC page numbers |
| `assets/template.docx` | Maria's styles |
| `assets/scripts/Code.gs`, `full.gs` | Apps Script de-AI path (not run; `full.gs` carries the 9 docs' data) |
| `references/format-spec.md` | every style value and heading rules |
| `references/google-docs-upload.md` | Chrome upload, convert, TOC playbook |
| `references/example-content-rp-profits.py` | the LM3 copy, the bar to match |
| `references/examples/<LM>/` | content.py and outlines for SCOTT, EDIT (Claude guide), EDIT checklist, THUMBNAILS, MILLION, SCRIPT, ALGORITHM, SETUP, IDEAS (`LM2_edit/OUTLINE_v1,v2` belong to the checklist's older run). Verbatim copies; they keep original dashes and quotes. |
| `references/LEAD_MAGNET_GUIDES.md` | the registry of 9 guides, links, promise lines |
| `references/memory/project_lm*.md` | memory copies per guide |
| `references/prompts/` | recovered prompts: ICP audit agent per magnet, LM7 brief and research agent, SCRIPT QA checklist paste, thumbnailtest SOP paste, digest agents for the private PDFs |
| private, not copied | private course PDFs and decks (kept off the repo) |

Items not recovered: the OUTLINE and audit hand-back texts for sessions where the outline was never written to disk (SCRIPT, MILLION v2 table), the Strategy_Search result text (tool output only), the older Cowork studio prompt (never existed on disk), the text of `Offer Viral Bangers` (private).

## 10. Session provenance

`_mining/cards/`: 2026-10-06_763bbfe7 (LM3, the skill's birth), 2026-10-06_dc8f6d16 (video source, CLAUDE), 2026-10-06_f8a9e033 (SETUP), 2026-10-06_9b81e6cc (SCRIPT), 2026-10-06_dfb36fd0 (MILLION), 2026-10-06_0166c230 (IDEAS), 2026-10-06_722deb7b (ALGORITHM), 2026-10-06_88aa8292 (EDIT checklist), 2026-10-06_a5bc3aa5 (SCOTT), 2026-09-30_4e5b3ce4 (Apps Script de-AI, status), 2026-10-09_4056072d (handoff, Apps Script still waiting).
