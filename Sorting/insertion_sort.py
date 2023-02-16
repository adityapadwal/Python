def insertion_sort(list):
    for i in range (1, len(list)):
        temp = list[i]
        j = i-1
        while j >= 0:
            if(list[j] > temp):
                list[j+1] = list[j]
            else:
                break
            j = j-1
        list[j+1] = temp
    return list

list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("<-----Before Sorting----->")
print(list)
print("<-----After Sorting----->")
print(insertion_sort(list))