# brain/tools

## trope-lint.py
Checks email drafts against the AI-writing-tropes list. Run it on anything before it is called ready.

    python3 brain/tools/trope-lint.py drafts/relaunch-2026-08/
    python3 brain/tools/trope-lint.py drafts/relaunch-2026-08/ --quiet   # failures only
    python3 brain/tools/trope-lint.py path/to/one-draft.md
    python3 brain/tools/trope-lint.py drafts/ --json

Exits 1 on any ERROR or exceeded CAP, so it can gate a workflow.

**Severity**
- `ERROR` never acceptable: magic adverbs, the delve family, grandiose nouns, serves-as dodge,
  "Not X. Not Y.", question-then-answer, worth-noting filler, superficial -ing tails, here's-the-kicker,
  think-of-it-as, false vulnerability, truth-is-simple, stakes inflation, pedagogical voice, vague
  attributions, invented concept labels, em dashes, smart quotes, unicode arrows, bold-first bullets,
  corporate connectors, anaphora (3+ paragraphs), short-fragment runs (4+), listicle-in-a-trench-coat.
- `CAP:1` allowed once per email, flagged above that: negative parallelism, "here's", uncontracted forms.
- `INFO` judgement only, never fails: false ranges, a distinctive word repeated 6+ times.

**Why some tropes are capped rather than banned.** Bryan's verified corpus has 100 fragment paragraphs
opening with Because/And/But/So across 15 emails, and the "X isn't the hard part, Y is" contrast is a
documented signature. Banning those would strip the voice, so they are capped at the level the tropes doc
itself recommends: effective once, an insult at ten.

**Extraction.** Strips YAML frontmatter, note blockquotes, «BRYAN: …» placeholders, headers, subject and
preview lines, numbered subject options, scorecards, tables, merge fields, URLs and signoff lines, so only
the prose a reader sees gets linted. Splits multi-email files on `## Email N` / `## Day N` and ignores
build-spec and appendix sections.
