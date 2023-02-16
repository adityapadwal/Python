# <============ without using multithreading =============>
'''
# from thread import *
import time

def add(num):
    for n in num:
        time.sleep(1)
        print("\n Add = ", 2+n)
        print()

def mul(num):
    for n in num:
        time.sleep(1)
        print("\n Mult = ", n*n)
        print()

def sub(num):
    for n in num:
        time.sleep(1)
        print("\n Sub = ", n-n)
        print()

num = [2, 4, 6, 8, 9]
starttime = time.time()
add(num)
mul(num)
sub(num)
print("The total time = ", time.time()-starttime)
'''
# <======== using multithreading =============>

from threading import *
import time

def add(num):
    for n in num:
        time.sleep(1)
        print("\n Add = ", 2+n)
        print()

def mul(num):
    for n in num:
        time.sleep(1)
        print("\n Mult = ", n*n)
        print()

def sub(num):
    for n in num:
        time.sleep(1)
        print("\n Sub = ", n-n)
        print()

num = [2, 4, 6, 8, 9]
starttime = time.time()
t1 = Thread(target = add,args=(num,))
t2 = Thread(target = mul,args=(num,))
t3 = Thread(target = sub,args=(num,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("The total time = ", time.time()-starttime)
