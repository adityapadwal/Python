import re
obj = input("Enter any string: ")
objmatch = re.finditer(obj, "hiadihowareyouadi")
for match in objmatch:
    print(match.start(), ".....", match.group)
