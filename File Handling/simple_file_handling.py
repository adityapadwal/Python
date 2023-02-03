import csv
f = open("student.csv", "a", newline="")
a = csv.writer(f)

a.writerow(["studentID", "rollno", "name", "mobileno"])
studentid = int(input("Enter student id: "))
rollno = int(input("Enter student rollno: "))
name = input("Enter student name: ")
mobileno = int(input("Enter student mobile no: "))

a.writerow([studentid, rollno, name, mobileno])
print('Student record saved!')
