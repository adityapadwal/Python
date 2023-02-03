import os
l = os.listdir(path=f"B:/Web Series/The Big Bang Theory/Season 1")

for i in l:
    path = "B:/Web Series/The Big Bang Theory/Season 1/" + i
    print(i, os.path.getsize(path))
