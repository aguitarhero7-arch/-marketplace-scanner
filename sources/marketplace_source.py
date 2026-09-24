import os 
from models import Listing
import requests
APIFY_TOKEN = os.getenv("APIFY_API_TOKEN")

class MarketplaceSource:
    def __init__(self, provider):
        self.provider = provider

    def listings(self):
        return [Listing(**item) for item in self.provider() 