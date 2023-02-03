import os
while True:
    try:
        path = input("Enter a path => ")
        if os.listdir(path):
            break
    except:
        print('Wrong path:-(')
        break
    else: 
        print('Inside else block')
        break
    finally:
        print("Inside finally block")
        break
    