# -*- coding: utf-8 -*-
import threading
import operator
#import time
import random

nomprocess=["A","B","C","D","E","F","G","H"]
semaforo=threading.Semaphore(0)
        
def main():
    global nomprocess, semaforo
    print("Lotería:\n")
    print("Inicia ejecución\n")
    
    tamaño=random.randint(5, 8) #se determina el número de procesos
    tiemposf=[] #lita de tiempos iniciales de cada proceso
    tiemposi=[] #lista de tiempos finales de cada proceso
    cola=[]
    prio=[]
    procprio={}
    for i in range (0,tamaño):
        cola.append(nomprocess[i]) #se llena la cola con los procesos
        
    semaforo.release()
    print("Procesos:\tPrioridad\n")
    for i in range(0,tamaño):
        a=random.randint(80,120)
        prio.append(a)
        print(str(cola[i])+"\t\t\t\t"+str(a)) #Se imprime el proceso y su prioridad
        
    col=[]
    print("\n\n") 
    tiempo=0
    
    for i in range(0,tamaño):
        duracion=random.randint(2, 3) #duración aleatoria de procesos
        tick=random.randint(80,120) #Se eligen los tickets de cada proceso de manera aleatoria
        semaforo.acquire()
        bandera=0
        for j in range(0,duracion):
            print("t= "+str(tiempo)+"\n") #se imprime el tiempo actual
            if(tick==prio[i]):  
                if(j==0):
                    tiemposi.append(tiempo) #se agrega el tiempo en que inicia el proceso
                bandera=1
                print(""+str(cola[i])+": "+str(tick)+" tick(s)\n") #se imprime el proceso y el num de tickets
                if(col[i-1] != cola[i]): #se evita que la lista de procesos ejecutados tenga repeticiones
                    col.append(cola[i])
            elif(tick>prio[i]):
                w=tick-prio[i]
                print(""+str(cola[i])+" recibió: "+str(w)+" tick(s)\n")
                print(""+str(cola[i])+": "+str(tick)+" tick(s)\n")
                col.append(cola[i])
                bandera=1
                if(j==0):
                    tiemposi.append(tiempo)#se agrega el tiempo en que inicia el proceso
            tiempo+=1
        if(bandera==1):
             tiemposf.append(tiempo) #se agrega el tiempo de finalización a la lista de tiempos
        semaforo.release()
    
    time=[]
    
    for i in range(0,len(tiemposi)):
        for j in range(0,len(tiemposf)):
            if(tiemposi[i]==tiemposf[j]-1 or tiemposi[i]-1==tiemposf[j]):
                time.append(tiemposi[i])
    
        
    h=len(col)
    lf=[]
    for i in range(0,h-1): #proceso que evita la repetición en la cola de procesos
        if(i==h-2):
            lf.append(col[i])
        elif(col[i] != col[i+1]):
            lf.append(col[i])
     
    v=len(lf)
    print("Tabla de ejecución\n")
    print("Proc  Inic.  Fin  T   E   \tP\n")
    for k in range(0,v):
        print("\n")
        c=random.uniform(0, 1)
        inicio=tiemposi[k] #se asigna el valor de inicio de proceso
        fin=tiemposf[k]-1 #se asigna el valor de fin de proceso
        T=fin-inicio #se asigna el valor del tiempo que dura el proceso
        e=T-c #se asigna el valor de tiempo de espera
        E=round(e,3)
        p=T/c #se asigna el valor de tiempo de respuesta
        P=round(p,3)
        print(" "+str(lf[k])+"\t\t"+str(inicio)+"  \t"+str(fin)+" \t "+str(T)+"\t"+str(E)+"\t"+str(P)) #Se imprimen los datos
            
main()