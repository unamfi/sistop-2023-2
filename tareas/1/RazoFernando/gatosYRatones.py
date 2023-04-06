import threading
from threading import Semaphore
import random
import time


#Obtengo del usuario los datos requeridos
numGatos = int(input("Ingrese el número de gatos: "))
numRatones = int(input("Ingrese el número de ratones: "))
numPlatos = int(input("Ingrese el número de platos: "))


#Creo los semáforos para que haya gatos y ratones en la habitación
ratones = 0
gatos = 0
mutexRaton = Semaphore(1)
mutexGato = Semaphore(1)
platos = Semaphore(numPlatos)
gatoComiendo = Semaphore(1) #Si un gato está comiendo, un ratón no puede entrar 


#Listas para almacenar los ratones muertos y vivos
ratonesVivos = []
ratonesMuertos = []


#Función para mostrar los ratones vivos y muertos al final del programa
def VivosYMuertos():
    print("\n\n🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭🐭")
    print("Ratones vivos y muertos:")
    print("\nRatones Vivos: ")
    for i in ratonesVivos:
        print(f"Ratón: {i}")
    print("\nRatones Muertos: ")
    for j in ratonesMuertos:
        print(f"Ratón: {j}")


#Función para que el gato coma
def GatoCome(id):
    global gatos
    gatoComiendo.acquire()
    gatoComiendo.release()
    platos.acquire()
    print(f"\nEl gato {id} está comiendo")        
    mutexGato.acquire()
    # Entra un gato y avisa que está presente
    gatos+=1
    time.sleep(random.random()) #Espera
    mutexGato.release()
    print(f"El gato {id} ha terminado de comer")
    mutexGato.acquire()
    gatos-=1
    # Se retira la advertencia
    mutexGato.release()
    platos.release()


#Función para que el ratón coma o se lo coman 
def RatonCome(id):
    global ratones, gatos
    platos.acquire()
    mutexRaton.acquire()
    ratones+=1
    if ratones == 1:
        gatoComiendo.acquire()
    mutexRaton.release()
    print(f"\nEl ratón {platos._value} está comiendo en el plato ")

    # Liberamos al mutex del ratón para avisar que pueden ingresar gatos y ahora los gatos pueden entrar
    mutexGato.acquire()

    # Si un ratón está comiendo y llega un gato
    if(gatos > 0):
        print(f"\nUn gato ha entrado a comer en el plato {platos._value}")
        print(f"\n❌ El gato se ha comido al ratón {id}❌ ")
        ratonesMuertos.append(id)
    else:
        print(f"\nAcabó de comer el ratón {id}")
        ratonesVivos.append(id)

    # En caso que no se encuentren ninguno de los dos
    mutexGato.release()
    mutexRaton.acquire()
    ratones-=1

    # Si no hay ratones por alimentar liberamos los mutex
    if ratones == 0:
        gatoComiendo.release()
        
    mutexRaton.release()
    platos.release()


# Hilos de los gatos
for i in range(numGatos):
    threading.Thread(target=GatoCome, args=[i+1]).start()


# Hilos de los ratones
for i in range(numRatones):
    threading.Thread(target=RatonCome, args=[i+1]).start()


# Esperamos a que el programa termine de enumerar todos los hilos y hasta cuando hagan join se muestra el marcador
for thread in threading.enumerate():
    if thread.daemon:
        continue
    try:
        thread.join()
    except RuntimeError as err:
        if 'cannot join current thread' in err.args[0]:
            continue
        else:
            raise

VivosYMuertos()