# Tarea interseccion de caminos
from threading import Semaphore, Thread
from time import sleep
import random

Cuadrantes = []
Mutex = Semaphore(1)

Cuadrantes.append(Semaphore(1))
Cuadrantes.append(Semaphore(1))
Cuadrantes.append(Semaphore(1))
Cuadrantes.append(Semaphore(1))

# Carros que pasan por los cuadrantes con semaforos y un mutex para evitar la inanicion
def Carros(Direccion,C1,C2,num):
    Mutex.acquire()
    print('Nuevo carro 🚗 numero:',num,Direccion)
    Cuadrantes[C1].acquire()
    print("carro:",num,"🛑 pasando por el cuadrante ", C1)
    Cuadrantes[C1].release()
    Cuadrantes[C2].acquire()
    print("carro:",num,"🛑 pasando por el cuadrante ", C2)
    Cuadrantes[C2].release()
    print("carro 🚗 numero:",num,"Sali del cruce!!! 🎉🎉🎉")
    Mutex.release()

# Creación de Carros con una direccion aleatoria
for i in range(99999):
    aleatorio=random.randint(1,4)
    if aleatorio==1:
        Thread(target=Carros, args=("Voy del sur hacia el norte ⬆️",2,1,i)).start()
    elif aleatorio==2:
        Thread(target=Carros, args=("Voy del norte hacia el sur ⬇️",0,3,i)).start()
    elif aleatorio==3:
        Thread(target=Carros, args=("Voy del oeste hacia el este ➡️",3,2,i)).start()
    else:
        Thread(target=Carros, args=("Voy del este hacia el oeste ⬅️",1,0,i)).start()