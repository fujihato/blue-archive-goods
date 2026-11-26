import json,re,sys,urllib.request
from pathlib import Path
URL='https://schaledb.com/data/jp/students.json'
raw=json.loads(Path(sys.argv[1]).read_text()) if len(sys.argv)>1 else json.load(urllib.request.urlopen(URL,timeout=60))
rows={}
for x in raw.values():
 if not x['IsReleased'][0]: continue
 n,_,v=x['Name'].partition('（');v=v.rstrip('）') or '通常'
 if n in ('初音ミク','御坂美琴','佐天涙子','食蜂操祈'):continue
 k=(n,v); rows.setdefault(k,{'n':n,'v':v,'id':x['Id'],'icon':x['Icon']})
assert len(rows)>200 and ('シロコ＊テラー','通常') in rows
p=Path('students.json')
if p.exists():
 for x in json.loads(p.read_text()):rows.setdefault((x['n'],x['v']),x)
p.write_text(json.dumps(list(rows.values()),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(len(rows),'items')
