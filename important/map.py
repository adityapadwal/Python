numbers = [1, 2, 3, 4]

def square(a):
    return a**2

squares = list(map(square, numbers))
print(squares)


newSquares = list(map(lambda x : x**2, numbers))
print(newSquares)