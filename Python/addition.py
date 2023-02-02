# WAP for arithmetic operation
a = 4
b = 6
print("Addition = ", a+b)
print("Subtraction = ", a-b)
print("Muliplication = ", a*b)
print("Division = ", a/b)

# WAP for calculating Simple Interest
p = 155000
r = 8.2
t = 2
si = p*r*t / 100
print(' Simple Interest = ', si)

# WAP for swapping using a third variable 
a = 10
b = 20
print('Before Swapping', 'A = ', a, "B = ", b)
temp = a 
a = b 
b = temp 
print('After Swapping ', 'A = ', a, "B = ", b)

# swapping without using 3rd variable 
first = 10
second = 20
print("Before Swapping")
print("First: ", first)
print("Second: ", second)
first , second = second, first
print("After Swapping")
print("First: ", first)
print("Second: ", second)

# net salary from basic salary 
basic_salary = 20000
def salary(percent):
    salary = (percent * 20000) / 100
    return salary 
print(salary(40))
print(salary(30))
print(salary(20))

# Conversion in inch and centimeter
h = float(input("Enter height in feet: "))
print('Height in cm: ', h*30.48)
print('Height in inch: ', h*12)

