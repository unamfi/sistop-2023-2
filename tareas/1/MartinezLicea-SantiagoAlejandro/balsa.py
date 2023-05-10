# EJERCICIO EL CRUCE DEL RIO
"""
- Para llegar a un encuentro de desarrolladores de sistemas
operativos, hace falta cruzar un río en balsa.
- Los desarrolladores podrían pelearse entre sí, hay que cuidar
que vayan con un balance adecuado
- En la balsa caben cuatro (y sólo cuatro) personas
    - La balsa es demasiado ligera, y con menos de cuatro puede
    volcar.
- Al encuentro están invitados hackers (desarrolladores de Linux)
y serfs (desarrolladores de Microsoft).
    - Para evitar peleas, debe mantenerse un buen balance: No
    debes permitir que aborden tres hackers y un serf, o tres serfs y
    un hacker. Pueden subir cuatro del mismo bando, o dos y dos.
- Hay sólo una balsa.
"""
# -------------------- Inicio Codigo ---------------------------#

from threading import Thread, Semaphore
import time

TOTAL_INVITADOS = 8 # Total de personas a cruzar la balsa
MAX = 4 # Maximo MAX personas de la balsa

# Contador de Hackers y Refs a bordo de la balsa
numHackers = 0
numRefs = 0

# Semaforos necesarios
mutex = Semaphore(1)
semaforoH = Semaphore(0)
semaforoS = Semaphore(0)
balsa = Semaphore(0)

# Se encarga de llenar la balsa. Libera el mutex
def abordarBalsa(tipo):
    # GLOBAL para usar las variables por referencia
    global numHackers
    global numRefs
    
    mutex.acquire()
    if tipo == "Hacker":
        numHackers += 1
        if numHackers == MAX:
            semaforoH.release(MAX)
            numHackers -= MAX
            balsa.acquire()
    else:
        numRefs += 1
        if numRefs == MAX:
            semaforoS.release(MAX)
            numRefs -= MAX
            balsa.acquire()
    # Simula la ida y el regreso de la balsa, una vez que 
    print("La balsa ha cruzado.")
    time.sleep(2)
    print("La balsa ha regresado.")
    mutex.release()

# Adquiere el control y sube al hacker a la balsa
def subirHacker():
    semaforoH.acquire()
    abordarBalsa("Hacker")
    print("Hacker ha subido a la balsa")

# Adquiere el control y sube al serf a la balsa
def subirSerf():
    semaforoS.acquire()
    abordarBalsa("Serf")
    print("Serf ha subido a la balsa")

def main():
    for i in range(TOTAL_INVITADOS):
        # No funciona si no es par
        if i % 2 == 0:
            Thread(target=subirHacker).start()
        else:
            Thread(target=subirSerf).start()
            
main()