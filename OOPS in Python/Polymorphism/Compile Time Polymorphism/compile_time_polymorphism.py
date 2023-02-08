class Principal:
    def role(self):
        print("I am the principal class role method")

class Dean:
    def role(self):
        print("I am the dean class role method")

class Hod:
    def role(self):
        print("I am the Hod class role method")

class Faculty:
    def role(self):
        print("I am the Faculty class role method")

def func(obj): 
    obj.role()

campus = [Principal(), Dean(), Hod(), Faculty()]

for obj in campus:
    func(obj)