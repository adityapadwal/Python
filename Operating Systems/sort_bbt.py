import os

path = "B:/Web Series/The Big Bang Theory/Season 1"
content = os.listdir(path)

list1 = []
list2 = []

for file in content:
    list1.append(file)
    list2.append(os.path.getsize(path + "//" + file))

final = list(zip(list1, list2))
final.sort(key = lambda x : x[1])

for i, j in final:
    print(i, "has size = ", j)
