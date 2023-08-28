
class Set:

    def __init__(self, raw):
        self.process(raw)
        self.raw = raw

        self.number = None
        self.counts = None
        self.coordinate = None
    
    def process(self, raw):
        print("processing a line WIP")