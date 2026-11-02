# Lead Magnet System (Viral Bangers)

The full system we use to build lead magnets: comment keyword, then Google Doc guide, then opt-in page, then delivery email. It's built to run with Claude Code skills and agents.

## What's in here

| Folder | What it is |
|---|---|
| `keywords/` | `LEAD_MAGNET_GUIDES.md`: every comment keyword, the guide it sends, the doc link and the promise line to paste into CTAs. `KEYWORD_RULES.md`: how keywords are picked and which topic gets which keyword. |
| `skills/lead-magnet-doc/` | The main skill: outline, ICP audit agent, copy in the creator's voice, humanizer pass, images, .docx build, render check, upload to Google Docs, contents page. Includes the builder (`scripts/docbuilder.py`), image tools (`scripts/images.py`), render check, format spec, the Google Docs upload playbook and the agent prompts. |
| `skills/lead-magnet-optin-pipeline/` | Framer opt-in page, Kit form, delivery sequence and automation for each keyword, plus the test script. |
| `skills/cta-keyword-migration/` | How to add, retire or rename a keyword and update every carousel, caption, email and planner row that uses it. |
| `skills/humanizer/` | The zero-AI-tells rules (`references/DEAI_RULES.md`) and the de-AI pass. |
| `briefs/` | The agent brief used to build several guides in parallel (one agent per guide), plus the phase brief and style notes for long course docs. |
| `builders/` | `docbuilder_v3.py`: current format (Lora headings, Arial body, hard black-line tables and diagrams, no captions). `docbuilder_ss.py`: the screen-share variant. |
| `image-scripts/` | The actual scripts used to pull and combine images for each guide: frame grabs, thumbnail downloads, collages, charts, client logos. |
| `examples/` | The `content.py` for every built guide (SCRIPT, SCOTT, THUMBNAILS, MILLION, ALGORITHM, IDEAS, SETUP, EDIT, CLAUDE, NICHE, STUDIO, ANALYTICS, TIKTOK, and the full course doc). Rebuild any of them with the builder once you have the images. |
| `SOURCES.md` | Every place images and numbers come from, with the exact commands. |

## How a guide gets built

1. Pick the keyword and headline (`keywords/`).
2. Research: Strategy Search, Nexlev and vidIQ MCPs, transcripts, and the creator's own videos (`SOURCES.md`).
3. Outline, then an ICP audit agent reads it as the buyer and lists drop-off points, jargon and gaps.
4. Write `content.py` in the creator's voice and run the humanizer rules.
5. Pull images: frames, thumbnails, proof, charts, diagrams (`image-scripts/`).
6. Build: `python3 builders/docbuilder_v3.py content.py "<Title>.docx" --img-dir img`
7. Render check: `bash skills/lead-magnet-doc/scripts/render_check.sh "<abs docx>" "<abs out dir>"`, then read the page sheets.
8. Upload to Drive through Chrome, Save as Google Docs, insert the contents page (`skills/lead-magnet-doc/references/google-docs-upload.md`).
9. Opt-in page, Kit form and delivery email (`skills/lead-magnet-optin-pipeline/`), then wire the keyword in ManyChat.

## Requirements

Python 3 with `python-docx` and `Pillow`, `ffmpeg`, `yt-dlp`, macOS Pages (for the render check), and Claude Code with the Nexlev, vidIQ and Subscribr MCPs plus Claude in Chrome.

Client images and private research aren't included. Only claims cleared by each client are used in the guides.
