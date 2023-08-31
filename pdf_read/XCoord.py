import re

class XCoord:
    def __init__(self, fstring):
        self.fstring = fstring

        #find yard line referenced in the instructions
        yard_line = int(FindYardLine(fstring)[0]) 

        #if the dot is not exactly on the line, record the step adjustment
        if 'steps' in fstring:
            step_adjust = float(StepsSearch(fstring)[0])*0.625
        else:
            step_adjust = 0
        translated_yard_line = 50 - yard_line

        #factor in the steps inside/outside the yard line
        if 'inside' in fstring:
            from_fifty = translated_yard_line - step_adjust
        elif 'outside' in fstring:
            from_fifty = translated_yard_line + step_adjust
        else:
            from_fifty = translated_yard_line

        #accounts for side in position.
        if 'Side 1' in fstring:
            from_fifty = -abs(from_fifty)
        else:
            from_fifty = abs(from_fifty)

        #returns x coordinate
        self.x_coordinate = from_fifty


#function that finds the number of steps off of a yard line
def StepsSearch(fstring):
    return re.findall(r'(?<=:\s).+(?= steps)', fstring)

#function that identifies the yard line indicated by the instructions
def FindYardLine(fstring):
    return re.findall(r'\b(\w+)\s+yd\b', fstring)
