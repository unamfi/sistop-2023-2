import random

# Definir parámetros del algoritmo
n = 2
Q = n + 1

# Definición de procesos
procesos = [{'nombre': 'A', 'duracion': 4, 'llegada': 0, 'prioridad': 0},
            {'nombre': 'B', 'duracion': 8, 'llegada': 3, 'prioridad': 0},
            {'nombre': 'C', 'duracion': 3, 'llegada': 7, 'prioridad': 0},
            {'nombre': 'D', 'duracion': 5, 'llegada': 11, 'prioridad': 0}]

# Imprimir tabla de carga de trabajo
print("Proceso Duración Llegada")
for proceso in procesos:
    print(f"{proceso['nombre']}       {proceso['duracion']}       {proceso['llegada']}")

# Generar procesos aleatorios y agregarlos a la lista
procesos_aleatorios = []
primer_proc = 'E'
for i in range(random.randint(4,8)):
    # Genero los 4 a 8 procesos aleatorios
    procesos_aleatorios.append({'nombre': chr( ord(primer_proc)+i ),
                     'llegada': random.randint(0, 10*i),
                     'duracion': random.randint(4,10),
                     'prioridad': 0
                     })

# Unir listas de procesos
procesos += procesos_aleatorios

# Implementar algoritmo de planificación de lotería
t = 0
res = ''
procesos_restantes = list(procesos)
num_procesos = len(procesos_restantes)

print('* Inicia ejecución')
while num_procesos > 0:
    print("t=%d" % t)
    # Generar número aleatorio para la lotería
    r = random.randint(1, sum(p['duracion'] for p in procesos_restantes))
    i = 0
    while i < len(procesos_restantes) and r > 0:
        r -= procesos_restantes[i]['duracion']
        i += 1
    # Seleccionar el proceso y ejecutar
    i -= 1
    proceso_actual = procesos_restantes[i]
    res += proceso_actual['nombre']
    duracion_ejecucion = min(Q, proceso_actual['duracion'])
    proceso_actual['duracion'] -= duracion_ejecucion
    if proceso_actual['duracion'] == 0:
        num_procesos -= 1
        procesos_restantes.pop(i)
    else:
        # Reinsertar proceso en la lista de procesos restantes
        procesos_restantes[i] = proceso_actual
    t += duracion_ejecucion
    print("    ⌚ %s %d tick" % (proceso_actual['nombre'], duracion_ejecucion))

print("Planificación realizada: \n" + res)
print("\n\nDuración total: %d" % t)

# Ordenar la lista de procesos por tiempo de inicio
procesos_ordenados = sorted(procesos, key=lambda x: res.index(x['nombre']))

# Imprimir la tabla de forma ordenada
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Proceso", "Inicio", "Fin", "T", "E", "P"))
tiempo_espera_total = 0
tiempo_respuesta_total = 0
for proceso in procesos:
    inicio = res.index(proceso['nombre'])
    fin = inicio + proceso['duracion']
    t = fin - proceso['llegada']
    e = t - proceso['duracion']
    if proceso['duracion'] == 0:
        p = 0
    else:
        p = e / proceso['duracion']
    tiempo_espera_total += e
    tiempo_respuesta_total += t
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10.1f}".format(proceso['nombre'], inicio, fin, t, e, p))
promedio_espera = tiempo_espera_total / len(procesos)
promedio_respuesta = tiempo_respuesta_total / len(procesos)
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Prom", "-", "-", "{:.1f}".format(promedio_respuesta), "{:.1f}".format(promedio_espera), "-"))
