import threading
import time
import random

hackers = 0
serfs = 0
mutex = threading.Semaphore(1)
mutex_hacker = threading.Semaphore(1)
mutex_serf = threading.Semaphore(1)
cola_serf=threading.Semaphore(0)
check=threading.Semaphore(0)
cola_hacker=threading.Semaphore(0)


def hacker_thread():
    while True:
        time.sleep(0.5) 
        global hackers
        with mutex_hacker:
            hackers += 1
            print("Hacker esperando (num hackers = %d)" % hackers)
        cola_hacker.acquire()

    
def serf_thread():
    while True:
        time.sleep(0.5) 
        global serfs
        with mutex_serf:
            serfs += 1
            print("Serf esperando (num serfs = %d)" % serfs)
        cola_serf.acquire()
        
    
    
def checador():
    while True:
        time.sleep(0.5)  
        global hackers,serfs
        with mutex:
            if hackers >=4:
                print('Parten 4 hackers')
                hackers-=4
                cola_hacker.release(4)              
            elif serfs >= 4:
                print('Parten 4 serfs')
                serfs-=4
                cola_serf.release(4)
            elif serfs >= 2 and hackers>=2:
                print('Parten 2 serfs y 2 hackers')
                hackers-=2
                serfs-=2
                cola_hacker.release(2)
                cola_serf.release(2)
                

threads = []
for i in range(10): 
    t1 = threading.Thread(target=hacker_thread)
    t2 = threading.Thread(target=serf_thread)
    threads.append(t1)
    threads.append(t2)
    
random.shuffle(threads) 

for i in range(5):
    threading.Thread(target=checador).start()

for t in threads:
    t.start()