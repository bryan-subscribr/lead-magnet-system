import sys,glob,os
from PIL import Image,ImageDraw
fs=sorted(glob.glob(sys.argv[1]+'/*.jpg')); out=sys.argv[2]
T=300; cells=[]
for f in fs:
    im=Image.open(f); im.thumbnail((T,T)); c=Image.new('RGB',(T,T+16),'white'); c.paste(im,((T-im.width)//2,16)); ImageDraw.Draw(c).text((2,2),os.path.basename(f)[:40],fill='black'); cells.append(c)
cols=7; rows=(len(cells)+cols-1)//cols
S=Image.new('RGB',(cols*T,rows*(T+16)),'white')
for i,c in enumerate(cells): S.paste(c,((i%cols)*T,(i//cols)*(T+16)))
S.save(out,quality=80); print(len(cells))
