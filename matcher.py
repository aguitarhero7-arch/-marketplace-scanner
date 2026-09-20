import re
def norm(s): return re.sub(r'[^a-z0-9]+',' ',(s or '').lower()).strip()
def find_matches(x, searches):
 h=norm(x.title+' '+x.description)
 if any(w in h for w in ['wanted','wtb','looking for','iso ']): return []
 return [s['query'] for s in searches if norm(s['query']) in h]
