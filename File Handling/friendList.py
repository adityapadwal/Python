while True:
    print('<---------------------->')
    user = int(input("1.Write 2.Read 3.Exit \n Enter your choice: "))
    print('<---------------------->')
    if user == 1:
        name = input("Enter name: ")
        with open(file="friendList.txt", mode = "a", newline="") as f:
            f.write(" , " + name)
    elif user == 2:
        with open("friendList.txt") as f:
            print(f.readlines())
    else:
        break
