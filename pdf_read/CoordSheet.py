import re

from Set import Set


def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

class CoordSheet:

    def __init__(self, raw):
        self.raw = raw

        stripped_raw = raw.strip()
        self.sets = []


        self.symbol = re.search("(?<=Symbol:).+(?=Label)", stripped_raw)[0].strip()
        self.number = re.search("(?<=Label:).+(?=ID)", stripped_raw)[0].strip()
        self.number = "0" if self.number == "(unlabeled)" else self.number

        raw_sets = re.search("(?<=Front-Back).+(?=Performer)", stripped_raw, re.DOTALL)[0].splitlines()

        raw_sets = remove_items(raw_sets, "")
        for instructions in raw_sets:
            self.sets.append(Set(instructions))

        self.name = f"{self.symbol}{self.number}"
        

