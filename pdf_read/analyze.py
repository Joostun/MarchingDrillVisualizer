import re

from CoordSheet import CoordSheet


with open("text_output.txt") as f:
    raw = f.read()



sheets = raw.split("Printed:")[:-1]

for sheet in sheets:
    print(CoordSheet(sheet))