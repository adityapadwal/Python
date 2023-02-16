# Creating a thread by extending the thread class 

from threading import *
import time

class MyThread(Thread):  # child class 
    def run(self):
        for i in range(10):
            time.sleep(2)
            print("\n Child Thread - 1")

obj_t = MyThread()
obj_t.start()

for i in range(10):
    time.sleep(2)
    print("\n Main Thread - 1")
