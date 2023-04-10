#Librerias utilizadas
import threading        # Manejo de hilos
import time             # Manejo de tiempo, principalmente sleep

import colorama         # Para colores!!
from colorama import Fore
from colorama import Style


                                                ###############################
                                                # Creación del comportamiento #
                                                ###############################

# Semáforos que seran usados
mutex_checkVar = threading.Semaphore(1)
elfos_semaforo = threading.Semaphore(1)
renos_semaforo = threading.Semaphore(0)
Santa_semaforo = threading.Semaphore(0)

torniquete = threading.Semaphore(0)

signaling_messages = threading.Semaphore(0)     # Un semáforo para controlar flujo de mensajes. 
mutex2 = threading.Semaphore(1)

mutexRenos = threading.Semaphore(1)
mutexElfos = threading.Semaphore(1)

# Contadores
elfos_count = renos_count = 0
n = 0


# ---------------------------
# -- Funciones de mensajes --
# ---------------------------

def santa_despierta():
    print("*Bosteza* \U0001F385 Ho! Ho! Ho! Estoy despierto.")

def preparar_renos():
    print("* Santa Claus empieza a preparar los renos *")

def santa_estado():
    print(Fore.LIGHTBLUE_EX+"\n\t\t\t* Santa Claus se encuentra dormido actualmente * \U0001F6CC\n"+ Style.RESET_ALL)

def inicio_viaje():
    print(Fore.LIGHTGREEN_EX +"\t\t\t\t * Santa inicia el viaje *  \U0001F30E \n\t      \U0001F384      \U0001F381 F e l i z  N a v i d a d !   H o !   H o !   H o !  \U0001F381"+ Style.RESET_ALL)

def ayudar_elfos():
    print(Fore.GREEN+"\t\t¿En qué les puedo ayudar?         * Empieza asesorar *"+ Style.RESET_ALL)

def santa_regresa():
    print(Fore.LIGHTBLUE_EX+" > * Santa Claus regresa del viaje muy cansado y se va a dormir \U0001F6CC *"+ Style.RESET_ALL)

def santa_duerme():
    print(Fore.LIGHTBLUE_EX+"* Santa Claus vuelve a dormir \U0001F6CC *"+ Style.RESET_ALL)

def reno_llega(num):
    print(f"\t * El reno {num} \U0001F98C regresó de sus vacaciones *")

def renos_descansan():
    print("* El reno procede a descansar en el establo \U0001F4A4 *")

def reno_aviso(id):
    print(Fore.LIGHTYELLOW_EX + f"\t\t### Ha llegado el último reno ###          ~~ Ahora el reno {id} se dirige con Santa Claus ~~" + Style.RESET_ALL)

def renos_preparados(num):
    print(f"\t\t~~~~~~      El reno {num} ya está listo para el viaje!      ~~~~~~")

def renos_vacacionar():
    print(Fore.LIGHTRED_EX+" > * Los renos vuelven a ir de vacaciones \U0001F3D6 *"+ Style.RESET_ALL)

def grupo_formado_aviso(num):
    print(Fore.LIGHTYELLOW_EX+f"\t> Elfo número {num}: El grupo ya está formado ¡Ya podemos preguntar!  \U0001F512\U0001F5DD"+ Style.RESET_ALL)

def elfo_recibe_ayuda(id):
    print(f"* Elfo número {id} recibe ayuda por parte de Santa Claus *")

def elfo_salida(id):
    print(f"~~~~   M u c h a s  g r a c i a s,  S a n t a !  \U0001FAC2   ~~~~   \t* Elfo número {id} procede a salir *")

def elfo_avisa_siguiente():
    print(Fore.RED+" > Último elfo en entrar: ¡El siguiente grupo ya puede pasar! \U0001F6C2"+ Style.RESET_ALL)

def elfos_esperando(num,id):
    print(f"* Llega el elfo {id} con duda en la elaboración de un juguete, se encuentra esperando formar un grupo de 3. Ocupa la posición {num} dentro del grupo \U0001F465 *")


def espacio():
    print("\n\n")



# -----------------------------
# -- Comportamiento de Santa --
# -----------------------------
'''
Se tiene primero a Santa, se contemplas las dos unicas acciones que lo pueden despertar:
    1. Los 9 renos han llegado al polo norte.
    2. Hay exactamente 3 duendes que necesitan de la ayuda de Santa Claus
'''

def santa_claus():
    global renos_count,Santa_semaforo,mutex_checkVar,renos_semaforo,elfos_count,elfos_semaforo,n,torniquete,signaling_messages
    santa_estado()
    Santa_semaforo.acquire()       # Se encuentra bloqueado en un inicio, hasta que una condición lo saque de bloqueados

    mutex_checkVar.acquire()       # Hay que forzar una exclusividad mutua de acceso
    if renos_count ==  9:          # Por prioridad, se checa la cantidad de renos.
        elfos_semaforo.acquire()   # Se debe de bloquear el paso de grupo de dudas ya que santa está preparando a los renos. 
        
        espacio()
        santa_despierta()
        preparar_renos()
        n = 0

        renos_semaforo.release(9)
        renos_count = 0
        signaling_messages.acquire()

        inicio_viaje()
        santa_regresa()            # Santa se va a vacaciones
        renos_vacacionar()         # Los renos se van de vacaciones
        espacio()

        elfos_semaforo.release()

    else:
        if elfos_count == 3:         # En este caso se tiene 3 elfos que preguntan algo
            espacio()
            santa_despierta()
            ayudar_elfos()
            torniquete.release()     # Se deja pasar al grupo de 3 elfos
            signaling_messages.acquire()
            santa_duerme()
            espacio()
    mutex_checkVar.release()




# -----------------------------
# -- Comportamiento de Renos --
# -----------------------------
'''
Los renos estarán llegando de sus vacaciones, mientras no hayan llegado todos los renos estos se van a descansar mientras
van llegando los que faltan.
En cuanto llegue el último reno, este mimsmo va ir a despertar a Santa.
'''
def renos(id):        # Barrier pattern.
    global renos_count,Santa_semaforo,mutex_checkVar,renos_semaforo,mutex2,mutexRenos
    global n
    mutexRenos.acquire()            # Modificación 1:1 del contador de renos.
    reno_llega(id)
    renos_count=renos_count+1
    if renos_count == 9:
        Santa_semaforo.release()    # Va y despierta a Santa Claus.
        reno_aviso(id)
    else:
        renos_descansan()
    mutexRenos.release()


    renos_semaforo.acquire()        # Se van durmiendo hasta que son despertados por Santa.
    renos_preparados(id)
    
    
    mutex2.acquire()
    n=n+1
    if n == 9:
        signaling_messages.release()
    mutex2.release()



# -----------------------------
# -- Comportamiento de Elfos --
# -----------------------------
'''
Los elfos solo van a despertar a santa en grupos de tres, tal que cada uno tenga una duda.
Lo importante es deberan de ser tres elfos, además de que una vez que santa se encuentre ocupado con un grupo de 3 elfos, 
otro grupo no podrá acceder a pedir ayudar a Santa, por ende deberán de esperar hasta que santa brinde ayuda y los elfos
salgan.
'''
def elfos(id,no_formado):
    global Santa_semaforo,mutex_checkVar,elfos_count,elfos_semaforo,mutexElfos
    
    elfos_semaforo.acquire()    # Los elfos entrantes serán bloqueados.
    elfos_esperando(no_formado,id)
    
    mutexElfos.acquire()    # Control de cantidad de elfos que van entrando
    elfos_count=elfos_count+1
    
    if elfos_count == 3:
        grupo_formado_aviso(id)
        Santa_semaforo.release()    # El último elfo ya no permite que más elfos formen parte del grupo que va preguntar, 
                                    # por ende los demas se bloquean.
    else:
        elfos_semaforo.release()    # Va permitiendo que otro elfo pueda ser parte del grupo.
    mutexElfos.release()
    
    
    torniquete.acquire()                # Para que los 3 elfos vayan en grupo y no por partes.
    torniquete.release()

    elfo_recibe_ayuda(id)               # Van entrando y van preguntando


    mutexElfos.acquire()    # Control de elfos que van saliendo
    elfos_count=elfos_count-1
    elfo_salida(id)
    if elfos_count == 0:                # El último elfo en salir informa a los demás y ya se puede armar el siguiente grupo. 
        elfo_avisa_siguiente()
        torniquete.acquire()    
        elfos_semaforo.release()        # Se va juntando el siguiente grupo.
        signaling_messages.release()
    
    mutexElfos.release()



                                                ################################
                                                # Creacion del flujo principal #
                                                ################################

# Se crea tres funciones con whiles con un ciclo infinito para emular el comportamiento
def lanzando_renos():
    num = 1
    while True:
        num = num+1
        if num == 10:
            num = 1
        threading.Thread(target=renos,args=[num]).start()
        time.sleep(1)
        

def lanzando_elfos():           # Cualquier cantidad de elfos...
    num = 1
    no_formado = 1
    while True:
        num = num+1
        no_formado = no_formado+1
        if no_formado == 4:
            no_formado = 1
        threading.Thread(target=elfos,args=[num,no_formado]).start()
        time.sleep(0.5)


def lanzando_santa_claus():  
    while True:
        threading.Thread(target=santa_claus).start()
        time.sleep(1.25)
    


threading.Thread(target=lanzando_santa_claus).start()
threading.Thread(target=lanzando_renos).start()
threading.Thread(target=lanzando_elfos).start()
