from dataclasses import dataclass
from typing import Optional
@dataclass
class Listing:
 source:str
 external_id:str
 title:str
 price:Optional[float]=None
 location:str=''
 state:str=''
 url:str=''
 description:str=''
