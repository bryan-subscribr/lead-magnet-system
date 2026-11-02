# usage: sheet.py video start end step outprefix [cols]
import sys, subprocess, os, tempfile
from PIL import Image, ImageDraw, ImageFont
v, s, e, st, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
cols = int(sys.argv[6]) if len(sys.argv) > 6 else 4
td = tempfile.mkdtemp()
times = []; t = s
while t <= e: times.append(t); t += st
thumbs = []
for t in times:
    p = f"{td}/{t:08.1f}.jpg"
    subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",v,"-frames:v","1","-vf","scale=480:-2","-y",p])
    if os.path.exists(p): thumbs.append((t, Image.open(p).convert("RGB")))
font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)
per = cols*5
for k in range(0, len(thumbs), per):
    chunk = thumbs[k:k+per]
    w, h = chunk[0][1].size
    rows = (len(chunk)+cols-1)//cols
    sheet = Image.new("RGB", (cols*w, rows*h), "white")
    d = ImageDraw.Draw(sheet)
    for i,(t,im) in enumerate(chunk):
        x, y = (i%cols)*w, (i//cols)*h
        sheet.paste(im.resize((w,h)), (x,y))
        lab = f"{int(t//60)}:{t%60:04.1f}"
        d.rectangle([x,y,x+110,y+28], fill="black"); d.text((x+4,y+2), lab, fill="yellow", font=font)
    sheet.save(f"{out}_{k//per:02d}.jpg", quality=70)
print(len(thumbs))
