"""Apply de-AI rewrites to HQ planner.json and re-render every image that has copy baked in.

python3 apply.py           -> writes planner.json (backup planner.json.pre_deai), re-renders images
Inputs: units.json (original units + row ids), final_units.json (first pass + hand fixes),
        review_a_out.json / review_b_out.json (second pass, optional).
"""
import json, os, re, sys, glob
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = os.path.join(ROOT, 'template_vault/site')
IMG = os.path.join(SITE, 'cal/img')
sys.path.insert(0, ROOT)
import render as R

U = {u['key']: u for u in json.load(open(os.path.join(HERE, 'units.json')))}
F = json.load(open(os.path.join(HERE, 'final_units.json')))
for f in ('review_a_out.json', 'review_b_out.json'):
    p = os.path.join(HERE, f)
    if os.path.exists(p):
        F.update(json.load(open(p)))


def clean(t):
    # mechanical: en dashes in number ranges -> hyphen, curly quotes -> straight
    t = re.sub(r'(\d)\s?–\s?(\d)', r'\1-\2', t).replace('–', '-')
    return t.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")


F = {k: clean(v) for k, v in F.items()}
json.dump(F, open(os.path.join(HERE, 'final_applied.json'), 'w'), ensure_ascii=False, indent=1)

pp = os.path.join(SITE, 'planner.json')
P = json.load(open(pp))
if not os.path.exists(pp + '.pre_deai'):
    json.dump(P, open(pp + '.pre_deai', 'w'), ensure_ascii=False, indent=1)
rows = {r['id']: r for r in P['rows']}
n = 0
for k, u in U.items():
    new = F.get(k, u['text'])
    if new == u['text']:
        continue
    for rid in u['ids']:
        r = rows[rid]
        if (r.get(u['field']) or '').strip() == u['text']:
            r[u['field']] = new
            n += 1
json.dump(P, open(pp, 'w'), ensure_ascii=False, indent=1)
print('planner fields updated:', n)


def row(date, pref):
    m = [r for r in P['rows'] if r['date'] == date and r['id'].startswith(f'{date}_{pref}')]
    return m[0] if m else None


# --- black screens 1920x1080 (Oct 9-13): text = row cap
F_BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'


def black(text, out):
    W, H = 1920, 1080
    img = Image.new('RGB', (W, H), (17, 17, 17))
    d = ImageDraw.Draw(img)
    size = 88
    f = ImageFont.truetype(F_BOLD, size)
    words, lines, line = text.split(), [], ''
    for w in words:
        t = (line + ' ' + w).strip()
        if d.textlength(t, font=f) <= 1560:
            line = t
        else:
            lines.append(line)
            line = w
    lines.append(line)
    lh = int(size * 1.3)
    y = H / 2 - lh * len(lines) / 2 + lh / 2
    for l in lines:
        d.text((W / 2, y), l, font=f, fill=(255, 255, 255), anchor='mm')
        y += lh
    img.save(out)


for dd in ('09', '10', '11', '12', '13'):
    r = row(f'2026-10-{dd}', '1000_facebook-black')
    if r and r.get('cap'):
        black(r['cap'].strip(), os.path.join(IMG, f'black_{dd}.png'))
        r['hook'] = r['cap']

# --- tweet cards (YT community 11:00 + FB tweet 12:00): text = YT community 11:00 cap
R.set_style('single')
av = R.circle_avatar(os.path.join(ROOT, 'avatar.jpg'))
cfg = {'name': 'Bryan Ng', 'handle': '@boomerrbryan', 'verified': True}
for dd in ('09', '10', '11', '12', '13'):
    r = row(f'2026-10-{dd}', '1100_youtube-community')
    if r and r.get('cap'):
        img, _ = R.render_slide(r['cap'].strip(), cfg, av, ROOT)
        img.save(os.path.join(IMG, f'tweet_{dd}.png'))
        fb = row(f'2026-10-{dd}', '1200_facebook-tweet')
        if fb:
            fb['cap'] = r['cap']

# --- LinkedIn tweet cards Oct 10, 11, 13: first paragraph(s) of the caption, up to the first list
for dd in ('10', '11', '13'):
    r = row(f'2026-10-{dd}', '1400_linkedin')
    if not r or not r.get('cap'):
        continue
    paras = [p for p in r['cap'].split('\n\n') if p.strip()]
    hook = paras[0]
    if len(hook) < 60 and len(paras) > 1 and len(paras[1]) < 140:
        hook = hook + '\n\n' + paras[1]
    img, _ = R.render_slide(hook, cfg, av, ROOT)
    img.convert('RGB').save(os.path.join(IMG, f'linkedin_{dd}.jpg'), quality=92)

json.dump(P, open(pp, 'w'), ensure_ascii=False, indent=1)
print('images re-rendered')
