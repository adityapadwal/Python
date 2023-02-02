list = ['Aditya', 'Ankit', 'Abhishek', 'Shriram', 'Rahul', 'Raj']
newList = [x for x in list if 'A' in x]

print('List => ', list)
print('newList => ',newList)

# <=============== Syntax ============>
# newlist = [expression for item in iterable if condition == True]