# Single Inheritance

class Faculty: # parent class
    def __init__(self, f_name, department, f_id):
        self.f_name = f_name
        self.department = department
        self.f_id = f_id

    def print_info(self):
        print('faculty information = ', self.f_name, self.department, self.f_id)

class Cse(Faculty):  #child class 
    pass

obj = Cse("Jyoti Maam", "Computer Science", 1002)
obj.print_info()
