# constructor overloading
# constructor overloading is not possible in pyhton.
# If we define multiple constructors, then the last constructor will be constructor will be considered

class Arithmetic:
    def __init__(self):
        print("No Argument")
    def __init__(self, a):
        print("One argument passed")
    def __init__(self, a, b):
        print("Two arguments passed")

obj = Arithmetic()
obj = Arithmetic(10)
obj = Arithmetic(1, 2)
