class Stack: 
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def view_stack(self):
        print(self.items)
 
s = Stack()               # object of stack class         
while True:
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. View Stack')
    print('0. Quit')
    choice = int(input("Enter your choice: "))
    print("--------------------")

    if choice == 1:
        data = int(input("Enter data: "))
        s.push(data)
    elif choice == 2:
        if s.is_empty():
            print('Stack is empty!')
        else:
            print('Popped value: ', s.pop())
    elif choice == 3:
        print("Peek value: ", s.peek())
    elif choice == 4:
        s.view_stack()
    elif choice == 0:
        break
    else: 
        print("Wrong choice! Enter value again")
    print("--------------------")