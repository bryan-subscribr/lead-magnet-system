import json,sys,re
d=json.load(open(sys.argv[1])); pat=sys.argv[2]
t=d['transcript']; last=-99
for i,x in enumerate(t):
    if re.search(pat,x['text'],re.I) and i-last>3:
        last=i; print(x['startTime'], ' '.join(y['text'] for y in t[i:i+5]))
