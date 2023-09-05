import re
import gc

from CoordSheet import CoordSheet

with open("text_output.txt") as f:
    raw = f.read()



sheets = raw.split("Printed:")[:-1]

for sheet in sheets:
    indexValue = sheets.index(sheet)
    id = ids[indexValue]
    constructor = globals()[id]
    constructor = CoordSheet(sheet)
    print(constructor.name)



