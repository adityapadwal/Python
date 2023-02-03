import os

def function(path):
    try:
        content = os.listdir(path = path)
        list1 = []
        list2 = []
        for file in content:
            list1.append(file)
            list2.append(os.path.getsize(path + "//" + file))

        final = list(zip(list1, list2))
        final.sort(key = lambda x : x[1])

        for i, j in final:
            print(i, "has size = ", j)
    except:
        print("Oops! Path doesn't exist!!!")

path = input("Enter the path: ")
function(path)