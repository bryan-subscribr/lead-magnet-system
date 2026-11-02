# STYLE CHANGE (overrides PHASE_BRIEF.md where they conflict) — Bryan, 2026-10-30

Bryan: "I don't want this to be some gay fucking shit. I want something I can screen-share, like Linden Chasteen's video (https://www.youtube.com/watch?v=4f64hPyy978, 'Every $1M/Mo YouTube Channel Explained in 1 Hour'). No AI boilerplate."

Reference look: /Users/bryanng/lead_magnets/MAGNUM/work/linden/docpages.jpg (READ IT). It's an operator's research doc you scroll through on camera, not a blog post or ebook.

## Writing
- Terse operator notes. Short bold subheads, 1 to 3 sentence paragraphs that state facts, numbers and mechanics. Nested bullets for steps. No warm-up sentences, no "In this section", no motivational lines, no rhetorical questions, no "Try this:" lines, no "Now, you might be thinking", no wrap-up lines. Every line should be something Bryan can point at while talking.
- Still Bryan's first person where it's his view ("We do X for Clover"), still zero AI tells (DEAI_RULES.md), still numbers in full, still strict sourcing rules from PHASE_BRIEF.md.
- Prefer structure over prose: stacks, flows, tables, bullets, screenshots. Prose only to explain a mechanic.
- Keep the soft CTA as a single plain line: para("**Book your 30-minute strategy call here:** [[viralbangers.com/book|https://www.viralbangers.com/book]]")

## Builder (NEW): /Users/bryanng/lead_magnets/MAGNUM/tools/docbuilder_ss.py  (same CLI as before)
- h1(text, stat=None): bold sans heading with black rule; stat = grey right-aligned figure, e.g. h1('Scott Taylor', stat='~$40,000/mo from YouTube')
- h2(text), h3(text) (small bold subhead like "Offer Stack")
- label('CHANNEL:', '[[@handle|url]] · 35,800 subs')  small-caps grey line
- stack([('Bold item text', 'grey right value'), ...], title='Offer Stack')  cyan left-bar list (Linden's Offer Stack)
- flow([('TOF','Search videos'), ('MIDDLE','Strategy video'), ('BOTTOM','Webinar')])  colored step boxes with arrows (auto PNG). Use for funnels, processes, pipelines.
- bullets([...]) supports nesting: bullets([('Promo starts 1 month out', ['1 trailer video 2 weeks out', '4 videos promoting registration']), 'Next item'])
- para(text), img(name, width, caption='(...)') (caption renders small grey), table(rows, widths, bold_rows=(0,)), checklist([...])
- Screenshots should be big and real (channel pages, video pages with pinned comments, thumbnails grids, Social Blade-style growth charts, Studio graphs, funnel pages). Lots of them. No text labels on images.
- Test build with docbuilder_ss.py (wrapper: title_page('Test', [('x', False)]); toc_page(levels=1); then exec your part). Render-check and READ pages.

If you already wrote parts/phase<N>.py in the old style, rewrite it to this style (keep the research and images you gathered).
