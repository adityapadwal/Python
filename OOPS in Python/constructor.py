class Hod:
    def __init__(self):   # constructor
        self.name = "Aditya"
        self.age = 21
        self.empid = 1001

    def info(self):       # instance method
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("empid: ", self.empid)

obj = Hod()
obj.info()
