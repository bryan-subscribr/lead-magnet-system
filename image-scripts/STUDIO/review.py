import sys,glob,os
from PIL import Image, ImageDraw, ImageFont
pat,out=sys.argv[1],sys.argv[2]; cols=3
fs=sorted(glob.glob(pat)); font=ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf",20)
W=640
ims=[]
for f in fs:
    im=Image.open(f).convert("RGB"); h=int(im.height*W/im.width); ims.append((os.path.basename(f),im.resize((W,h))))
H=max(i.height for _,i in ims); rows=(len(ims)+cols-1)//cols
s=Image.new("RGB",(cols*W,rows*H),"white"); d=ImageDraw.Draw(s)
for k,(n,im) in enumerate(ims):
    x,y=(k%cols)*W,(k//cols)*H; s.paste(im,(x,y)); d.rectangle([x,y,x+230,y+26],fill="black"); d.text((x+4,y+2),n,fill="yellow",font=font)
s.save(out,quality=75)
