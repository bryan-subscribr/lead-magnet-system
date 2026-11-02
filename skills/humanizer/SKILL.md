---
name: humanizer
description: Bryan's humanizer and de-AI SOP. Strips AI writing tropes from any copy (negative parallelism and chiasmus, "The X? A Y.", "Here's the thing", em dashes and arrows, bold-first bullets, punchy-fragment spam, magic adverbs, delve/leverage words, fractal summaries, vague attributions, invented concept labels) and holds the zero-tolerance list Bryan set on 2026-10-09. Includes the grumpy-grandpa cut pass, the trope-lint script, the structural-guard recipe for batch humanizing blog posts, the de-AI pipeline for planner copy and baked-in image text, and an allow-list of Bryan signature lines that must survive. Use it on every draft before showing it: lead magnets, docs, emails, posts, captions, scripts, headings, slide and card text. Triggers: "humanize this", "humanizer", "does this sound like AI", "remove AI writing", "make it sound human", "AI tells", "de-AI", "no AI specific tells". NOT for fact-checking (use proof-claims-ledger) and not a voice generator (use bryan-voice).
---

# Humanizer and de-AI

## 1. What this does and when
Two lists plus a process. List A is Bryan's zero-tolerance rule sheet (`references/DEAI_RULES.md`, 2026-10-09). List B is the tropes.fyi catalogue (SOP 1 below, credit: tropes.fyi by ossama.is). Run both on every draft before it is shown, including text baked into images, labels, slide text, docx placeholders and Google Doc headings. Pair with `bryan-voice` when writing as Bryan; where the two disagree on a trope, section 3 says who wins.

## 2. Load first
`docs/rules/GLOBAL_RULES.md` section 1. Then `references/DEAI_RULES.md`. For Bryan-voice text also `bryan-voice/references/voice-dna.md` (never-say list) so you do not strip what he really says aloud.

## 3. Fixed rules
- Zero tolerance (Bryan 2026-10-09): "no AI specific tells from any of the writing. This is something that we cannot tolerate." Not fewer; zero. Source of the rule sheet: `references/DEAI_RULES.md` (18 banned patterns, a must-keep list, a voice paragraph, a self-check).
- Image text, labels, slide text, captions on cards, Google Doc headings and docx placeholders count as writing (2026-10-09, de-AI of the planner re-rendered every card and story frame).
- Never add a fact, number, story or feeling while de-AI-ing; never round a number; keep keywords, CTAs, emojis, hashtags, quoted text and production notes untouched (full list in `DEAI_RULES.md` "Must keep").
- If a piece has no tells, return it unchanged.
- Formatting: no em dashes, no en dashes as dashes, no arrows of any kind, no curly quotes, no bold-first bullets, no bold in cards.
- Headings say plainly what the section is ("Who Is RP Profits?"), never a clever stat label (2026-10-07).
- Conflict rule: published content follows the zero-tolerance sheet. The older cap rules in `scripts/trope_lint.py` (one "not X, it's Y" and one "here's" per email, fragment paragraphs allowed in Bryan's emails) came from the 2026-08 Subscribr email corpus; use them only when Bryan or the email-writing skill says so. The old humanizer note "Bryan does say not X, it's Y out loud, one per piece at most" applies to spoken YouTube scripts, not to captions, cards, emails or docs.
- Quoted policy text, H2 anchors tied to images, and real quotations are exempt from rewrites (a9cf1c44 recipe).

## 4. Workflow
1. Draft (or take the copy).
2. Mechanical pass: `python3 scripts/trope_lint.py <file-or-dir> --quiet` (email drafts; exit 1 on any ERROR or exceeded CAP) or the grep below. For blog posts, `python3 scripts/blog_trope_scan.py <dir>` scores each post (start 100, deduct per hit).
   grep for the em dash, the unicode arrow, the two-character ascii arrow and curly quotes, plus the words: delve, leverage, quietly, deeply, genuinely, truly, "Here's", "isn't just", "serves as", "Let's dive", landscape, Imagine, "Think of it".
3. Structural pass by reading: reframes and chiasmus, "Not X. Not Y. Just Z.", self-asked question then answer, tricolon stacks, anaphora, fragment-paragraph runs, false vulnerability, fake-deep closers, fractal summary lines, invented concept labels, vague attributions. Rewrite as a plain positive statement of the point, never swap a word for a synonym.
4. Grumpy-grandpa cut pass (Bryan 2026-09-28): read every sentence aloud like "an old grandpa yelling over your shoulder" and ask "what is the purpose of this and can I cut this? Because a lot of editing is elimination". If a sentence repeats a concept, or does not add to the sentence, cut it. Verbatim instruction: `references/prompts/2026-09-28_grumpy-grandpa-cut-pass.md`. Delivered as a .docx in ~/Downloads when Bryan asks for a doc.
5. Headings and image text: re-read all headings; for every image with baked-in copy, run steps 2 and 3 on its text and re-render.
6. Allow-list check (section 6): restore nothing silently; flag softened signature lines to Bryan.
7. Self-check from `DEAI_RULES.md`: zero banned items left, every number and name still present, nothing new added, no dashes, arrows or curly quotes.

### 4a. Batch humanizing blog posts (structural-guard recipe, 2026-09-22, card a9cf1c44)
Used on 40 Subscribr blog posts. Baseline mean score 95 (worst 45 with 11 banned words); after: mean 98.5, 36 of 40 files edited, 166 lines changed.
1. Score every post with `scripts/blog_trope_scan.py` (vocabulary, filler, copula dodge, negative parallelism, hedges, -ing tails, em dashes, bold lists, title-case H2s, same-starter paragraphs).
2. Write the shared agent brief (`references/BLOG_HUMANIZE_AGENT_BRIEF.md`) and the guard `scripts/blog_structural_guard.py` (set `BLOG_REPO`).
3. Split the files into groups of 5 and run one Sonnet editor agent per group (8 groups in parallel). Each edits in place with the Edit tool, no git, no files outside its list, and must run the guard until it passes. Prompts: `references/prompts/2026-09-22_blog-humanize-scan-guard-and-agent.md` and `...-groups-2-8-and-tropes-fyi-second-scan.md`.
4. Guards the script enforces: frontmatter byte-identical; heading lines identical (images attach to H2 text); FAQ `**Q:**` and `**A:**` counts equal; no dropped links; no lost numbers (warning, confirm each); tables untouched; zero em dashes; image anchors still present.
5. A thin pass is sent back: group 1's first pass changed only 9 lines and was returned with SendMessage.
6. Second scan for patterns the first pass did not cover (tropes.fyi patterns): prompts in the groups-2-8 file (13:29 and 13:36 agents).

### 4b. De-AI pipeline for planner copy and cards (2026-10-09, card 4e5b3ce4 section I)
1. Gather every copy unit from today onward from the planner (`planner.json` rows, fields `hook` and `cap`), dedupe by text, split into batches of about 22,000 characters in date order: `scripts/deai_prep_units.py` (writes `units.json`, `batch_N.json`). Result: 328 unique units.
2. 6 rewriter agents (general-purpose, one per batch), each reading `DEAI_RULES.md` and the humanizer, writing `out_N.json` as `{key: rewritten text}`, then running the mechanical regex check in the prompt (`references/prompts/2026-10-09_deai-rewriter-agent.md`). 148 units changed.
3. 2 reviewer agents second pass over all outputs (`..._deai-reviewer-agent.md`): 31 more changed.
4. `scripts/deai_apply.py` applies `final_units.json` + review outputs to `planner.json` (backup `planner.json.pre_deai`), straightens curly quotes, re-renders every black-screen, tweet, LinkedIn card and story frame with `render.py`. Paths inside assume the `bryan-system` layout (`HERE/..`, `template_vault/site/cal/img`); keep that layout or edit the three path constants at the top.
5. Propagate: Metricool (14 updates on 13 pending posts), Canva authority headlines, 10 blog posts and the Kit drafts (agent prompts `..._deai-blog-posts-agent.md`, `..._deai-kit-drafts-agents.md`, `..._deai-push-to-kit-agent.md`; Kit drafts only, re-read before overwrite and skip any Bryan edited). 2026-10-10: 9 B-roll version B reels (`..._deai-broll-version-b-agent.md`).
6. Live lead-magnet Google Docs: Apps Script `references/deai-apps-script/Code.gs` edits the 9 docs in place from `{name: {id, pairs, unbold}}` (495 swaps; keeps doc ID, images, links, TOC; a pair applies only when the old text is found exactly once outside the TOC). It was parked awaiting Bryan's OAuth click and never run. Do not run it without that click.

## 5. Variants
- Spoken YouTube script: Bryan's contrast pairs ("clear not clever") are his; keep one or two, strip the rest.
- Client voice: do not call a word a tell if the client actually says it (Razvan says "leverage" and "journey").
- Emails with `scripts/trope_lint.py`: ERROR rules block; CAP rules (negative parallelism, "here's", uncontracted forms) allow one per email; INFO is judgement.
- Shelby Sapp: her project knowledge base has the same tropes list (`~/shelby sapp/docs/tropes.md`, content identical to SOP 1); her compliance rules sit on top (no em dashes, no italics, no quotation marks in script body).

## 6. Signature lines that must survive (allow-list)
From memory `project_open_items.md` (2026-10-09 de-AI pass softened these; "ask if any are catchphrases to restore"): 
- "creating thumbnails is not an art. It's engineering."
- "I don't brainstorm, I steal formats"
- "I'm not a camera guy. I'm a script guy"
- the tweet "Just you vs you"
Spoken signature moves from `bryan-voice`: "clear not clever", "known well, not well known", "need to know, not nice to know", "sorry to tell you, but you're probably not going to make it", "See what I did there?", "Once again,". These are spoken devices; in written pieces keep at most one per piece.
Rule: a signature line is rewritten only if Bryan approves. Until then, in written copy, keep the line exactly if it is the only reframe in the piece, otherwise flag it. «BRYAN: which of the four softened lines do you want restored as written?»

## 7. QA checklist
- [ ] A grep for em dashes, arrows and curly quotes on the output is empty (except quoted source text).
- [ ] No item from `DEAI_RULES.md` banned list remains (1 to 18).
- [ ] Every number, name, keyword, CTA, emoji, hashtag and quote from the input is still present; no new facts.
- [ ] Images with baked-in text were re-rendered after the text change.
- [ ] Headings are plain.
- [ ] Batch jobs: guard script passes, tests pass, thin passes were sent back.
- [ ] Allow-list lines either intact or flagged.

## 8. Outputs and where they go
Same file type as the input (Google Doc edits are new docs; the Drive MCP cannot edit existing doc text). De-AI of planner: `planner.json` plus re-rendered images; log counts in the memory note `project_open_items.md`.

## 9. Open questions
- «BRYAN: restore the four softened signature lines?»
- «BRYAN: run the Apps Script de-AI on the 9 live lead-magnet docs (needs your OAuth click)».

## 10. Files
| Path | What it is |
|---|---|
| `references/DEAI_RULES.md` | Bryan's zero-tolerance sheet, copied from `~/budgetdog-analysis/bryan-system/deai/RULES.md` |
| `references/BLOG_HUMANIZE_AGENT_BRIEF.md` | shared brief for blog editor agents |
| `references/TROPE_LINT_README.md` | trope-lint usage and severity model |
| `references/deai-apps-script/Code.gs` | in-place Google Docs edit script (not run) |
| `references/prompts/` | recovered prompts: grandpa pass, blog humanize scan/guard/agents, trope-lint creation, de-AI rewriters, reviewers, blog, Kit, B-roll |
| `scripts/trope_lint.py` | email trope linter (copied from `~/subscribr/.claude/email-os/brain/tools/`) |
| `scripts/blog_trope_scan.py`, `blog_structural_guard.py` | blog scorer and guard (a9cf1c44) |
| `scripts/deai_prep_units.py`, `deai_apply.py` | planner de-AI pipeline |

## 11. Session provenance
Cards: `2026-09-28_7970e1ef.md` (grandpa pass, 09:31), `2026-09-22_a9cf1c44.md` (structural guard recipe), `2026-07-11_348f7868.md` (trope-lint, 2026-08-24), `2026-09-30_4e5b3ce4.md` section I (de-AI pipeline). Rule sheet: `~/budgetdog-analysis/bryan-system/deai/RULES.md`. Tropes source: https://tropes.fyi by ossama.is.

## SOP 1: AI writing tropes to avoid (tropes.fyi)
Add this file to your AI assistant's system prompt or context to help it avoid
common AI writing patterns. Source: [tropes.fyi](az) by [ossama.is](https://ossama.is)
---
## Word Choice
### "Quietly" and Other Magic Adverbs
Overuse of "quietly" and similar adverbs to convey subtle importance or understated power. AI reaches for these adverbs to make mundane descriptions feel significant. Also includes: "deeply", "fundamentally", "remarkably", "arguably".
**Avoid patterns like:**
- "quietly orchestrating workflows, decisions, and interactions"
- "the one that quietly suffocates everything else"
- "a quiet intelligence behind it"
### "Delve" and Friends
Used to be the most infamous AI tell. "Delve" went from an uncommon English word to appearing in a staggering percentage of AI-generated text. Part of a family of overused AI vocabulary including "certainly", "utilize", "leverage" (as a verb), "robust", "streamline", and "harness".
**Avoid patterns like:**
- "Let's delve into the details..."
- "Delving deeper into this topic..."
- "We certainly need to leverage these robust frameworks..."
### "Tapestry" and "Landscape"
Overuse of ornate or grandiose nouns where simpler words would do. "Tapestry" is used to describe anything interconnected. "Landscape" is used to describe any field or domain. Other offenders: "paradigm", "synergy", "ecosystem", "framework".
**Avoid patterns like:**
- "The rich tapestry of human experience..."
- "Navigating the complex landscape of modern AI..."
- "The ever-evolving landscape of technology..."
### The "Serves As" Dodge
Replacing simple "is" or "are" with pompous alternatives like "serves as", "stands as", "marks", or "represents". AI avoids basic copulas because its repetition penalty pushes it toward fancier constructions (I've studied this!).
**Avoid patterns like:**
- "The building serves as a reminder of the city's heritage."
- "Gallery 825 serves as LAAA's exhibition space for contemporary art."
- "The station marks a pivotal moment in the evolution of regional transit."
---
## Sentence Structure
### Negative Parallelism
The "It's not X -- it's Y" pattern, often with an em dash. The single most commonly identified AI writing tell. Man I f*cking hate it. AI uses this to create false profundity by framing everything as a surprising reframe. One in a piece can be effective; ten in a blog post is a genuine insult to the reader. Before LLMs, people simply did not write like this at scale. Includes the causal variant "not because X, but because Y" where every explanation is framed as a surprise reveal, the em-dash dismissal "X -- not Y", and the cross-sentence reframe where the same noun is negated then repositioned: "The question isn't X. The question is Y."
**Avoid patterns like:**
- "It's not bold. It's backwards."
- "Feeding isn't nutrition. It's dialysis."
- "Half the bugs you chase aren't in your code. They're in your head."
### "Not X. Not Y. Just Z."
The dramatic countdown pattern. AI builds tension by negating two or more things before revealing the actual point. Creates a false sense of narrowing down to the truth.
**Avoid patterns like:**
- "Not a bug. Not a feature. A fundamental design flaw."
- "Not ten. Not fifty. Five hundred and twenty-three lint violations across 67 files."
- "not recklessly, not completely, but enough"
### "The X? A Y."
Self-posed rhetorical questions answered immediately in the next sentence or clause. The model asks a question nobody was asking, then answers it for dramatic effect. Thinks this is the epitome of great writing.
**Avoid patterns like:**
- "The result? Devastating."
- "The worst part? Nobody saw it coming."
- "The scary part? This attack vector is perfect for developers."
### Anaphora Abuse
Repeating the same sentence opening multiple times in quick succession.
**Avoid patterns like:**
- "They assume that users will pay... They assume that developers will build... They assume that ecosystems will emerge... They assume that..."
- "They could expose... They could offer... They could provide... They could create... They could let... They could unlock..."
- "They have built engines, but not vehicles. They have built power, but not leverage. They have built walls, but not doors."
### Tricolon Abuse
Overuse of the rule-of-three pattern, often extended to four or five. A single tricolon is elegant; three back-to-back tricolons are a pattern recognition failure.
**Avoid patterns like:**
- "Products impress people; platforms empower them. Products solve problems; platforms create worlds. Products scale linearly; platforms scale exponentially."
- "identity, payments, compute, distribution"
- "workflows, decisions, and interactions"
### "It's Worth Noting"
Filler transitions that signal nothing. AI uses these phrases to introduce new points without actually connecting them to the previous argument. Also includes: "It bears mentioning", "Importantly", "Interestingly", "Notably".
**Avoid patterns like:**
- "It's worth noting that this approach has limitations."
- "Importantly, we must consider the broader implications."
- "Interestingly, this pattern repeats across industries."
### Superficial Analyses
Tacking a present participle ("-ing") phrase onto the end of a sentence to inject shallow analysis that says nothing. The model attaches significance, legacy, or broader meaning to mundane facts using phrases like "highlighting its importance", "reflecting broader trends", or "contributing to the development of...".
**Avoid patterns like:**
- "contributing to the region's rich cultural heritage"
- "This etymology highlights the enduring legacy of the community's resistance and the transformative power of unity in shaping its identity."
- "underscoring its role as a dynamic hub of activity and culture"
### False Ranges
Using "from X to Y" constructions where X and Y aren't on any real scale. In legitimate use, "from X to Y" implies a spectrum with a meaningful middle. AI uses it as a fancy way to list two loosely related things. "From innovation to cultural transformation" -- what's in between???? Nothing!
**Avoid patterns like:**
- "From innovation to implementation to cultural transformation."
- "From the singularity of the Big Bang to the grand cosmic web."
- "From problem-solving and tool-making to scientific discovery, artistic expression, and technological innovation."
---
## Paragraph Structure
### Short Punchy Fragments
Excessive use of very short sentences or sentence fragments as standalone paragraphs for manufactured emphasis. RLHF training has pushed models toward "writing for readability" aimed at the lowest common denominator: one thought per sentence, no mental state-keeping required. It's an inhuman style. No real person writes first drafts this way because it doesn't match how humans think or speak.
**Avoid patterns like:**
- "He published this. Openly. In a book. As a priest."
- "These weren't just products. And the software side matched. Then it professionalised. But I adapted."
- "Platforms do."
### Listicle in a Trench Coat
Numbered or labeled points dressed up as continuous prose. The model writes what is essentially a listicle but wraps each point in a paragraph that starts with "The first... The second... The third..." to disguise the format. Perhaps you told it to stop generating lists and it decided to do this instead... still very common.
**Avoid patterns like:**
- "The first wall is the absence of a free, scoped API... The second wall is the lack of delegated access... The third wall is the absence of scoped permissions..."
- "The second takeaway is that... The third takeaway is that... The fourth takeaway is that..."
---
## Tone
### "Here's the Kicker"
False suspense transitions that promise a revelation but deliver a point that did NOT need the buildup. The model uses these phrases to manufacture drama before an otherwise unremarkable observation LOL. Also includes: "Here's the thing", "Here's where it gets interesting", "Here's what most people miss", "Here's the starting point", "Here's the deal".
**Avoid patterns like:**
- "Here's the kicker."
- "Here's the thing about AI adoption."
- "Here's where it gets interesting."
### "Think of It As..."
The patronizing analogy. AI constantly reaches for "Think of it as..." or "It's like a..." to simplify concepts. The model defaults to teacher mode and assumes the reader needs a metaphor to understand anything. Often produces analogies that are less clear than the original concept.
**Avoid patterns like:**
- "Think of it like a highway system for data."
- "Think of it as a Swiss Army knife for your workflow."
- "It's like asking someone to buy a car they're only allowed to sit in while it's parked."
### "Imagine a World Where..."
The classic AI invitation to futurism. To sell the argument usually begins with "Imagine" followed by a list of wonderful things that will happen if the reader agrees with the premise.
**Avoid patterns like:**
- "Imagine a world where every tool you use -- your calendar, your inbox, your documents, your CRM, your code editor -- has a quiet intelligence behind it..."
- "In that world, workflows stop being collections of manual steps and start becoming orchestrations."
### False Vulnerability
Simulated self-awareness or honesty that reads as performative. The model pretends to break the fourth wall or admit a bias, creating a false sense of authenticity. Real vulnerability is specific and uncomfortable; AI vulnerability is polished and risk-free!!!!
**Avoid patterns like:**
- "And yes, I'm openly in love with the platform model"
- "And yes, since we're being honest: I'm looking at you, OpenAI, Google, Anthropic, Meta"
- "This is not a rant; it's a diagnosis"
### "The Truth Is Simple"
Asserting that something is obvious, clear or simple instead of actually proving it. If you have to tell the reader your point is clear, it very likely isn't. Also includes the dramatic reveal variant: "but none of them is the real story. The real story is..." -- claiming privileged insight while waving away everything before it.
**Avoid patterns like:**
- "The reality is simpler and less flattering"
- "History is unambiguous on this point"
- "History is clear, the metrics are clear, the examples are clear"
### Grandiose Stakes Inflation
Everything is the most important thing ever. AI inflates the stakes of every argument to world-historical significance. A blog post about API pricing becomes a meditation on the fate of civilization.
**Avoid patterns like:**
- "This will fundamentally reshape how we think about everything."
- "will define the next era of computing"
- "something entirely new"
### "Let's Break This Down"
The pedagogical voice that assumes the reader needs hand-holding. AI defaults to a teacher-student dynamic even when writing for expert audiences. Also includes: "Let's unpack this", "Let's explore", "Let's dive in".
**Avoid patterns like:**
- "Let's break this down step by step."
- "Let's unpack what this really means."
- "Let's explore this idea further."
### Vague Attributions
Attributing claims to unnamed authorities instead of being specific. AI loves to invoke "experts", "observers", "industry reports", and "several publications" without naming anyone. It also inflates the quantity of sources -- presenting what one person said as a widely held view, or writing "several publications have cited" when it means two. If you can't name the expert, you don't have a source.
**Avoid patterns like:**
- "Experts argue that this approach has significant drawbacks."
- "Industry reports suggest that adoption is accelerating."
- "Observers have cited the initiative as a turning point."
### Invented Concept Labels
AI clusters invented compound labels that sound analytical without being grounded. It appends abstract problem-nouns (paradox, trap, creep, divide, vacuum, inversion) to domain words, "supervision paradox", "acceleration trap", "workload creep", and uses them as if they're established, rigorously defined terms. They function as rhetorical shorthand: name a thing, skip the argument. Multiple such labels in the same piece is a strong signal of AI slop.
**Avoid patterns like:**
- "the supervision paradox"
- "the acceleration trap"
- "workload creep"
---
## Formatting
### Em-Dash Addiction
Compulsive overuse of em dashes for dramatic pauses, parenthetical asides and pivot points. A human writer might use 2-3 per piece (and naturally); AI will use 20+.
**Avoid patterns like:**
- "The problem -- and this is the part nobody talks about -- is systemic."
- "The tinkerer spirit didn't die of natural causes -- it was bought out."
- "Not recklessly, not completely -- but enough -- enough to matter."
### Bold-First Bullets
Every bullet point or list item starts with a bolded phrase or sentence. Extremely common in Claude and ChatGPT markdown output. Almost nobody formats lists this way when writing by hand. It's a telltale sign of AI-generated documentation and blog posts AND README files (especially with emojis).
**Avoid patterns like:**
- "Every single bullet point begins with a bold keyword."
- "**Security**: Environment-based configuration with..."
- "**Performance**: Lazy loading of expensive resources..."
### Unicode Decoration
Use of unicode arrows, smart/curly quotes, and other special characters that can't be easily typed on a standard keyboard. Real writers typing in a text editor produce straight quotes and plain ascii arrows. Claude in particular loves the arrow.
**Avoid patterns like:**
- "Input [arrow] Processing [arrow] Output" (written with the unicode arrow character)
- "This leads to better outcomes [arrow] which means higher engagement"
- Curly (smart) quotes and curly apostrophes instead of the straight ones you would actually type
---
## Composition
### Fractal Summaries
"What I'm going to tell you; what I'm telling you; what I just told you" -- applied at every level of the document. Every subsection gets a summary. Every section gets a summary. The document itself gets a summary.
**Avoid patterns like:**
- "In this section, we'll explore... [3000 words later] ...as we've seen in this section."
- "A conclusion that restates every point already made in the previous 3000 words"
- "And so we return to where we began."
### The Dead Metaphor
Latching onto a single metaphor and beating it into the ground across the entire thing. A human writer would introduce a metaphor, use it then move on. AI will repeat the same metaphor 5-10 times.
**Avoid patterns like:**
- "The ecosystem needs ecosystems to build ecosystem value."
- "Walls and doors used 30+ times in the same article"
