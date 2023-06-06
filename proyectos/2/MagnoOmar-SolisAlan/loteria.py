#Proyecto 2 de Sistemas Operativos: Planificación por lotería
#Magno García Omar
#Solis González Alan David

from random import randint
import time
import random
#Vamos a comenzar a generar nuestros procesos candidatos.

#random.seed(24)

print("A continuación, mostraremos los procesos que participarán en la lotería!! 🥳🥳")
time.sleep(1)

process = []
first_proc = 'A'
lowest_ticket = 1
limit_tickets = 30
# La cantidad de tickets que puede sacar cada proceso varia entre 1 y 30 tickets
ticket_counter = 0

for i in range (randint(4,8)):
    #Se generan los tickets par cada proceso
    proc_tickets = randint(lowest_ticket, limit_tickets)

    #Despues de esto, se deben calcular el numero de Tickets totales:
    ticket_counter += proc_tickets

    proc = {'Nombre': chr( ord(first_proc)+i ),
        'Llegada' : randint(0,10*i),
        'Duracion': randint(4,10),
        'Tickets': proc_tickets, #Cada proceso podra tener hasta 30 tickets
        'Max_Num_ticket': ticket_counter #Es el número de ticket máximo que le corresponde al proceso
       }
    process.append(proc)
    
#Muy bien, ya se han generado todos los procesos, es tiempo de mostrarlos
print("| Nombre | Llegada | Duracion | Tickets |Tick Max|")
for proc in process:
    print("|  %2s    |  %3d    |  %3d     |  %3d    |  %3d   |" % (proc['Nombre'],
    proc['Llegada'], proc['Duracion'], proc['Tickets'], proc['Max_Num_ticket']))

print("\nEl total de tickets es... %d" % ticket_counter)
print("\nAhora... Comienza la loteria!!!")
time.sleep(1)

#Si el proceso resulta ganador, se le concederá 1 tick de uso de CPU para
#Procesarse, terminado el tiempo, se vuelve a sortear 
current_time = 0
tick_count = 0
History_Process = ''

while process.__len__() != 0:
    # Seleccionar un billete al azar
    ticket = randint(lowest_ticket, ticket_counter)
    # Encontrar el proceso correspondiente al billete seleccionado
    for proc in process:
        if ticket <= proc['Max_Num_ticket']:
            if ticket > proc['Max_Num_ticket']-proc['Tickets']:
                # Ahora se ejecuta el proceso por cada tick
                print("❗❗Ticket ganador❗❗: %d" %ticket, "Pertenece al Proceso:", proc['Nombre'])
                time.sleep(0.2)
                print("Proceso", proc['Nombre'], "en ejecución durante 1 Tick")
                time.sleep(0.2)
                tick_count += 1
                print("Ticks hasta el momento: ", tick_count)
                History_Process += proc['Nombre']
                proc['Duracion'] -= 1
                current_time += 1
                # ¿Ya terminó el proceso? Que bien, ahora debemos retirarlo de la lista
                if proc['Duracion'] == 0:
                    print("\n🟡🟡 Proceso", proc['Nombre'], "completado, puede retirarse 🟡🟡\n")
                    process.remove(proc)
                break

#Una vez se completan todos los procesos, se imprime la lista de planificación
            
print("Todos los procesos han sido completados.")
print("Duracion Total:", tick_count )
print("Planificacion Realizada: " + History_Process)