import time
print('The time is: ', time.ctime())
msg = time.ctime().split()
print(msg)
print(f"Today's date is : {msg[2]} {msg[1]},{msg[4]}")