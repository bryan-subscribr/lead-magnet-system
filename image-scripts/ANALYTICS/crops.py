from PIL import Image, ImageOps
import numpy as np, os
F='vid/fr/'; O='../img/'
def save(im,name,maxw=1600):
    im=im.convert('RGB')
    if im.width>maxw: im=im.resize((maxw,int(im.height*maxw/im.width)),Image.LANCZOS)
    im.save(O+name,quality=88); print(name,im.size)
def autocrop(path,thr=60,pad=20):
    im=Image.open(path).convert('RGB'); a=np.asarray(im.convert('L'))
    ys,xs=np.where(a>thr)
    # ignore tiny noise: use percentiles
    x0,x1=np.percentile(xs,1),np.percentile(xs,99); y0,y1=np.percentile(ys,1),np.percentile(ys,99)
    return im.crop((max(0,int(x0)-pad),max(0,int(y0)-pad),min(im.width,int(x1)+pad),min(im.height,int(y1)+pad)))
print(Image.open(F+'yyd_62.jpg').size, Image.open(F+'xvf_330_17.jpg').size, Image.open(F+'qde_144.jpg').size, Image.open(F+'pgc0_8.jpg').size)
for src,name in [('yyd_62','studio_impressions_ctr.jpg'),('yyd_56','studio_traffic_sources.jpg'),('yyd_88','studio_retention_graph.jpg'),('yyd_104','studio_watch_time.jpg'),('yyd_116','studio_views_since_published.jpg'),('yyd_146','test_compare_report.jpg')]:
    save(autocrop(F+src+'.jpg'),name)
save(Image.open(F+'yyd_50.jpg'),'bryan_study_analytics.jpg')
