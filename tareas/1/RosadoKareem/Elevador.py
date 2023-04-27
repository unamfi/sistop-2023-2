import time
import threading
import random

class Elevator:
    def __init__(self, capacity, floors, mutex):
        self.capacity = capacity
        self.floors = floors
        self.current_floor = 1
        self.direction = "up"
        self.passengers = []
        self.running = True
        self.mutex = mutex

    def run(self):
        while self.running:
            # Esperar a que lleguen pasajeros
            while not self.passengers:
                time.sleep(1)

            # El ascensor sube
            self.direction = "up"
            for i in range(1, self.floors + 1):
                self.current_floor = i
                print(f"El ascensor está en el piso {i}")
                time.sleep(1)
                with self.mutex:
                    if i in self.passengers:
                        self.passengers.remove(i)
                        print(f"Las puertas del ascensor se abren en el piso {i}")
                        time.sleep(1)
                        print(f"{self.capacity} pasajeros salen del ascensor")
                        time.sleep(1)
                    if len(self.passengers) == 0:
                        print("El ascensor está vacío")
                        break

            # El ascensor baja
            self.direction = "down"
            for i in range(self.floors, 0, -1):
                self.current_floor = i
                print(f"El ascensor está en el piso {i}")
                time.sleep(1)
                with self.mutex:
                    if i in self.passengers:
                        self.passengers.remove(i)
                        print(f"Las puertas del ascensor se abren en el piso {i}")
                        time.sleep(1)
                        print(f"{self.capacity} pasajeros salen del ascensor")
                        time.sleep(1)
                    if len(self.passengers) == 0:
                        print("El ascensor está vacío")
                        break

    def stop(self):
        self.running = False


class Person:
    def __init__(self, elevator, floors, mutex):
        self.elevator = elevator
        self.floors = floors
        self.current_floor = random.randint(1, floors)
        self.mutex = mutex

    def run(self):
        while True:
            time.sleep(random.randint(1, 5))
            with self.mutex:
                if len(self.elevator.passengers) < self.elevator.capacity:
                    if self.current_floor != self.elevator.current_floor:
                        print(f"Persona llega al piso {self.current_floor}")
                        self.elevator.passengers.append(self.current_floor)
                        print(f"Persona entra en el ascensor en el piso {self.current_floor}")
                    else:
                        print(f"Persona sale del ascensor en el piso {self.current_floor}")
                        break
                else:
                    print(f"El ascensor está lleno, persona espera en el piso {self.current_floor}")
                    break

def main():
    floors = 5
    capacity = 5
    mutex = threading.Lock()

    elevator = Elevator(capacity, floors, mutex)
    elevator_thread = threading.Thread(target=elevator.run)
    elevator_thread.start()

    threads = []
    for i in range(10):
        person = Person(elevator, floors, mutex)
        person_thread = threading.Thread(target=person.run)
        person_thread.start()
        threads.append(person_thread)

    for t in threads:
        t.join()

    time.sleep(5)
    elevator.stop()
    elevator_thread.join()

if __name__ == "__main__":
    main()


