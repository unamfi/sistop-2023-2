from threading import Semaphore, Thread
from time import sleep
hackers=Semaphore(0)
serfs=Semaphore(0)
mutex = Semaphore(1)

def lanzarSerf():
    for i in range(12):
        Thread(target=serf, args=[i]).start()
        sleep(0.2)

def lanzarHacker():
    for i in range(12):
        Thread(target=hacker, args=[i]).start()
        sleep(0.8)

def serf(id):
    global hackers,serfs,mutex
    with mutex:
        print("El serf %d espera para subir a la balsa"%id)
        serfs.release()
        if serfs._value==4:
            for j in range(4):
                serfs.acquire()
            print("La balsa partirá con 4 serfs")
        elif serfs._value==2 and hackers._value>=2:
            hackers.acquire()
            hackers.acquire()
            serfs.acquire()
            serfs.acquire()
            print("La balsa partirá con 2 serfs y 2 hackers")
        else:
            mutex.release()

def hacker(id):
    global hackers,serfs,mutex
    with mutex:
        print("El hacker %d espera para subir a la balsa"%id)
        hackers.release()
        if hackers._value==4:
            for j in range(4):
                hackers.acquire()
            print("La balsa partirá con 4 hackers")
        elif serfs._value>=2 and hackers._value==2:
            hackers.acquire()
            hackers.acquire()
            serfs.acquire()
            serfs.acquire()
            print("La balsa partirá con 2 serfs y 2 hackers")
        else:
            mutex.release()



Thread(target=lanzarSerf).start()
Thread(target=lanzarHacker).start()



