class Hod:
    def __init__(self, name, age, roll_no):   # constructor
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def info(self):       # instance method
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("rollno: ", self.roll_no)

obj = Hod('Aditya', 22, 1002)
obj.info()
