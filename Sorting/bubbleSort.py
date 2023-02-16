def bubble_sort(list):
    for i in range (0, len(list)):
        for j in range (i+1, len(list)):
            if(list[i] > list[j]):
                # list[i], list[j] = list[j], list[i]   shortcut 
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    
    print("<----- Sorted list ----->")
    print(list)
    
list = [5, 4, 3, 2, 1]
print("<----- Unsorted list ----->")
print(list)
bubble_sort(list)