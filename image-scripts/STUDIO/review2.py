import sys,glob,os
from PIL import Image, ImageDraw, ImageFont
fs=sorted(glob.glob(sys.argv[1])); out=sys.argv[2]; per=6; cols=2; W=800
font=ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf",22)
for k in range(0,len(fs),per):
    ims=[]
    for f in fs[k:k+per]:
        im=Image.open(f).convert("RGB"); im=im.resize((W,int(im.height*W/im.width))); ims.append((os.path.basename(f),im))
    H=max(i.height for _,i in ims); rows=(len(ims)+1)//2
    s=Image.new("RGB",(cols*W+10,rows*(H+10)),"grey"); d=ImageDraw.Draw(s)
    for j,(n,im) in enumerate(ims):
        x,y=(j%2)*(W+10),(j//2)*(H+10); s.paste(im,(x,y)); d.rectangle([x,y,x+len(n)*13,y+28],fill="black"); d.text((x+4,y+2),n,fill="yellow",font=font)
    s.save(f"{out}_{k//per:02d}.jpg",quality=72)
