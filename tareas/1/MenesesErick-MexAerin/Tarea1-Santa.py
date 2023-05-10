import threading
import time
import random

renoSema= threading.Semaphore(0)
santaSema= threading.Semaphore(0)
elfoSema= threading.Semaphore(0)
elfosSema=threading.Semaphore(3)#Semaforo que actua de barrera para hacer grupos de 3 en 3 hilos elfos
mutexR = threading.Semaphore(1)#Mutex para proteger el contador de los renos
mutexE = threading.Semaphore(1)#Mutex para proteger el contador de los elfos
elfos=0  #variable compartida entre los hilos santa y elfos (es un contador)
renos=0 #variable compartida entre los hilos santa y renos (es un contador)
renostot=9#El mismo nombre lo dice, variable que limita la cantidad de renos
grupoElfos=3#variable que limita el grupo de elfos que pasan por ronda (cada 3)

#La funcion santa, el encargado de ir liberando a los elfos o renos al momento de la condicion dada
def Santa():
    global elfos,renos
    print("Santa: estoy cansado")
    print("Santa: Voy ir a dormir")
    while True:
        santaSema.acquire()
        print("Santa: Ya DESPERTE")
        if renos==renostot:
            print("Santa sale a repartir jueguetes")
            renos=0
            for i in range(renostot):
                renoSema.release()

        elif elfos==grupoElfos:
            elfos=0
            print("Santa:Cual es el problema?")
            for i in range(grupoElfos):
                elfosSema.release()
            for i in range(grupoElfos):
                elfoSema.release()

#Funcion de los renos que despertara a santo cuando se reunan los 9 renos
def Renos(n):
    global renos
    while True:
        time.sleep(random.randint(3,5))
        mutexR.acquire()
        renos+=1
        if renos==renostot:
            print("El reno",n,"Llego de vacaciones T_T y despertó a santa")
            santaSema.release()
        else:
            print("El reno",n,"Llego de vacaciones T_T")
        mutexR.release()
        renoSema.acquire()
        print("El reno ",n,"se va de vacas ;)" )

#Funcion de los elfos que van a ir despertando a santo en grupos de 3 en 3
def Elfos(n):
    global elfos
    while True:
        time.sleep(random.randint(3,5))
        elfosSema.acquire()#Deja pasar al tamaña necesario del grupo(3)
        mutexE.acquire()
        elfos+=1
        if elfos<3:
            print("El elfo ",n,"tiene una duda  o_O")
        elif elfos==grupoElfos:
            print("El elfo ",n,"tiene una duda o_O y despierta a santa")
            santaSema.release()
        mutexE.release()
        elfoSema.acquire()
        print("Santa ayuda al elfo ",n, "^_^")

#Funcion para crear elfos infitos
def lanza_elfos():
    num = 1
    while True:
        threading.Thread(target=Elfos, args=[num]).start()
        time.sleep(0.5)
        num += 1

threading.Thread(target=Santa).start()
for i in range(9):
    threading.Thread(target=Renos,args=[i+1]).start()
    time.sleep(0.5)
threading.Thread(target=lanza_elfos).start()