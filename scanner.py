import json
from database import connect,save
from matcher import find_matches
from sources.json_import import JsonImportSource
def scan(source):
 cfg=json.load(open('config/searches.json')); d=connect(); n=0
 for x in source.listings():
  if x.state.upper() in cfg['excluded_states']: continue
  m=find_matches(x,cfg['searches'])
  if m and save(d,x,m): n+=1
 return n
if __name__=='__main__': print('Added',scan(JsonImportSource('sample_listings.json')),'listing(s)')
