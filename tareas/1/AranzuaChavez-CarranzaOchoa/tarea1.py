#!/usr/bin/python3
from threading import Thread, Semaphore
import random
import time
import os

## Constantes
NUM_ALUMNOS = 4
NUM_SILLAS = 3
TIEMPO_ESPERA = 0.3
PREGUNTAS = 5
buffer = []

aux = 0 

## Semáforos
despertar = Semaphore(0)
señal = Semaphore(1)
impresionSem = Semaphore(1)  #Para la protección de print's
mut_buffer = Semaphore(1)
multiplexAlu =Semaphore(NUM_SILLAS)

def alumno(id):
    global aux
    numPreg = random.randint(1,PREGUNTAS)
    #Considerando el número de preguntas con un inicio de 1 para cada alumno
    var = 1
    with impresionSem:
        print('\t\t\t - - - - Ha entrado el alumno %d' %id)

    while var <= numPreg:
        with impresionSem:
            print(' El alumno %d  tiene %d preguntas' %(id,numPreg))
        #Señalizando para mostrar la disponibilidad del alumno
        señal.acquire()

        #Sección critica para almacenado del alumno y la cantidad de preguntas
        with mut_buffer:
            buffer.append([id,var])

        #Se comunica con el profesor para informar que existen preguntas pendientes
        despertar.release()

        var += 1
        time.sleep(TIEMPO_ESPERA)

    with impresionSem:
        print('\t\t\t Saliendo alumno %d \n' %id)

    #La salida depende del tope de alumnos y la ejecución de estos
    if (NUM_ALUMNOS == id+1):
        print('\t\t\t\t\t\t PROFE DORMIDO SALIENDO')
        #Considerar la salida forzada
        os._exit(0)

def profesor():
    global aux
    while True:
        if (aux==0):
            print('\t\t\t\t\t\t PROFE DORMIDO ENTRANDO')
            aux += 1
            
        else:
            print('\t Profe despierto')
            despertar.acquire()

            #Sección crítica para extraer y responder las preguntas
            with mut_buffer:
                infoPreg = buffer.pop(0)
                contPreg=infoPreg[1]
                print(' Respondiendo la pregunta %d del alumno %d ' % (contPreg, infoPreg[0]))
                time.sleep(TIEMPO_ESPERA)

            #Se notifica que se han respondido N preguntas
            señal.release()

#Por medio de un multiplex generamos la restricción de solo NUM_SILLAS dentro del cúbiculo 
def llamada(id,multiplexAlu):
    multiplexAlu.acquire()
    alumno(id)
    multiplexAlu.release()

#Llamada a 1 hilo de profesor y N hilos de alumnos
Thread(target=profesor,args=[]).start()

for i in range(NUM_ALUMNOS):
    Thread(target=llamada,args=[i,multiplexAlu]).start()