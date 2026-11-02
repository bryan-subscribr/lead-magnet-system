import json,sys
d=json.load(open(sys.argv[1])); a,b=float(sys.argv[2]),float(sys.argv[3])
print(' '.join(x['text'] for x in d['transcript'] if a<=int(x['startMs'])/1000<=b))
