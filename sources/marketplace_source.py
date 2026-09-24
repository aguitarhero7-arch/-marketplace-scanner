from models import Listing

class MarketplaceSource:
    def __init__(self, provider):
        self.provider = provider

    def listings(self):
        return [Listing(**item) for item in self.provider()]