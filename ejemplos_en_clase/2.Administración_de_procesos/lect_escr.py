#!/usr/bin/python3
import threading
import time
import random

lectores = 0
mutex = threading.Semaphore(1)
cuarto_vacio = threading.Semaphore(1)
demora_lect = 0.3
demora_escr = 1

def lanza_escritores():
    num = 0
    while True:
        threading.Thread(target=escritor, args=[num]).start()
        time.sleep(demora_escr)
        num += 1

def lanza_lectores():
    num = 0
    while True:
        threading.Thread(target=lector, args=[num]).start()
        time.sleep(demora_lect)
        num += 1

def escritor(id):
    print("  E%d: Llega el escritor..." % id)
    cuarto_vacio.acquire()
    print("  E%d: Escribiendo." % id)
    time.sleep(random.random())
    cuarto_vacio.release()
    print("  E%d: Me voy." % id)

def lector(id):
    global lectores
    print("L%d: Llegando..." % id)
    mutex.acquire()
    lectores = lectores + 1
    if lectores == 1:
        print("L%d: El cuarto estaba vacío" % id)
        cuarto_vacio.acquire()
    mutex.release()

    print("L%d: Leyendo..." % id)
    time.sleep(random.random())

    mutex.acquire()
    lectores = lectores - 1
    if lectores == 0:
        print("L%d: El cuarto queda vacío." % id)
        cuarto_vacio.release()
    mutex.release()
    print("L%d: Ya me fui." % id)

threading.Thread(target=lanza_lectores).start()
threading.Thread(target=lanza_escritores).start()
