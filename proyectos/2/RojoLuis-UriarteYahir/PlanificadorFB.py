import queue
from random import randint

# Define las constantes para los niveles de prioridad
alta_prio = 0
media_prio = 1
baja_prio = 2

n=1
q=n+1

# Define la función que simula el procesamiento de un proceso
def run_proceso(proceso, tick_ejecucion):
    if proceso['duración'] > tick_ejecucion:
        proceso['duración'] -= tick_ejecucion
        print(f"El proceso {proceso['nombre']} se ejecuta por {tick_ejecucion} ticks")
        return tick_ejecucion
    else:
        tiempo = proceso['duración']
        proceso['duración'] = 0
        return tiempo

# Define la función que simula el planificador
def planificador(procs):
    # Inicializa las colas para cada nivel de prioridad
    alta_prio_queue = queue.Queue()
    media_prio_queue = queue.Queue()
    baja_prio_queue = queue.Queue()
    
    tiempo_actual = 0
    
    procesos_pasados=[]
    for p in procs:
            if tiempo_actual == p['llegada']:
                alta_prio_queue.put(p)
                

    while not alta_prio_queue.empty() or not media_prio_queue.empty() or not baja_prio_queue.empty():
        
        if not alta_prio_queue.empty():
            proceso = alta_prio_queue.get()
            procesos_pasados.append(proceso['nombre'])
            print(f"t={tiempo_actual} soy el proceso {proceso['nombre']} y tengo una prioridad de {proceso['prioridad']}")
            tiempo_procesado = run_proceso(proceso, n)
            tiempo_actual += tiempo_procesado

            if proceso['duración'] > 0:
                # Si el proceso aún no ha terminado, lo baja de nivel de prioridad y lo agrega a la cola
                proceso['prioridad'] = media_prio
                media_prio_queue.put(proceso)
            else:
                print(f"{proceso['nombre']} terminó en el tiempo {tiempo_actual}")
                
                

        elif not media_prio_queue.empty():
            proceso = media_prio_queue.get()
            print(f"t={tiempo_actual} soy el proceso {proceso['nombre']} y tengo una prioridad de {proceso['prioridad']}")
            tiempo_procesado = run_proceso(proceso, q)
            tiempo_actual += tiempo_procesado

            if proceso['duración'] > 0:
                # Si el proceso aún no ha terminado, lo baja de nivel de prioridad y lo agrega a la cola
                proceso['prioridad'] = baja_prio
                baja_prio_queue.put(proceso)
            else:
                print(f"{proceso['nombre']} terminó en el tiempo {tiempo_actual}")
                
                

        elif not baja_prio_queue.empty():
            proceso = baja_prio_queue.get()
            print(f"t={tiempo_actual} soy el proceso {proceso['nombre']} y tengo una prioridad de {proceso['prioridad']}")
            tiempo_procesado = run_proceso(proceso, q+1)
            tiempo_actual += tiempo_procesado

            if proceso['duración'] > 0:
                # Si el proceso aún no ha terminado, lo sube de nivel para evitar que el proceso pase más tiempo sin ejecutarse
                proceso['prioridad'] = alta_prio
                alta_prio_queue.put(proceso)
            else:
                print(f"{proceso['nombre']} terminó en el tiempo {tiempo_actual}")
                
            
        for p in sorted(procs, key=lambda p: p['llegada']):
            if tiempo_actual >= p['llegada'] and p['nombre'] not in procesos_pasados:
                alta_prio_queue.put(p)


procs =[]
primer_proc = 'A'

for i in range(randint(4,8)):
    # Genero los 4 a 8 procesos aleatorios
    procs.append({'nombre': chr( ord(primer_proc)+i ),
                     'llegada': randint(0, 10*i),
                     'duración': randint(4,10),
                     'prioridad': 0
                     })

print("Lista de procesos:")
print("Proceso\t\tDuración\tLlegada")
for proc in procs:
    print("%4s  %14d  %14d" % (proc['nombre'], proc['duración'], proc['llegada']))

planificador(procs)
