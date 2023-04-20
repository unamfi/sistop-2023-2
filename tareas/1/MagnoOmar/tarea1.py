#Magno Garcia Omar
#Vamos a realizar (o intentar realizar el problema del alumno y asesor)
import threading
import time
import random

#Una condicion para ayudarnos
profesor = 0

#Para este caso, va a atender solo 5 alumnos.
num_sillas = 5 

#De momento, no hay alumnos
num_alumnos = 0


def durmiendo():
    global profesor
    if (num_alumnos == 0):
        
        profesor = 0
        print("Shhh, el profe anda durmiendo zzzz")
        time.sleep(1)
        
        
def llegando_alumnos():
    global num_sillas
    global num_alumnos
    global profesor
    #Pueden desde no llegar ni un alumno, hasta 10 porque ya es semana de examen
    num_alumnos = random.randrange(0,10)
    print("Toc, toc, hay %d alumnos" % (num_alumnos))
    
    #El profesor debe despertar, hay alumnos por atender, solo y solo si hay al menos 1 alumno
    if num_alumnos != 0:
        profesor = 1
    
def atendiendo_alumnos():
    global profesor
    global num_alumnos
    global num_sillas
    #Si el profe esta despierto, puede atender
    while (profesor == 1):
        #Ahora, atendera mientras haya alumnos
        while (num_alumnos !=0):
            #Que entren los primeros 5 (o 4, o 3... ya entiedes)
            if (num_alumnos > 5):
                num_alumnos = num_alumnos - 5
                alumnos_atendiendo = 5
            else:
                #Si son menos de 5, son los ultimos, por lo que metemos a todos de una vez
                alumnos_atendiendo = num_alumnos
                num_alumnos = 0
            #Usamos un torniquete para atender uno por uno.
            torniquete = threading.Semaphore(0)
            while (alumnos_atendiendo !=0):
                torniquete.release()
                print("Profesor: Cual es tu duda?, alumno de la silla %d" % (alumnos_atendiendo))
                time.sleep(0.5)
                print("Mire, mi duda es bla bla bla....")
                time.sleep(0.5)
                print("Mira, tu solucion es bla bla bla...")
                time.sleep(0.5)
                print("Muchas gracias!!!!!")
                alumnos_atendiendo = alumnos_atendiendo -1
                time.sleep(0.5)
                torniquete.acquire()
            #Fua, terminamos los primeros 5, ahora a atender a otros mas...
        #Vaya dia, ahora toca descansar un poco
    profesor = 0