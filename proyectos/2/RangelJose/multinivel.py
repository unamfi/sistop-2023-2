import threading
import time
import random

class Proceso:
    def __init__(self,nombre):
        self.nombre = nombre
        self.prioridad = random.randint(0,4)
        self.tiempo = random.randint(3,10)
        self.llegada = random.randint(0,15)
        self.numTickets = int(35/(self.prioridad+1))
        self.utilizados = 0
        self.ejecucion = 0
        self.fin = 0
        self.espera =  0

class Loteria:
    listaLoteria = []

    ##Función para agregr un ticket
    @staticmethod
    def agregaTicket(ticket):
        Loteria.listaLoteria.append(ticket)
    
    @staticmethod
    ##Función que sirve para obtener un ticker de manera aleatoria
    def sacaTicket():
        num = random.randint(0,len(Loteria.listaLoteria)-1)
        dato = Loteria.listaLoteria[num]
        return dato

def agregaProcesos(proceso):
    time.sleep(proceso.llegada + 0.01)
    for num in range(proceso.numTickets):
        Loteria.agregaTicket(proceso)
    print(f"  ->Proceso {proceso.nombre} ahora esta activo")
    if(len(procesosActivos)== 0 ):
        esperar.release()
    procesosActivos.append(proceso)

def ejecutaProcesos(totalTime):
    global orden, ordenTerminados, minimo
    tiempoEjecutado = 0
    while(True):
        if(tiempoEjecutado < (totalTime + minimo)):
            for i in range(totalTime + minimo + 1):
                print(f"->t = {i}")
                time.sleep(1)
                tiempoEjecutado +=1
                if(len(procesosActivos) > 0 ):
                    boleto = Loteria.sacaTicket()
                    boleto.utilizados += 1
                    boleto.ejecucion += 1  
                    orden += boleto.nombre
                    print(f"    ->Proceso {boleto.nombre} ")
                    print(f"      ->Ticket {boleto.utilizados}")
                    if(boleto.ejecucion >= boleto.tiempo):
                        for j in range(boleto.numTickets):
                            Loteria.listaLoteria.remove(boleto)
                        boleto.fin = i
                        boleto.espera = (boleto.fin+1 - boleto.llegada - boleto.tiempo)
                        ordenTerminados += boleto.nombre
                        print(f"        ->Proceso {boleto.nombre} termina")
                        procesosActivos.remove(boleto)
        else:
            print("\n\n->En espera de un proceso")
            esperar.acquire()

print("Carga de trabajo a simular por Multinivel:")
procesosCreados = []
procesosActivos = []
orden = ""
ordenTerminados = ""
totales = [0,0,0,0]
esperar = threading.Semaphore(0)
letras = ['A','B','C','D','E','F','G','H']
for i in range(random.randint(5,8)):
    procesosCreados.append(Proceso(letras[i]))

print("Proceso    Prioridad    NumTickets    Tiempo[S]      Llegada")
for aux in procesosCreados:
    print("{:>4}{:>12}{:>14}{:>12}{:>15}".format(aux.nombre,aux.prioridad,aux.numTickets,aux.tiempo,aux.llegada))
    totales[0] += aux.numTickets
    totales[1] += aux.tiempo
print("{:>0}{:>22}{:>12}".format("Totales:",totales[0],totales[1]))
print("\n\n")

minimo = procesosCreados[0].llegada
for i in procesosCreados:
    if(i.llegada < minimo):
        minimo = i.llegada

threading.Thread(target=ejecutaProcesos,args=[totales[1]]).start()

for i in procesosCreados:
    threading.Thread(target=agregaProcesos, args=[i]).start()

time.sleep(totales[1] + minimo + 1)
print("\n\n============================")
print("Orden de ejecución de todos los tickets")
print(orden)
print("============================")
print("Listado de como temrinaron los procesos")
print(ordenTerminados)
print("\n\n")
print("Proceso    Inicio    Fin    T[S]     E[S]     P")
for aux in procesosCreados:
    print("{:>4}{:>11}{:>9}{:>7}{:>9}{:>9}".format(aux.nombre,aux.llegada,aux.fin,(aux.fin - aux.llegada),aux.espera,round((aux.fin - aux.llegada)/aux.tiempo,3)))