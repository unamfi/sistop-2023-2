# -*- coding: utf-8 -*-
import threading
import operator
#import time
import random

nomprocess=["A","B","C","D","E","F","G","H"]
semaforo=threading.Semaphore(0)
        
def main():
    global nomprocess, semaforo
    print("Retroalimentación Multinivel:\n")
    print("Inicia ejecución\n")
    
    tamaño=random.randint(5, 8)
    tiempos=[]
    cola=[]
    prio=[]
    procprio={}
    for i in range (0,tamaño):
        cola.append(nomprocess[i]) #se llena la cola con los procesos
        
    semaforo.release()
    print("Procesos:\tPrioridad\n")
    for i in range(0,tamaño):
        a=random.randint(0,4)
        prio.append(a)
        print(str(cola[i])+"\t\t\t\t"+str(a)) #Se imprime el proceso y su prioridad
        
    procprio=dict(zip(nomprocess,prio)) #se hace un diccionario con el nombre y la prioridad del proceso
    listaprio = sorted(procprio.items(), key=operator.itemgetter(1)) #se ordena el diccionario por prioridad
    
    print("\n\n") 
    tiempo=0
    tiempos.append(tiempo)
    for i in range(0,tamaño):
        duracion=random.randint(2, 3) #duración aleatoria de procesos
        tick=0
        semaforo.acquire()
        for j in range(0,duracion):
            print("t= "+str(tiempo)+"\n") #se imprime el tiempo actual
            print(""+str(listaprio[i])+": "+str(tick)+" tick(s)\n") #se imprime el proceso y el tick
            tick+=1
            tiempo+=1
        tiempos.append(tiempo) #se agrega el tiempo de finalización a la lista de tiempos
        semaforo.release()
        
    print("Tabla de ejecución\n")
    print("Proc y prio  Inic.  Fin  T   E   \tP\n")
    for k in range(0,tamaño):
        print("\n")
        c=random.uniform(0, 1)
        inicio=tiempos[k] #se asigna el valor de inicio de proceso
        fin=tiempos[k+1]-1 #se asigna el valor de fin de proceso
        T=fin-inicio #se asigna el valor del tiempo que dura el proceso
        e=T-c #se asigna el valor de tiempo de espera
        E=round(e,3)
        p=T/c #se asigna el valor de tiempo de respuesta
        P=round(p,3)
        print(" "+str(listaprio[k])+"   \t"+str(inicio)+"\t"+str(fin)+" \t "+str(T)+"\t"+str(E)+"\t"+str(P)) #Se imprimen los datos
            
main()