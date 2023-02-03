import time

def registration():
    global password
    global username
    username = input("Enter Username: ")
    password = input("Enter password: ")

def login():
    while(True):
        user_input = input("Enter your username: ")
        if user_input == username:
            print('Username verified!')
            break
        else:
            print('Wrong Username')

    count = 0
    while(True):
        user_pass = input("Enter your password: ")
        if user_pass == password:
            print('Login Successful!')
            break
        else:
            count = count + 1
            if count < 3:
                print('Wrong Password! Enter password again')
            else:
                print("Password Attempts exceeded! Login again after 5 seconds")
                count = 0
                time.sleep(5)
            
registration()
login()