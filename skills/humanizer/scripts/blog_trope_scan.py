import re,sys,glob,os,json
BANNED=r"\b(delve|delves|delving|tapestry|leverage|leverages|leveraging|multifaceted|nuanced|pivotal|realm|robust|seamless|seamlessly|testament|transformative|underscores?|underscoring|utilize|utilizes|utilizing|whilst|embark|comprehensive|intricate|intricacies|commendable|meticulous|meticulously|paramount|groundbreaking|innovative|cutting-edge|synergy|holistic|paradigm|ecosystem|additionally|crucial|crucially|enduring|enhance|enhances|enhancing|fostering|foster|garner|interplay|showcase|showcases|showcasing|vibrant|valuable|invaluable|profound|profoundly|renowned|breathtaking|nestled|stunning|furthermore|moreover|consequently|hence|thus|therefore|accordingly|game-changer|plethora|myriad|remarkable|remarkably|elevate|elevates|streamline|streamlines|streamlined|empower|empowers|empowering|unlock|unlocks|unlocking|harness|harnessing|navigate|navigating|landscape|dynamic|essential|vital|significant|significantly|substantial)\b"
FILLER=[r"in order to",r"due to the fact that",r"at this point in time",r"it is important to note",r"it's worth noting",r"it is worth noting",r"needless to say",r"at the end of the day",r"in today's world",r"a testament to",r"here's the kicker",r"the bottom line",r"the key takeaway",r"here's the thing",r"the truth is",r"the reality is",r"setting the stage",r"let's dive in",r"i'll walk you through",r"here is a breakdown",r"great question",r"hope this helps",r"in conclusion",r"in summary"]
COPULA=[r"\bserves? as\b",r"\bstands? as\b",r"\bmarks a\b",r"\brepresents? a\b",r"\bboasts?\b",r"\bfeatures a\b",r"\boffers a\b",r"\breflects? broader\b",r"\bsymboli[sz]"]
NEGPAR=[r"\bnot only\b.{0,80}\bbut\b",r"\bnot just\b.{0,60}\b(it's|it is|but|,)\b",r"\bisn't just\b",r"\bis not just\b",r"\bnot merely\b",r"\bit's not about\b",r"\bless about\b.{0,60}\bmore about\b"]
HEDGE=[r"\bcould potentially\b",r"\bmight potentially\b",r"\bit could be argued\b",r"\bsome might argue\b",r"\bsome critics\b",r"\bexperts (say|argue|believe|agree)\b",r"\bindustry reports?\b",r"\bmany creators (say|believe|find)\b",r"\bit may seem\b",r"\bon the other hand\b",r"\binterestingly\b"]
ING=r",\s(highlighting|underscoring|emphasizing|emphasising|ensuring|reflecting|symbolizing|contributing to|fostering|showcasing|demonstrating|signaling|signalling)\b"
def body_of(t):
    m=re.match(r"^---\n.*?\n---\n",t,re.S); return t[m.end():] if m else t
def strip_code(b): return re.sub(r"```.*?```","",b,flags=re.S)
rows=[]
for f in sorted(glob.glob(sys.argv[1]+"/*.md")):
    t=open(f).read(); b=strip_code(body_of(t)); low=b.lower()
    words=len(re.findall(r"\w+",b))
    hits={}
    def add(k,pat,flags=re.I):
        n=len(re.findall(pat,b,flags))
        if n: hits[k]=hits.get(k,0)+n
    add("vocab",BANNED)
    for p in FILLER: add("filler",p)
    for p in COPULA: add("copula",p)
    for p in NEGPAR: add("negpar",p)
    for p in HEDGE: add("hedge",p)
    add("ing",ING)
    em=b.count("—")+b.count(" -- "); 
    if em: hits["emdash"]=em
    bold_colon=len(re.findall(r"^\s*[-*]\s+\*\*[^*]+\*\*:",b,re.M))
    if bold_colon>3: hits["boldlist"]=bold_colon
    # title-case H2s
    h2=re.findall(r"^## (.+)$",b,re.M)
    tc=sum(1 for h in h2 if len(h.split())>=4 and all(w[0].isupper() for w in h.split() if w.isalpha() and len(w)>3))
    if tc: hits["titlecase_h2"]=tc
    # same-starter paragraphs
    same=0
    for para in re.split(r"\n\s*\n",b):
        if para.startswith(("#","-","*","|","**Q","**A","!")): continue
        sents=[s.strip() for s in re.split(r"(?<=[.!?])\s+",para) if s.strip()]
        starts=[s.split()[0].lower().strip('"*') for s in sents if s.split()]
        for w in set(starts):
            if starts.count(w)>=3: same+=1
    if same: hits["same_start"]=same
    # rule of three: "X, Y, and Z" noun triples in one sentence, crude
    tri=len(re.findall(r"\b\w+, \w+,? and \w+\b",b))
    hits["_triples"]=tri
    pen=hits.get("vocab",0)*5+hits.get("filler",0)*5+hits.get("copula",0)*5+hits.get("negpar",0)*5+hits.get("hedge",0)*8+hits.get("ing",0)*8+min(hits.get("emdash",0),10)*5+(5 if hits.get("boldlist") else 0)+(3 if hits.get("titlecase_h2") else 0)+hits.get("same_start",0)*3
    score=max(0,100-pen)
    rows.append((score,os.path.basename(f),words,hits))
rows.sort()
for s,f,w,h in rows:
    print(f"{s:3d} {w:5d} {f:50s} {json.dumps(h)}")
print("mean",sum(r[0] for r in rows)/len(rows),"below90",sum(1 for r in rows if r[0]<90))
