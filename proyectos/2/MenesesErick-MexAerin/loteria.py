import time
import random

nombres=['A','B','C','D','E','F','G','H']
procesos_creados=[] #lista para poner los procesos creados
loteria=[] #lista para poner a los procesos tantas veces como boletos poseen
num_procesos=random.randint(5,8)

class process:
    def __init__(self,nombre):
        self.nombre = nombre
        self.prioridad = random.randint(0,5)
        self.numboletos = int(50/(self.prioridad+1))
        self.tiempo = random.randint(100,200)/1000
        self.utilizados = 0
        self.ejecucion = 0
        self.primeraPasada = 0

def main():
    for i in range(num_procesos):
        procesos_creados.append(process(nombres[i]))

    print("Carga de trabajo a simular por lotería")
    print("Proceso  Prioridad   #Boletos    Tiempo(s)")

    total1=0

    for i in range(num_procesos):
        total1=procesos_creados[i].tiempo+total1
        print(procesos_creados[i].nombre,"\t",procesos_creados[i].prioridad,"\t\t",procesos_creados[i].numboletos,
            "\t",procesos_creados[i].tiempo)
    print("Total\t\t\t\t",total1)

    for i in procesos_creados:
        for j in range(i.numboletos):
            loteria.append(i)
    
    print("\n")

    orden=""
    while(len(loteria)>0):
        for i in range(0,len(loteria)):
            n = random.randint(0,len(loteria)-1) #escogemos un ganador al azar
            ganador = loteria[n] # ese ganador lo "copiamos" en la variable ganador
            if(ganador.primeraPasada==0):
                print("El proceso ",ganador.nombre," esta activo\n")
                ganador.primeraPasada+=1
            ganador.utilizados += 1
            ganador.ejecucion += 0.02  
            orden += ganador.nombre #concatenacion para saber el orden de los procesos en ejecucion
            print("El proceso ",ganador.nombre," ha utilizado ",ganador.utilizados,"quantums\n")
            if(ganador.ejecucion >= ganador.tiempo): #para poder saber si el proceso ha terminado o no
                for j in range(ganador.numboletos):
                    loteria.remove(ganador) #el proceso termino y se elimina de la lista loteria
                print("El proceso ",ganador.nombre," ha terminado\n")
            if(len(loteria)==0): #todos los procesos han terminado de ejecutarse
                break
    
    
    print("\n")
    print("Orden de ejecucion")
    print(orden)
    print("\n")
    print("Proceso    Prioridad    #Boletos    Quantums    Tiempo(s)    TiempoUtilizado(s)")
    total=0
    for i in procesos_creados:
        total=total+i.ejecucion
        print(i.nombre,"\t\t",i.prioridad,"\t",i.numboletos,"\t\t",i.utilizados,
              "\t\t",i.tiempo,"\t\t",round(i.ejecucion,2))
    print("Total","\t\t\t\t\t\t\t",round(total1,2),"\t\t",round(total,2))


    






main()