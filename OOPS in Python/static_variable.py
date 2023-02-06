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
