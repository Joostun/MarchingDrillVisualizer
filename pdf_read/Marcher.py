import re

#function to clear a list
def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

#function that finds the number of steps off of a yard line for x
def xStepsSearch(fstring):
    return re.findall(r'(?<=:\s).+(?= steps)', fstring)

#function that finds the number of steps off of a yard line for y
def yStepsSearch(fstring):
    step_adjust = re.findall(r'(?<=ln\s).+(?= steps)',fstring)
    yard_adjust = .625 * float(step_adjust[0])
    return yard_adjust

#function that identifies the yard line indicated by the instructions
def FindYardLine(fstring):
    return re.findall(r'\b(\w+)\s+yd\b', fstring)

#XCoordinate Finder Function
def xCoord(fstring):
    #find yard line referenced in the instructions
    yard_line = int(FindYardLine(fstring)[0]) 

    #if the dot is not exactly on the line, record the step adjustment
    if 'steps' in fstring:
        step_adjust = float(xStepsSearch(fstring)[0])*0.625
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
    return from_fifty

#YCoordinate Finder Function
def yCoord(fstring):
    if 'front' in fstring:
        adjustment = -abs(yStepsSearch(fstring))
    elif 'behind' in fstring:
        adjustment = abs(yStepsSearch(fstring))
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

    return y_coordinate


#Marcher class
class Marcher:
    def __init__(self, raw):
        self.raw = raw

        self.sets = []

        #Marching identification
        self.symbol = None
        self.number = None

        #List of set counts
        self.counts = []

        #coordinates
        self.x = []
        self.y = []

        #Marching id
        self.name = None
        self.coordSheetProcess(raw)

    def coordSheetProcess(self, raw):

        #Seperating the raw data into lines
        raw = raw.strip()

        #Finding identification data
        self.symbol = re.search("(?<=Symbol:).+(?=Label)", raw)[0].strip()
        self.number = re.search("(?<=Label:).+(?=ID)", raw)[0].strip()
        self.number = "0" if self.number == "(unlabeled)" else self.number

        
        raw_sets = re.search("(?<=Front-Back).+(?=Performer)", raw, re.DOTALL)[0].splitlines()
        
        raw_sets = remove_items(raw_sets, "")

        #Marching id
        self.name = f"{self.symbol}{self.number}"

        for instructions in raw_sets:
            self.sets.append(self.setProcess(instructions))
    def setProcess(self, setRaw):

        self.number = setRaw.split()[0]

        if "Side" in setRaw:
            self.counts.append(re.findall("\d+(?=Side)",setRaw, re.DOTALL)[0].strip())
        elif "On 50 yd ln" in setRaw:
            self.counts.append(re.findall("\d+(?=On 50)",setRaw, re.DOTALL)[0].strip())


        split_list = setRaw.split("ln")
        split_list[1] = 'ln ' + split_list[1]

        self.x.append(xCoord(split_list[0]))
        self.y.append(yCoord(split_list[1]))

        
