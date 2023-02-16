import requests

# Making a get request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# status code - 200
print(r)

# printing the content of the request
print(r.content)