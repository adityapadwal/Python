stack = []
print("Add 5 elements in the stack")
for i in range(5):
    a = int(input("Enter a number: "))
    stack.append(a)                           # stack push operation

print(stack)

print("Popping 2 elements from the stack")
for i in range(2):
    stack.pop()                              # stack pop operation

print(stack)

print("Using Peak opearion")
print(stack.top())



'''
Stack operations
push -> append()
pop -> pop()
'''