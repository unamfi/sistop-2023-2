#!/usr/bin/python3
import random
from random import randint
from random import sample
duracion=0
aux=0
num_procesos= randint(5,8)
procesos= []
primer_proc = 'A'
tickets= sample(range(3,18),num_procesos)	#Se obtiene un numero aleatorio para
						#tickets no repetido entre 3-18

"""
Se Obtienen la lista de procesos (entre 5-8), se le asigna nombre en orden
alfabético, la llegada de A siempre es en 0, pq son el número de procesos que
existen cuando llega, para los demás la llegada es entre 0 e i*10, su duración
varia entre 80 y 120 ticks y se le asignan los tickets previamente obtenidos
"""
for i in range (num_procesos):
	procesos.append({'nombre':chr(ord(primer_proc)+i), 'llegada': randint(0,10*i), 'duración': randint(80,120), 'tickets': tickets[i] 
	})
#Se obtiene la suma total del número de ticks
print(duracion)

#Se imprime la lista de procesos existentes
print("**** Lista de procesos ****")
print("PROCESO LLEGADA DURACION TICKETS")
for proc in procesos:
	print("%2s	%3d	%3d	%2d" % (proc['nombre'], proc['llegada'], proc['duración'], proc['tickets']))
	duracion+= proc['duración']
print("Total:\t\t %2d"%duracion)
t=0
res= ''
#quantum elegido
quantum = 25
#A continuación, se va a realizar el proceso de planificar
print("\n--- Inicio de ejecución ---")
for i in range(int(duracion/quantum)+(quantum)):
	if len(tickets)!=0:
		ganador = random.choice(tickets)
		for p in procesos:
     #Verificamos si es ticket ganador
			if ganador == p['tickets']:
				print("\nGano la lotería el boleto %2d" %p['tickets'])
				print("Iniciando ejecucion proceso: %s " %p['nombre'])
				p['duración'] = p['duración'] - quantum
				if(p['duración']<=0):
					aux= -1* p['duración']
				
					res+= p['nombre']*aux
					res+= '-'*(quantum-aux)
					print(p['nombre']*aux + ('-'*(quantum-aux)))
					aux=0
					tickets.remove(ganador)
					print("El proceso %s ha terminada"%p['nombre'])
				else:
					res += p['nombre']*quantum
					print( p['nombre']*quantum)
					
	
print("\n\nPlanificación realizada: \n"+res)








