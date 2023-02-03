import os
l = os.listdir(path=f"A:/Academics/TE/Training/Python MiniProjects")

print('<===Printing all .txt files===>')
for i in l:
    if(i.endswith('.txt')):
        print(i)

print(end="\n")

print('<===Printing all .py files===>')
for i in l:
    if(i.endswith('.py')):
        print(i)