import csv
id = 0
f = open("student_data.csv", "a", newline="")
a = csv.writer(f)

a.writerow(["ID", "Name", "RollNo", "Email ID", "Address", "Mobile No", "Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5", "Total", "Percentage", "Result"])
while True:
    val = int(input("1=> Write 2=> Read 3=> Exit \n Enter Your Choice : "))
    if val == 1:
        name = input("Enter student's name: ")
        rollno = int(input("Enter student's rollno: "))
        emailid = input("Enter emailID : ")
        address = input("Enter student address : ")
        mobileno = input("Enter student's mobileno : ")

        sub1 = int(input("Enter marks of subject 1 => "))
        sub2 = int(input("Enter marks of subject 2 => "))
        sub3 = int(input("Enter marks of subject 3 => "))
        sub4 = int(input("Enter marks of subject 4 => "))
        sub5 = int(input("Enter marks of subject 5 => "))

        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = total/500*100

        if percentage >= 40:
            result = "Pass :)"
        else:
            result = "Fail :("

        id += 1
        a.writerow([id, name, rollno, emailid, address, mobileno, sub1, sub2, sub3, sub4, sub5, total, percentage, result])
        print('\n <====Student Data Saved Successfully!====> \n')
    elif val == 2:
        with open('student_data.csv', mode = 'r') as file:
            data = csv.reader(file)
            for lines in data:
                print(lines)
    else:
        break

f.close()
