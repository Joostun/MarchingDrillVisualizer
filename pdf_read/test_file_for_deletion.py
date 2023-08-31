import re

def LeftSearch(fstring):
    return re.findall(r'(?<=:\s).+(?= steps)', fstring)

def FindYardLine(fstring):
    return re.findall(r'\b(\w+)\s+yd\b', fstring)

def XCoord(fstring):
    yard_line = int(FindYardLine(fstring)[0]) 
    if 'steps' in fstring:
        step_adjust = float(LeftSearch(fstring)[0])*0.625
    else:
        step_adjust = 0
    print(yard_line)
    print(step_adjust)
    print('.')
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

       
print(XCoord("1    0Side 2: On 45 yd"))
print(XCoord('24Side 1: 2.0 steps inside 35 yd'))
print(XCoord('18   32Side 2: 0.25 steps outside 50 yd'))
