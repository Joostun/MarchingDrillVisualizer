import re

from Set import Set


def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

class CoordSheet:

    def __init__(self, raw):
        self.raw = raw

        self.sets = []

        self.symbol = None
        self.number = None

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

        #self.sets = [Set(raw_set) for raw_set in raw_sets]
        

