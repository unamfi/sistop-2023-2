import threading
import random
from time import sleep


class Alumno(threading.Thread):
    def __init__(self, origin_floor, destination_floor, elevator, id):
        threading.Thread.__init__(self)
        self.origin_floor = origin_floor
        self.destination_floor = destination_floor
        self.elevator = elevator
        self.id = id

    def run(self):
        # Espera activa
        # Esperar a que el elevador llegue al piso en donde se encuentre el alumno
        while True:
            # Adquirir permiso para acceder al recurso compartido (capacidad actual del elevador)
            self.elevator.mutex.acquire()
            # Checar si el elevador esta en el piso y hay espacio para entrar
            if (self.elevator.current_floor == self.origin_floor) and (self.elevator.actualCapacity < self.elevator.capacity):
                self.elevator.actualCapacity += 1  # Entrar en el elevador
                print(f"\nAlumno {self.id} entró en el elevador")
                self.elevator.mutex.release()  # devolver el permiso para que pueda entrar otro alumno
                break
            else:
                self.elevator.mutex.release()  # devolver el permiso si el alumno no entre

        # Espera activa
        # Esperar a que el elevador llegue al piso destino del alumno
        while True:
            if self.elevator.current_floor == self.destination_floor:
                self.elevator.mutex.acquire()  # Adquirir permiso
                self.elevator.actualCapacity -= 1  # Salir del elevador
                print(f"\nAlumno {self.id} salió del elevador")
                # Registrar que se dejo un alumno más para saber cuando se hayan ido todos los alumnos
                self.elevator.dropped += 1
                self.elevator.mutex.release()  # devolver permiso
                break


class System(threading.Thread):
    def __init__(self, num_alumnos):
        threading.Thread.__init__(self)
        self.current_floor = 1
        self.floors = [[], [], [], [], []]
        self.direction = 1  # 1: up, 0: down
        self.capacity = 5
        self.mutex = threading.Lock()  # mutex para controlar acceso al elevador por alumnos
        self.actualCapacity = 0
        self.dropped = 0
        self.num_alumnos = num_alumnos

    def run(self):

        while True:
            sleep(1)

            self.mutex.acquire()  # Pedir permiso para que el elevador no se mueva mientras un alumno quiere entrar
            # Cambio de dirección de movimiento al llegar a los pisos extremos
            if self.current_floor == 1:
                self.direction = 1

            elif self.current_floor == 5:
                self.direction = 0

            # Mover hacia arriba o hacia abajo según la dirección
            if self.direction == 1:
                self.current_floor += 1
                print(f"El elevador se movio al piso {self.current_floor} (Cantidad actual: {self.actualCapacity})")

            elif self.direction == 0:
                self.current_floor -= 1
                print(f"El elevador se movio al piso {self.current_floor} (Cantidad actual: {self.actualCapacity})")

            self.mutex.release()  # devolver el permiso

            # Terminar ejecución al dejar todos los alumnos
            if self.dropped == self.num_alumnos:
                break


num = random.randint(10, 15)  # generamos el número de alumnos aleatorio
print(f"Hay {num} alumnos")

my_elevator = System(num)  # Crear instancia del elevador

# Crear y colocar los alumnos en pisos aleatorios
for i in range(num):
    randfloor = random.randint(1, 5)  # Queremos saber en donde colocar al alumno
    rand_dest = random.randint(1, 5)  # Queremos saber el destino

    while rand_dest == randfloor:  # Evitamos que el origen sea igual al destino
        rand_dest = random.randint(1, 5)

    thread = Alumno(randfloor, rand_dest, my_elevator, i + 1)  # Crear el alumno
    my_elevator.floors[randfloor-1].append(thread)  # Agregar al piso

# Mostrar donde se encuentran los alumnos y a donde van
for i in range(5):
    print(f"\n ******* Piso {i + 1} *********")

    if len(my_elevator.floors[i]) == 0:
        print("No hay nadie esperando el elevador en este piso")
        continue

    print("+-------+------------+-------------+")
    print("|{:^7}|{:^12}|{:^13}|".format("Alumno", "Piso origen", "Piso destino"))
    print("+-------+------------+-------------+")
    for l in my_elevator.floors[i]:
        print("|{:^7}|{:^12}|{:^13}|".format(l.id, l.origin_floor, l.destination_floor))
        print("+-------+------------+-------------+")

print("El elevador esta en el piso 1")
for i in range(5):
    for thread in my_elevator.floors[i]:
        thread.start()

my_elevator.start()  # Empezar a mover el elevador
