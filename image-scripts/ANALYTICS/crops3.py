from PIL import Image
F='vid/fr/'; O='../img/'
def save(im,name,maxw=1600):
    im=im.convert('RGB')
    if im.width>maxw: im=im.resize((maxw,int(im.height*maxw/im.width)),Image.LANCZOS)
    im.save(O+name,quality=88); print(name,im.size)
def c(src,box):
    im=Image.open(F+src+'.jpg'); W,H=im.size
    return im.crop((int(box[0]*W),int(box[1]*H),int(box[2]*W),int(box[3]*H)))
save(c('pgc0_8',(0.13,0.10,0.87,0.88)),'retention_slow_decline.jpg')
save(c('qde_294',(0,0,1,0.93)),'check_24h.jpg')
im=Image.open(F+'yyd_62.jpg'); save(im.crop((200,250,1760,830)),'studio_impressions_ctr.jpg')
save(c('geo_32',(0.55,0.15,0.88,0.60)),'tristan_geography.jpg')
