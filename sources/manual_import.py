import json
from models import Listing


class ManualImportSource:
    def __init__(self, data):
        self.data = data

    def listings(self):
        if isinstance(self.data, str):
            self.data = json.loads(self.data)

        return [Listing(**item) for item in self.data]