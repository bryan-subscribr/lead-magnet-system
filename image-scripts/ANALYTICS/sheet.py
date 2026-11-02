import sys,subprocess,os,glob
from PIL import Image,ImageDraw
# usage: sheet.py video out.jpg every_sec offset_label_sec
v,out,every=sys.argv[1],sys.argv[2],float(sys.argv[3]); base=float(sys.argv[4]) if len(sys.argv)>4 else 0
tmp=out+'_frames'; os.makedirs(tmp,exist_ok=True)
for f in glob.glob(tmp+'/*.jpg'): os.remove(f)
subprocess.run(['ffmpeg','-loglevel','error','-i',v,'-vf',f'fps=1/{every},scale=400:-1',tmp+'/f%04d.jpg'])
fs=sorted(glob.glob(tmp+'/*.jpg'))
cols=5; w,h=Image.open(fs[0]).size; rows=(len(fs)+cols-1)//cols
S=Image.new('RGB',(cols*w,rows*(h+18)),'white'); d=ImageDraw.Draw(S)
for i,f in enumerate(fs):
    x=(i%cols)*w; y=(i//cols)*(h+18); S.paste(Image.open(f),(x,y+18))
    t=base+i*every; d.text((x+4,y+2),f'{int(t//60)}:{int(t%60):02d}',fill='black')
S.save(out,quality=70); print(out,len(fs))
