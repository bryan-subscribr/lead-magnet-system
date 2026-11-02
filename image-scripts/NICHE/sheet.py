import sys,glob,os
from PIL import Image,ImageDraw,ImageFont
d,out,step,offset=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
fs=sorted(glob.glob(d+'/f_*.jpg'))
f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',22)
cols=6; w,h=Image.open(fs[0]).size
rows=(len(fs)+cols-1)//cols
S=Image.new('RGB',(cols*w,rows*h),'white'); dr=ImageDraw.Draw(S)
for i,p in enumerate(fs):
    x,y=(i%cols)*w,(i//cols)*h; S.paste(Image.open(p),(x,y))
    t=offset+i*step; dr.rectangle([x,y,x+90,y+28],fill='black'); dr.text((x+4,y+2),f"{t//60}:{t%60:02d}",fill='yellow',font=f)
S.save(out,quality=60)
