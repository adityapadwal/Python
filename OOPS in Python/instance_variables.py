# accessing and deleting instance variables from the class
class Student:
    def __init__(self):
        self.s_name = input("Enter name: ")
        self.s_rollno = 101

    def getdata(self):
        self.s_mb = 6969696969

obj = Student()
obj.getdata()
obj.s_branch = "CS"    # adding an instance variable using an object
print('Before deleting rollno')
print(obj.__dict__)
del obj.s_rollno       # deleting an instance variable
print(obj.__dict__)