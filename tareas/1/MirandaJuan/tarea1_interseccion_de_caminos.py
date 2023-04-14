#!/usr/bin/python3

#   Interseccion de caminos 

import threading
import time

mutex = threading.Semaphore(1)
barrera = threading.Semaphore(0)
autos_pasa = 5
autos_esperando = 0


def pasa(id):
    global autos_esperando,mutex,autos_pasa
    
    with mutex:
        autos_esperando = autos_esperando + 1
        print("Habemos",autos_esperando, "autos esperando a pasar" )
        if autos_esperando == autos_pasa:
            print("\nSomos 5, es nuestro turno de paso\n")
            print("Choches que han transitado la avenida....",id+1,"\n")
            barrera.release()

    barrera.acquire()
    barrera.release()
    
    with mutex:
        print(id+1," paso la barrera!")
    
    with mutex:
        autos_esperando = autos_esperando - 1
        if autos_esperando == 0:
            barrera.acquire()
                

for i in range(20):
    time.sleep(0.5)
    threading.Thread(target=pasa,args=[i]).start()
