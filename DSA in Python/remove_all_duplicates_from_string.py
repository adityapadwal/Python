'''
Problem Statement
Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from the given string and return it.

Sample Input
1122334455ababzzz@@@123#*#*

Expected Output
12345abz@#*
'''

#lex_auth_01269446319507046499
from collections import OrderedDict

def remove_duplicates(value):
    #start writing your code here
    return "".join(OrderedDict.fromkeys(value))
    
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))