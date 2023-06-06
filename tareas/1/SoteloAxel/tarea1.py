import threading
import time
import random

numHackers = 1
numSerfs = 1
numHackersBalsa = 0
numSerfsBalsa = 0

lugaresBalas = threading.Semaphore(5)
mutexSubiendoBalsa = threading.Semaphore(1)


def subeBalsa(persona, numero):
    global numHackersBalsa, numSerfsBalsa

    with mutexSubiendoBalsa:
        if persona == 'hacker':
            if numSerfsBalsa >= 3:
                print(f'{persona} {numero-1} no puede subir, hay demasiados serfs')
            elif numSerfsBalsa == 1 and numHackersBalsa == 2:
                print(f'{persona} {numero-1} no puede subir porque habrá pelea')
            else:
                numHackersBalsa += 1
                print(f"{persona} {numero-1} sube a la balsa ({numHackersBalsa} hackers, {numSerfsBalsa} serfs)")
            time.sleep(random.random())
        elif persona == 'serf':
            if numHackersBalsa >= 3:
                print(f'{persona} {numero-1} no puede subir, hay demasiados hackers')
            elif numHackersBalsa == 1 and numSerfsBalsa == 2:
                print(f'{persona} {numero-1} no puede subir porque habrá pelea')
            else:
                numSerfsBalsa += 1
                print(f"{persona} {numero-1} sube a la balsa ({numHackersBalsa} hackers, {numSerfsBalsa} serfs)")
            time.sleep(random.random())
        
        if (numHackersBalsa + numSerfsBalsa) == 4:
            print(f"Balsa completa con {numHackersBalsa} hackers y {numSerfsBalsa} serfs.")
            print("CRUZANDO RIO")
            print('Hackers y serf bajan de la balsa')
            numHackersBalsa = 0
            numSerfsBalsa = 0
            print('Balsa regresa \n\n')


def hacker():
    global numHackers
    print("hacker llega ⚫")

    while True:
        time.sleep(random.random())
        with lugaresBalas:
            lugaresBalas.acquire()
            persona = 'hacker'
            print(f"{persona} {numHackers} se pone en fila para subir")
            numHackers = numHackers+1
        
        subeBalsa(persona, numHackers)

        lugaresBalas.release()


def serf():
    global numSerfs
    print("serf llega ⚪")

    while True:
        time.sleep(random.random())
        with lugaresBalas:
            lugaresBalas.acquire()
            persona = 'serf'
            print(f"{persona} {numSerfs} se pone en fila para subir")
            numSerfs = numSerfs+1
                
        subeBalsa(persona,numSerfs)

        lugaresBalas.release()

for i in range(numSerfs):
    threading.Thread(target=serf).start()

for i in range(numHackers):
    threading.Thread(target=hacker).start()
