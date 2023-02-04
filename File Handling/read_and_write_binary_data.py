f1 = open("guido.jpeg", "rb")
f2 = open("rossom.jpg", "wb")
data = f1.read()
f2.write(data)
print("New image is available!")

f1.close()
f2.close()


# Same for videos
