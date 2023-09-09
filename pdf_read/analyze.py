import re

from CoordSheet import CoordSheet
from Marcher import Marcher

marcher_list=[]

with open("text_output.txt") as f:
    raw = f.read()

sheets = raw.split("Printed:")[:-1]

for sheet in sheets:
    marcher_list.append(Marcher(sheet))

print(marcher_list[0].x)
print(marcher_list[0].y)