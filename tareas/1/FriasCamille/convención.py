import threading
from threading import Semaphore, Thread
from time import sleep
import time
sHacker=Semaphore(1)
sSerf=Semaphore(1)
capBalsa = 4
num_hilos = 2
cuenta = 0
cuenta_hacker = 0
mutex = Semaphore(1)
barrera = Semaphore(0)
cuenta_serf = 0
balsa = Semaphore(1)
cs=0
ch=0
def lanza_hacker():
    num = 0
    while num<16:
        threading.Thread(target=hacker, args=[num]).start()
        time.sleep(0.1)
        num += 1

def lanza_serf():
    num = 0
    while num<16:
        threading.Thread(target=serf, args=[num]).start()
        time.sleep(0.2)
        num += 1

def hacker(id):

    global cuenta_hacker, cuenta, cuenta_serf, cs, ch
    print("Hacker %d llegó a la orilla" % id)
    with balsa:
        print("La balsa está en la orilla y %d hacker está formado para subir"% id)
    with sHacker:
        with mutex:
            cuenta= cuenta+1
            cuenta_hacker= cuenta_hacker+1
            print("Hacker %d se sube a la balsa" %id, "hay %d hackers"% cuenta_hacker, " / %d serf" %cuenta_serf)
    with mutex:
        if (cuenta_hacker==3 and cuenta_serf==0)or(cuenta_hacker==1 and cuenta_serf==2):
            sSerf.acquire()
            cs=1
        if (cuenta_serf==3 and cuenta_hacker==0)or(cuenta_serf==1 and cuenta_hacker==2):
            sHacker.acquire()
            ch=1
        if cuenta==capBalsa:
            print("La balsa se va")
            barrera.release()
            balsa.acquire()
    barrera.acquire()
    barrera.release()

    with mutex:
        cuenta = cuenta - 1
        cuenta_hacker= cuenta_hacker-1
        print("¡Hacker %d llegó a la convención!" % id)
        if cuenta == 0:
            print("Ya todos se bajaron de la balsa, la balsa se regresa")
            barrera.acquire()
            balsa.release()
            if cs==1:
                cs=0
                sSerf.release()
            if ch==1:
                ch=0
                sHacker.release()
   
def serf(id):

    global cuenta_serf, cuenta, cuenta_hacker, ch, cs
    print("Serf %d llegó a la orilla" % id)
    with balsa:
        print("La balsa está en la orilla y %d serf está formado para subir"% id)
    with sSerf:
        with mutex:
            cuenta= cuenta+1
            cuenta_serf= cuenta_serf+1
            print("Serf %d se sube a la balsa" %id, "hay %d hackers"% cuenta_hacker, " / %d serf" %cuenta_serf)
    with mutex:
        if (cuenta_serf==3 and cuenta_hacker==0)or(cuenta_serf==1 and cuenta_hacker==2):
            sHacker.acquire()
            ch=1
        if (cuenta_hacker==3 and cuenta_serf==0)or(cuenta_hacker==1 and cuenta_serf==2):
            sSerf.acquire()
            cs=1
        if cuenta==capBalsa:
            print("La balsa se va")
            barrera.release()
            balsa.acquire()
    barrera.acquire()
    barrera.release()

    with mutex:
        cuenta = cuenta - 1
        cuenta_serf= cuenta_serf-1
        print("¡Serf %d llegó a la convención!" % id)
        if cuenta == 0:
            print("Ya todos se bajaron de la balsa, la balsa se regresa")
            barrera.acquire()
            balsa.release()
            if ch==1:
                ch=0
                sHacker.release()
            if cs==1:
                cs=0
                sSerf.release()
    
        
    
threading.Thread(target=lanza_hacker).start()
threading.Thread(target=lanza_serf).start()
