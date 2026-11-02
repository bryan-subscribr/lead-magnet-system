import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
plt.rcParams.update({'font.family':'Arial','font.size':15,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#888','axes.labelcolor':'#333','xtick.color':'#333','ytick.color':'#333'})
O='../img/'; BLUE='#2b6cb0'; GREY='#b8c2cc'; RED='#d64545'; GREEN='#2f9e5b'
def fin(fig,name): fig.tight_layout(); fig.savefig(O+name,dpi=130,facecolor='white'); plt.close(fig); print(name)

# 1 CTR falls as strangers see it (Bryan's Subscribr-channel example, weekly call 6 Nov 2025)
fig,ax=plt.subplots(figsize=(10,5.2))
b=ax.bar(['Day 1\n(mostly people who know you)','Day 3\n(mostly strangers)'],[4.6,1.5],color=[BLUE,GREY],width=0.5)
for r,v in zip(b,[4.6,1.5]): ax.text(r.get_x()+r.get_width()/2,v+0.1,f'{v}%',ha='center',fontsize=20,fontweight='bold')
ax.set_ylabel('Click-through rate'); ax.set_ylim(0,5.6); ax.set_yticks([])
ax.set_title('Same video, same thumbnail. The CTR dropped because the audience changed.',fontsize=14,loc='left',color='#333')
fin(fig,'chart_ctr_drop.jpg')

# 2 CTR averages by age of video (example numbers from Bryan's Claude course)
fig,ax=plt.subplots(figsize=(10,5.2))
v=[14,9,7]; b=ax.bar(['24 hours','7 days','30 days'],v,color=[BLUE,'#5a8fd0','#8fb3e0'],width=0.55)
for r,x in zip(b,v): ax.text(r.get_x()+r.get_width()/2,x+0.3,f'{x}%',ha='center',fontsize=20,fontweight='bold')
ax.set_ylim(0,17); ax.set_yticks([]); ax.set_ylabel('Average CTR of your last 10 videos')
ax.set_title('Example: one channel, three different "normal" CTRs',fontsize=14,loc='left',color='#333')
fin(fig,'chart_ctr_benchmarks.jpg')

# 3 Bryan's last 30 long-form videos (Nexlev 2026-10-29)
views=[801,1300,988,60000,835,23000,2900,1400,1200,1100,655,16000,851,968,1200,1500,1100,6400,1300,3100,1700,1700,1700,3700,6800,1500,1300,2200,1800,3100][::-1]
med=float(np.median(views))
fig,ax=plt.subplots(figsize=(11,5.4))
cols=[BLUE if x>=3*med else GREY for x in views]
ax.bar(range(len(views)),views,color=cols)
ax.axhline(med,color=RED,lw=2,ls='--'); ax.text(29.4,med*0.62,f'Middle video: about {int(round(med,-2)):,} views',color=RED,fontsize=13,ha='right',bbox=dict(fc='white',ec='none',alpha=0.9))
ax.axhline(3*med,color=GREEN,lw=1.5,ls=':'); ax.text(29.4,3*med*1.12,f'3x that: {int(round(3*med,-2)):,}',color=GREEN,fontsize=13,ha='right',bbox=dict(fc='white',ec='none',alpha=0.9))
ax.set_yscale('log'); ax.set_ylabel('Views (log scale)'); ax.set_xticks([])
ax.set_xlabel('My last 30 long-form videos, oldest to newest')
ax.set_yticks([1000,3000,10000,30000,60000]); ax.set_yticklabels(['1,000','3,000','10,000','30,000','60,000'])
ax.set_title('Blue bars beat 3x my middle video. Those are the ones I study.',fontsize=14,loc='left',color='#333')
fin(fig,'chart_my_last_30.jpg')

# 4 GPT-5 expectation
fig,ax=plt.subplots(figsize=(10,5.2))
lab=['A normal\nscriptwriting video','What I expected\nfrom GPT-5','What it had\nafter 4 weeks','Where it is\ntoday']
v=[2000,5000,1800,3100]; c=[GREY,GREEN,RED,'#8fb3e0']
b=ax.bar(lab,v,color=c,width=0.55)
for r,x in zip(b,v): ax.text(r.get_x()+r.get_width()/2,x+90,f'{x:,}',ha='center',fontsize=18,fontweight='bold')
ax.set_ylim(0,5900); ax.set_yticks([]); ax.tick_params(axis='x',labelsize=12)
ax.set_title('Judge views against what you expected from that idea',fontsize=14,loc='left',color='#333')
fin(fig,'chart_gpt5_expectation.jpg')

# 5 Retention shapes (drawings)
x=np.linspace(0,100,300)
shapes={'Healthy: small drop, then flat':np.where(x<5,100-6*x,70-0.25*(x-5)),
'Weak hook: half gone in 30 seconds':np.where(x<5,100-11*x,45-0.2*(x-5)),
'Staircase: people leave after each point':100-30*(1-np.exp(-x/3))-np.floor(x/20)*8-0.05*x,
'Cliff near the end: a recap or a goodbye':np.where(x<85,np.where(x<5,100-6*x,70-0.25*(x-5)),np.where(x<5,0,70-0.25*80)-18-0.3*(x-85)),
'Spike: people rewatched this part':np.where(x<5,100-6*x,70-0.25*(x-5))+14*np.exp(-((x-55)/2.5)**2),
'Slow slide all the way: the middle drags':np.where(x<5,100-6*x,70-0.6*(x-5))}
fig,axs=plt.subplots(2,3,figsize=(13,7))
for ax,(t,y) in zip(axs.flat,shapes.items()):
    ax.plot(x,np.clip(y,0,110),color=BLUE,lw=2.5); ax.set_ylim(0,110); ax.set_xticks([]); ax.set_yticks([0,50,100]); ax.set_yticklabels(['0%','50%','100%'],fontsize=11)
    ax.set_title(t,fontsize=12.5,loc='left')
fig.suptitle('Six retention graph shapes (drawings, not real data)',fontsize=15,x=0.02,ha='left',color='#333')
fin(fig,'chart_retention_shapes.jpg')

# 6 Watch time math (Bryan LA_gt6OrSl8)
fig,ax=plt.subplots(figsize=(10,5))
lab=['10-minute video,\nwatched for 5 minutes\n(50% viewed)','3-minute video,\nwatched for 2 minutes\n(67% viewed)']
b=ax.barh(lab,[5,2],color=[BLUE,GREY],height=0.5)
for r,v in zip(b,[5,2]): ax.text(v+0.1,r.get_y()+r.get_height()/2,f'{v} minutes per viewer',va='center',fontsize=16,fontweight='bold')
ax.set_xlim(0,8.5); ax.set_xticks([]); ax.invert_yaxis()
ax.set_title('The lower percentage still gives YouTube more minutes',fontsize=14,loc='left',color='#333')
fin(fig,'chart_watch_time_math.jpg')

# 7 Diagnosis quadrant
fig,ax=plt.subplots(figsize=(10,8))
ax.axhline(0.5,color='#999'); ax.axvline(0.5,color='#999')
txt={(0.75,0.75):('Both good','Leave it alone.\nIf views still stall,\nthe topic is too small\nor needs time.',GREEN),
(0.25,0.75):('Low CTR, strong first 30s','People who click like it.\nFix the thumbnail first,\nthen the title.',BLUE),
(0.75,0.25):('High CTR, weak first 30s','The packaging promised\nsomething the opening\ndidn\'t deliver. Fix the hook.',RED),
(0.25,0.25):('Both low','Usually the idea.\nDon\'t polish it.\nMove on to a better idea.','#7a5ea8')}
for (cx,cy),(h,b,c) in txt.items():
    ax.text(cx,cy+0.12,h,ha='center',fontsize=18,fontweight='bold',color=c)
    ax.text(cx,cy-0.06,b,ha='center',va='center',fontsize=16,color='#333')
ax.set_xlim(0,1); ax.set_ylim(0,1); ax.set_xticks([0.1,0.9]); ax.set_xticklabels(['Below your average','Above your average'])
ax.set_yticks([0.1,0.9]); ax.set_yticklabels(['Below\nyour average','Above\nyour average'])
ax.set_xlabel('Click-through rate (vs your own 7-day average)',fontsize=14); ax.set_ylabel('Still watching at 30 seconds',fontsize=14)
fin(fig,'chart_diagnosis.jpg')

# 8 Link clicks vs money (client tracking, approved LM6 numbers)
fig,axs=plt.subplots(1,2,figsize=(12,5.4))
ax=axs[0]; b=ax.bar(['Under 0.25%\nclicked a link','0.5% to 1%\nclicked a link'],[33,1395],color=[GREY,BLUE],width=0.55)
for r,v in zip(b,[33,1395]): ax.text(r.get_x()+r.get_width()/2,v+30,f'${v:,}',ha='center',fontsize=18,fontweight='bold')
ax.set_yticks([]); ax.set_ylim(0,1650); ax.set_title('Money made per video',fontsize=14,loc='left')
ax=axs[1]; b=ax.bar(['The 100 most\nviewed videos'],[11],color=GREY,width=0.4)
ax.text(0,12,'11% of the money',ha='center',fontsize=16,fontweight='bold'); ax.set_ylim(0,100); ax.set_yticks([0,50,100]); ax.set_yticklabels(['0%','50%','100%'])
ax.set_title('Share of all tracked sales',fontsize=14,loc='left')
fig.suptitle('From the tracking we run for clients: 207 channels, 26,621 videos',fontsize=13,x=0.02,ha='left',color='#555')
fin(fig,'chart_link_clicks_money.jpg')
