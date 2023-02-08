class College:                 # first class first level (Grandfather)

    def college_name(self):
        print("DYPIT")

class Student(College):      # second class second level (Father)

    def student_info(self):
        print("Name: Aditya Padwal")
        print("Branch: Computer Engineering")

class Exam(Student):         # child class (Son)

    def subject(self):
        print("Subject1 : DSA")
        print("Subject2 : TOC")
        print("Subject3 : DBMS")

obj = Exam()
obj.college_name()
obj.student_info()
obj.subject()
