class Student:
    roll_no = 101    # data members
    name = "Aditya"
    num1 = 10
    num2 = 20

    def add(self):  # syntax for member functions
        print("The addition is: ", self.num1 + self.num2)
        self.name = input("Enter your name: ")
        print("Hi, ", self.name)

obj = Student()
obj.add()
print(obj.roll_no)