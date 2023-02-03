'''
Question
    1  5
    2  4 
    4  2 
    5  1
'''

for i, j in zip(range(1, 6), range(5, 0, -1)):
    if(i==3 & j==3):
        continue
    print(i, "\t", j)