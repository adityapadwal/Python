# Multiple inheritance

class SubjMarks:          # parent-class 1
    math = int(input("Enter maths marks: "))
    science = int(input("Enter science marks: "))
    english = int(input("Enter english marks: "))
    history = int(input("Enter history marks: "))

class PractMarks:
    spract = int(input("Enter science practical marks: "))

class Result(SubjMarks, PractMarks):
    def total(self):
        if self.math >= 40 and self.science >= 40 and self.history >= 40 and self.history >= 40 and self.spract >= 40:
            print("Student has passed!")
        else:
            print("Student has failed!")

obj = Result()
obj.total()