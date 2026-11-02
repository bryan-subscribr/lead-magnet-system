import csv, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'Helvetica','font.size':12})
W='/Users/bryanng/lead_magnets/NICHE/'
rows=list(csv.DictReader(open(W+'work/niche_rpm.csv')))
rows.sort(key=lambda r:-float(r['rpm']))
def k(n):
    n=int(float(n)); return f"{n:,}"
cell=[[r['niche'],r['channel'].split(' |')[0].replace('Moving to Chicago Suburbs with ','').replace(' YouTube Blog YouTube News','').replace(' Estates Group','').replace(', P.A.','').replace(' P.A.',''),k(r['channel_subs']),f"{float(r['length_min']):.0f} min",'\\$'+f"{float(r['rpm']):.2f}",'\\$'+f"{float(r['rpm'])*100:,.0f}"] for r in rows]
hdr=['Niche','Example channel','Subscribers','Length','1,000 views pays','100,000 views pays']
fig=plt.figure(figsize=(13,0.36*len(cell)+0.8)); ax=fig.add_axes([0,0.04,1,0.96]); ax.axis('off')
t=ax.table(cellText=cell,colLabels=hdr,bbox=[0,0,1,1],cellLoc='left',colWidths=[0.27,0.27,0.11,0.09,0.13,0.14])
t.auto_set_font_size(False); t.set_fontsize(11)
BUY={'business','finance','real estate','legal','health'}
for (i,j),c in t.get_celld().items():
    c.set_edgecolor('#BFBFBF')
    if i==0: c.set_facecolor('#F3F3F3'); c.set_text_props(weight='bold')
    elif rows[i-1]['group'] in BUY: c.set_facecolor('#eef3fc')
fig.text(0.01,0.005,'Blue rows: niches where service businesses sell. Source: Nexlev get_video_rpm, one real video per niche, 29 Oct 2026. Estimates, not payouts.',fontsize=10,color='#555')
plt.savefig(W+'img/table_rpm_map.png',dpi=130,bbox_inches='tight',pad_inches=0.1); print('ok')
