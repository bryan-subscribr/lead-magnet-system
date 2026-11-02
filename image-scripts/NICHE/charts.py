import csv, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
plt.rcParams.update({'font.family':'Helvetica','font.size':13,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','axes.facecolor':'white'})
W='/Users/bryanng/lead_magnets/NICHE/'
rows=list(csv.DictReader(open(W+'work/niche_rpm.csv')))
for r in rows:
    for k in ['rpm','rpm_min','rpm_max','length_min','views','channel_subs','est_earnings']: r[k]=float(r[k])
BUY={'business','finance','real estate','legal','health'}
C_B='#1f5fbf'; C_E='#b8bec8'; C_HI='#e8590c'
src='Source: Nexlev get_video_rpm, one real video per niche, pulled 29 Oct 2026'

# 1 full ranking
rs=sorted(rows,key=lambda r:r['rpm'])
fig,ax=plt.subplots(figsize=(11,15))
y=range(len(rs))
cols=[C_B if r['group'] in BUY else C_E for r in rs]
ax.barh(y,[r['rpm'] for r in rs],color=cols,height=0.7)
ax.errorbar([r['rpm'] for r in rs],y,xerr=[[r['rpm']-r['rpm_min'] for r in rs],[r['rpm_max']-r['rpm'] for r in rs]],fmt='none',ecolor='#555',elinewidth=1,capsize=2)
ax.set_yticks(list(y)); ax.set_yticklabels([r['niche'] for r in rs],fontsize=12)
for i,r in enumerate(rs): ax.text(r['rpm_max']+0.4,i,f"${r['rpm']:.2f}",va='center',fontsize=11)
ax.set_xlabel('Estimated RPM (dollars per 1,000 views). Line = low to high estimate')
ax.legend(handles=[Patch(color=C_B,label='Niches where service businesses sell'),Patch(color=C_E,label='Entertainment and general')],loc='lower right',frameon=False)
ax.set_xlim(0,40)
fig.text(0.01,0.005,src,fontsize=10,color='#666')
plt.tight_layout(rect=(0,0.015,1,1)); plt.savefig(W+'img/chart_rpm_all_niches.png',dpi=130); plt.close()

# 2 length vs rpm
fig,ax=plt.subplots(figsize=(11,7))
for r in rows:
    ax.scatter(r['length_min'],r['rpm'],s=70,color=C_B if r['group'] in BUY else C_E,edgecolor='#333',linewidth=0.5,zorder=3)
lab={'HubSpot':'T9tnDlEvlQg','True crime 3h':'Hztf3WSRRck','Lawyer clip 6 min':'aHk7i-B6N-g','Doctor clip 5 min':'7JDgHvgWsZo','Salesforce 11h course':'qN95TmywOko','Kids songs':'4alYTXo3Iro','History doc 66 min':'e7-Y7Hs7Dqw'}
for name,vid in lab.items():
    r=[x for x in rows if x['video_id']==vid][0]
    ax.annotate(name,(r['length_min'],r['rpm']),xytext=(6,6),textcoords='offset points',fontsize=11)
ax.set_xscale('log'); ax.set_xticks([2,5,10,20,60,180,600]); ax.set_xticklabels(['2','5','10','20','60','180','600'])
ax.set_xlabel('Video length (minutes, log scale)'); ax.set_ylabel('Estimated RPM ($)')
ax.axvline(8,color='#999',ls='--',lw=1); ax.text(8.3,27,'8 minutes:\nmid-roll ads unlock',fontsize=11,color='#555')
fig.text(0.01,0.01,src,fontsize=10,color='#666')
plt.tight_layout(rect=(0,0.03,1,1)); plt.savefig(W+'img/chart_length_vs_rpm.png',dpi=130); plt.close()

# 3 creator reported ranges
data=[('Finance (Grow With Kaz)',15,50),('Business, finance, real estate CPM (Think Media)',20,45),('Finance (Shane Hummus)',20,40),('Real estate investing (Make Money Matt)',20,30),('General education (Shane Hummus)',8,10),("Bryan's target: tier 1, older audience",8,8),('Long-form, all niches (Business Insider via Think Media)',1.61,29.3),('Shorts (Think Media)',0.04,0.06)]
fig,ax=plt.subplots(figsize=(11,6.5))
for i,(n,a,b) in enumerate(reversed(data)):
    ax.plot([a,b],[i,i],color=C_B,lw=10,solid_capstyle='round')
    if a==b: ax.scatter([a],[i],s=120,color=C_B,zorder=3)
    ax.text(b+1,i,(f"\\${a:g} to \\${b:.2f}" if b<1 or b==29.3 else f"\\${a:g} to \\${b:g}") if a!=b else f"\\${a:g}",va='center',fontsize=11)
ax.axvline(44,color=C_HI,lw=2,ls='--'); ax.text(44.5,len(data)-0.6,'$44',color=C_HI,fontsize=13,fontweight='bold')
ax.set_yticks(range(len(data))); ax.set_yticklabels([d[0] for d in reversed(data)],fontsize=11)
ax.set_xlim(0,60); ax.set_xlabel('Dollars per 1,000 views (as the creators reported them)')
fig.text(0.01,0.01,'Source: Subscribr Strategy Search, creator videos listed in the guide',fontsize=10,color='#666')
plt.tight_layout(rect=(0,0.03,1,1)); plt.savefig(W+'img/chart_creator_reported_rpm.png',dpi=130); plt.close()

# 4 country CPM
c=[('Australia',40),('United States',36),('Canada',32),('New Zealand',30),('Switzerland',25),('United Kingdom',23),('Norway',22),('Germany',20),('Ireland',20),('Netherlands',19)]
fig,ax=plt.subplots(figsize=(10,6))
ax.barh(range(len(c))[::-1],[x[1] for x in c],color=C_B)
ax.set_yticks(range(len(c))[::-1]); ax.set_yticklabels([x[0] for x in c])
for i,x in enumerate(c): ax.text(x[1]+0.5,len(c)-1-i,f"${x[1]}",va='center')
ax.set_xlabel('Approximate CPM (what advertisers pay per 1,000 ad views)')
fig.text(0.01,0.01,'Source: Dan the creator (ub8E-f7W4JU), top YouTube CPM countries 2024, via Subscribr Strategy Search',fontsize=10,color='#666')
plt.tight_layout(rect=(0,0.03,1,1)); plt.savefig(W+'img/chart_cpm_by_country.png',dpi=130); plt.close()

# 5 shorts vs long
fig,ax=plt.subplots(figsize=(10,5))
ax.bar(['Shorts','Long-form'],[0.06,7.36],color=[C_E,C_B],width=0.5)
ax.text(0,0.3,'$0.06',ha='center',fontsize=14); ax.text(1,7.6,'$7.36',ha='center',fontsize=14)
ax.set_ylabel('RPM ($ per 1,000 views)'); ax.set_ylim(0,9)
fig.text(0.01,0.01,'Source: Think Media Podcast (oKYeGfZnznk). An 11.2 million view Short earned $536.74',fontsize=10,color='#666')
plt.tight_layout(rect=(0,0.04,1,1)); plt.savefig(W+'img/chart_shorts_vs_long.png',dpi=130); plt.close()

# 6 ad revenue vs one client
fig,ax=plt.subplots(figsize=(11,5.5))
labels=['AdSense on 100 views\nat $26.53 RPM','AdSense on 51,818 views\n(HubSpot tutorial)','One recruiting placement\n(Shane Hummus client)']
vals=[2.65,1374.73,50000]
ax.bar(labels,vals,color=[C_E,C_E,C_B],width=0.55)
for i,v in enumerate(vals): ax.text(i,v+800,f"${v:,.2f}" if v<100 else f"${v:,.0f}",ha='center',fontsize=14)
ax.set_ylabel('Dollars'); ax.set_ylim(0,56000)
fig.text(0.01,0.01,'Sources: Nexlev get_video_rpm (T9tnDlEvlQg); Shane Hummus (PgzuN7D05LM): ~100 views per video, up to $50,000 per placement',fontsize=10,color='#666')
plt.tight_layout(rect=(0,0.04,1,1)); plt.savefig(W+'img/chart_ads_vs_client.png',dpi=130); plt.close()

# 7 keyword check
k=[('gohighlevel tutorial',124609,63),('go high level tutorial',110294,56),('hubspot crm tutorial for beginners',71438,44),('hubspot tutorial',32641,22),('hubspot crm tutorial',10794,34),('gohighlevel funnel tutorial',8989,15),('gohighlevel funnels',4699,16)]
fig,ax=plt.subplots(figsize=(11,6))
for n,v,cp in k:
    col=C_HI if cp<=25 else C_B
    ax.scatter(cp,v,s=160,color=col,edgecolor='#333',zorder=3)
    ax.annotate(n,(cp,v),xytext=(8,-14) if n.startswith('go high') else (8,4),textcoords='offset points',fontsize=11)
ax.set_yscale('log'); ax.set_xlim(0,80)
ax.set_xlabel('vidIQ competition score (lower is easier)'); ax.set_ylabel('Estimated monthly searches (log)')
ax.axvspan(0,25,color='#fff1e6',zorder=0); ax.text(1.5,150000,'Easy zone',color=C_HI,fontsize=12)
fig.text(0.01,0.01,'Source: vidIQ keyword research, 29 Oct 2026',fontsize=10,color='#666')
plt.tight_layout(rect=(0,0.03,1,1)); plt.savefig(W+'img/chart_check1_keywords.png',dpi=130); plt.close()

# 8 saturation check
s=[('Charlie Chang',580668),('Kuys RJ (Tagalog, 4h46m)',59533),('Funnel Scene',53139),('Daniel | Tech & Data',23656),('GHL Wizard',11393),('Funnel Scene #2',6152),('Danyyil Giba',3571),('The Stuff',3130),('Juan GHL',2638),('Dom Bavaro',2525),('GHL Mastery',2491),('Tutorial Stack',2150),('Kevin Hogan',1431),('GHLGrowthGarage',1194),('Tutorial Stack #2',1110),('Gijs Marketing',1013),('Tutorial Stack #3',965),('Ali Hassan',503),('Andrew George',420),('High Level Profit Systems',349)]
fig,ax=plt.subplots(figsize=(11,8))
ax.barh(range(len(s))[::-1],[x[1] for x in s],color=[C_HI if x[1]>=100000 else C_B for x in s])
ax.set_yticks(range(len(s))[::-1]); ax.set_yticklabels([x[0] for x in s],fontsize=11)
ax.set_xscale('log'); ax.set_xlabel('Views (log scale)')
for i,x in enumerate(s): ax.text(x[1]*1.08,len(s)-1-i,f"{x[1]:,}",va='center',fontsize=10)
ax.set_xlim(200,2000000)
fig.text(0.01,0.01,'Top 20 YouTube results for "gohighlevel funnel tutorial", Nexlev youtube_search, 29 Oct 2026',fontsize=10,color='#666')
plt.tight_layout(rect=(0,0.03,1,1)); plt.savefig(W+'img/chart_check2_saturation.png',dpi=130); plt.close()

# 9 outliers small channels
o=[('SliceofLifeMD (Medicare)',12200,346000,1804),('CalHealth (Medicare)',6900,205500,695),('Landmark Legal (police rights)',2500,81800,527),('John Farrell (real estate)',1100,66400,265),('Jamie Hering (home buying)',43600,107500,251),('Law Office of John Guidry',29500,44700,155),('BizMoney Explained (finance)',21500,96300,149),('Drew Brockbank (HubSpot)',16300,51800,52),('Mariah Peace (QuickBooks)',6400,29500,25),('Jack McColl (business credit)',7000,20400,23)]
fig,ax=plt.subplots(figsize=(11,7))
ax.barh(range(len(o))[::-1],[x[3] for x in o],color=C_B)
ax.set_yticks(range(len(o))[::-1]); ax.set_yticklabels([f"{x[0]}\n{x[1]:,} subs, {x[2]:,} views" for x in o],fontsize=10)
for i,x in enumerate(o): ax.text(x[3]+20,len(o)-1-i,f"{x[3]:,}x",va='center',fontsize=11)
ax.set_xlabel('Times above that channel\'s normal views (vidIQ breakout score)')
ax.set_xlim(0,2100)
fig.text(0.01,0.01,'Source: vidIQ outliers, channels under 50,000 subscribers, last 6 months, pulled 29 Oct 2026',fontsize=10,color='#666')
plt.tight_layout(rect=(0,0.03,1,1)); plt.savefig(W+'img/chart_check3_outliers.png',dpi=130); plt.close()

# 10 seasonality
fig,ax=plt.subplots(figsize=(10,5))
ax.bar(['Lowest day\n(15 October)','Highest day\n(28 November)'],[9.41,71.48],color=[C_E,C_B],width=0.5)
ax.text(0,11,'$9.41',ha='center',fontsize=14); ax.text(1,73.5,'$71.48',ha='center',fontsize=14)
ax.set_ylabel('AdSense earned that day ($)'); ax.set_ylim(0,85)
fig.text(0.01,0.01,"Source: Aprilynne Alter (sFwdctKMUaE), first year on YouTube, via Subscribr Strategy Search",fontsize=10,color='#666')
plt.tight_layout(rect=(0,0.04,1,1)); plt.savefig(W+'img/chart_q4_days.png',dpi=130); plt.close()
print('done')
