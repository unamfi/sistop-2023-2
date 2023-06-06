#Ramirez Medina Daniel

import threading
import time

MAX_PERSONAS = 4

semHackers = threading.Semaphore(MAX_PERSONAS)
semSefrs = threading.Semaphore(MAX_PERSONAS)

def cruzar(bando):
    if bando == "Hackers":
        semHackers.acquire()
        print("Hachers cruzando el río...")
        time.sleep(2)
        print("Hackers ha cruzado el río.")
        semHackers.release()
    elif bando == "Serfs":
        semSefrs.acquire()
        print("Serfs cruzando el río...")
        time.sleep(2)
        print("Serfs ha cruzado el río.")
        semSefrs.release()

def cruzar_juntos():
    semHackers.acquire()
    semSefrs.acquire()
    print("Hackers y Serfs cruzando el río...")
    time.sleep(2)
    print("Hackers y Serfs han cruzado el río.")
    semHackers.release()
    semSefrs.release()

# Ejemplo de simulación
personas = ["Hackers", "Hackers", "Serfs", "Serfs", "Hackers", "Serfs", "Hackers", "Serfs", "Serfs", "Hackers"]

for persona in personas:
    if persona == "Hackers":
        threading.Thread(target=cruzar, args=("Hackers",)).start()
    elif persona == "Serfs":
        threading.Thread(target=cruzar, args=("Serfs",)).start()

    if semHackers._value < MAX_PERSONAS and semSefrs._value < MAX_PERSONAS:
        threading.Thread(target=cruzar_juntos).start()



