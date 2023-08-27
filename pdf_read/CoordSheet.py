import re

class CoordSheet:

    def __init__(self, raw):
        self.process(raw)

        self.sets = {}

        self.symbol = None
        self.number = None
    
    def process(self, raw):
        raw = raw.strip()

        self.symbol = re.search("(?<=Symbol:).+(?=Label)", raw)[0].strip()
        self.number = re.search("(?<=Label:).+(?=ID)", raw)[0].strip()
        self.number = "0" if self.number == "(unlabeled)" else self.number


