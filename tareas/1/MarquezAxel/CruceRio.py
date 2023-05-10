from threading import Semaphore, Thread
import time
import random 

serf_cont = 0
hacker_cont = 0

Max = 4
serf = Semaphore(0)
hacker= Semaphore(0)
balsa = Semaphore(1)

def lanza_serf():
    global serf_cont, hacker_cont

    while True:
        balsa.acquire()
        serf_cont += 1 
        print("Acomodando a Serf en la balsa")
        if serf_cont == Max:
            serf.release(4)            
            print("Balsa se lleno de SERFS!!")
        elif serf_cont == 2 and hacker_cont >= 2:
            serf.release(2)
            hacker.release(2)
            print("Balsa llena por 2 Serfs y 2 Hackers!!")           
        else:
            balsa.release()
        serf.acquire()
        

def lanza_hacker():
    global serf_cont, hacker_cont

    while True:
        balsa.acquire()
        hacker_cont += 1 
        print("Acomodando a Hacker en la balsa")
        if hacker_cont == Max:
            hacker.release(4)
            print("Balsa se lleno de HACKERS!!")
        elif hacker_cont == 2 and serf_cont >= 2:
            serf.release(2)
            hacker.release(2)
            print("Balsa llena por 2 Serfs y 2 Hackers!!")
        else:
            balsa.release()
        hacker.acquire()
        

for i in range(16):
    if random.randint(0, 1) == 0:
        Thread(target=lanza_hacker).start()
    else:
        Thread(target=lanza_serf).start()