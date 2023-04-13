from threading import Semaphore, Thread
from time import sleep
from random import random, choice

multiplex = Semaphore(5) #creación del limite para estudiantes
pisos =[0,1,2,3,4]
colas = {}
for i in pisos:
	colas[i] = Semaphore(0)

# para iniciar el elevador
def elevador():
	p_actual = 0
	direccion = True # true = arriba, false = abajo
	while True:
		p_previo = p_actual #en donde esta
		sleep(0.5)# una espera
		if direccion:
			if p_actual < pisos[-1]:
				p_actual += 1
			else:
				direccion = False
		else:
			if p_actual > pisos[0]:
				p_actual -= 1
			else:
				direccion = True
		print('Elevador desde el piso : %d al piso: %d' % (p_previo, p_actual))

def alumno (num):
	hacia = choice(pisos)
	desde = choice(pisos)
	print('Alumno %d quiere ir de %d a %d' % (num, desde, hacia))
	if desde == hacia:
		print('Estoy donde quiero estar')
		return True #nada que hacer
	print('Alumno %d: Me pondré en la cola %d'%(num,desde))
	colas[desde].acquire()
	

def subir_elevador():
	multiplex.acquire()

def najar_elevador():
	multiplex.release()

Thread(target=elevador).start()

numero=0
while True:
	numero+=1
	Thread(target=alumno, args=[numero]).start()
	sleep(1)