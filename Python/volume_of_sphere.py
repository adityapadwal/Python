from math import pi

def calculate(radius):
    # pi = 3.1415
    ans = 4/3 * pi * radius ** 3
    print('Answer is: ', round(ans, 4))

radius = int(input("Enter the radius: "))
calculate(radius)