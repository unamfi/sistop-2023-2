#Arellano Hernandez Israel -- Elevador

import threading
import random
import time

llamadas_elevador =[]
mutex_llamada = threading.Semaphore(1)
movimiento_elevador = threading.Semaphore(0)

class Persona(threading.Thread): #Clase para las personas del elevador
    def __init__(self, nombre, piso): #!Inicializacion de la clase persona(atributos)
        super().__init__(target = self.llama_elevador, name = nombre)
        self.piso = piso

    def llama_elevador(self): #!llamadas al elevador
            global mutex_llamada, llamadas_elevador, movimiento_elevador
            mutex_llamada.acquire()
            llamadas_elevador.append([self.piso,self.paseo_elevador(),self.getName()])
            mutex_llamada.release()
            movimiento_elevador.release()
            
    def paseo_elevador(self)->int: #!Recorrido del elevador
        if self.piso == 1:#*Se encuentra en el piso mas bajo
            sentido_elevador = 1 #*Por lo tanto estara subiendo
            return random.randint(2,5) #*Del 2 al 5 ya que no tomaremos el primer nivel
        elif self.piso == 5: #*Se encuentra en el piso mas alto
            sentido_elevador = 0 #*Por lo tanto tendra que subir
            return random.randint(1,4) #*Del 2 al 4 para no tomar el ultimo nivel
        else: #*En caso de que este en un piso intermedio
            sentido_elevador = random.randint(0,1)
            if sentido_elevador == 1:
                return random.randint(self.piso+1,5)
            return random.randint(1,self.piso-1)

class Elevador(threading.Thread): #Clase para el manejo del elevador
    __MAXIMA_CAPACIDAD = 5 #*Capacidad maxima de personas que pueden estar en el elevador a la vez
    def __init__(self,piso_minimo,piso_max): #!Inicializacion de la clase elevador (atributos)
        super().__init__(target = self.run, args=[])
        self.piso_actual = piso_minimo #*Piso actual 
        self.__PISO_MINIMO = piso_minimo #*piso mas bajo posible (1)
        self.__PISO_MAX = piso_max #*Piso mas alto posible (5)
        self.mutex_personas = threading.Semaphore(1)
        self.personas_en_elevador = []
    
    def run(self): #!Proceso total del elevador
        global movimiento_elevador, llamadas_elevador, mutex_llamada
        sentido_elevador= None #*Ya que el elevador solo puede ir en 2 sentidos, necesitamos esta variable para ver en que direccion va
        primer_usuario = None #*Variable para registrar que usuario tiene la prioridad
        while True:
            aux = 0
            movimiento_elevador.acquire()
            movimiento_elevador.release()
            for i in self.personas_en_elevador:
                if i[1] == self.piso_actual: #*Si la persona esta por llegar a su piso coloca a que piso desea llegar
                    print(f"🎯 🎯 Persona{i[2]}: desea ir al piso {self.piso_actual}🎯 🎯\n")
            print(f"📌 📌 El elevador se encuentra en el piso {self.piso_actual}📌 📌\n")
            self.mutex_personas.acquire()
            for i in self.personas_en_elevador:#*Si la persona esta en la lista de llamadas y esta en el piso destino entonces
                                               #*Llego a su destino
                if i[1] == self.piso_actual:
                    print("👍 👍 Persona%s: ha llegado a su piso👍 👍\n" % i[2])
                    self.personas_en_elevador.pop(aux)#*Se quita la persona de la lista ya que ya llego a su destino
                    movimiento_elevador.acquire()
                aux = aux+1
            self.mutex_personas.release()
            mutex_llamada.acquire()
            aux = 0
            for i in llamadas_elevador: #*Codigo para detectar que el elevador esta a su maxima capacidad
                if len(self.personas_en_elevador) == self.__MAXIMA_CAPACIDAD:
                    print("***😰 😰 El elevador esta a su maxima capacidad***😰 😰\n")
                    break
                elif self.piso_actual == i[0]:
                    persona_en_elevador = llamadas_elevador.pop(aux)
                    self.personas_en_elevador.append(persona_en_elevador)
                    print(f"🤠 🤠 Persona{persona_en_elevador[2]} entra al elevador🤠 🤠\n")
                aux = aux+1
            mutex_llamada.release()
            #*Movimiento de elevador (sentido al que se dirige dependiendo en que nivel esta)
            if self.piso_actual == self.__PISO_MAX: #*Si esta el piso mayor es claro que tiene que bajar
                sentido_elevador = -1 
            elif self.piso_actual == self.__PISO_MINIMO: #*Si esta el piso menor es claro que tiene que subir
                sentido_elevador = 1 
            elif len(self.personas_en_elevador) != 0: 
                primer_usuario = self.personas_en_elevador[0]
                if primer_usuario[1] - primer_usuario[0] <0:
                    sentido_elevador = -1
                else:
                    sentido_elevador = 1
            print("***⬆⬇ El elevador se esta moviendo⬆⬇***\n")
            time.sleep(1)
            self.piso_actual = self.piso_actual + sentido_elevador

#!Creacion de hilos para las personas que subiran al elevador ademas de los hilos necesarios para manejar los pisos totales.
Elevador(1,5).start()
for i in range(20):
    time.sleep(random.random())
    Persona(i+1,random.randint(1,5)).start()