import threading
import time
import random

#!EN ESTE PROGRAMA NO ES POSIBLE QUE MAS DE 5 PERSONAS ENTREN AL ELEVADOR, AUNQUE NO NOTIFIQUE EL PROGRAMA QUE ESTA LLENO
#!NO ES POSIBLE QUE SUBAN MAS DE 5 POR COMO ESTA EHCHO EL CODIGO
class Elevador(threading.Thread): #!ATRIBUTOS PARA EL ELEVADOR
    def __init__(self):
        threading.Thread.__init__(self)
        self.piso_actual = 1
        self.direccion = "subiendo"
        self.max_capacidad = 5
        self.capacidad_actual = 0
        self.paradas = set()
        self.condicion = threading.Condition()

    def run(self): #Logica del elevador
        while True:
            self.condicion.acquire() 
            while not self.paradas: #*Si no hay paradas, esperamos
                self.condicion.wait()
            self.mueve_elevador() #*Cuando haya paradas movemos el elevador
            self.condicion.release()

    def mueve_elevador(self): #Se encarga de actualizar el piso actual, la dirección y observar las paradas. 
        hay_paradas = any(piso > self.piso_actual for piso in self.paradas) if self.direccion == "subiendo" else any(piso < self.piso_actual for piso in self.paradas)
        if self.direccion == "subiendo":
            self.piso_actual += 1
            if self.piso_actual == 5 or (self.piso_actual == 1 and not hay_paradas):
                self.direccion = "bajando"
        elif self.direccion == "bajando":
            self.piso_actual -= 1
            if self.piso_actual == 1 or (self.piso_actual == 5 and not hay_paradas):
                self.direccion = "subiendo"
        self.observa_paradas()

    def observa_paradas(self): #Paradas en el elevador
        if self.piso_actual in self.paradas: #*si el piso actual esta en la lista de pisos por hacer una parada
            self.puertas_abiertas() #*Se abren las puertas
            self.paradas.remove(self.piso_actual) #*se remueve el piso actual

    def puertas_abiertas(self): #Movimiento de las puertas
        print(f"🤠 🤠 El ascensor abre las puertas en el piso {self.piso_actual}🤠 🤠\n")
        time.sleep(2)
        self.capacidad_actual = 0
        print(f"🤠 🤠 El ascensor cierra las puertas en el piso {self.piso_actual}🤠 🤠\n")

class Persona(threading.Thread): #!ATRIBUTOS PARA LA PERSONA
    def __init__(self, name, piso_actual, piso_destino, elevador):
        threading.Thread.__init__(self)
        self.name = name
        self.piso_actual = piso_actual
        self.piso_destino = piso_destino
        self.elevador = elevador

    def run(self):  #Corre clase de persona
        self.llama_elevador()
        self.paseo_elevador()
        print(f"👍 👍 {self.name} ha llegado al piso {self.piso_destino}👍 👍\n")
        #self.espera()

    #def espera(self): #*Espera a que el elevador sea notificado para subir hacia una persona
        #while self.elevador.piso_actual != self.piso_destino or self.elevador.capacidad_actual != 0:
        #    time.sleep(1)
        #self.elevador.condicion.acquire()
        #self.elevador.condicion.notify()
        #self.elevador.condicion.release()

    def llama_elevador(self): #llamada del elevador
        self.elevador.condicion.acquire()
        self.elevador.paradas.add(self.piso_actual)
        self.elevador.condicion.notify() #*Notifica en que piso esta
        self.elevador.condicion.release()

    def paseo_elevador(self): #Paseo total del elevador
        while self.elevador.piso_actual != self.piso_actual:
            time.sleep(1)
        self.elevador.condicion.acquire() #En este codigo no es posible que mas de 5 personas suban al elevador
        while self.elevador.capacidad_actual == self.elevador.max_capacidad or \
            (self.elevador.direccion == "subiendo" and self.piso_destino < self.elevador.piso_actual) or \
            (self.elevador.direccion == "bajando" and self.piso_destino > self.elevador.piso_actual):
            self.elevador.condicion.wait()
        self.elevador.capacidad_actual += 1
        print(f" ➡ ⬅{self.name} entra al ascensor en el piso {self.piso_actual}➡ ⬅\n")
        self.elevador.paradas.add(self.piso_destino)
        print(f"🎯 🎯 {self.name} desea ir al piso {self.piso_destino}🎯 🎯\n")
        self.elevador.condicion.notify()
        self.elevador.condicion.release()
        while self.elevador.piso_actual != self.piso_destino:
            time.sleep(1)
        print(f" ⬅ ➡{self.name} sale del ascensor en el piso {self.piso_destino}⬅ ➡\n")

if __name__ == "__main__": #Creacion de hilos
    elevador = Elevador()
    elevador.start()
    for i in range(20):
        piso_actual = random.randint(1, 5)
        piso_destino = random.randint(1, 5)
        while piso_actual == piso_destino:
            piso_destino = random.randint(1, 5)
        person = Persona(f"Persona {i+1}", piso_actual, piso_destino, elevador)
        person.start()

