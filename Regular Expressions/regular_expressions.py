import re  # re module for performing all the regular expressions based operations

count = 0

pattern = re.compile("python")  # string converts into bytecode
matcher = pattern.finditer("A function in python is defined using a def statement, python is ont of the best programming languages, python has a lot of applications, python is the future!")
print(matcher)

for i in matcher: 
    count += 1
    print(i.start(), '...', i.end(), '...', i.group())

print("The number of occurances are: ", count)
