import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Arial'
out='/Users/bryanng/lead_magnets/TIKTOK/img/'
BLUE='#2a6fdb'; GREY='#9aa3ad'; ORANGE='#e8742a'
def style(ax):
    for s in ['top','right']: ax.spines[s].set_visible(False)
    ax.spines['left'].set_color('#cccccc'); ax.spines['bottom'].set_color('#cccccc')
    ax.tick_params(colors='#333333', labelsize=13)

# 1. 1M views earnings (vidIQ calculator)
fig,ax=plt.subplots(figsize=(8,5),dpi=200)
vals=[160,8000]; labs=['1,000,000 Shorts views','1,000,000 long-form views']
b=ax.bar(labs,vals,color=[GREY,BLUE],width=0.55)
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v+150,f'${v:,}',ha='center',fontsize=20,fontweight='bold',color='#222')
ax.set_ylim(0,9500); ax.set_yticks([]); ax.spines['left'].set_visible(False)
style(ax); ax.spines['left'].set_visible(False)
ax.set_title('What 1 million views pays (business niche, US audience)',fontsize=15,loc='left',color='#222',pad=14)
fig.text(0.01,0.01,'Source: vidIQ earnings calculator, mid estimate, run 29 Oct 2026. Range: Shorts \$96 to \$256, long \$4,800 to \$12,800.',fontsize=9,color='#666')
plt.tight_layout(rect=(0,0.04,1,1)); plt.savefig(out+'chart_1m_views.jpg'); plt.close()

# 2. Creator reported RPM: long vs shorts
rows=[('Think Media channel',7.36,0.06),('Aprilynne Alter (example)',2.50,0.06),('Grow With Kaz (cooking)',11.25,0.03),('Oscar Owen',None,0.03)]
fig,ax=plt.subplots(figsize=(8,5.2),dpi=200)
names=['Think Media','Aprilynne Alter\n(her example)','Grow With Kaz\n(cooking)']
longs=[7.36,2.50,11.25]; shorts=[0.06,0.06,0.03]
import numpy as np
x=np.arange(3); w=0.38
b1=ax.bar(x-w/2,longs,w,color=BLUE,label='Long-form RPM')
b2=ax.bar(x+w/2,shorts,w,color=GREY,label='Shorts RPM')
for r,v in zip(b1,longs): ax.text(r.get_x()+r.get_width()/2,v+0.2,f'${v:.2f}',ha='center',fontsize=15,fontweight='bold')
for r,v in zip(b2,shorts): ax.text(r.get_x()+r.get_width()/2,v+0.2,f'${v:.2f}',ha='center',fontsize=15,fontweight='bold',color='#555')
ax.set_xticks(x); ax.set_xticklabels(names,fontsize=13); ax.set_yticks([])
style(ax); ax.spines['left'].set_visible(False)
ax.legend(frameon=False,fontsize=12,loc='upper left')
ax.set_title('What creators say they earn per 1,000 views',fontsize=15,loc='left',pad=14)
fig.text(0.01,0.01,'Sources: Think Media (oKYeGfZnznk), Aprilynne Alter (Izmx3UVjNIc), Grow With Kaz (-KtSK0w2tvs). RPM = what you keep per 1,000 views.',fontsize=8.5,color='#666')
plt.tight_layout(rect=(0,0.04,1,1)); plt.savefig(out+'chart_creator_rpm.jpg'); plt.close()

# 3. Nav pair: views vs estimated earnings
fig,axs=plt.subplots(1,2,figsize=(9,4.8),dpi=200)
labs=['59-second Short','13:57 long video']
v=[2918783,559109]; e=[2918783*0.16/1000,559109*8/1000]
b=axs[0].bar(labs,v,color=[GREY,BLUE],width=0.55)
for r,val in zip(b,v): axs[0].text(r.get_x()+r.get_width()/2,val+60000,f'{val:,}',ha='center',fontsize=13,fontweight='bold')
axs[0].set_title('Views',fontsize=15,loc='left')
b=axs[1].bar(labs,e,color=[GREY,BLUE],width=0.55)
for r,val in zip(b,e): axs[1].text(r.get_x()+r.get_width()/2,val+90,f'${val:,.0f}',ha='center',fontsize=13,fontweight='bold')
axs[1].set_title('Estimated ad money',fontsize=15,loc='left')
for a in axs:
    style(a); a.set_yticks([]); a.spines['left'].set_visible(False); a.tick_params(labelsize=11)
axs[0].set_ylim(0,3400000); axs[1].set_ylim(0,5200)
fig.suptitle('Simon Squibb, same story (Nav and Pink Broccoli)',fontsize=15,x=0.02,ha='left')
fig.text(0.01,0.01,'Views: vidIQ, 29 Oct 2026. Money: views x vidIQ mid rates (\$0.16 Shorts, \$8 long per 1,000). Nexlev puts the long video at \$6,944.',fontsize=8,color='#666')
plt.tight_layout(rect=(0,0.05,1,0.93)); plt.savefig(out+'chart_nav_pair.jpg'); plt.close()

# 4. Simon channel views split
fig,ax=plt.subplots(figsize=(8,3.6),dpi=200)
s=435649216; l=76466619
ax.barh([0],[s],color=GREY); ax.barh([0],[l],left=[s],color=BLUE)
ax.text(s/2,0,f'Shorts: {s:,} views (85%)',ha='center',va='center',fontsize=12,color='white',fontweight='bold')
ax.text(s+l/2,0.55,f'Long: {l:,} (15%)',ha='center',fontsize=11,color=BLUE,fontweight='bold')
ax.set_yticks([]); ax.set_xticks([]); [ax.spines[k].set_visible(False) for k in ax.spines]
ax.set_ylim(-0.6,1)
ax.set_title("Simon Squibb's YouTube channel, all-time views",fontsize=14,loc='left')
fig.text(0.01,0.02,'Source: Nexlev short vs long views, 29 Oct 2026.',fontsize=9,color='#666')
plt.tight_layout(rect=(0,0.06,1,1)); plt.savefig(out+'chart_simon_split.jpg'); plt.close()
print('ok')
