import re

marcher_dict = {}

with open("text_output.txt") as file:
    data = file.read()

split_data = data.split("Printed:")

pattern1 = r"Symbol: (\w+)"
pattern2 = r"Label: (\w+)"

for i in split_data:
    section = re.findall(pattern1, i)
    label = re.findall(pattern2, i)
    if label == "":
        label = 0
    name = f"{section}{label}"
    temp_dict = {
        "section": section,
        "label": label,
        "dot": i
    }
    marcher_dict[name] = temp_dict

for x in marcher_dict:
    print (x)
    for y in marcher_dict[x]:
        print (y,':',marcher_dict[x][y]) 