import threading
import time
import random

class Proceso:
    def __init__(self,nombre):
        self.nombre = nombre
        self.prioridad = random.randint(0,4)
        self.tiempo = random.randint(200,400)/1000
        self.numTickets = int(35/(self.prioridad+1))
        self.utilizados = 0
        self.ejecucion = 0

class Loteria:
    listaLoteria = []

    ##Función para agregr un ticket
    @staticmethod
    def agregaTicket(ticket):
        Loteria.listaLoteria.append(ticket)
    
    @staticmethod
    ##Función que sirve para obtener un ticker de manera aleatoria
    def sacaTicket():
        try:
            num = random.randint(0,len(Loteria.listaLoteria)-1)
            dato = Loteria.listaLoteria[num]
            return dato
        except:
            return None

def agregaProcesos(proceso):
    time.sleep(random.randint(0,20)/100)
    for num in range(proceso.numTickets):
        Loteria.agregaTicket(proceso)
    print(f"->Proceso {proceso.nombre} ahora está activo")
    if(len(procesosActivos)== 0 ):
        esperar.release()
    procesosActivos.append(proceso)

    

def ejecutaProcesos():
    global orden, ordenTerminados
    while(True):
        if(len(procesosActivos)> 0):
            for i in range(0,len(Loteria.listaLoteria)):
                try:
                    time.sleep(0.001)
                    boleto = Loteria.sacaTicket()
                    boleto.utilizados += 1
                    boleto.ejecucion += 0.02  
                    orden += boleto.nombre
                    print(f"  ->Proceso {boleto.nombre} ")
                    print(f"    ->Ticket {boleto.utilizados}")
                    if(boleto.ejecucion >= boleto.tiempo):
                        for j in range(boleto.numTickets):
                            Loteria.listaLoteria.remove(boleto)
                        ordenTerminados += boleto.nombre
                        print(f"      ->Proceso {boleto.nombre} termina")
                        procesosActivos.remove(boleto)
                except:
                    pass
        else:
            print("\n\n->En espera de un proceso")
            esperar.acquire()

print("Carga de trabajo a simular por lotería:")
procesosCreados = []
procesosActivos = []
orden = ""
ordenTerminados = ""
totales = [0,0,0,0]
esperar = threading.Semaphore(0)
letras = ['A','B','C','D','E','F','G','H']
for i in range(random.randint(5,8)):
    procesosCreados.append(Proceso(letras[i]))

print("Proceso    Prioridad    NumTickets    Tiempo[S]")
for aux in procesosCreados:
    print("{:>4}{:>12}{:>14}{:>14}".format(aux.nombre,aux.prioridad,aux.numTickets,aux.tiempo))
    totales[0] += aux.numTickets
    totales[1] += aux.tiempo
print("{:>0}{:>22}{:>14}".format("Totales:",totales[0],round(totales[1],3)))

for i in procesosCreados:
    threading.Thread(target=agregaProcesos, args=[i]).start()

threading.Thread(target=ejecutaProcesos).start()

time.sleep(3)
print("\n\n============================")
print("Orden de ejecución de todos los tickets")
print(orden)
print("============================")
print("Listado de como temrinaron los procesos")
print(ordenTerminados)
print("\n\n")
print("Proceso    Prioridad    NumTickets    TicketsUtilizados    Tiempo[S]    TiempoUtilizado[S]")
for aux in procesosCreados:
    print("{:>4}{:>12}{:>14}{:>18}{:>18}{:>18}".format(aux.nombre,aux.prioridad,aux.numTickets,aux.utilizados,aux.tiempo,round(aux.ejecucion,2)))
    totales[2] += aux.utilizados
    totales[3] += aux.ejecucion
print("{:>0}{:>22}{:>18}{:>17}{:>19}".format("Totales:",totales[0],totales[2],round(totales[1],2),round(totales[3],2)))
 
