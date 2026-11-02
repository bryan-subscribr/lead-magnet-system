# Humanizer pass brief (blog posts, branch aeo/content-october)

Worktree: ~/Sites/subscribr-aeo-oct  Files: resources/blog/<slug>.md
Edit files in place with the Edit tool. Do NOT run any git command. Do NOT touch files outside your assigned list.

## Goal
Make every assigned post read like a sharp human practitioner wrote it, scored on the humanizer rubric below (target 95+), in Bryan's voice, without changing a single fact, heading, link, table, FAQ marker or frontmatter line.

## Hard constraints (structural guard will reject violations)
1. Frontmatter (between the first two `---` lines): byte-for-byte unchanged.
2. Every heading line (`#`, `##`, `###`): unchanged text and order. Images attach to H2 text; renaming one orphans a screenshot silently.
3. FAQ lines keep the exact format `**Q: question**` on its own line and `**A:** answer` on the next. Same count of Q and A. You may rewrite the answer prose.
4. Keep every number, price, date, percentage, product name, person name, video or document title, and URL exactly. Do not add facts, sources, or claims. Do not delete a paragraph's factual content; rewrite it.
5. Tables: leave rows and cells as they are.
6. Link anchors: keep the link, you may reword the sentence around it.
7. Zero em dashes (—). Use comma, period, colon, or rewrite. Also no " -- ".
8. Do not paste or echo phrasing from another post. Each sourced fact already has one canonical home; do not restate facts that live in other posts.
9. Answer-engine style stays: a short direct answer under a heading ("No.", "It does, with limits.") is deliberate and stays short. Do not inflate it.
10. Key-takeaways blocks, comparison tables, migration sections: keep.

## Rubric to score against (start 100, deduct)
Banned vocabulary (-5 each): delve, tapestry, landscape (abstract), leverage, multifaceted, nuanced, pivotal, realm, robust, seamless, testament, transformative, underscore (verb), utilize, whilst, keen, embark, comprehensive, intricate, commendable, meticulous, paramount, groundbreaking, innovative, cutting-edge, synergy, holistic, paradigm, ecosystem, additionally, align with, crucial, enduring, enhance, fostering, garner, highlight (verb), interplay, intricacies, showcase, vibrant, valuable, profound, renowned, breathtaking, nestled, stunning, essential, vital, significant, substantial, dynamic, elevate, streamline, empower, unlock, harness, navigate (abstract), game-changer, plethora, myriad, remarkable, furthermore, moreover, consequently, hence, thus, therefore, accordingly.
Patterns: significance inflation (-10: "stands as", "pivotal moment", "reflects broader", "setting the stage"); vague attribution (-8: "experts say", "industry reports", "many creators find" with no name); superficial -ing tails (-8: ", highlighting/ensuring/reflecting..."); promotional language (-8: "boasts", "rich", "exemplifies", "commitment to"); formulaic challenges/future sections (-10); copula avoidance (-5: "serves as", "represents", "marks", "offers a", "features a" instead of is/has); negative parallelism (-5: "not just X, it's Y", "not only... but", "isn't about X, it's about Y"); rule of three overuse (-8: forced triples of adjectives/nouns/clauses, more than about one per section); synonym cycling (-5); false ranges (-5: "from X to Y" on no real scale); em dash overuse (-5); bold on every key term (-3); inline-header bullet lists where every item is `**Label:** text` (-5, allowed in a real spec list, not as prose replacement); collaborative or chatbot artifacts (-10: "let's dive in", "here's a breakdown", "I hope this helps"); knowledge-cutoff disclaimers (-10: "as of this writing" is OK only when tied to a dated source check); sycophancy (-8); filler (-5 each: "in order to", "it is important to note", "it's worth noting", "at the end of the day", "here's the thing", "the truth is", "the bottom line", "the key takeaway"); excessive hedging (-8: "could potentially", "might possibly"); generic positive conclusion (-10: "the future looks bright", "exciting times").

## Bryan's voice (apply, do not caricature)
- Casual expert coach. First person "I" when the author speaks, heavy "you". Practitioner talking to a friend, not a press release.
- Short punchy sentence to land a point, then a longer one to explain why. Every paragraph has at least one sentence under 15 words and one over 25. Never three similar-length sentences in a row.
- Never two sentences in one paragraph starting with the same word. Never stack three sub-12-word sentences with the same subject; combine them.
- Simple words: use, about, do, help, show. Cap everyday words at two syllables where a shorter word exists.
- Replace weak verbs (was, had, made, got, went, said) with specific ones in at least half the cases.
- Vary transitions: instead of a drone of But/And/So/Then, use "which meant", "the problem was", "that changed when", "none of that mattered because". Do not use "here's the thing" or "the truth is".
- Opinions allowed and wanted: say what you would do, admit what is uncertain on subjective calls, keep confidence on process.
- End sections and the post on a concrete fact, consequence, or tension. Never vague optimism.
- Everyday analogies, one to three sentences, only where they clarify. Do not add "right?" more than once per post, and only if it fits.
- This is a web article, not a TTS script: fragments are fine as deliberate beats; rhetorical questions rare.

## Process per post
1. Read the whole file. Score it (before) with the rubric; note every hit with the offending phrase.
2. Rewrite offending passages with Edit calls. Also fix rhythm problems the rubric misses: same-starter paragraphs, runs of similar-length sentences, triples, generic section closers.
3. Re-read the edited post start to finish once. Fix anything that still sounds like a chatbot, a press release, or a LinkedIn guru.
4. Run the guards and fix until both pass:
   python3 SCRATCH/check.py <slug>.md
   python3 SCRATCH/scan.py ~/Sites/subscribr-aeo-oct/resources/blog | grep <slug>
   (SCRATCH = /private/tmp/claude-501/-Users-bryanng-subscribr/a9cf1c44-352a-42d5-8fe2-a30d145bf1cd/scratchpad/humanize)
   check.py "numbers reduced" is a warning: confirm each listed number still appears exactly (moved is fine, lost is not).
5. Report per post: before score, after score, word count before/after, the 5 most important changes as before/after snippets, any constraint you could not satisfy and why.

Do not summarise the posts. Do not create new files. Do not commit.
