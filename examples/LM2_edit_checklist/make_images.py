# Builds every image for LM2 EDIT checklist. Run from LM folder: python3 make_images.py
import subprocess, os
from PIL import Image, ImageDraw, ImageFont
W='work/hi/'; O='img/'; S=os.path.expanduser('~/.claude/skills/lead-magnet-doc/scripts/images.py')
F=lambda s,b=True: ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial%s.ttf'%(' Bold' if b else ''), s)
RED=(230,40,40); BLUE=(40,90,220); GREY=(170,170,170); DARK=(40,40,40)
def row(out,h,imgs,labels=None,cols=None):
    cmd=['python3',S,'row',O+out,str(h)]+imgs
    if labels: cmd+=['--labels','|'.join(labels)]
    if cols: cmd+=['--cols',str(cols)]
    subprocess.run(cmd,check=True)
def tag(d,xy,text,size=30):
    f=F(size); x,y=xy; tw=d.textlength(text,font=f)
    d.rounded_rectangle([x,y,x+tw+24,y+size+18],8,fill=RED); d.text((x+12,y+7),text,font=f,fill='white')
def annotate(src,out,boxes):
    im=Image.open(W+src).convert('RGB'); d=ImageDraw.Draw(im)
    for (x0,y0,x1,y1),label,lxy in boxes:
        d.rounded_rectangle([x0,y0,x1,y1],10,outline=RED,width=6); tag(d,lxy,label)
    im.save(O+out,quality=88)

# cover
row('hero.jpg',300,[W+f for f in ['a_close.jpg','a_title.jpg','a_card_debt.jpg','b_table.jpg','a_chapter1.jpg','b_sons.jpg']],cols=2)
# two angles
row('angles.jpg',300,[W+'a_wide.jpg',W+'a_close.jpg'],['Camera 1: the wide shot','Camera 2: the close-up'])
# cold open
row('cold_open.jpg',300,[W+f for f in ['a_quote1.jpg','a_quote2.jpg','a_quote3.jpg','a_title.jpg']],
    ['1. His best line, on screen','2. More of his best lines','3. Over moody B-roll','4. Then the title card'],cols=2)
# lower third
annotate('a_lower.jpg','lower_third.jpg',[((820,225,1190,305),'His name + who he is, early on',(820,330))])
# chapters
row('chapters.jpg',300,[W+'a_chapter1.jpg',W+'a_chapter3.jpg'],['Chapter 1: Stay In The Arena','Chapter 3: Young & Ambitious'])
# text cards
row('text_cards.jpg',300,[W+f for f in ['a_card_debt.jpg','a_card_humble.jpg','a_card_option.jpg','a_card_younger.jpg']],cols=2)
# charts
row('charts.jpg',300,[W+f for f in ['b_table.jpg','b_table2.jpg','b_nov2021.jpg','b_sons.jpg']],
    ['He says a number: we build the table','Then animate it to the big one','He names a date: it goes on a chart','He compares two people: two lines'],cols=2)
# first 60 seconds filmstrip
fr=['work/H_0-LAT4HjWPo/a%03d.jpg'%n for n in range(1,32,2)]
row('first_60.jpg',200,fr,['0:%02d'%((n-1)*2) if (n-1)*2<60 else '1:00' for n in range(1,32,2)],cols=4)

# diagram: interview to video
im=Image.new('RGB',(1600,620),'white'); d=ImageDraw.Draw(im)
d.text((40,30),'What we film',font=F(40),fill=DARK)
segs=[('Q',140,GREY),('Answer 1',260,BLUE),('restart',90,RED),('Q',120,GREY),('Answer 2 (the best one)',330,BLUE),('Q',120,GREY),('Answer 3',300,BLUE),('um...',90,RED)]
x=40
for t,w,c in segs:
    d.rectangle([x,100,x+w-6,200],fill=c); d.text((x+10,135),t,font=F(24),fill='white'); x+=w
d.text((40,280),'What you watch',font=F(40),fill=DARK)
x=40
for t,w,c in [('Answer 2 (the best one)',330,BLUE),('Title',110,DARK),('Answer 1',260,BLUE),('Answer 3',300,BLUE)]:
    d.rectangle([x,350,x+w-6,450],fill=c); d.text((x+10,385),t,font=F(24),fill='white'); x+=w
d.text((40,500),'Questions, restarts and ums are gone. The best answer moves to the front.',font=F(30,False),fill=DARK)
d.text((40,545),'It plays like he is talking straight to you.',font=F(30,False),fill=DARK)
im.save(O+'interview_to_video.jpg',quality=90)

# diagram: music level
im=Image.new('RGB',(1600,640),'white'); d=ImageDraw.Draw(im)
secs=[('Cold open',0,300,0.85),('Title card',300,480,1.0),('Talking',480,860,0.25),('Chapter card',860,1080,0.9),('Talking',1080,1520,0.25)]
base=430; top=120
for name,a,b,lvl in secs:
    x0=60+a; x1=60+b
    d.rectangle([x0,base+20,x1-6,base+90],fill=BLUE if 'Talking' in name or 'Cold' in name else (220,220,220))
    d.text((x0+8,base+40),name,font=F(24),fill='white' if 'Talking' in name or 'Cold' in name else DARK)
pts=[]
for name,a,b,lvl in secs:
    y=base-(base-top)*lvl; pts+= [(60+a+20,y),(60+b-20,y)]
d.line(pts,fill=RED,width=8,joint='curve')
d.text((60,30),'How loud the music is',font=F(40),fill=RED)
d.text((60,base+110),'Blue = someone talking. Music drops whenever words matter, and comes back up between them.',font=F(28,False),fill=DARK)
im.save(O+'music_levels.jpg',quality=90)
subprocess.run(['python3',S,'compress','img/chamath_proof_raw.jpg','img/chamath_proof.jpg'],check=True)
print('done')
