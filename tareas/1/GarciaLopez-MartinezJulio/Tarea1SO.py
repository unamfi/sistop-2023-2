import threading
import time
import random

SemSanta = threading.Semaphore(0)    # Santa
SemRenos = threading.Semaphore(0)     # Renos
SemElfosA = threading.Semaphore(3)   # 3 Elfos que piden ayuda
SemElfos = threading.Semaphore(0)    # Elfos ayudados

numRenos = 0      # Num renos que han llegado
ren = 0 
numElfos = 0      # Num elfos que han llegado
elfs = 0

Renos = 9
Elfos = 9
ElfosAY = 3
Despierto = 7
Ayudar = 2

NombreRenos = ["R1","R2","R3","R4","R5","R6","R7","R8","R9"]
NombreElfos = ["E1","E2","E3","E4","E5","E6","E7","E8","E9"]

def santa():
    global numRenos, elfs
    print("Santa: Voy a dormir! Zzzz...")
    for i in range (Despierto):
        SemSanta.acquire()
        print("------Santa: Estoy despierto------")
        if elfs == ElfosAY:
            elfs = 0;
            print("Santa: Cual es el problema?")
            for i in range (ElfosAY):  # 3 veces
                print("Santa ayuda al elfo ({}/3)".format(i+1))
                SemElfosA.release()
            #print("Santa le ha acabao de ayudar a 3 renos")
            for i in range(ElfosAY):
                SemElfos.release()
        elif numRenos == Renos:     #Si llegan 9 renos
            numRenos = 0
            print("                     Santa: He despertado para iniciar el recorrido!!!")
            for i in range(Renos):
                SemRenos.release()

def reno():
    global numRenos
    global ren

    num = numRenos
    numRenos += 1
    print("Hola, soy el reno "+ NombreRenos[num])
    time.sleep(random.randint(5,7))

    ren += 1
    if ren == 9:
        print(" Reno "+ NombreRenos[num] +" aqui!. Soy el "+ str(ren) + " , ya somos todos los renos!")
        SemSanta.release()
    else:
        print(" Reno "+ NombreRenos[num] +" ha llegado")

    SemRenos.acquire()  #Santa despierta
    #print(" {} listo y atado".format(NombreRenos[num]))
    #print(" Reno {} acaba ".format(NombreRenos[num]))

def elfo():
    global numElfos
    global elfs

    num = numElfos
    numElfos += 1
    print("Hola, soy el elfo "+NombreElfos[num])

    for i in range(Ayudar):   #Cada elfo pide ayuda 2 veces
        time.sleep(random.randint(1,5))
        SemElfosA.acquire()  #Deja pasar 3 elfos
        elf = elfs + 1
        elfs += 1
        if elf < 3:
            print("Elfo "+ NombreElfos[num] + " : Tengo una pregunta. Soy el ("+str(elf)+"/3) en la espera  ")
        elif elf == ElfosAY:
            print("Elfo "+NombreElfos[num]+" : Tengo una pregunta. Soy el ("+str(elf)+"/3) SANTAAA DESPIERTAAAA ")
            SemSanta.release()
        SemElfos.acquire()
        print("Elfo "+ NombreElfos[num]+" esta siendo ayudado")
    print("Elf "+ NombreElfos[num]+" acaba")


threads = []      #Arreglo de hilos

s = threading.Thread(target=santa)  #Santa
threads.append(s)

for i in range (Elfos):              #Elfos
    e = threading.Thread(target=elfo)
    threads.append(e)
    
for i in range (Renos):            #Renos
    r = threading.Thread(target=reno)
    threads.append(r)

for t in threads:
    t.start()

for t in threads:
    t.join()
    
print("FIN")