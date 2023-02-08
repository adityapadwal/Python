choice = 0
class Exam(object):
    def __init__(self):
        self.sname = ""
        self.collegename=0
        self.classname = 0
        self.rollno = 0
        self.login()
    def login(self):
        print("=========================================")
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("=========================================") 
        print()
        if username == password:
            print('Login Successfull')
        else:
            print("Incorrect username or password")

        print("Choose any branch for givivng exam")
        print("1. Computer Science")
        print("2. Mechanical Engineering")
        print("3. Information Technology")
        print("4. Civil Engineering")
        print()

        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.computer()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print("you have entered wrong choice")

    def computer(self):
        self.dbms = int(input("Enter marks of Database Management System: "))
        self.toc = int(input("Enter marks of Theory of Computation: "))
        self.spos = int(input("Enter marks of Operating System: "))
        self.cns = int(input("Enter marks of Computer Networks: "))
        self.spm = int(input("Enter marks of Software Project Management: "))
        
class Calculation():
    def __init__(self):
        
        if self.dbms>=40 and self.toc >=40 and self.spos>=40 and self.cns >=40 and self.spm >=40:
            self.ps = "PASS"
        else:
            self.ps = "FAIL"
        self.total = self.dbms + self.toc + self.spos + self.cns + self.spm
        self.percentage = (self.total/500)*100

class Assesment(Exam, Calculation):
    def _init_(self):
        Exam.__init__(self)
        Calculation.__init__(self)
    def result(self):
        print("=============================================================")
        print("                                                             ")
        print("                     College Name: ",self.collegename,"      ")
        print("                                                             ")
        print("=============================================================")
       
        print("|                    Student Name: ",self.sname,"            ")
        print("|                    Class Name: ",self.classname,"         |")
        print("|                    Roll No: ",self.rollno,"               |")
        print("=============================================================")
        print(" Subject Name :       Total Marks   :   Obtained Marks:      ")
        print("                                                             ")
        print("DBMS          :",     "   100   "    "    :",  self.dbms,   ":")
        print("TOC           :",     "   100   "    "    :",  self.toc,   ":")
        print("SPOS          :",     "   100   "    "    :",  self.spos,   ":")
        print("CNS           :",     "   100   "    "    :",  self.cns,   ":")
        print("SPM           :",     "   100   "    "    :",  self.spm,   ":")
        
        print("")
        print("==========================================================================================")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("==========================================================================================")

obj2 = Assesment()
obj2.result()