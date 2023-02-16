def Selection(list):
    i = 0
    while i<len(list):
        j = i+1
        while j<len(list):
            if(list[j] < list[i]):
                # list[i], list[j] = list[j], list[i]   shortcut 
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j = j+1
        i = i+1
    print("\n ----Sorted string----")
    print(list)
            


list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("\n -----Unsorted String-----")
print(list)
Selection(list)

def Selection_Sort(list):
    i = 0
    while i<len(list):
        j = i+1
        while j<len(list):
            if(list[j][1] < list[i][1]):
                # list[i], list[j] = list[j], list[i]   shortcut 
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j = j+1
        i = i+1
    print("\n ----Sorted string----")
    print(list)
            


list = [["Aditya", 21], ["Ankit", 20], ["Shriram", 11]]
print("\n -----Unsorted String-----")
print(list)
Selection_Sort(list)