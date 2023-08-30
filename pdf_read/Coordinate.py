import re

class Coordinate:

    def __init__(self, raw):
        self.raw = raw

        # Coordinates measured in Steps
        # X -> Steps from 50 yd line (Side 2 is [+] and Side 1 is [-])
        # Y -> Steps behind the front sideline

        self.x = None
        self.y = None

        self.process(raw)
    
    def process(self, raw):
        
        side = 1 if re.search("(?<=Side )\d")[0].strip() == "2" else -1

        re.search("(?<-:).+ln"),raw
        
        