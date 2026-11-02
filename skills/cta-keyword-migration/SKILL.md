---
name: cta-keyword-migration
description: SOP for changing which ManyChat comment keywords exist and rewriting every asset that uses them (carousels, Canva designs, Metricool scheduled slides and captions, story and reel templates, lead magnets, planner rows, emails), plus the keyword history 3, 7, 5, 8, 9 and the topic-to-keyword table. Includes the cta_migrate.py helper, the rule sheet CTA_MIGRATION.md, the 3-worker pattern used on 2026-10-05 and the verbatim worker briefs. Use when Bryan says "only use these keywords", "retire AUDIT", "retire BANGER", "add a keyword", "change the CTAs everywhere", "which keyword for this post", "migrate the CTAs", "update every carousel". Not for building the lead-magnet guides themselves (lead-magnet-doc) or the ManyChat flows (lead-magnet-optin-pipeline and the automation docs).
---

# CTA keyword migration

## 1. What this does and when

Every comment or DM call to action in Bryan's content uses one of a short list of ManyChat keywords, each routed to one lead-magnet guide. Whenever the list changes, the change has to reach every place the old word lives: slide images, Canva designs, scheduled Metricool posts, captions, planner rows, templates, lead-magnet docs, Kit emails and ManyChat flows. On 2026-10-05 this was done in one afternoon with one rule sheet, one helper script and three parallel workers. Use this skill to repeat it for the next change, and to pick the right keyword for a new piece.

## 2. Load first

1. `docs/rules/GLOBAL_RULES.md` section 3 (the nine keywords) and `docs/proof/CLAIMS_LEDGER.md` (promise lines carry numbers).
2. `references/CTA_MIGRATION.md` (the rule sheet, copied) and `references/CTA_MIGRATION_LOG.md` (44,247 bytes: every file, Canva page and Metricool id changed on 2026-10-05, with before and after).
3. `~/budgetdog-analysis/bryan-system/LEAD_MAGNET_GUIDES.md` (master list with Google Doc links) and `final_ragebait/MANYCHAT.md` (the nine automations).
4. Memory `feedback_manychat_keywords.md`; sibling skills `carousel-system`, `ig-captions`, `content-os`.

## 3. Fixed rules

Keyword history (all Bryan's decisions)
- 2026-09-30 23:51 to 10-01: carousels ended in per-post words (OWN, Q4, HUMAN, TV, CITED, IDEA, GLOBAL, RESTRICTED, COURSE, CALLS, VOICE, STORY, REVIVE, BOOKED, FORMULA, SEARCH) and "comment YouTube or comment banger" (his words). Retired.
- 2026-10-02 12:43: "For all of the manychats automations, i only want it to be 3 words and 3 CTAs: 1- AUDIT (free audit) 2- YouTube 3- Banger". Full text: `skills/content-os/references/prompts/2026-10-02_three_keywords_rule.md`.
- 2026-10-02 23:41: one keyword per lead magnet: SCOTT, EDIT, THUMBNAILS, MILLION, SCRIPT plus AUDIT and BANGER (7); YOUTUBE retired.
- 2026-10-05 09:51: "I only want to use these 5, i want to get rid of the toehr 2 CTAs, modify it in every single carousel, and every single script to change to one of these 5 CTAs." AUDIT and BANGER retired. Why: the coach said a specific, quick resource beats a free audit; BANGER had no booking link; AUDIT scope was undecided.
- 2026-10-06 11:53: added ALGORITHM, IDEAS, SETUP (8). 13:13: the EDIT guide exists. CLAUDE added the same day, proposed by Claude, unconfirmed (9).
- 2026-10-10: Bryan used VIRAL ("Comment 'Viral' to get my 9 Best YouTube trainings") on two carousels and "work" as a DM keyword. Neither is a ManyChat keyword; no flow exists. Flagged.

The nine and their guides (ids in `docs/access/ACCESS_REGISTRY.md`): SCRIPT (default) Jordan Welch script breakdown plus the free course; SCOTT Scott Taylor case study (also the keyword for offers, audits, work-with-me, done-for-you and dead-channel pieces after 2026-10-05); THUMBNAILS RP Profits; MILLION Inayah McMillan; EDIT Chamath editing checklist (we edit his channel, never imply strategy); ALGORITHM The New Rules of The YouTube Algorithm (for 2027); IDEAS How To Come Up With BANGER Video Ideas (the word is IDEAS, not BANGER); SETUP the recording setup guide; CLAUDE How To Edit YouTube Videos Using Claude. Promise lines are in `scripts/cta_migrate.py` (PROMISE) and `LEAD_MAGNET_GUIDES.md`.

Topic to keyword: ads vs YouTube, booked calls, a restricted channel, results, offers: SCOTT; editing: EDIT; packaging, thumbnails, titles: THUMBNAILS; positioning, story, outliers: MILLION; scripts, hooks, the course, anything general: SCRIPT; algorithm and reach: ALGORITHM; video ideas: IDEAS; camera, mic, lighting: SETUP; AI editing: CLAUDE.

Rule sheet (CTA_MIGRATION.md, 2026-10-05), condensed
1. A secondary retired-keyword line after a primary CTA is deleted, with its punctuation and emoji tidied.
2. A retired keyword as the only CTA is replaced by the topic keyword's promise line. Keep the body copy; rewrite only sentences that only made sense for the audit or booking.
3. Do not invent claims, numbers or scarcity. A line that only sold spots or the audit and cannot point at a magnet is deleted.
4. «BRYAN» placeholders that existed only for the BANGER booking link, audit scope or audit capacity are removed; other placeholders stay.
5. Structured fields (`cta`, `cta_keyword`, `keyword`, `lead_magnet`, `magnet`, chips, filters) are set to the new keyword and its magnet name.
6. Lead-magnet guides and ManyChat flows drop the DM 3 audit offer 24 hours later; guides that closed with "Reply AUDIT" and "Reply BANGER" close by cross-selling one other magnet (SCOTT guide to SCRIPT, ALGORITHM to IDEAS, IDEAS to SCRIPT, SETUP to SCRIPT, CLAUDE to EDIT). Kit tags stay (`lm-<keyword>`).
7. Bryan's voice, numbers in full, no new hashtags.
8. Leave archives alone: `*_backup*`, `*pre_metricool*`, `pb_scheduled_snapshot*`, `REWRITE_LOG.md`, anything under `raw/`, `site/out/`, `site/cal/`, and the old `final/` folder.
9. Canva: edit the text in the design, then re-export any preview the vault uses. Keyword stays pink #E1306C where it was pink.
10. Log every change (file or Canva design id and page, before and after) to `CTA_MIGRATION_LOG.md`, one section per worker.

## 4. Workflow

1. Write the new rule sheet (copy `references/CTA_MIGRATION.md`, change the table). Commit it.
2. Grep the live content repo for every retired word (and its variants: "audit your channel", "free channel audit", the old per-post words) across `bryan-system`, minus the archive paths in rule 8. Also grep `~/subscribr/.claude/email-os` (the Subscribr Customer.io email "Reply AUDIT" was left alone on 2026-10-05 because it is another product).
3. Run `python3 scripts/cta_migrate.py` functions on text sources: `migrate_text(text, kw=None)` rewrites in place by the regex rules above; `topic_keyword(text)` picks the keyword (existing keyword in the piece, else topic regex, else SCOTT); `migrate_kw(kw, text)` for structured fields. `build_planner.py` imports it so planner rows migrate on rebuild.
4. Spawn 3 parallel Sonnet workers with the briefs saved in `references/prompts/`:
   - Worker A: the carousels in `final_ragebait/`, their Canva designs (DAHWuK3ER0k, DAHWuNVXvgU, DAHWuFTrg54, DAHWuBYtkJ0, DAHWuAFNQQk), and the slide images already scheduled in Metricool. Urgent first: scheduled posts due within hours.
   - Worker B1: story templates (01_stories_vault 12 frames, 02_story_templates 7, 07_story_swipes S5; 16 Canva designs, 27 pages).
   - Worker B2: reels and carousel templates (03 carousels, 04 B-roll, 05 faceless, 06 talking head, 08 carousel swipes; 5 Canva edits).
   Main thread meanwhile: planner builder, `blog_email_plan.py`, lead magnets LM1 to LM5 (closing plus the DM 3 audit offer replaced by a cross-link), `build_reels.py`, proof posts, VA_WEEK_1, OPEN_QUESTIONS, the PLAYBOOK lane system, memory.
5. Canva edit recipe: `read-design` with open transaction, `find_and_replace_text` or `replace_text` on the page's text element (font, size and layout unchanged), commit, `export-design` the page as PNG 1080 x 1350, download at once.
6. Metricool slide swap (for a scheduled carousel whose last slide carries the old CTA): `getScheduledPosts` for that day, upload the new PNG (Framer upload URL or Canva export URL with `saveExternalMediaFiles: true`), `updateScheduledPost` with the FULL payload and the new slide URL in the same position. Each update gives a NEW post id with the same uuid; record both. Instagram, Threads, Bluesky and Pinterest are separate posts; Bluesky (first 4 slides) and Pinterest (first 5) usually do not carry the last slide. Check the fresh `getScheduledPosts` after.
7. Captions on scheduled posts: `updateScheduledPost` per network; Pinterest needs `pinterestData.pinLink`.
8. Verify: grep again, count zero outside archives; open the exported images; check Metricool.
9. Update `LEAD_MAGNET_GUIDES.md`, `MANYCHAT.md`, memory `feedback_manychat_keywords.md`, the ig-captions skill's keyword table and `docs/rules/GLOBAL_RULES.md`.

## 5. Variants

- Adding a keyword (2026-10-06): add its PROMISE and MAGNET lines to `cta_migrate.py`, its topic regex to `topic_keyword`, its Kit tag `lm-<keyword>`, its ManyChat automation, its guide row in `LEAD_MAGNET_GUIDES.md`; then update only pieces where the new keyword fits better (no mass migration needed).
- Per-post one-off keyword (VIRAL, "work"): not allowed; either build a ManyChat flow first or use a real keyword.
- Structured data only (planner, JSON): script it with `migrate_text`; no workers needed.

## 6. QA checklist

- [ ] Zero retired words outside the archive paths.
- [ ] Every migrated CTA is the exact promise line for its keyword; one keyword per piece.
- [ ] No new claim introduced; «BRYAN» tags tied to the retired CTA removed, others kept.
- [ ] Canva text edited and exported again; Metricool slide URLs swapped; fresh `getScheduledPosts` read-back done.
- [ ] Log written, with before and after, per worker.
- [ ] Lead-magnet closings cross-link another magnet; no "Reply AUDIT" left.
- [ ] Do not rerun `08_carousel_swipes/_build/gen_swipes.py` (hand fixes in the .md would be lost).

## 7. Outputs and where they go

`CTA_MIGRATION.md` and `CTA_MIGRATION_LOG.md` in `~/budgetdog-analysis/bryan-system/`; changed assets in place; memory `feedback_manychat_keywords.md` plus one line in MEMORY.md; ManyChat flows are built by Bryan or the flow owner (the API key saved on 2026-10-05 returned "Wrong token"; the 9 flows must exist in ManyChat, see lane E notes).

## 8. Open questions

- «BRYAN: confirm» CLAUDE as the ninth keyword (proposed by Claude 2026-10-06).
- «BRYAN: confirm» whether to build a VIRAL flow pointing at /trainings, or move the two posts to a real keyword.
- The Oct 10 trial-reel caption still said EDIT when the guide was not built (resolved by building the guide on 2026-10-06).
- Pink color on "SCOTT" pills in story templates #10 V1 and #16 V2 needs a manual fix; S5, C19, C20 had retired words, decided to become SCOTT, with a warning in HQ.
- YOUTUBE CTA leftovers in some `final_ragebait` captions and an audit sentence inside `final_ragebait/rewrite/*.json` and `apply.py` remain.
- Subscribr Customer.io email with "Reply AUDIT" unchanged by design.

## 9. Files

| File | What it is |
|---|---|
| `scripts/cta_migrate.py` | PROMISE and MAGNET tables, `topic_keyword`, `migrate_text`, `migrate_kw` (copied unchanged; no hard-coded paths) |
| `references/CTA_MIGRATION.md` | The rule sheet (copied; header still says 5 then 8 keywords, the nine apply) |
| `references/CTA_MIGRATION_LOG.md` | Full change log of 2026-10-05 (copied) |
| `references/prompts/2026-10-05_worker_A_carousel_ctas_and_metricool.md` | Worker A brief, verbatim from the raw jsonl |
| `references/prompts/2026-10-05_worker_B1_story_templates.md` | Worker B1 brief |
| `references/prompts/2026-10-05_worker_B2_reels_carousel_templates.md` | Worker B2 brief |
| `~/budgetdog-analysis/bryan-system/final_ragebait/MANYCHAT.md`, `LEAD_MAGNET_GUIDES.md` | Flows and master list (not copied) |

## 10. Session provenance

- `_mining/cards/2026-10-04_faf86e1c.md` (10-05 09:49 to 10:30 migration, the three Agent calls)
- `_mining/cards/2026-09-30_4e5b3ce4.md` (keyword history, 10-02 and 10-06 messages)
- Memory: `feedback_manychat_keywords.md`.
