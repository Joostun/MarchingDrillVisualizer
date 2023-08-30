import re
re_value = re.findall(":.+","1    0Side 2: On 45 yd ln 8.0 steps behind Front side line")
split_list = re_value[0].split("ln")

find_number = re.findall(r'\d+', split_list[0])

if 'inside' in split_list[0]:
    print("contains inside")
else if 'outside' in split_list[0]:
    print("contains outside")

                      
print(find_number)