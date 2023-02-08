class Principal:
    def role(self):
        print("Principal: I am visiting the campus! :)")

class Dean:
    def order(self):
        print("Dean: Aaja bhai mai toh dean hoon! :))")

def call(obj):  # called function
    if hasattr(obj, 'role'):
        obj.role()
    elif hasattr(obj, 'order'):
        obj.order()

obj = Principal()  # Creating obj of the principal class 1
call(obj)          # calling function

obj = Dean()       # Creating obj of the Dean class 2
call(obj)          # calling function