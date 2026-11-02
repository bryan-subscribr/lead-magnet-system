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
