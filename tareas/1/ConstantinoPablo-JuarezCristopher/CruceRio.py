import threading # Manejo de hilos, semaforos, mutex 
import time # Manejo de sleep 

tripulantes = 0
num_Hackers = 0 
num_Serfs = 0
num_Viaje = 1
#Contabilizar pasjeros
Hackers = threading.Semaphore(0) 
Serfs = threading.Semaphore(0)
#Mutex para crear el bloque del bote
mutexBote = threading.Semaphore(1) 

def suben_hackers(): 

    global num_Hackers, num_Serfs
    
    num_Hackers += 1 #Se considera que sube el primer hacker 

    if num_Hackers == 4: 
        [Hackers.release() for _ in range(num_Hackers)]#El bote se llena de 4 hackers
        num_Hackers = 0 #Vaciar bote 
         
        zarpar("Hacker") 

    else: 
        if num_Hackers == 2 and num_Serfs == 2: 
            Hackers.release() 
            Serfs.release()
            Serfs.release()
            #Vaciar bote
            num_Hackers = 0 
            num_Serfs = 0
            zarpar("Hacker")

        else:
            Hackers.acquire() #Esperar a que se ocupe lugar
            zarpar("Hacker")

def suben_serfs():

    global num_Serfs, num_Hackers     
     
    num_Serfs += 1       
    
    if num_Serfs == 4:
        [Serfs.release() for _ in range(num_Serfs)]  
        num_Serfs = 0 # Vaciar bote 

        zarpar("Serf")

    else: 
        if (num_Serfs == 2 and num_Hackers == 2):   
            Hackers.release()
            Hackers.release()
            Serfs.release()
            num_Hackers = 0
            num_Serfs = 0
            zarpar("Serf")

        else:
        
            Serfs.acquire()  
            zarpar("Serf")

def zarpar(desarrollador):  
    global tripulantes, num_Viaje

    mutexBote.acquire()
    tripulantes += 1       #contador de tripulantes
    print('tripulante {} -  {}. A bordo'.format(tripulantes, desarrollador)) 
    time.sleep(.5)

    if tripulantes == 4:  
        print("Viaje {}".format(num_Viaje))
        time.sleep(1)
        num_Viaje += 1
        tripulantes = 0 # Reiniciar el conteo para la siguinete balsa

    mutexBote.release()  #proteger la variable tripulantes
 
for i in range(10):
    threading.Thread(target = suben_hackers, args = []).start()
    threading.Thread(target = suben_serfs, args = []).start()


    
    