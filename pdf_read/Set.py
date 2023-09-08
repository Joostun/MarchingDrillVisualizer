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
        if "Side" in raw:
            self.counts = re.findall("\d+(?=Side)",raw, re.DOTALL)[0].strip()
        elif "On 50 yd ln" in raw:
            self.counts = re.findall("\d+(?=On 50)",raw, re.DOTALL)[0].strip()

        self.coordinate = Coordinate(raw)
