#!/usr/bin/env python3
"""Build a lead-magnet .docx in the Maria Wendt Google-Doc format.

Usage:
    python3 docbuilder.py CONTENT.py OUT.docx --img-dir DIR

CONTENT.py is plain Python that calls the helpers below, top to bottom:
    title_page(title, subtitle_parts, hero_img)   # subtitle_parts = [("And ", False), ("Exactly", True), (" How...", False)]
    toc_page(levels=2)                             # real Word TOC field (dotted leaders, page numbers); levels=1 for H1 only.
                                                   # Two-pass: build, render_check, toc_pages.py, rebuild with --toc-pages
    h1(text, page_break=False) / h2(text)
    para(text) / img(name, width_in, caption=None, center=False)
    bullets([...], numbered=False) / checklist([...]) / table(rows, widths_in, bold_rows=())
    cta_link(label, url)
Inline markup in text: **bold**, *italic*, [[label|url]], {AST} = a literal asterisk (e.g. f{AST}cking).
"""
import argparse, os, re, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'skills', 'lead-magnet-doc', 'scripts')
TEMPLATE = os.path.join(HERE, '..', 'assets', 'template.docx')
CENTER = WD_ALIGN_PARAGRAPH.CENTER

ap = argparse.ArgumentParser()
ap.add_argument('content'); ap.add_argument('out'); ap.add_argument('--img-dir', required=True)
ap.add_argument('--docs', action='store_true', help='Google Docs upload copy: leave 2 empty lines under the TOC heading for the native Docs TOC instead of static entries')
ap.add_argument('--toc-pages', help='JSON list of page numbers, one per H1/H2 in order (from toc_pages.py); omit for placeholder numbers')
args = ap.parse_args()
IMG = args.img_dir.rstrip('/') + '/'

doc = Document(TEMPLATE)
body = doc.element.body
for el in list(body):
    if el.tag != qn('w:sectPr'):
        body.remove(el)
HEADS = []
TOC = []  # (level, text, bookmark)
TOC_ANCHOR = []
TOC_LEVELS = [2]


def fonts(run, name):
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.insert(0, rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), name)


def _hyperlink(p, label, url, size=None):
    rid = p.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), rid)
    r = OxmlElement('w:r'); rpr = OxmlElement('w:rPr')
    c = OxmlElement('w:color'); c.set(qn('w:val'), '1155CC'); rpr.append(c)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rpr.append(u)
    rpr.append(OxmlElement('w:b'))
    if size:
        sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(int(size * 2))); rpr.append(sz)
    r.append(rpr); t = OxmlElement('w:t'); t.text = label; t.set(qn('xml:space'), 'preserve'); r.append(t)
    h.append(r); p._p.append(h)


def add_runs(p, text, size=None, font=None, italic_all=False):
    for tok in re.split(r'(\*\*.+?\*\*|\*.+?\*|\[\[.+?\]\])', text):
        if not tok:
            continue
        if tok.startswith('[['):
            label, url = tok[2:-2].split('|'); _hyperlink(p, label, url, size); continue
        b = tok.startswith('**'); i = (not b) and tok.startswith('*') and len(tok) > 1
        t = tok[2:-2] if b else tok[1:-1] if i else tok
        r = p.add_run(t.replace('{AST}', '*'))
        r.bold = b or None
        r.italic = (i or italic_all) or None
        if size: r.font.size = Pt(size)
        if font: fonts(r, font)
    return p


def blank():
    doc.add_paragraph()


def page_break():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def para(text, blank_after=True, align=None):
    p = doc.add_paragraph(); add_runs(p, text)
    if align: p.alignment = align
    if blank_after: blank()
    return p


def _bookmark(p, level, text):
    n = len(TOC); bm = f'_Toc{100000 + n}'
    s = OxmlElement('w:bookmarkStart'); s.set(qn('w:id'), str(n)); s.set(qn('w:name'), bm)
    e = OxmlElement('w:bookmarkEnd'); e.set(qn('w:id'), str(n))
    p._p.insert(1 if p._p.pPr is not None else 0, s); p._p.append(e)
    TOC.append((level, text, bm))


def h1(text, page_break_before=False, page_break=False):
    if page_break_before or page_break:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    p = doc.add_paragraph(style='Heading 1'); fonts(p.add_run(text), 'Lora'); HEADS.append(text)
    _bookmark(p, 1, text)
    blank()


def h2(text):
    p = doc.add_paragraph(style='Heading 2'); fonts(p.add_run(text), 'Lora')
    _bookmark(p, 2, text)
    blank()


def _build_toc(pages):
    # Static TOC: dotted leaders, page numbers from toc_pages.py, entries link to heading bookmarks.
    anchor = TOC_ANCHOR[0]
    out = []  # static entries, no TOC field: Pages/Word would regenerate a field in their own style and shift page numbers
    def run(parent, text=None, bold=False, tab=False):
        r = OxmlElement('w:r'); rpr = OxmlElement('w:rPr'); rf = OxmlElement('w:rFonts')
        for a in ('w:ascii', 'w:hAnsi', 'w:cs'): rf.set(qn(a), 'Arial')
        rpr.append(rf)
        if bold: rpr.append(OxmlElement('w:b'))
        sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '22'); rpr.append(sz); r.append(rpr)
        if tab: r.append(OxmlElement('w:tab'))
        if text is not None:
            t = OxmlElement('w:t'); t.set(qn('xml:space'), 'preserve'); t.text = text; r.append(t)
        parent.append(r); return r
    ents = [e for e in TOC if e[0] <= TOC_LEVELS[0]]
    for i, (lvl, text, bm) in enumerate(ents):
        p = OxmlElement('w:p'); ppr = OxmlElement('w:pPr')
        tabs = OxmlElement('w:tabs'); tb = OxmlElement('w:tab'); tb.set(qn('w:val'), 'right'); tb.set(qn('w:leader'), 'dot'); tb.set(qn('w:pos'), '9350'); tabs.append(tb); ppr.append(tabs)
        sp = OxmlElement('w:spacing'); sp.set(qn('w:before'), '120' if lvl == 1 else '40'); sp.set(qn('w:after'), '40'); ppr.append(sp)
        if lvl == 2:
            ind = OxmlElement('w:ind'); ind.set(qn('w:left'), '360'); ppr.append(ind)
        p.append(ppr)
        h = OxmlElement('w:hyperlink'); h.set(qn('w:anchor'), bm); h.set(qn('w:history'), '1')
        run(h, text, bold=(lvl == 1)); run(h, None, tab=True)
        run(h, str(pages[i]) if pages else '00', bold=(lvl == 1))
        p.append(h)
        out.append(p)
    for p in reversed(out):
        anchor.addnext(p)


def img(name, width=6.0, caption=None, center=False):
    p = doc.add_paragraph()
    if center: p.alignment = CENTER
    p.add_run().add_picture(IMG + name, width=Inches(width))
    if caption:
        c = doc.add_paragraph(); add_runs(c, caption, italic_all=True)
        if center: c.alignment = CENTER
    blank()


def bullets(items, numbered=False):
    for n, it in enumerate(items, 1):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.left_indent = Inches(0.35); pf.first_line_indent = Inches(-0.25); pf.space_after = Pt(6)
        pf.tab_stops.add_tab_stop(Inches(0.35))
        add_runs(p, (f'{n}.\t' if numbered else '•\t') + it)
    blank()


def checklist(items):
    for it in items:
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(8); add_runs(p, '☐  ' + it)
    blank()


def _shade(cell, hexfill):
    tcPr = cell._tc.get_or_add_tcPr(); s = OxmlElement('w:shd')
    s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), hexfill); tcPr.append(s)


def table(rows, widths, bold_rows=()):
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    borders = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        b = OxmlElement(f'w:{e}'); b.set(qn('w:val'), 'single'); b.set(qn('w:sz'), '4'); b.set(qn('w:color'), 'BFBFBF'); borders.append(b)
    t._tbl.tblPr.append(borders)
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = t.cell(i, j); c.width = Inches(widths[j]); p = c.paragraphs[0]
            add_runs(p, f'**{val}**' if (i == 0 or i in bold_rows) and val else val)
            p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(4)
            if i == 0: _shade(c, 'F3F3F3')
    blank()


def title_page(title, subtitle_parts, hero=None, title_pt=30, subtitle_pt=22):
    p = doc.add_paragraph(style='Title'); p.alignment = CENTER
    r = p.add_run(title); fonts(r, 'Lora'); r.font.size = Pt(title_pt)
    p = doc.add_paragraph(); p.alignment = CENTER
    for t, blue in subtitle_parts:
        r = p.add_run(t); fonts(r, 'Lora'); r.italic = True; r.underline = True; r.font.size = Pt(subtitle_pt)
        if blue: r.font.color.rgb = RGBColor(0, 0, 0xFF)
    blank()
    if hero: img(hero, 6.5, center=True)


def toc_page(levels=2):
    TOC_LEVELS[0] = levels
    page_break()
    p = doc.add_paragraph(); p.alignment = CENTER
    r = p.add_run('Table Of Contents'); fonts(r, 'Lora'); r.italic = True; r.font.size = Pt(28)
    a = doc.add_paragraph(); TOC_ANCHOR.append(a._p)
    page_break()


def cta_link(label, url, lead='**Go to** ', size=14):
    p = doc.add_paragraph(); add_runs(p, f'{lead}[[{label}|{url}]]', size=size)


# ==== Screen-share doc style (Linden Chasteen-like): clean sans, cyan rule, stacks, flows ====
from PIL import Image as _PI, ImageDraw as _PD, ImageFont as _PF
SANS = 'Arial'; CYAN = '2BD4E8'; GREY = RGBColor(0x99, 0x99, 0x99)
def _rule(p, color='000000', sz=12, space=4):
    pPr = p._p.get_or_add_pPr(); bdr = OxmlElement('w:pBdr'); b = OxmlElement('w:bottom')
    b.set(qn('w:val'), 'single'); b.set(qn('w:sz'), str(sz)); b.set(qn('w:space'), str(space)); b.set(qn('w:color'), color)
    bdr.append(b); pPr.append(bdr)
def _leftbar(p, color=CYAN, sz=18):
    pPr = p._p.get_or_add_pPr(); bdr = OxmlElement('w:pBdr'); b = OxmlElement('w:left')
    b.set(qn('w:val'), 'single'); b.set(qn('w:sz'), str(sz)); b.set(qn('w:space'), '8'); b.set(qn('w:color'), color)
    bdr.append(b); pPr.append(bdr)
def _tabstop(p, pos_in=6.4):
    pPr = p._p.get_or_add_pPr(); tabs = OxmlElement('w:tabs'); t = OxmlElement('w:tab')
    t.set(qn('w:val'), 'right'); t.set(qn('w:pos'), str(int(pos_in * 1440))); tabs.append(t); pPr.append(tabs)
def _sans_all():
    for p in doc.paragraphs:
        for r in p.runs:
            if r._element.find(qn('w:rPr')) is None or r._element.find(qn('w:rPr')).find(qn('w:rFonts')) is None:
                fonts(r, SANS)
def title_page(title, subtitle_parts=None, hero=None, title_pt=30, subtitle_pt=12):
    p = doc.add_paragraph(); r = p.add_run(title); fonts(r, SANS); r.bold = True; r.font.size = Pt(title_pt)
    _rule(p, CYAN, 24, 8)
    if subtitle_parts:
        p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(10)
        for t, _blue in (subtitle_parts if isinstance(subtitle_parts, list) else [(subtitle_parts, False)]):
            r = p.add_run(t); fonts(r, SANS); r.font.size = Pt(subtitle_pt); r.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    blank()
    if hero: img(hero, 6.5)
def h1(text, stat=None, page_break=False, page_break_before=False):
    if page_break or page_break_before: page_break_fn()
    p = doc.add_paragraph(style='Heading 1'); r = p.add_run(text); fonts(r, SANS); r.bold = True; r.font.size = Pt(20)
    r.font.color.rgb = RGBColor(0, 0, 0)
    if stat:
        _tabstop(p); r2 = p.add_run('\t' + stat); fonts(r2, SANS); r2.font.size = Pt(10); r2.font.color.rgb = GREY; r2.bold = False
    _rule(p, '000000', 12, 6); HEADS.append(text); _bookmark(p, 1, text)
    p.paragraph_format.space_before = Pt(18)
def h2(text):
    p = doc.add_paragraph(style='Heading 2'); r = p.add_run(text); fonts(r, SANS); r.bold = True; r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0, 0, 0); p.paragraph_format.space_before = Pt(12); _bookmark(p, 2, text)
def page_break_fn():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
def para(text, blank_after=False, align=None):
    p = doc.add_paragraph(); add_runs(p, text, size=10.5, font=SANS)
    p.paragraph_format.space_after = Pt(8); p.paragraph_format.line_spacing = 1.3
    if align: p.alignment = align
    return p
def label(text, links=None):
    """Small caps grey label line, e.g. label('CHANNELS:', '[[@x|url]] · [[@y|url]]')"""
    p = doc.add_paragraph(); r = p.add_run(text.upper() + '  '); fonts(r, SANS); r.font.size = Pt(8.5); r.bold = True
    r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    if links: add_runs(p, links, size=9, font=SANS)
    p.paragraph_format.space_after = Pt(6)
def stack(rows, title=None):
    """Cyan left-bar list: rows = [(bold_text, grey_right_value_or_None), ...]"""
    if title: h3(title)
    for t, v in rows:
        p = doc.add_paragraph(); _leftbar(p); _tabstop(p)
        add_runs(p, '**' + t + '**' if not t.startswith('**') else t, size=10, font=SANS)
        if v:
            r = p.add_run('\t' + v); fonts(r, SANS); r.font.size = Pt(9); r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
        p.paragraph_format.space_after = Pt(6); p.paragraph_format.left_indent = Inches(0.1)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
def h3(text):
    p = doc.add_paragraph(); r = p.add_run(text); fonts(r, SANS); r.bold = True; r.font.size = Pt(12)
    p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(6)
_FLOWC = ['2BD4E8', 'F2C94C', 'F28B82', '222222', '6FCF97', 'BB86FC']
def flow(steps, name=None, width=6.5):
    """Colored step boxes with arrows, rendered to PNG. steps = [('TOF','Main Channel Content'), ...]"""
    n = len(steps); W = 1800; gap = 0; bw = W // n; H = 190
    im = _PI.new('RGB', (W + 4, H + 4), 'white'); d = _PD.Draw(im)
    try:
        fs = _PF.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 26); fb = _PF.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 34)
    except Exception:
        fs = fb = _PF.load_default()
    for i, (tag, txt) in enumerate(steps):
        x0 = 2 + i * bw; c = '#' + _FLOWC[i % len(_FLOWC)]
        d.rectangle((x0, 2, x0 + bw - 6, H), outline=c, width=6)
        tw = d.textlength(tag.upper(), font=fs); d.text((x0 + (bw - 6 - tw) / 2, 45), tag.upper(), fill='#555555', font=fs)
        words = txt.split(); lines = []; cur = ''
        for w in words:
            if d.textlength((cur + ' ' + w).strip(), font=fb) > bw - 40: lines.append(cur); cur = w
            else: cur = (cur + ' ' + w).strip()
        lines.append(cur)
        for j, ln in enumerate(lines[:2]):
            tw = d.textlength(ln, font=fb); d.text((x0 + (bw - 6 - tw) / 2, 90 + j * 40), ln, fill='#111111', font=fb)
        if i < n - 1:
            ax = x0 + bw - 6; d.polygon([(ax - 8, H / 2 - 16), (ax + 18, H / 2), (ax - 8, H / 2 + 16)], fill='#2BD4E8')
    fn = name or f'_flow_{len(HEADS)}_{abs(hash(str(steps))) % 10**6}.png'
    im.save(IMG + fn); img(fn, width)
def bullets(items, numbered=False):
    """Supports nesting: an item can be ('text', ['sub1', 'sub2'])."""
    for n, it in enumerate(items, 1):
        txt, subs = (it if isinstance(it, tuple) else (it, []))
        p = doc.add_paragraph(); pf = p.paragraph_format
        pf.left_indent = Inches(0.35); pf.first_line_indent = Inches(-0.2); pf.space_after = Pt(4); pf.tab_stops.add_tab_stop(Inches(0.35))
        add_runs(p, (f'{n}.\t' if numbered else '\u2022\t') + txt, size=10.5, font=SANS)
        for s2 in subs:
            q = doc.add_paragraph(); qf = q.paragraph_format
            qf.left_indent = Inches(0.7); qf.first_line_indent = Inches(-0.2); qf.space_after = Pt(3); qf.tab_stops.add_tab_stop(Inches(0.7))
            add_runs(q, '\u25e6\t' + s2, size=10.5, font=SANS)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
_img_orig = img
def img(name, width_in=6.5, caption=None, center=False):
    _img_orig(name, width_in, None, center)
    if caption:
        p = doc.add_paragraph(); r = p.add_run(caption.strip('()')); fonts(r, SANS); r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0x77, 0x77, 0x77); p.paragraph_format.space_after = Pt(10)

ns = dict(globals())
# keep old content files working: they call h1(..., page_break=True) and the doc/TOC lines are skipped
src = open(args.content).read()
exec(compile(src, args.content, 'exec'), ns)
if TOC_ANCHOR and args.docs:
    TOC_ANCHOR[0].addnext(OxmlElement('w:p'))
elif TOC_ANCHOR:
    import json
    pages = json.load(open(args.toc_pages)) if args.toc_pages else None
    ents = [e for e in TOC if e[0] <= TOC_LEVELS[0]]
    if pages and len(pages) != len(ents):
        sys.exit(f'--toc-pages has {len(pages)} numbers but TOC has {len(ents)} headings')
    _build_toc(pages)
    json.dump([[l, t] for l, t, _ in ents], open(args.out + '.headings.json', 'w'))
doc.save(args.out)
print('saved', args.out, '| H1 sections:', len(HEADS))
for h in HEADS: print('  -', h)
