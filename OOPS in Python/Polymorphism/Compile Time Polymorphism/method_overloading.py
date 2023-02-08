# Python method overloading is not possble 

# In case of method overloading, if multiple methods having the same name are present, 
# pyhton always considers the last method, hence method overloading is not possible in python

# Same is the issue with constructor overloading

class Arithmetic:
    def add(self, a):
        print(a)
    
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)

obj = Arithmetic
obj.add(12)
obj.add(12, 13)
obj.add(12, 13, 14)

# To handle overloaded methods in python, 
# if method wirth variable number of arguments required
# then we can handle it with default arguments

class Arithmetic:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None:
            print(a+b)
        elif  a!=None and b!=None and c!=None:
            print(a+b+c)
        else:
            print("mf, enter at least two arguments" )

obj = Arithmetic()
obj.add(100)
obj.add(10, 20)
obj.add(1, 2, 3)
