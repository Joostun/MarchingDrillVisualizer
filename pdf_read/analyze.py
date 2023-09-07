import re

from CoordSheet import CoordSheet

marcher_list=[]

with open("text_output.txt") as f:
    raw = f.read()

sheets = raw.split("Printed:")[:-1]

for sheet in sheets:
    marcher_list.append(CoordSheet(sheet))

print(marcher_list[0].sets[1].coordinate.coords)