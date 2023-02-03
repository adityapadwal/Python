
while True:
    user = input('Enter a character: ')
    if user != "Quit":
        input = ord(user)
        if(input >= 97 and input<= 122):
            print('Entered character in a lowercase character.')
        elif(input >= 65 and input<= 91):
            print('Entered character is an uppercase character.')
        elif(input >= 48 and input <= 57):
            print("Entered character is a digit.")
        else:
            print("Entered character is a special character.")
    else:
        break