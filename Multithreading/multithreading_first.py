# Creating a thread without using a class 
from threading import *
import threading
import time

def activate():         # user defined method
    for i in range(1, 11):
        time.sleep(2)
        print("\n This is => Child Thread")

t = Thread(target = activate)  # creating a thread
t.start()   # starting a thread

# <============== child thread ================>
for i in range(1, 11):
    time.sleep(2)
    print("\n This is => Main Thread")