# CTA migration: 5 keywords only (Bryan, 2026-10-05) · now 8 (6 Oct: + ALGORITHM, IDEAS, SETUP, see LEAD_MAGNET_GUIDES.md)

Bryan's decision: **only 5 comment keywords exist now: SCRIPT, SCOTT, THUMBNAILS, MILLION, EDIT.** AUDIT and BANGER are retired everywhere: every carousel, script, caption, story, reel, email, lead magnet flow and doc.

## The 5 keywords and their exact promise lines (copy these)

| Keyword | Use it when the piece is about | Promise line |
|---|---|---|
| **SCRIPT** (default) | scripts, hooks, the course, anything general | Comment "SCRIPT" and I'll send you my scriptwriting guide (the one behind Jordan Welch's 923,571-view video) plus my free full course 🤝 |
| **SCOTT** | ads vs YouTube, booked calls, a "restricted" or "dead" channel, results/proof, offers, work-with-me, done-for-you, audits | Comment "SCOTT" and I'll send you the full Scott Taylor case study: how he tracks about $40,000 a month back to YouTube 🤝 |
| **THUMBNAILS** | packaging, thumbnails, titles | Comment "THUMBNAILS" and I'll send you the 6-part thumbnail formula that gets RP Profits 4.4x the views 🤝 |
| **MILLION** | positioning, story, outliers, niche angle | Comment "MILLION" and I'll send you how we got Inayah McMillan 1,185,797 views on one video 🤝 |
| **EDIT** | editing, music, pacing, CapCut | Comment "EDIT" and I'll send you the editing checklist we use on Chamath Palihapitiya's channel 🤝 |

Short versions are fine where space is tight (story frames, on-screen text, Bluesky): `Comment "SCOTT" for the Scott Taylor case study`, `Reply "SCRIPT" ⤵️`, etc.

## Rules

1. **Secondary AUDIT/BANGER lines after a primary CTA: delete them.** Examples: `Want us to look at your channel too? Comment "AUDIT"`, `If you want, my team will audit your channel too`, `Reply BANGER to work with me`, `Comment AUDIT for a free audit` as a P.S. Tidy the punctuation/emoji left behind.
2. **AUDIT or BANGER as the only CTA: replace it** with the keyword that fits the topic (table above). Offer, scarcity, work-with-me, done-for-you, audit and "dead account" pieces → **SCOTT**. Rewrite the promise so it names what they get (use the promise line). Keep the body copy; only change the CTA and any sentence that only makes sense for the audit/booking (e.g. "book your spot", "I'll audit it for free", "link to apply") → point it at the magnet instead.
3. **Don't invent claims.** No new numbers, no fake scarcity. If a line only existed to sell spots/the audit and can't be pointed at a magnet, delete it.
4. **«BRYAN» placeholders that only existed for the BANGER booking link, the audit scope/turnaround, or audit capacity** → remove them (the question is now moot). Leave every other «BRYAN» placeholder alone.
5. **Structured data:** wherever a field holds the keyword (`cta`, `cta_keyword`, `keyword`, `lead_magnet`, `magnet`, chips, filters), set it to the new keyword and its magnet name:
   - SCRIPT → `LM5: Jordan Welch scriptwriting guide + free course`
   - SCOTT → `LM1: Scott Taylor case study`
   - THUMBNAILS → `LM3: RP Profits thumbnail formula`
   - MILLION → `LM4: Inayah McMillan positioning guide`
   - EDIT → `LM2: Chamath editing checklist`
6. **Lead magnet guides and ManyChat flows:** drop the DM 3 "audit offer 24h later" step. Guides that closed with "Reply AUDIT" + "Reply BANGER" now close by cross-selling one other magnet (e.g. SCOTT guide → "Comment SCRIPT for the scriptwriting guide"). Kit tags stay.
7. **Voice and format:** Bryan's voice, numbers in full (539,000 not 539K), no new hashtags.
8. **Leave archives alone:** files named `*_backup*`, `*pre_metricool*`, `pb_scheduled_snapshot*`, `REWRITE_LOG.md`, anything under `raw/`, `site/out/`, `site/cal/`, and the old `final/` folder (superseded by `final_ragebait/`).
9. **Canva:** if a design's text contains AUDIT or BANGER (or "audit your channel"), edit the text in Canva the same way, then re-export any preview PNG the vault uses. Keyword stays pink (#E1306C) where it was pink.
10. **Log every change** (file or Canva design id + page, before → after) to `~/budgetdog-analysis/bryan-system/CTA_MIGRATION_LOG.md` (append; one section per worker).
