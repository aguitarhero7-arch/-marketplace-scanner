import json
from models import Listing
class JsonImportSource:
 def __init__(self,path): self.path=path
 def listings(self):
  with open(self.path) as f: return [Listing(**x) for x in json.load(f)]
