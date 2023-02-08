import re
a = input("Enter any string to perform match operation: ")
mtch = re.match(a, "pythonisveryimportant")

print(mtch)

if mtch != None:
    print("match found at beginning level")
    print(mtch.start(), "...", mtch.end())
else:
    print("There is no matching at beginning level")