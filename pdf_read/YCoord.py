import re

def StepsSearch(fstring):
    step_adjust = re.findall(r'(?<=ln\s).+(?= steps)',fstring)
    yard_adjust = .625 * float(step_adjust[0])
    return yard_adjust

class YCoord:
    def __init__(self, fstring):
        self.fstring = fstring
        if 'front' in fstring:
            adjustment = -abs(StepsSearch(fstring))
        elif 'behind' in fstring:
            adjustment = abs(StepsSearch(fstring))
        else:
            adjustment = 0

        #finds front hash or frsont side line
        if 'Front Hash' in fstring:
            raw_dist = 17.5
        elif 'Back Hash' in fstring:
            raw_dist = 35
        else:
            raw_dist = 0
        
        #combines adjustment and raw_dist
        y_coordinate = raw_dist + adjustment

        self.y_coordinate = y_coordinate



