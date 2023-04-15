# Programa para resolver el problema de sincronización
# del cruce del rio 
# Desarrollado por Rojo López Luis Felipe 
import threading 
import random
import time

# Este problema lo encuentro similar al problema clásico 
# de los fumadores compulsivos, por lo que su resolución 
# la plantearé mediante el uso de un intermediario

desarrolladores = ['hacker','serf']
semaforos = {}
for i in desarrolladores:
    semaforos[i] = threading.Semaphore(0)

semaforo_oportunista = threading.Semaphore(1)

mutex_num_hackers = threading.Semaphore(1) #Para proteger el numero de hackers/serfs en la balsa
mutex_num_serfs = threading.Semaphore(1)
hackers_en_balsa = 0
serfs_en_balsa = 0

semaforos_acom = {}
for i in desarrolladores:
    semaforos_acom[i] = threading.Semaphore(0)

acom_mutex = threading.Semaphore(1)

# Se definen a los desarrolladores listillos que se suben a la balsa en cuanto
# la ven libre
def oportunista():
    global hackers_en_balsa, serfs_en_balsa
    while True:
        semaforo_oportunista.acquire()
        # Se dejan subir a 3 desarrolladores
        oportunista_balsa = []
        for i in range(3):
            oportunista_balsa.append(random.choice(desarrolladores))
            dentro = oportunista_balsa[i]
            if dentro == 'hacker':
                with mutex_num_hackers:
                    hackers_en_balsa += 1 # Se contabiliza el número de hackers/serfs que suben
            elif oportunista_balsa[i] == 'serf':
                with mutex_num_serfs:
                    serfs_en_balsa += 1
        for i in oportunista_balsa:
            print("Soy %s y me subiré a la balsa ahora" %i)
            semaforos[i].release()
        
# Este es el desarrollador que el acomodador va a subir a la balsa
# para cumplir con la condicion de 4 del mismo grupo o 2 y 2
def ultimo_invitado(desa):
    while True:
        semaforos_acom[desa].acquire()
        cruza_rio(desa)
        semaforo_oportunista.release()

# La función que va a ver quién fue el último que subió a la balsa
# y la va a liberar para cruzar el río
def cruza_rio(desa):
    global hackers_en_balsa, serfs_en_balsa
    if desa == 'hacker':
        with mutex_num_hackers:
            hackers_en_balsa += 1
    elif desa == 'serf':
        with mutex_num_serfs:
            serfs_en_balsa += 1
    print("--Balsa cruzando rio con %i hackers y %i serfs"%(hackers_en_balsa, serfs_en_balsa))
    time.sleep(0.3)
    with mutex_num_hackers:
        hackers_en_balsa = 0
    with mutex_num_serfs:
        serfs_en_balsa = 0

# El acomodador va a observar quién hace falta en la balsa para cumplir con la condición 
def acomodador(desa):
    while True:
        semaforos[desa].acquire()
        acom_mutex.acquire()
        print("Hay %i hackers y %i serfs en la balsa"%(hackers_en_balsa, serfs_en_balsa))
        if hackers_en_balsa == 3:
            invitado = desarrolladores [:]
            invitado.remove('serf')
            print("Notificar a un hacker que debe subirse")
            semaforos_acom[invitado[0]].release()
        elif hackers_en_balsa == 2:
            invitado = desarrolladores [:]
            invitado.remove('hacker')
            print("Notificar a un serf que debe subirse")
            semaforos_acom[invitado[0]].release()
        elif serfs_en_balsa == 3:
            invitado = desarrolladores [:]
            invitado.remove('hacker')
            print("Notificar a un serf que debe subirse")
            semaforos_acom[invitado[0]].release()
        elif serfs_en_balsa == 2:
            invitado = desarrolladores [:]
            invitado.remove('serf')
            print("Notificar a un hacker que debe subirse")
            semaforos_acom[invitado[0]].release()
        acom_mutex.release()

# A lanzar los hilos y esperar que funcione o.O
threading.Thread(target=oportunista, args=[]).start()
acomodadores = [threading.Thread(target=acomodador, args=[i]) for i in desarrolladores]
for acomodador in acomodadores:
    acomodador.start()

for i in desarrolladores:
    threading.Thread(target=ultimo_invitado, args=[i]).start()

