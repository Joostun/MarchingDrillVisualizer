import re
import gc

from CoordSheet import CoordSheet

dotbook_list = []

with open("text_output.txt") as f:
    raw = f.read()



sheets = raw.split("Printed:")[:-1]

for sheet in sheets:
    dotbook = CoordSheet(sheet)
    dotbook_list.append(dotbook)


