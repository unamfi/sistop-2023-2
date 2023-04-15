#!/usr/bin/python3

import threading
import time
import random

capacidad = 3 #Variable para indicar la capacidad del salón
numSillas = 0 #Variable que indica el numero de sillas ocupadas


profesor = threading.Semaphore(0)	#Hilo para el profesor atender dudas 
mutex = threading.Semaphore(1)		#Mutex
duda = threading.Semaphore(0)		#Hilo para realizar una duda/tomar un lugar
alumno= threading.Semaphore(0)		#Hilo para indicar si hay alumnos

def profe ():
	while True:
		print("Profesor 🐺, esperando...")
	
		#Espera a que llegue un alumno
		alumno.acquire()
		#Ya llego un alumno
		print("Ya desperte, estoy listo para resolver dudas")
		profesor.release()
		resuelveDuda()
	
		
def alu (n):
	global numSillas
	flag=0
	print("Alumno",n," creado")
	numDudas= random.randrange(2)+1			#num random de dudas
	print(f"Alu {n}: Tengo {numDudas} dudas")

	while numDudas>0:	
		#Adquirimos el mutex para entrar a la región crítica numSillas
		mutex.acquire()

		#Busca entrar al salon
		if numSillas>=capacidad and flag==0:
			print("Alumno ",n," Toco esperar desde afuera 😴")
			mutex.release()
			duda.acquire()
			numDudas=numDudas-1
			print("Ya puedo entrar a resolver duda, soy alumno",n)	

		#Sigue con dudas, pero ya habíaentrado al salón
		elif flag==1:
			print("Alumno ",n," Toco esperar desde adentro 😁")
			mutex.release()
			duda.acquire()
			numDudas=numDudas-1
			print("Ya puedo decir duda, soy alumno",n)	

		#Ya entro al salón
		else:
			flag=1
			numSillas+=1
			mutex.release()
			
			
		#Se indica que existe un alumno esperando a resolver duda...
		alumno.release()
		#El alumno se agarra al profesor para que le resuelva su duda
		profesor.acquire()
		print(f"Alu {n}: Tengo {numDudas} dudas")

		#Liberamos el lugar del alumno que ya resolvió sus dudas
		duda.release()

	#Quitamos el lugar del alumno que ya resolvió todas sus dudas
	mutex.acquire()
	print("Alumno",n,": ya no tengo dudas. 👻 \n")
	numSillas=numSillas-1
	mutex.release()
	

def resuelveDuda ():
	print("Resolviendo duda de alumno 😎 ")
	time.sleep(0.5)

#Hilo del profe que atiende dudas
profesLobo=threading.Thread(target=profe).start()
""""Se indican el número de alumnos que van a existir para 
querer entrar a tener dudas""" 
for i in range (5):
	threading.Thread(target=alu, args=[i]).start() 

