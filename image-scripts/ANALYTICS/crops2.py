from PIL import Image
F='vid/fr/'; O='../img/'
def save(im,name,maxw=1600):
    im=im.convert('RGB')
    if im.width>maxw: im=im.resize((maxw,int(im.height*maxw/im.width)),Image.LANCZOS)
    im.save(O+name,quality=88); print(name,im.size)
def c(src,box): 
    im=Image.open(F+src+'.jpg'); W,H=im.size
    return im.crop((int(box[0]*W),int(box[1]*H),int(box[2]*W),int(box[3]*H)))
save(c('xvf_330_17',(0.45,0.08,0.97,0.75)),'tristan_traffic_sources.jpg')
save(c('xvf_330_52',(0.40,0.40,0.99,0.98)),'tristan_browse_circled.jpg')
save(c('xvf_1360_110',(0.33,0.05,0.99,0.85)),'tristan_ctr_avd.jpg')
save(c('geo_32',(0.66,0.05,0.99,0.62)),'tristan_geography.jpg')
save(c('xvf_1960_26',(0.33,0.05,0.99,0.82)),'tristan_short_3m.jpg')
save(Image.open(F+'xvf_330_22.jpg'),'bryan_tristan.jpg')
for s,n in [('qde_144','avg_ctr_steps.jpg'),('qde_164','avg_ctr_example.jpg'),('qde_302','check_24h.jpg'),('qde_306','check_7day.jpg'),('qde_314','check_30day.jpg'),('qde_214','testing_rules.jpg'),('qde_328','new_upload_strategy.jpg')]:
    save(c(s,(0,0,1,0.93)),n)
save(c('qde_94',(0,0.12,1,0.95)),'channel_ctr_screen.jpg')
save(c('pgc0_8',(0.28,0.30,0.73,0.80)),'retention_slow_decline.jpg')
save(c('pgcb_34.6',(0.15,0.05,0.85,0.95)),'retention_recap_dip.jpg')
