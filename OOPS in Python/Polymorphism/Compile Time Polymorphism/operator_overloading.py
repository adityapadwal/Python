# Operator overloading is internally implemented using magic methods
'''
class Deposit:
    def __init__(self, cash):
        self.cash = cash

d1 = Deposit(1000)
d2 = Deposit(2000)
print(d1 + d2)
'''

# The above code wont execute and will generate the folllowing error
# unsupported operand type(s) for +: 'Deposit' and 'Deposit'

# magic method is available for every operator
# To overload any operator we have to override that method in our class 
# __add__ method is a magic method which gets called when we add two numbers using the + operator

class Deposit:
    def __init__(self, cash):
        self.cash = cash
    
    def __add__(self, other):  # magic method
        return self.cash + other.cash

d1 = Deposit(1000)
d2 = Deposit(2000)
print("Total cash deposit amount: ", d1+d2)

# Below are some magic methods
'''
==>   object.__add__(self, other)
==>   object.__sub__(self, other)
==>   object.__mul__(self, other)
==>   object.__div__(self, other)
==>   object.__floordiv__(self, other)
==>   object.__mod__(self, other)
.... and many more 
'''

