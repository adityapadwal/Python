'''
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 
The array is virtually split into a sorted and an unsorted part.
Values from the unsorted part are picked and placed at the correct position in the sorted part.
'''

def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i-1
        while j >= 0:
            if(list[j] > temp):
                list[j+1] = list[j]
            else:
                break
            j = j-1
        list[j+1] = temp
    
    print("----- After Sorting -----")
    print(list)
    
list = [12, 11, 13, 5, 6]
print("----- Before sorting -----")
print(list)
insertion_sort(list)