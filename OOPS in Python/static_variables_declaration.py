# where can we declare static variables?

# 1. <============= inside a class but outside a method ===========>
'''
class College:
    collegename = "DIT"    # Static variable (1 memory)

    def __init__(self):
        self.studentname = "Aditya" # Instance variable (3 separate memory)
    
principal = College()  # Object creation
teacher = College()
accoutant = College()

print("principal: ", principal.collegename, " => ", principal.studentname)
print("teacher: ", teacher.collegename, " => ", teacher.studentname)
print("accoutant: ", accoutant.collegename, " => ", accoutant.studentname)

print(end="\n")
College.collegename = "DYPIT"  # Second way to add a static variable
principal.studentname = "Aditya Padwal"
print(end="\n")

print("principal: ", principal.collegename, " => ", principal.studentname)
print("teacher: ", teacher.collegename, " => ", teacher.studentname)
print("accoutant: ", accoutant.collegename, " => ", accoutant.studentname)
'''

# <======================2. Inside a constructor by using a classname===========>
'''
class College:
    collegename = "DIT"    # Static variable (1 memory)

    def __init__(self):
        College.collegename = "DYPIT"
    
principal = College()  # Object creation
teacher = College()
accoutant = College()

print("principal: ", principal.collegename)
print("teacher: ", teacher.collegename)
'''

# <================= 3. In a instance method by using class name =============>

class College:
    collegename = "DIT"    # Static variable (1 memory)

    def __init__(self):
        College.collegename = "DYPIT"

    def instance_method(self):
        College.collegename = "Dr. D. Y. Patil Institute Of Technology"
    

principal = College()  # Object creation
print("principal: ", College.collegename)

principal.instance_method()
print("principal: ", College.collegename)

# <=============== 4. In a class Method using class name or cls variable======>

# <============== 5. static method by using class name =================>

# How do we access static variable?

#<================ 1. inside instance method using self or class name ========>

#<================ 2. in a constructor using self or class name ==============>

#<=============== 3. in a class method using cls variable or class name =======>

#<=============== 4. in a static method using class name =============>

# <============= 5. Outside of a class using object or a class name =========>

#How do we delete the static variable 

#<============= 1. del classname.Staticvariablename ================>

#<============= 2. inside classname we can use cls variable: del cls: Staticvariablename

