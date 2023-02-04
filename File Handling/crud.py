while True:
    print('<-------------------------->')
    user = int(input("1.Write 2.Read 3.Update 4.Delete 5.Exit \n Enter your choice: "))
    print('<-------------------------->')
    if user == 1:
        # Write
        name = input("Enter name: ")
        with open(file="crud.txt", mode = "a", newline="") as f:
            f.write(name + " ")
    elif user == 2:
        # Read
        with open("crud.txt") as f:
            print(f.readlines())
    elif user == 3:
        # Update
        update = input("Enter the data to be updated: ")
        with open(file="crud.txt", mode="a") as f:
            f.seek(f.tell(update))
            update = input("Enter new value: ")
            f.write(update)
    # elif user == 4:
        # Delete
        
    elif user == 5:
        print("Thank you!!!")
        break
    else:
        print("Wrong input, try again!")