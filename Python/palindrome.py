def palindrome(name):
    s = 0
    e = len(name) - 1
    while(s <= e):
        if(name[s] == name[e]):
            s = s + 1
            e = e - 1
        else:
            return False
    return True

name = str(input("Enter the name: "))
ans = palindrome(name)
if(ans == True):
    print('The given string is a palindrome')
else:
    print("The given string is not a palindrome")
