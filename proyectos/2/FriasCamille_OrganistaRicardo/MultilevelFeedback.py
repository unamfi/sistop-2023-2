import random
import time
import queue

Quantum = 5
rango = 5 # Rango de llegada de los procesos, desde 0 hasta 'rango'

# Definición de las colas de tareas
q0 = queue.Queue()
q1 = queue.Queue()
q2 = queue.Queue()
# Se usa la biblioteca queue para crear colas con una estructura FIFO,
# lo que facilita el manejo de los procesos, junto a las funciones que
# estan en la libreria: '.empty()' para verificar que no esten vacias,
# '.put()' para agregar un proceso y '.get()' para sacarlo


# Función para generar tareas aleatorias
def generar_procesos():
    no_procesos = random.randint(5, 8)
    print("=== Procesos creados ===")
    print("Id | Tiempo de ejecucion | Tiempo de llegada")
    for i in range(no_procesos): # Se crean de 5 a 8 hilos aleatoriamente
        tiempo_ejecucion = random.randint(80, 120) # Se les da tiempo de ejecucion de entre 80 y 120 ticks
        aparicion = random.randint(0, rango) # Tiempo de aparicion aleatori de entre 0 y el rango especificado arriba
        print(f"{i} |          {tiempo_ejecucion}          |          {aparicion}          ")
        proceso = {'id': i, 'tiempo': tiempo_ejecucion, 'tiempo_restante': tiempo_ejecucion, 'llegada':aparicion}
        q0.put(proceso) # Se ingresan los hilos a la cola de mayor prioridad

# Función para ejecutar las tareas
def ejecutar_procesos():
    tiempo_actual = 0
    while not q0.empty() or not q1.empty() or not q2.empty():
        # Ejecutar las tareas en la cola de nivel 0
        while not q0.empty():
            tiempo_actual += 1 # Aumenta un ciclo
            proceso_actual = q0.get() # Obtiene el primer proceso de la cola
            if proceso_actual['llegada'] <= tiempo_actual: # Si el ciclo actual es mayor o igual que el ciclo de llegada se continua
                print(f"Ciclo {tiempo_actual}: Ejecutando proceso {proceso_actual['id']} (nivel 0) - Tiempo restante: {proceso_actual['tiempo_restante']}")
                time.sleep(1)
                proceso_actual['tiempo_restante'] -= Quantum # Al realizar una 'ejecucion' el tiempo se reduce
                if proceso_actual['tiempo_restante'] <= 0: # Si el tiempo de ejecucion es ha llegado a 0 el proceso termina
                    print(f"Tiempo {proceso_actual+1}: Proceso {proceso_actual['id']} (nivel 0) completada")
                    tiempo_actual += 1 # Debido a la estructura de las colas, el proceso ya se saco de esta al usar q0.get()
                else:
                    q1.put(proceso_actual) #En caso de que aun no haya terminado, se regresa el proceso a la cola
            else: # Si no se cumple regresa el proceso a la cola para 'ejecutar' el siguiente
                q0.put(proceso_actual)

        # El proceso para las demas colas se repite
        # por lo que podemos omitir los comentarios,
        # solo seria repetir la informacion =)

        # Ejecutar las tareas en la cola de nivel 1
        while not q1.empty():
            tiempo_actual += 1
            proceso_actual = q1.get()
            if proceso_actual['llegada'] <= tiempo_actual:
                print(f"Ciclo {tiempo_actual}: Ejecutando proceso {proceso_actual['id']} (nivel 1) - Tiempo restante: {proceso_actual['tiempo_restante']}")
                time.sleep(1)
                proceso_actual['tiempo_restante'] -= 2*Quantum
                if proceso_actual['tiempo_restante'] <= 0:
                    print(f"Tiempo {proceso_actual+1}: Proceso {proceso_actual['id']} (nivel 1) completada")
                    tiempo_actual += 1
                else:
                    q2.put(proceso_actual)
            else:
                q1.put(proceso_actual)

        # Ejecutar las tareas en la cola de nivel 2
        while not q2.empty():
            tiempo_actual += 1
            proceso_actual = q2.get()
            if proceso_actual['llegada'] <= tiempo_actual:
                print(f"Ciclo {tiempo_actual}: Ejecutando proceso {proceso_actual['id']} (nivel 2) - Tiempo restante: {proceso_actual['tiempo_restante']}")
                time.sleep(1)
                proceso_actual['tiempo_restante'] -= 3*Quantum
                if proceso_actual['tiempo_restante'] <= 0:
                    print(f"Tiempo {tiempo_actual+1}: Proceso {proceso_actual['id']} (nivel 2) completada")
                    tiempo_actual += 1
                else:
                    q2.put(proceso_actual)
            else:
                q2.put(proceso_actual)

# En caso de que se quieran usar mas colas, seria suficiente copiar el codigo para cada cola
# y alterar algunas variables como el nombre de las colas, y claro, crear las nuevas colas al
# inicio del codigo

# Iniciar la simulación
generar_procesos()
ejecutar_procesos()
