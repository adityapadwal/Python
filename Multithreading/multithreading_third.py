# Creating a thread without extending the thread class
import time
from threading import *
class MyTest:
    def display(self):
        for i in range(10):
            time.sleep(2)
            print("\n Child Thread")

obj = MyTest()
t = Thread(target = obj.display)
t.start()

for i in range(10):
    time.sleep(2)
    print("\n Main Thread")