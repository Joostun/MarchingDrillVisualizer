import re

def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

def Set():
    number = raw.split()[0]
    if "Side" in raw:
        counts = re.findall("\d+(?=Side)",raw, re.DOTALL)[0].strip()
    elif "On 50 yd ln" in raw:
        counts = re.findall("\d+(?=On 50)",raw, re.DOTALL)[0].strip()

    coordinate = Coordinate(raw)
    

class Marcher:

    def __init__(self, raw):
        self.raw = raw

        self.sets = []

        self.symbol = None
        self.number = None
        self.name = f"{self.symbol}{self.name}"
        self.process(raw)

    def process(self, raw):
        raw = raw.strip()

        self.symbol = re.search("(?<=Symbol:).+(?=Label)", raw)[0].strip()
        self.number = re.search("(?<=Label:).+(?=ID)", raw)[0].strip()
        self.number = "0" if self.number == "(unlabeled)" else self.number

        raw_sets = re.search("(?<=Front-Back).+(?=Performer)", raw, re.DOTALL)[0].splitlines()
        
        raw_sets = remove_items(raw_sets, "")

        for instructions in raw_sets:
            self.sets.append(Set(instructions))