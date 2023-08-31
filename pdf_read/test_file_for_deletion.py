import re

def LeftSearch(fstring):
    return re.findall(r'\b(\w+)\s+steps\b', fstring)

def FindYardLine(fstring):
    return re.findall(r'\b(\w+)\s+yd\b', fstring)

def XCoord(fstring):
    yard_line = int(FindYardLine(fstring)[0]) 
    step_adjust = int(LeftSearch(fstring)[0])*0.625
    translated_yard_line = 50 - yard_line
    if 'inside' in fstring:
        from_fifty = translated_yard_line - step_adjust
    elif 'outside' in fstring:
        from_fifty = translated_yard_line - step_adjust
    else:
        from_fifty = translated_yard_line
    return from_fifty


re_value = re.findall(":.+","1    0Side 2: On 45 yd ln 8.0 steps behind Front side line")
split_list = re_value[0].split("ln")

       
print(XCoord("1    0Side 2: On 45 yd ln 8.0 steps behind Front side line"))