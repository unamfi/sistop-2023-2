# Código hecho por Fernando Arciga Guzmán
import random

                # variables y datos a usar

procesos = []
primer_proc = 'A' # aunque no se ejecuta primero jeje
plan = ""
loteria = []
total_tickets = 0
total_tickets_x_proceso = {}
ticks = 0
tiempo_inicial = {}
tiempo_final = {}
total_procesos = random.randint(5, 8)
lista_colores = ['\033[92m', '\033[91m',
                 '\033[93m', '\033[94m', 
                 '\033[96m', '\033[95m', 
                 '\033[97m', '\033[90m']

Q = 10 # cada 10 ticks cambiamos el boleto

for i in range(total_procesos):
    # De 5 a 8 procesos
    procesos.append({
        'nombre': chr(ord(primer_proc)+i),
        'duración': random.randint(80, 120),
        'color': lista_colores[i],
        'boletos': 0
    })

promedio = 0
for proceso in procesos:
    promedio += proceso['duración']

            # acomodo para ejecución

print('\nLista de procesos:')
print('Proceso\tDuración')
for proc in procesos:
    print("%2s\t%3d" %(proc['nombre'], proc['duración']))

# Guardamos los procesos en una lista para 
for proceso in procesos:
    tickets = random.randint(1, 100)
    for i in range(tickets):
        loteria.append(proceso['nombre'])
        total_tickets += 1

for proceso in procesos:
    proceso['boletos'] = loteria.count(proceso['nombre'])

random.shuffle(loteria)  # reordenamos los procesos

for i in range(total_tickets): # son todos los tickets en la lista
    if len(loteria) > 1: # siempre y cuando haya tickets pendientes
        random.shuffle(loteria)  # reordenamos los procesos
        ganador = loteria.pop(0) # sacamos un ganador al azar
        while (ticks < Q and ganador in loteria): # mientras aumentamos el tick actual hasta alcanzar el Quantum
            # debemos checar que estemos en el proceso verdadero
            if ganador not in tiempo_inicial:
                # cuando comienza no está en tiempo inicial
                tiempo_inicial[ganador] = ticks
            for proceso in procesos:
                # para ello verificamos si el ganador es el proceso actual
                if ganador == proceso['nombre']:
                    plan += proceso['color'] + ganador + '\033[0m' # y le damos colorcito para impresión
                    if proceso['duración'] < 1: # si la duración está por debajo de 1
                        # sacamos de la loteria los boletos de ese proceso
                        while True: # ya que ya terminó de ejecutarse
                            if(proceso['nombre'] not in loteria):
                                ticks += 1
                                break
                            else:
                                # y borramos de la loteria el proceso
                                loteria.remove(proceso['nombre'])
                        tiempo_final[proceso['nombre']] = ticks
                    else: 
                        proceso['duración'] -= 1
                        ticks += 1  # aumentan los ticks
        Q = ticks + 10

print("\nPlanificador de procesos: {} ".format(plan))

estimado = promedio
promedio = promedio / total_procesos

print("\nTabla de ejecución:")

for proceso in procesos:
    print("{}\t inicio: {}\t final: {}\t ETA: {}\t tickets: {}".format(
            proceso['nombre'], 
            tiempo_inicial[proceso['nombre']], 
            tiempo_final[proceso['nombre']],
            tiempo_final[proceso['nombre']] - tiempo_inicial[proceso['nombre']],
            proceso['boletos']
        )
    )

print("Promedio de ejecucion {} ticks".format(promedio))
print("Repartidos en total: %d tickets" % total_tickets)
print("Tiempo esperado: {}".format(estimado))