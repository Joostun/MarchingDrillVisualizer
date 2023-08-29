import re

from Coordinate import Coordinate

class Set:

    def __init__(self, raw):
        self.raw = raw

        self.number = None
        self.counts = None
        self.coordinate = None
        self.process(raw)
    
    def process(self, raw):
        self.number = raw.split()[0]
        self.counts = re.search("\d+(?=Side)")[0].strip()

        self.coordinate = Coordinate()
