import threading
from threading import Semaphore, Thread
from time import sleep
import time
import random 
bol=Semaphore(1)
lot=Semaphore(1)
numB=20
bolR=[]
quantum=28
j=0
k=0
max=0
loto=0
def process(id): #definición del hilo proceso 
    global j, bol,k,max, bolR,loto
    bole=[] #arreglo de los números de boletos de lotería
    temp=random.randint(85,120) #Se le asigna un tiempo de 85-120 ticks
    print("El proceso %d " %id, "tiene %d tiempo de procesamiento"% temp,)
    with bol: #mutex que asigna los números de cada boleto
        for i in range(0,8-j):#Se asignan en orden porque me dió flojera que fueran aleatorios
                bole.append(k+i)
        for i in bole:
            bolR.append(i)# Arreglo del cual el scheduler eligirá el número ganador 
        j=j+1 #Hago que la cantidad de boletos sea cada vez menor de forma que el primer proceso tiene más prioridad pero puedo cambiar eso según se nos pida
        k=bole[8-j]# El número donde termino el arreglo anterior 
        max=k+i# Se asigna el número máximo que tienen los boletos hasta ahora 
    while temp>0: #mientras siga teniendo tiempo de procesamiento
         with lot: #mutex para saber si se ganó la lotería
             if loto in bole:# Si ganó la lotería
                print("Proceso %d ha ganado" %id, "continuará su ejecución") 
                temp=temp-quantum #continua su ejecución un quantum y su tiempo se va acabando
                time.sleep(2) #Duerme 2 segundos simulando que hace algo
                if (temp>0):#si el proceso no ha acabado
                    print("Al proceso %d"%id, "Le queda %d" %temp) #imprime el tiempo restante del proceso
                else:
                    print("El proceso %d terminó" %id)
                    for i in bole:
                         bolR.remove(i) #quita los números que tenía de lotería del arreglo de números aleatorio
                if len(bolR)==0:#Si ya no hay más procesos
                    print("Los procesos se han acabado")
                else:
                    f=random.randint(0,len(bolR)-1)#Elije el nuevo número de lotería ganador
                    loto=bolR[f]

def lanza_process(): #Esta funcioón crea los hilos que serán los procesos
    a=random.randint(5,8) # Pueden ser de 5-8 procesos
    b=random.uniform(0,3) # Pueden aparecer cada 0 a 3 segundos
    num = 0
    while num<a:
        threading.Thread(target=process, args=[num]).start()
        print("El proceso %d ha sido creado" %num )
        time.sleep(b)
        num += 1

threading.Thread(target=lanza_process).start()#inicia todo

    
            
