"""
Solis González Alan David
Sistemas Operativos
Ejercicios de sincronización: Santa Claus
El programa crea hilos de ejecución que simulan ser elfos, renos y santa.
Estos hilos estan sincronizados de acuerdo al planteamiento del problema.
Fecha de entrega: 13/04/2023
"""

import threading
import random as rand
import time                                 #La función sleep() se usó para ayudar a visualizar el funcionamiento del código

num_elfos = 15
num_renos = 9

mutex_elfos = threading.Semaphore(1)
mutex_renos = threading.Semaphore(1)
torniquete = threading.Semaphore(1)         #El torniquete se usa para una mejor visibilidad de los prints
barrera_elfos = threading.Semaphore(0)
barrera_renos = threading.Semaphore(0)

problemas = 0
renos_listos = 0

#######     ELFOS     ########

def elfos(id):
    while True:
        trabajar(id)
        problem(id)

def trabajar(n):
    torniquete.acquire()
    torniquete.release()
    print('Elfo ', n, ': Trabajando 🎁🎄', sep='')

#Probabilidad de problema en el trabajo: 20% = 1/5
def problem(n):
    global problemas
    mutex_elfos.acquire()
    prob = rand.randint(1,5)
    if (prob == 5):
        problemas += 1
        torniquete.acquire()
        torniquete.release()
        print('Elfo ', n, ': Oh no, tuve un problema 🤯', sep='')
        mutex_elfos.release()
        barrera_elfos.acquire()
    else:
        mutex_elfos.release()

#######     RENOS       #######

def renos(id):
    while True:
        descansar(id)
        volver_al_polo_norte(id)

def descansar(n):
    torniquete.acquire()
    torniquete.release()
    print('Reno ', n,': Descansando 😎🧉🌴', sep='')

#Probabiliadad de volver al polo norte: 10% = 1/10
def volver_al_polo_norte(n):
    global renos_listos
    mutex_renos.acquire()
    ganas = rand.randint(1, 10)
    if (ganas == 10):
        renos_listos += 1
        torniquete.acquire()
        torniquete.release()
        print('Reno ', n, ': Es hora de volver al polo norte 🥶❄️☃️')
        mutex_renos.release()
        barrera_renos.acquire()
    else:
        mutex_renos.release()

######      SANTA       #######

def Santa():
    while True:
        #Santa esta durmiendo 😴😴😴
        comprobar_elfos()
        comprobar_renos()

def comprobar_elfos():
    global problemas
    mutex_elfos.acquire()
    if (problemas >= 3):
        barrera_elfos.release(3)
        torniquete.acquire()
        print('Santa se ha despertado 🎅')
        print('Santa esta ayudando a los elfos 🎅🥳')
        print('Santa acabo de ayudar a los elfos 😇')
        torniquete.release()
        problemas -= 3
    mutex_elfos.release()

def comprobar_renos():
    global renos_listos
    mutex_renos.acquire()
    if (renos_listos == 9):
        barrera_renos.release(9)
        torniquete.acquire()
        print('Es hora de repartir los regalos 🎅🎁🎄')
        #time.sleep(0.3)
        print('🦌🦌🦌🦌🦌🦌🦌🦌🦌🛷🎅')
        #time.sleep(0.3)
        #print('🦌🦌🦌🦌🦌🦌🛷🎅')
        #time.sleep(0.3)
        #print('🦌🦌🦌🛷🎅')
        #time.sleep(0.3)
        torniquete.release()
        renos_listos = 0
    mutex_renos.release()

######      EJECUCIÓN DE LOS HILOS      ######

for i in range(num_elfos):
    threading.Thread(target=elfos, args=[i]).start()

for i in range(num_renos):
    threading.Thread(target=renos, args=[i]).start()

threading.Thread(target=Santa, args=[]).start()
