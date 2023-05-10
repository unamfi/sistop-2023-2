import threading
import random
import time

class Alumno:
    def __init__(self,alumno_id,num_preguntas):
        self.alumno_id = alumno_id
        self.num_preguntas = num_preguntas
        self.contestadas = 0
        
class Respuesta:
    def __init__(self, alumno_id, pregunta_id):
        self.alumno_id = alumno_id
        self.pregunta_id = pregunta_id

def alumno(num):
    num_preguntas = random.randint(1,5)
    lista_alumnos.append(Alumno(i,num_preguntas))
    time.sleep(random.randint(0,15))
    sillas_libres.acquire()
    print("El alumno %d entra al salon con %d dudas" %(num, num_preguntas))
    while(num_preguntas > 0):
        orden_preguntas.append(Respuesta(num,num_preguntas))
        mutex_profesor.acquire()
        if (sillas_libres._value == num_sillas-1):
            dormir.release()
        mutex_profesor.release()
        num_preguntas -=1

def pregunta(respuesta):
    print("El profesor responde la pregunta %d del alumno %d" %(respuesta.pregunta_id, respuesta.alumno_id))
    time.sleep(1)
    print("Duda %d del alumno %d resuelta" %(respuesta.pregunta_id, respuesta.alumno_id))
    al= "" 
    for i in lista_alumnos:
        if i.alumno_id == respuesta.alumno_id:
            al = i
            al.contestadas +=1
    if(al.contestadas == al.num_preguntas):
        sillas_libres.release()
        print("Todas las dudas del alumno %d han sido resueltas y sale del salon" % al.alumno_id)


def profesor():
    while (True):
        if(len(orden_preguntas) > 0):
            index = random.randint(0,len(orden_preguntas)-1)
            pareja = orden_preguntas.pop(index)
            pregunta(pareja)
        else:
            print("El profesor está durmiendo")
            dormir.acquire()
            print("El profesor empieza a resolver dudas")

#Número máximo de alumnos
num_alumnos = random.randint(0,35)

#Númerp máximo de sillas
num_sillas = random.randint(10,20)
mutex_profesor = threading.Semaphore(1)
sillas_libres = threading.Semaphore(num_sillas)
dormir = threading.Semaphore(0)

#lista para ordenar las dudas que le hacen al profesor.
#Se ingresa tanto el alumno que hace la duda como el número de duda
orden_preguntas = []

#lista para guardar a todos los alumnos
#Se guarda su identificardor, el todal de preguntal y las preguntas actuales que ha resuelto el profesor.
lista_alumnos = []

print("Alumnos totales = %d" %num_alumnos)
print("Sillas  totales = %d" %num_sillas)
print("\n\n==============================\n\n")

threading.Thread(target=profesor).start()

for i in range(num_alumnos):
    threading.Thread(target = alumno, args =[i]).start()