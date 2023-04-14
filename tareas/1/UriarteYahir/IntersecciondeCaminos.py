import threading
from threading import Semaphore
import random
import time

#Datos proporcionados por usuario
numCarros1 = int(input("Número de carros que transitaran por carril 1: "))
numCarros2 = int(input("Número de carros que transitaran por carril 2: "))
numCarros3 = int(input("Número de carros que transitaran por carril 3: "))
numCarros4 = int(input("Número de carros que transitaran por carril 4: "))

carrotransitando = Semaphore(1) #Si un carro transita por el carril 1 o 2, no pueden transitar carros por el carrril 3 o 4 y viseversa.
carroschocados = []#Listas del num. choques

#Semáforos para carros y carriles.
nc = 4
carros1 = 0
carros2 = 0
carros3 = 0
carros4 = 0
eleccion = 0
carriles = Semaphore(nc)
mutexcarril1 = Semaphore(1)
mutexcarril2 = Semaphore(1)
mutexcarril3 = Semaphore(1)
mutexcarril4 = Semaphore(1)
carroschocados = []#Listas del num. choques

def numperdidas():#Función para mostrar los choques totales al termina.
    for i in carroschocados: print(f"\n#ACCIDENTES = Choques ocurridos hasta el momento: {i}")

def Carros1Cruza(id):#Función para que el carro cruze.
    global carros1
    carrotransitando.acquire()
    carrotransitando.release()
    carriles.acquire()
    print(f"\nCarro{id} transitando por su carril().")        
    mutexcarril1.acquire()
    carros1+=1 #Entra un carro de por el carril 1 y avisa que está por cruzar.
    time.sleep(random.random())#Espera
    mutexcarril1.release()
    print(f"Carro{id} termino de transitar por el carril(1).")
    mutexcarril1.acquire()
    carros1-=1 #Se retira la advertencia
    mutexcarril1.release()
    carriles.release()

def CarroCruzeContrario(id):#Función para cruzar o chocar de los carriles contrarios.
    global carros1,carros3,carros4 
    carriles.acquire()
    mutexcarril3.acquire()
    carros3+=1
    if carros3 == 1:
        carrotransitando.acquire()
    mutexcarril3.release()
    print(f"\nUn carro3, el {carriles._value}, está transitando.")
    mutexcarril1.acquire()#Liberamos al mutex del carros3 para avisar que pueden ingresar carros1 y ahora pueden entrar
    if(carros1 > 0):#Si un carro3 transita y un carro1 tambien quiere cruzar
        print(f"\nUn carro1 intentara cruzar ... ¡CHIN! Ya cochocaron 🚑🚑🚑🚑🚑.")
        numperdidas()
        print(f"\n")
        carroschocados.append(id)
    else: print(f"\nAmbos carros cruzaron correto{id}")

    mutexcarril1.release()#No se encuentren ninguno
    mutexcarril3.acquire()
    carros3-=1

    if carros3 == 0:#Si no hay carros liberamos mutexs
        carrotransitando.release()
        mutexcarril3.release()
        carriles.release()

for i in range(numCarros1):#Hilos para carros de carril 1.
    threading.Thread(target=Carros1Cruza, args=[i+1]).start()

for i in range(numCarros3):#Hilos para carros de carril 3.
    threading.Thread(target=CarroCruzeContrario, args=[i+1]).start()

for thread in threading.enumerate():#Enumerar hilos.
    if thread.daemon:
        continue
    try:
        thread.join()
    except RuntimeError as err:
        if 'Error' in err.args[0]:
            continue
        else:
            raise