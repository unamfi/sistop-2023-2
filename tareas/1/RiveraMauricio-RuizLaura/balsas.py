#Problema del cruce del rio

#Bibliotecas
import threading
import time
import random

#Variables para delimitar limites en barreras
num_desarrolladores = 2
soporte_barca = 4

#Utilidades
numH = 0
numS = 0
cuentaH = 0
cuentaS = 0
cuentaB = 0
cuentaS2 = 0
cuentaH2 = 0

#Primitivas utilizadas
mutex = threading.Semaphore(1)
barreraH = threading.Semaphore(0)
barreraS = threading.Semaphore(0)
barreraB = threading.Semaphore(0)


#Define las caracteristicas de los hilos. Cada Hacker y Serf será identificado.
#ademas, se distinguirá su tipo dentro de 'espera' como cero o uno para cumplir condiciones.

def lanzaHackers():
    numH = 0
    while True:
        print("Se creo el Hacker %d" %numH)
        threading.Thread(target=espera, args=[numH,0]).start()
        time.sleep(random.random())
        numH+=1
def lanzaSerfs():
    numS = 0
    while True:
        print("Se creo el Serf %d" %numS)
        threading.Thread(target=espera, args=[numS,1]).start()
        time.sleep(random.random())
        numS+=1

#Se basa en tres barreras. Toma como argumentos su identificador y el tipo (0 para Hackers, 1 para Serfs)
def espera(id,tipo):
    global mutex, cuentaS, cuentaB, cuentaH, num_desarrolladores, soporte_barca, barreraB, barreraH, barreraS, cuentaS2, cuentaH2
    with mutex:
        #Barrera para hackers. Se libera cuando hay dos en espera.
        if tipo==0:
            cuentaH=cuentaH+1
            print("Hackers en la cola: %d" % cuentaH)
            if cuentaH==num_desarrolladores:
                barreraH.release()

        #Lo mismo sucede con los serfs.
        if tipo==1:
            cuentaS=cuentaS+1
            print("Serfs en la cola: %d" % cuentaS)
            if cuentaS==num_desarrolladores:
                barreraS.release()

    #Cuando llegan los dos, seguirá el camino a una tercera barrera ("la balsa")
    if tipo==0:
        print("Hacker %d en la cola" %id)
        barreraH.acquire()
        barreraH.release()
        print("Sube hacker %d a la balsa" % id)

        with mutex:
            cuentaH = cuentaH - 1
            if cuentaH == 0:
                barreraH.acquire()

    #Lo mismo ocurre para los serfs. Se reincian las barreras.
    if tipo==1:
        print("Serf %d en la cola" %id)
        barreraS.acquire()
        barreraS.release()
        print("Sube serf %d a la balsa" %id)

        with mutex:
            cuentaS = cuentaS - 1
            if cuentaS == 0:
                barreraS.acquire()

    #Barrera "final", representa a la balsa.
    with mutex:
        cuentaB=cuentaB+1
        if tipo==0:
            cuentaH2=cuentaH2+1
            print("Hackers en la balsa: %d" %cuentaH2)
            print("Serfs en balsa: %d" %cuentaS2)
        if tipo==1:
            cuentaS2=cuentaS2+1
            print("Hackers en la balsa: %d" %cuentaH2)
            print("Serfs en balsa: %d" %cuentaS2)
        print("Total de desarrolladores en la balsa: %d" % cuentaB)
        if cuentaB==soporte_barca:
            barreraB.release()
            print("Arranca la balsa.")

    barreraB.acquire()
    barreraB.release()

    with mutex:
        cuentaB = cuentaB - 1
        if tipo==0:
            cuentaH2=cuentaH2-1
        if tipo==1:
            cuentaS2=cuentaS2-1
        if cuentaB == 0:
            barreraB.acquire()


threading.Thread(target=lanzaHackers).start()
threading.Thread(target=lanzaSerfs).start()