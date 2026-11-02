#!/usr/bin/env python3
"""Find the page each H1/H2 lands on in a rendered PDF, for docbuilder --toc-pages.
Usage: python3 toc_pages.py RENDER.pdf OUT.docx.headings.json PAGES.json
Searches pages in order after the TOC page(s), so headings must appear in doc order."""
import json, re, subprocess, sys
pdf, heads, out = sys.argv[1:4]
H = json.load(open(heads))
n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
norm = lambda x: re.sub(r'[^a-z0-9]', '', x.lower())
raw = [subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), '-layout', pdf, '-'], capture_output=True, text=True).stdout for i in range(1, n + 1)]
txt = [norm(r) for r in raw]
lines = [[norm(l) for l in r.splitlines() if norm(l)] for r in raw]
def is_head(key, page):
    # a heading sits on its own line (or wraps): the line is a prefix of the heading, not a longer body sentence
    return any(key.startswith(l) and len(l) >= min(12, len(key)) for l in lines[page])
start = max(i for i, t in enumerate(txt) if 'tableofcontents' in t) + 1
# skip the TOC pages themselves: they list every heading; body starts at the first page that is not TOC-dense
while start < n and sum(norm(h[1])[:30] in txt[start] for h in H) > len(H) * 0.3:
    start += 1
pages, cur = [], start
for lvl, t in H:
    key = norm(t)
    j = next((k for k in range(cur, n) if is_head(key, k)), None)
    if j is None:
        sys.exit(f'not found: {t}')
    pages.append(j + 1); cur = j
json.dump(pages, open(out, 'w')); print(pages)
