import re
obj = input("Enter any character: ")
objmatch = re.finditer(obj, "a7b @9z")
print(objmatch)
for match in objmatch:
    print(match.start(), "...", match.end(), "...", match.group())