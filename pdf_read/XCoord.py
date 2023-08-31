import re

class XCoord:
    def __init__(self, fstring):
        self.fstring = fstring

    def XCoord(fstring):
        #find yard line referenced in the instructions
        yard_line = int(FindYardLine(fstring)[0]) 

        #if the dot is not exactly on the line, record the step adjustment
        if 'steps' in fstring:
            step_adjust = float(LeftSearch(fstring)[0])*0.625
        else:
            step_adjust = 0
        translated_yard_line = 50 - yard_line

        #factor in the steps inside/outside the yard line
        if 'inside' in fstring:
            from_fifty = translated_yard_line - step_adjust
        elif 'outside' in fstring:
            from_fifty = translated_yard_line - step_adjust
        else:
            from_fifty = translated_yard_line

        #accounts for side in position.
        if 'Side 1' in fstring:
            from_fifty = -abs(from_fifty)
        else:
            from_fifty = abs(from_fifty)

        #returns x coordinate
        return from_fifty


def LeftSearch(fstring):
    return re.findall(r'(?<=:\s).+(?= steps)', fstring)

def FindYardLine(fstring):
    return re.findall(r'\b(\w+)\s+yd\b', fstring)
