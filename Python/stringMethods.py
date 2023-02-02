fruits = ["   ManGo", "@apple@", "bananas", "CHIKU", "Guava"]
print('Before using string methods: ', fruits)

# fruits[0] = fruits[0].lstrip().title()
# fruits[1] = fruits[1].strip("@").title()
# fruits[2] = fruits[2].title()
# fruits[3] = fruits[3].strip().title()

# print('After using string methods: ',fruits)

def newFruits(x):
    return x.strip().strip("@").title()

fruits = list(map(newFruits, (fruits)))
print('After using string methods: ', fruits)

# Difference between capitalize() and title()
# str = 'My name is Aditya'
# print(str.title())
# print(str.capitalize())