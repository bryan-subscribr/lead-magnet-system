#!/usr/bin/env python3
"""Image helpers for lead-magnet docs.

  python3 images.py extract-pdf  SRC.pdf OUTDIR          # every embedded image (pdfimages -png), plus a page list
  python3 images.py extract-pptx SRC.pptx OUTDIR         # media files + per-slide text/image map (slides.txt)
  python3 images.py slides-keynote SRC.pptx OUTDIR       # full slide renders via Keynote (for diagram slides)
  python3 images.py contact OUTPNG IMG1 IMG2 ...         # labelled contact sheet so you can eyeball candidates
  python3 images.py row OUT.jpg H IMG1 IMG2 ... [--labels a,b,c  or  'a|b|c' when labels contain commas] [--cols N]   # side-by-side / grid collage
  python3 images.py compress SRC OUT.jpg [MAXW]          # resize to <=MAXW (1600) and JPEG q84

Collages: white background, 24px gaps, optional bold Arial labels under each image.
"""
import os, re, sys, glob, shutil, subprocess, zipfile
from PIL import Image, ImageDraw, ImageFont

FONT = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'


def compress(src, out, maxw=1600):
    im = Image.open(src).convert('RGB')
    if im.width > maxw:
        im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(out, quality=84, optimize=True)


def row(out, h, paths, labels=None, cols=None, gap=24):
    font = ImageFont.truetype(FONT, max(24, h // 12))
    ims = [Image.open(p).convert('RGB') for p in paths]
    ims = [i.resize((int(i.width * h / i.height), h), Image.LANCZOS) for i in ims]
    cols = cols or len(ims)
    rows = [ims[i:i + cols] for i in range(0, len(ims), cols)]
    lab = int(h / 6) if labels else 0
    W = max(sum(i.width for i in r) + gap * (len(r) - 1) for r in rows)
    H = len(rows) * (h + lab) + gap * (len(rows) - 1)
    c = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(c); k = 0
    for ri, r in enumerate(rows):
        x = (W - (sum(i.width for i in r) + gap * (len(r) - 1))) // 2; y = ri * (h + lab + gap)
        for im in r:
            c.paste(im, (x, y))
            if labels:
                t = labels[k]; tw = d.textlength(t, font=font)
                d.text((x + (im.width - tw) / 2, y + h + 10), t, fill='black', font=font)
            x += im.width + gap; k += 1
    if c.width > 1800:
        c = c.resize((1800, int(c.height * 1800 / c.width)), Image.LANCZOS)
    c.save(out, quality=85, optimize=True)


def contact(out, paths, cell=(300, 200)):
    cells = []
    for p in paths:
        im = Image.open(p).convert('RGB'); size = im.size; im.thumbnail(cell)
        c = Image.new('RGB', (cell[0], cell[1] + 22), 'white'); c.paste(im, (0, 0))
        ImageDraw.Draw(c).text((4, cell[1] + 6), f'{os.path.basename(p)} {size}', fill='red'); cells.append(c)
    cols = 6; rows = (len(cells) + cols - 1) // cols
    s = Image.new('RGB', (cell[0] * cols, (cell[1] + 22) * rows), 'white')
    for i, c in enumerate(cells):
        s.paste(c, ((i % cols) * cell[0], (i // cols) * (cell[1] + 22)))
    s.save(out)


def extract_pdf(src, outdir):
    os.makedirs(outdir, exist_ok=True)
    print(subprocess.run(['pdfimages', '-list', src], capture_output=True, text=True).stdout)
    subprocess.run(['pdfimages', '-png', src, os.path.join(outdir, 'i')], check=True)
    # drop tiny assets (logos, smasks, "Made with Gamma" badge)
    for f in glob.glob(os.path.join(outdir, 'i-*.png')):
        w, h = Image.open(f).size
        if w < 300 or h < 150 or (w, h) == (921, 220):
            os.remove(f)
    print('kept', sorted(os.listdir(outdir)))


def extract_pptx(src, outdir):
    os.makedirs(outdir, exist_ok=True)
    z = zipfile.ZipFile(src)
    for n in z.namelist():
        if n.startswith('ppt/media/'):
            with open(os.path.join(outdir, os.path.basename(n)), 'wb') as f:
                f.write(z.read(n))
    slides = sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)],
                    key=lambda n: int(re.search(r'(\d+)', n.split('/')[-1]).group(1)))
    lines = []
    for n in slides:
        num = int(re.search(r'slide(\d+)', n).group(1))
        x = z.read(n).decode('utf8', 'ignore')
        text = ' | '.join(t for t in re.findall(r'<a:t>([^<]*)</a:t>', x) if t.strip())
        rel = n.replace('slides/', 'slides/_rels/') + '.rels'
        imgs = re.findall(r'media/([^"]+)', z.read(rel).decode()) if rel in z.namelist() else []
        lines.append(f'{num} :: {text[:400]} || IMG: {",".join(imgs)}')
    open(os.path.join(outdir, 'slides.txt'), 'w').write('\n'.join(lines))
    print(f'{len(slides)} slides; map in {outdir}/slides.txt (images repeated on every slide are template chrome)')


def slides_keynote(src, outdir):
    os.makedirs(outdir, exist_ok=True)
    subprocess.run(['osascript', '-e', 'tell application "Keynote" to activate'])
    script = f'''
set src to POSIX file "{os.path.abspath(src)}"
set outF to POSIX file "{os.path.abspath(outdir)}"
tell application "Keynote"
  set d to open src
  delay 3
  export d to outF as slide images with properties {{image format:PNG, skipped slides:false}}
  close d saving no
end tell'''
    subprocess.run(['osascript', '-e', script], check=True)
    print(len(os.listdir(outdir)), 'slide PNGs in', outdir)


if __name__ == '__main__':
    cmd, *a = sys.argv[1:]
    if cmd == 'extract-pdf': extract_pdf(a[0], a[1])
    elif cmd == 'extract-pptx': extract_pptx(a[0], a[1])
    elif cmd == 'slides-keynote': slides_keynote(a[0], a[1])
    elif cmd == 'contact': contact(a[0], a[1:])
    elif cmd == 'compress': compress(a[0], a[1], int(a[2]) if len(a) > 2 else 1600)
    elif cmd == 'row':
        labels = cols = None; rest = []
        it = iter(a[2:])
        for x in it:
            if x == '--labels': v = next(it); labels = v.split('|') if '|' in v else v.split(',')
            elif x == '--cols': cols = int(next(it))
            else: rest.append(x)
        row(a[0], int(a[1]), rest, labels, cols)
    else:
        sys.exit(__doc__)
