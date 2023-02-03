try: 
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    try:
        print(a / b)
    except ZeroDivisionError as msg:
        print(msg)
except ValueError as msg:
    print(msg)