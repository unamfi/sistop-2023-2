#!/usr/bin/python3
import threading
import time
import random

palillos = [threading.Semaphore(1) for i in range(5)]

def piensa(n):
    print("%d: Pensando..." % n)
    #time.sleep(0.5)

def come(n):
    print("%d: Tengo hambre..." %n)
    palillos[n].acquire()
    print("%d: Tengo el palillo izquierdo 🍚" % n)
    palillos[(n+1) % 5].acquire()
    print("%d: Tengo el palillo derecho 🍛" % n)
    print("%d: Estoy comiendo 😃" % n)
    #time.sleep(0.3)
    palillos[n].release()
    palillos[(n+1) % 5].release()

def filosofo(n):
    while True:
        piensa(n)
        come(n)

for i in range(5):
    threading.Thread(target=filosofo, args=[i]).start()
