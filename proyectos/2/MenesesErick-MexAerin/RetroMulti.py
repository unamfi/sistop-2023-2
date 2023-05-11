import time
import random
#Creacion de listas necesarias y "colas"
nombres=['A','B','C','D','E','F','G','H']
procesos_creados=[]
cola_0=[]
cola_1=[]
cola_2=[]
cola_3=[]
cola_4=[]
#La cantidad de procesos a crear
num_procesos=random.randint(5,8)

class process:
    def __init__(self,nombre):
        self.nombre = nombre
        self.prioridad = 0
        self.tiempo = random.randint(5,8)
        self.llegada = random.randint(1,10) #El tiempo de sistema en el que deberia llegar el proceso
        self.inicio = 0 #El tiempo real en el que llega el proceso al sistema
        self.final = 0#El tiempo de sistema en el que acaba el proceso
        self.utilizados = 0#Variabla para saber cuando debe acabar el proceso
        self.primeraPasada = 0#como su nombre lo dice, una bandera para saber cuando se activa en pantalla

def main():

    for i in range(num_procesos):
        procesos_creados.append(process(nombres[i]))

    print("Carga de trabajo a simular por Retroalimentacion multinivel")
    print("Proceso  Prioridad   Llegada    Tiempo")
    total1=0

    for i in range(num_procesos):
        total1+=procesos_creados[i].tiempo
        print(procesos_creados[i].nombre,"\t",procesos_creados[i].prioridad,"\t\t",procesos_creados[i].llegada,
            "\t",procesos_creados[i].tiempo)
    print("Total\t\t\t\t",total1)

    for i in procesos_creados:
        if i.prioridad==0:
            cola_0.append(i)
        if i.prioridad==1:
            cola_1.append(i)
        if i.prioridad==2:
            cola_2.append(i)
        if i.prioridad==3:
            cola_3.append(i)
        if i.prioridad==4:
            cola_4.append(i)
    t=0
    orden=""
    #Cada n pasadas va a disminuir su prioridad ;)
    #Todo el proceso de la cola 0
    while(len(cola_0)>0):#bucle para esperar a que los procesos lleguen al tiempo de llegada
        for i in cola_0:
            t+=1
            if(t>=i.llegada):#Si el tiempo del sistema coincide con el de la llegada del proceso
                if(i.primeraPasada==0): #Si es la primera ves que pasa
                    print("t: ",t)
                    print("El proceso ",i.nombre," esta activo\n")
                    i.primeraPasada+=1
                    i.inicio=t#Se guarta el valor del tiempo real en el que llego el proceso al sistema
                i.utilizados += 1 #numero de Quantums que ha utilizado
                i.final += 1  #El tiempo en el sistema en que va a acabar el proceso
                orden += i.nombre
                print("Proceso: ",i.nombre," Quantum: ",i.utilizados,"Prioridad: ",i.prioridad,"\n")
                i.prioridad+=1 #Se degrada su prioridad
                if(i.utilizados >= i.tiempo):#Si ya llego al tiempo en que deberia acabar, se quita de la lista sin ponerlo en la siguiente
                    cola_0.remove(i)
                    print("El proceso ",i.nombre," a terminado\n")
                #Se coloca el proceso en la cola de la siguiente prioridad
                cola_0.remove(i)
                cola_1.append(i)
            else:
                print("t: ",t)
                print("Esperando Proceso\n")
        if(len(cola_0)==0):
                break
    #De aqui hasta la cola 3 es basicamente lo mismo    
    while(len(cola_1)>0):
        for i in cola_1:
            t+=1
            if(t>=i.llegada):
                if(i.primeraPasada==0): 
                    print("t: ",t)
                    print("El proceso ",i.nombre," esta activo\n")
                    i.primeraPasada+=1
                i.utilizados += 1 
                i.final = t  
                orden += i.nombre
                print("t: ",t)
                print("Proceso: ",i.nombre," Quantum: ",i.utilizados,"Prioridad: ",i.prioridad,"\n")
                i.prioridad+=1 
                if(i.utilizados >= i.tiempo):
                    cola_1.remove(i)
                    print("El proceso ",i.nombre," a terminado\n")
                cola_1.remove(i)
                cola_2.append(i)
            else:
                print("t: ",t)
                print("Esperando Proceso\n")
        if(len(cola_1)==0):
                break 

    while(len(cola_2)>0):
        for i in cola_2:
            t+=1
            if(t>=i.llegada):
                if(i.primeraPasada==0): 
                    print("t: ",t)
                    print("El proceso ",i.nombre," esta activo\n")
                    i.primeraPasada+=1
                i.utilizados += 1 
                i.final = t 
                orden += i.nombre
                print("t: ",t)
                print("Proceso: ",i.nombre," Quantum: ",i.utilizados,"Prioridad: ",i.prioridad,"\n")
                i.prioridad+=1 
                if(i.utilizados >= i.tiempo):
                    cola_2.remove(i)
                    print("El proceso ",i.nombre," a terminado\n")
                cola_2.remove(i)
                cola_3.append(i)
            else:
                print("t: ",t)
                print("Esperando Proceso\n")
        if(len(cola_2)==0):
                break    
        
    while(len(cola_3)>0):
        for i in cola_3:
            t+=1
            if(t>=i.llegada):
                if(i.primeraPasada==0): 
                    print("t: ",t)
                    print("El proceso ",i.nombre," esta activo\n")
                    i.primeraPasada+=1
                i.utilizados += 1 
                i.final = t  
                orden += i.nombre
                print("t: ",t)
                print("Proceso: ",i.nombre," Quantum: ",i.utilizados,"Prioridad: ",i.prioridad,"\n")
                i.prioridad+=1 
                if(i.utilizados >= i.tiempo):
                    cola_3.remove(i)
                    print("El proceso ",i.nombre," a terminado\n")
                cola_3.remove(i)
                cola_4.append(i)
            else:
                print("t: ",t)
                print("Esperando Proceso\n")
        if(len(cola_3)==0):
                break    
    
    #Para la cola 4, ya que es la ultima, solo se sacan los procesos de la cola si estos ya acabaron
    while(len(cola_4)>0):
        for i in cola_4:
            t+=1
            if(t>=i.llegada):
                if(i.primeraPasada==0): 
                    print("t: ",t)
                    print("El proceso ",i.nombre," esta activo\n")
                    i.primeraPasada+=1
                i.utilizados += 1 
                i.final = t 
                orden += i.nombre
                print("t: ",t)
                print("Proceso: ",i.nombre," Quantum: ",i.utilizados,"Prioridad: ",i.prioridad,"\n")
                if(i.utilizados >= i.tiempo):
                    cola_4.remove(i)
                    print("El proceso ",i.nombre," a terminado\n")
            else:
                print("t: ",t)
                print("Esperando Proceso\n")
        if(len(cola_4)==0):
                break    
    
    #El mismo sistema de impresion que en el de loteria solo que con otros atributos
    #para obtener T es final-inicio ya que es el tiempo total del sistema en que tardo en acabar el proceso
    #para obtener E es T-tiempo ya que es el tiempo que tardo realmente el proceso en acabar
    print("\n")
    print("Orden de ejecucion")
    print(orden)
    print("\n")
    print("Proceso    Prioridad     llegada    Tiempo    inicio    final    T       E")
    for i in procesos_creados:
        print(i.nombre,"\t\t",i.prioridad,"\t",i.llegada,"\t\t",i.tiempo,
              "\t",i.inicio,"\t",i.final,"\t",i.final-i.inicio,"\t",(i.final-i.inicio)-i.tiempo,)


main()