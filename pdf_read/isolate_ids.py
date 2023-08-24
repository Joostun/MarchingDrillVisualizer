import re

with open("text_output.txt") as file:
    data = file.read()

pattern1 = r"Symbol: (\w+)"
pattern2 = r"Label: (\w+)"
matches1 = re.findall(pattern1, data)
matches2 = re.findall(pattern2, data)
print(matches1)
print(matches2)