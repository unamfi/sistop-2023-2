#Programa para resolver el problema de los alumnos y el asesor

#Incluimos las bibliotecas que utilizaremos en nuestro programa
import threading as t
import time
import random

#Definimos el numero de sillas que hay en el cubiculo 
# y de alumnos que pueden entrar (puede variar)
num_Sillas = 5
num_Alum = 8
max_alum = 5
 
#Definimos los semaforos a utilizar

#Semaforo multiplex para sillas a ocupar
cubiculo = t.Semaphore(max_alum)
#Avisar si llegaron alumnos
tocar_Puerta = t.Semaphore(0)
#Semaforo para dudas
dudas = t.Semaphore(0)
#Semaforo pregunta
pregunta = t.Semaphore(1)
#Semaforo para alumnos
alum = t.Semaphore(0)

#Funcion Profesor
def profesor():
    global num_Sillas
    global max_alum
    while True:
        #Aula Vacía
        if num_Sillas == max_alum:
            print("\nNo hay nadie, Profesor se acuesta a dormir la siesta\n")
            time.sleep(0.3)
            break
        
#Funcion Alumno
def alumno(id):
    global num_Sillas
    #tamaño aleatorio de dudas
    numdudas = random.randint(1,3)
    #Entrando...
    cubiculo.acquire()
    print(f"Ha entrado el Alumno {id} con {numdudas} dudas") 
    #desocupa
    num_Sillas -= 1
    time.sleep(0.5)
    #atendiendo dudas
    for i in range(numdudas):
        pregunta.acquire()
        print(f"Atendiendo Alumno {id}...\n")
        time.sleep(0.5)
        #duda respondida
        numdudas = numdudas - 1
        print(f"Duda respondida! del Alumno {id}\n")
        print(f"{numdudas} Dudas restantes del Alumno {id} \n ")
        #Soltamos aumno que pregunto para que demás contesten
        pregunta.release()        
        time.sleep(0.3)
        
    num_Sillas += 1
    cubiculo.release()
        
def main():
    
    t.Thread(target=profesor).start()

    for i in range(num_Alum):
        t.Thread(target=alumno, args=[i]).start()
        
    t.Thread(target=profesor).start()  
main()