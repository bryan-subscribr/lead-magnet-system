import sys,subprocess,os,glob
from PIL import Image,ImageDraw
src,step,out=sys.argv[1],float(sys.argv[2]),sys.argv[3]
start=float(sys.argv[4]) if len(sys.argv)>4 else 0
end=float(sys.argv[5]) if len(sys.argv)>5 else None
tmp=out+'_tmp'; os.makedirs(tmp,exist_ok=True)
for f in glob.glob(tmp+'/*'): os.remove(f)
cmd=['ffmpeg','-loglevel','error','-ss',str(start)]
if end: cmd+=['-t',str(end-start)]
cmd+=['-i',src,'-vf',f'fps=1/{step},scale=320:-1',tmp+'/f%04d.jpg']
subprocess.run(cmd)
fs=sorted(glob.glob(tmp+'/*.jpg'))
ims=[Image.open(f) for f in fs]
if not ims: print('none'); sys.exit()
w,h=ims[0].size; cols=6 if w>h else 10
rows=(len(ims)+cols-1)//cols
S=Image.new('RGB',(cols*w,rows*(h+18)),'white'); d=ImageDraw.Draw(S)
for i,im in enumerate(ims):
    x=(i%cols)*w; y=(i//cols)*(h+18); S.paste(im,(x,y+18))
    t=start+i*step; d.text((x+3,y+2),f'{int(t//60)}:{int(t%60):02d}',fill='black')
S.save(out+'.jpg',quality=80); print(out, len(ims), S.size)
