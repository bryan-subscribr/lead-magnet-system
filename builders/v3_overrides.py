# ==== v3: lead-magnet format (Maria) + hard-line tables/diagrams, no captions, no colour ====
from PIL import Image as _PI, ImageDraw as _PD, ImageFont as _PF
_TOOLS = os.path.dirname(os.path.abspath(__file__)) + '/'
def _F(sz, bold=False, serif=False):
    if serif:
        f = _PF.truetype(_TOOLS + 'Lora.ttf', sz)
        try: f.set_variation_by_name('Bold' if bold else 'Regular')
        except Exception: pass
        return f
    return _PF.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf', sz)
_h1_orig = h1
def h1(text, stat=None, page_break=False, page_break_before=False):
    _h1_orig(text, page_break_before=page_break or page_break_before)
def h3(text):
    p = doc.add_paragraph(); add_runs(p, '**' + text + '**'); blank()
def label(text, links=None):
    para((text.rstrip(':') + ': ' + links) if links else text)
_img0 = img
def img(name, width_in=6.0, caption=None, center=False):
    _img0(name, width_in, None, center)
def _hard_table(rows, widths, header=False):
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    borders = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        b = OxmlElement(f'w:{e}'); b.set(qn('w:val'), 'single'); b.set(qn('w:sz'), '8'); b.set(qn('w:color'), '000000'); borders.append(b)
    t._tbl.tblPr.append(borders)
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = t.cell(i, j); c.width = Inches(widths[j]); p = c.paragraphs[0]
            add_runs(p, ('**' + val + '**') if (val and (j == 0 or (header and i == 0)) and not val.startswith('**')) else (val or ''))
            p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(5)
    blank()
def table(rows, widths, bold_rows=(0,)):
    _hard_table(rows, widths, header=True)
def stack(rows, title=None):
    if title: h3(title)
    has_v = any(v for _, v in rows)
    _hard_table([[t.replace('**', ''), v or ''] for t, v in rows] if has_v else [[t.replace('**', '')] for t, _ in rows],
                [3.6, 2.9] if has_v else [6.5])
def flow(steps, name=None, width=6.5):
    n = len(steps); S = 2; pad = 30 * S; gap = 46 * S; bh = 150 * S
    W = 1800 * S; bw = (W - 2 * pad - gap * (n - 1)) // n
    fl = _F(19 * S, bold=True); fb = _F(24 * S, bold=True, serif=True)
    im = _PI.new('RGB', (W, bh + 2 * pad), 'white'); d = _PD.Draw(im)
    for i, (tag, txt) in enumerate(steps):
        x0 = pad + i * (bw + gap); y0 = pad
        d.rectangle((x0, y0, x0 + bw, y0 + bh), outline='black', width=3 * S)
        t = tag.upper(); tw = d.textlength(t, font=fl); d.text((x0 + (bw - tw) / 2, y0 + 26 * S), t, fill='#555555', font=fl)
        words = txt.split(); lines = []; cur = ''
        for w in words:
            if cur and d.textlength(cur + ' ' + w, font=fb) > bw - 24 * S: lines.append(cur); cur = w
            else: cur = (cur + ' ' + w).strip()
        lines.append(cur); lines = lines[:3]
        ty = y0 + 62 * S + (2 - len(lines)) * 14 * S
        for ln in lines:
            tw = d.textlength(ln, font=fb); d.text((x0 + (bw - tw) / 2, ty), ln, fill='black', font=fb); ty += 30 * S
        if i < n - 1:
            ax0 = x0 + bw + 8 * S; ax1 = x0 + bw + gap - 8 * S; ay = y0 + bh / 2
            d.line((ax0, ay, ax1 - 10 * S, ay), fill='black', width=3 * S)
            d.polygon([(ax1, ay), (ax1 - 14 * S, ay - 9 * S), (ax1 - 14 * S, ay + 9 * S)], fill='black')
    im = im.resize((W // S, (bh + 2 * pad) // S), _PI.LANCZOS)
    fn = name or f'_flow_{len(HEADS)}_{abs(hash(str(steps))) % 10**6}.png'
    fn = fn if fn.startswith('_v3') else '_v3' + fn
    im.save(IMG + fn); _img0(fn, width, None, True)
def bullets(items, numbered=False):
    for n, it in enumerate(items, 1):
        txt, subs = (it if isinstance(it, tuple) else (it, []))
        p = doc.add_paragraph(); pf = p.paragraph_format
        pf.left_indent = Inches(0.35); pf.first_line_indent = Inches(-0.25); pf.space_after = Pt(6); pf.tab_stops.add_tab_stop(Inches(0.35))
        add_runs(p, (f'{n}.\t' if numbered else '•\t') + txt)
        for s2 in subs:
            q = doc.add_paragraph(); qf = q.paragraph_format
            qf.left_indent = Inches(0.75); qf.first_line_indent = Inches(-0.25); qf.space_after = Pt(4); qf.tab_stops.add_tab_stop(Inches(0.75))
            add_runs(q, '◦\t' + s2)
    blank()
