import re
a = input("Enter any string to perform match operation: ")
mtch = re.fullmatch(a, "pythonisveryimportant")

print(mtch)

if mtch != None:
    print("full match found")
    print(mtch.start(), "...", mtch.end())
else:
    print("no full match found")