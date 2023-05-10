#Organista Alvarez Ricardo

import threading
import time
import random

numero_de_sillas = 2
numero_de_alumnos_esperando = 10
me_puedo_dormir = numero_de_sillas

sillas = threading.Semaphore(numero_de_sillas)
preguntando = threading.Semaphore(1)

def profesor():
    global me_puedo_dormir
    global numero_de_sillas
    while True:
        if me_puedo_dormir == numero_de_sillas:
            print("P: No hay nadie aqui...")
            print("P: *Echando la siesta*")
            time.sleep(0.5)

def preguntar(id, pregunta): #Los alumnos hacen su pregunta
    print("%d: Haciendo mi pregunta #%d..." % (id,pregunta))
    time.sleep(0.3)
    print("%d: Escuchando la respuesta..." % id)
    time.sleep(0.3)
    print("%d: Mi pregunta fue respondida." % id)

def alumno(id):
    global me_puedo_dormir
    #time.sleep(2)
    sillas.acquire() #Entran cierto numero de alumnos al cubiculo
    me_puedo_dormir -= 1
    print("\n%d: Entre al cubiculo." % id)
    time.sleep(0.5)
    for i in range(random.randint(1,4)): #Hay un numero X de preguntas que el alumno hara
        preguntando.acquire() #Toma su turno para preguntar
        preguntar(id, i) #Hace una pregunta
        preguntando.release() #Deja a los demas hacer una pregunta mientras escribe
        time.sleep(0.5)
    me_puedo_dormir += 1
    sillas.release()

threading.Thread(target=profesor).start()

for i in range(numero_de_alumnos_esperando):
    threading.Thread(target=alumno, args=[i]).start()
    