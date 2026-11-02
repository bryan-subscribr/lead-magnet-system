#!/usr/bin/env python3
"""Structural guard: run after editing a post. Usage: check.py <slug>.md [...]"""
import re,subprocess,sys,os
ROOT=os.path.expanduser(os.environ.get("BLOG_REPO","~/Sites/subscribr-aeo-oct"))  # set BLOG_REPO to the repo holding resources/blog
fail=0
def fm_body(t):
    m=re.match(r"^(---\n.*?\n---\n)",t,re.S); return (m.group(1),t[m.end():]) if m else ("",t)
for name in sys.argv[1:]:
    rel=f"resources/blog/{os.path.basename(name)}"
    new=open(f"{ROOT}/{rel}").read()
    old=subprocess.run(["git","-C",ROOT,"show",f"HEAD:{rel}"],capture_output=True,text=True).stdout
    ofm,ob=fm_body(old); nfm,nb=fm_body(new)
    probs=[]
    if ofm!=nfm: probs.append("frontmatter changed")
    oh=re.findall(r"^#{1,6} .+$",ob,re.M); nh=re.findall(r"^#{1,6} .+$",nb,re.M)
    if oh!=nh: probs.append(f"headings changed: {set(oh)^set(nh)}")
    for a in re.findall(r'after_heading:\s*"?([^"\n]+)"?',nfm):
        if not re.search(r"^## "+re.escape(a.strip())+r"\s*$",nb,re.M): probs.append(f"image anchor missing: {a}")
    oq=len(re.findall(r"^\*\*Q: .+\*\*$",ob,re.M)); nq=len(re.findall(r"^\*\*Q: .+\*\*$",nb,re.M))
    oa=len(re.findall(r"^\*\*A:\*\* ",ob,re.M)); na=len(re.findall(r"^\*\*A:\*\* ",nb,re.M))
    if (oq,oa)!=(nq,na): probs.append(f"FAQ format count changed Q {oq}->{nq} A {oa}->{na}")
    ol=set(re.findall(r"\]\((https?://[^)\s]+)",ob)); nl=set(re.findall(r"\]\((https?://[^)\s]+)",nb))
    if ol-nl: probs.append(f"links dropped: {sorted(ol-nl)[:5]}")
    onum=re.findall(r"\$?\d[\d,.]*%?",ob); nnum=re.findall(r"\$?\d[\d,.]*%?",nb)
    lost=[n for n in set(onum) if onum.count(n)>nnum.count(n)]
    if lost: probs.append(f"numbers reduced (verify intentional): {sorted(lost)[:12]}")
    if "—" in nb: probs.append(f"em dashes: {nb.count('—')}")
    ot=ob.count("\n|"); nt=nb.count("\n|")
    if ot!=nt: probs.append(f"table rows changed {ot}->{nt}")
    ow=len(re.findall(r"\w+",ob)); nw=len(re.findall(r"\w+",nb))
    status="OK" if not probs else "PROBLEMS"
    if probs: fail=1
    print(f"{status} {os.path.basename(name)} words {ow}->{nw}")
    for p in probs: print("   -",p)
sys.exit(fail)
