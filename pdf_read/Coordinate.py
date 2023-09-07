import re
from XCoord import XCoord
from YCoord import YCoord

class Coordinate:

    def __init__(self, raw):
        self.raw = raw
        
        #splitting raw string into x and y instructions
        split_list = raw.split("ln")
        split_list[1] = 'ln ' + split_list[1]

        # Coordinates measured in Steps
        # X -> Steps from 50 yd line (Side 2 is [+] and Side 1 is [-])
        # Y -> Steps behind the front sideline
        XCoordClass = XCoord(split_list[0])
        YCoordClass = YCoord(split_list[1])

        raw.split("ln")
        self.x = XCoordClass.x_coordinate
        self.y = YCoordClass.y_coordinate
        self.coords = f"{self.x}, {self.y}"