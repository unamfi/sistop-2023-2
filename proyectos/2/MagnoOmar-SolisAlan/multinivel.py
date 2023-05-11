#Proyecto 2 de Sistemas Operativos: Planificación por Retroalimentación Multinivel
#Magno García Omar
#Solis González Alan David

import random as rand

print("¡¡Llegan los procesos!! 🥳🥳")

rand.seed(24)

process = []
first_proc = 'A'

for i in range(rand.randint(4,8)):
    # Genero los 4 a 8 procesos aleatorios
    process.append({'nombre': chr( ord(first_proc)+i ),
                     'llegada': rand.randint(0, 10*i),
                     'duracion': rand.randint(4,10),
                     'avance': 1,
                     'ejecuciones': 0
                     })

print('Lista de procesos:\n\n')
print("Nombre   Llegada   Duracion ")
for proc in process:
    print(" %2s      %3d       %3d" % (proc['nombre'], proc['llegada'], proc['duracion']))

# Parametros del algoritmo
n = 2
Q = n + 1
tick = 0

llegadas = []
duracion = []
total = 0
for p in process:
    llegadas.append(p['llegada'])
    duracion.append(p['duracion'])
total = max(llegadas) + max(duracion) + 1
    
# Como la duración máxima es de 10 ticks, y cada Quantum da 3 ticks
# se tiene que se necesitan a lo mucho 4 colas

queue_0 = []
queue_1 = []
queue_2 = []
queue_3 = []
empty_string = ''

print("\n\nInicia la ejecución")
while tick != total:
    print("t=", tick)
    for proc in process:
        if tick == proc['llegada']:         #Comprueba si ya llego el proceso
            print("⇒", proc['nombre'])
            queue_0.append(proc)            #El proceso nuevo lo agrega a la cola con prioridad 0
            process.remove(proc)

    for proc in queue_0:
        proc['duracion'] -= 1               #Se le resta la duración del proceso en 1
        if proc['duracion'] == 0:           #Si se acabo el proceso significa que se elimina de la cola
            print(proc['nombre'], "👍")
            print("\n🟢🟢 Proceso", proc['nombre'], "completado 🟢🟢\n")
            empty_string += proc['nombre']  #Se agrega a la lista de planificacion
            queue_0.pop(0)
            break
        else:
            print(proc['nombre'], ": prio: 0")
            print("⌚:", proc['nombre'], ":", proc['avance'], "tick")
            empty_string += proc['nombre']
            proc['avance'] += 1                 #Se notifica que su avance aumento en 1
            if proc['avance'] ==  Q:            #Si el avance es 2 veces el quantum se considera una ejecución
                proc['avance'] -= 5             #Se reestablece el avance a su valor default
                proc['ejecuciones'] += 1        #Las veces que se ha ejecutado el proceso aumenta en 1
                if proc['ejecuciones'] == n:    #Si las ejecuciones son igual al parametro dado, se mueve de cola de prioridad
                    queue_1.append(queue_0.pop())

                                                #El proceso anterior se repite  
    for proc in queue_1:
        proc['duracion'] -= 1
        if proc['duracion'] == 0:
            print(proc['nombre'], "👍")
            print("\n🟢🟢 Proceso", proc['nombre'], "completado 🟢🟢\n")
            empty_string += proc['nombre']
            queue_1.pop(0)
            break
        else:
            print(proc['nombre'], ": prio: 1")
            print("⌚:", proc['nombre'], ":", proc['avance'], "tick")
            empty_string += proc['nombre']
            proc['avance'] += 1
            if proc['avance'] == Q:
                proc['avance'] -= 5
                proc['ejecuciones'] += 1
                if proc['ejecuciones'] == n:
                    queue_2.append(queue_1.pop())


    for proc in queue_2:
        proc['duracion'] -= 1
        if proc['duracion'] == 0:
            print(proc['nombre'], "👍")
            print("\n🟢🟢 Proceso", proc['nombre'], "completado 🟢🟢\n")
            empty_string += proc['nombre']
            queue_2.pop(0)
            break
        else:
            print(proc['nombre'], ": prio: 2")
            print("⌚:", proc['nombre'], ":", proc['avance'], "tick")
            empty_string += proc['nombre']
            proc['avance'] += 1
            if proc['avance'] == Q:
                proc['avance'] -= 5
                proc['ejecuciones'] += 1
                if proc['ejecuciones'] == n:
                    queue_3.append(queue_2.pop())


    for proc in queue_3:
        proc['duracion'] -= 1
        if proc['duracion'] == 0:
            print(proc['nombre'], "👍")
            print("\n🟢🟢 Proceso", proc['nombre'], "completado 🟢🟢\n")
            empty_string += proc['nombre']
            queue_3.pop(0)
            break
        else:
            print(proc['nombre'], ": prio: 3")
            print("⌚:", proc['nombre'], ":", proc['avance'], "tick")
            empty_string += proc['nombre']
            proc['avance'] += 1
            if proc['avance'] == Q:
                proc['avance'] -= 5
                proc['ejecuciones'] += 1

    tick += 1
print("Planificación realizada:", empty_string)
