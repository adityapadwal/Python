name = input("Enter your name: ")
age = int(input("Enter age: "))

print(f'\n I am {name} and I am {age} years old')
print('\n I am', name, 'and I am', age, 'years old')
print('\n I am '+ name + ' and I am '+ str(age) + ' years old')
print('\n I am {} and I am {} years old'.format(name, age))
print('\n I am %s and I am %i years old' %(name, age))