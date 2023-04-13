#!/usr/bin/python3
#
# Implementemos una barrera usando Semaphore() que tenga el mismo
# comportamiento que Barrier(): Que una vez que pasen "n" hilos vuelva
# a cerrarse
from threading import Semaphore, Thread
from time import sleep

num_hilos = 4
cuenta = 0
mutex = Semaphore(1)
barrera = Semaphore(0)

def hilo_que_espera(id):
    global cuenta, mutex, barrera, num_hilos
    print("Hilo %d iniciando" % id)
    with mutex:
        cuenta = cuenta + 1
        print("Habemos %d hilos frente a la barrera." % cuenta)
        if cuenta == num_hilos:
            print("Levantando la barrera. Soy %d" % id)
            barrera.release()

    print("Hilo %d se forma frente a la barrera..." % id)
    barrera.acquire()
    barrera.release()
    print("¡%d pasó la barrera!" % id)

    with mutex:
        cuenta = cuenta - 1 # Ya terminé!
        if cuenta == 0:
            barrera.acquire()

for i in range(16):
    sleep(0.5)
    Thread(target=hilo_que_espera, args=[i]).start()
