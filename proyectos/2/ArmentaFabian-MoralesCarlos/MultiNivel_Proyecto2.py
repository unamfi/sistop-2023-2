#!/usr/bin/python3
import random
from random import randint
from random import sample

duracion=0 		#utilizada para la duracion total
aux=[]			#auxiliar para ordenar la procesos en base a la prioridad
aux2=0			#auxiliar2 para saber cuando se ha terminado un proceso
num_procesos= randint(5,8)
procesos= []
primer_proc = 'A'
res=''
cola=[]
quantum=12
"""
Se Obtienen la lista de procesos (entre 5-8), se le asigna nombre en orden
alfabético, la llegada de A siempre es en 0, pq son el número de procesos que
existen cuando llega, para los demás la llegada es entre 0 e i*10, su duración
varia entre 80 y se asigna de inicio una prioridad de 0
"""
for i in range (num_procesos):
	procesos.append({'nombre':chr(ord(primer_proc)+i), 'llegada': randint(0,10*i), 'duración': randint(80,120), 'prioridad': 0 
	})
#Se obtiene la suma total del número de ticks


#Se imprime la lista de procesos existentes
print("**** Lista de procesos ****")
print("PROCESO LLEGADA DURACION PRIORIDAD")
for proc in procesos:
	print("%2s	%3d	%3d	%2d" % (proc['nombre'], proc['llegada'], proc['duración'], proc['prioridad']))
	duracion+= proc['duración']
print("Total:\t\t %2d"%duracion)


#Se realiza la planificacion
print("\n\n--- Inicio de ejecución ---")
t=0
while(t<(int(duracion))):

	t+=quantum
	for p in sorted(procesos, key=lambda p: p['prioridad']):
		cola.append(p)
		aux= cola.pop(0)
		print("\nLa prioridad más alta es %d del proceso %s "%(aux['prioridad'], aux['nombre']))
		if p['llegada']<= t and p['prioridad']<=aux['prioridad']:
			print("Se realiza Proceso %s" %p['nombre'])
			p['duración']-= quantum
			if(p['duración']<=0):
				aux2= -1 * p['duración']
				res+= p['nombre']*aux2
				res+= '-' *(quantum-aux2)
				print("Proceso %s ha terminado"%p['nombre'])
				print(p['nombre']*quantum + ('-'*(quantum-aux2)))
				procesos.remove(p)
			else:	
				p['prioridad']= p['prioridad']+quantum
				print("Prioridad del proceso %s : %d"% (p['nombre'] ,p['prioridad']))
				res+=p['nombre']*quantum	
				print(p['nombre']*quantum)
			
print("\n\nPlanificación realizada: \n"+res)

	
				
		 
