# Loteria
from random import randint

procesos = []
primer_proc = 'A'

for i in range(randint(5, 8)):
    # Genero los 4 a 8 procesos aleatorios
    procesos.append({
        'nombre': chr(ord(primer_proc) + i),
        'llegada': randint(0, 10 * i),
        'duración': randint(4, 10),
        'prioridad': randint(1, 5)
    })

print('Lista de procesos:')
print("Proceso   Llegada   Duración    Prioridad")
for proc in procesos:
    print("%2s         %3d         %3d         %d" % (proc['nombre'], proc['llegada'], proc['duración'], proc['prioridad']))

print('\n* Inicia ejecución\n')

tiempo_actual = 0
tiempo_total = 0
tabla_ejecucion = []

while procesos:
    # Crear una lista de boletos para cada proceso, donde los boletos son proporcionales a la prioridad
    boletos = []
    for proc in procesos:
        for i in range(proc['prioridad']):
            boletos.append(proc['nombre'])

    # Sortear un boleto ganador
    boleto_ganador = boletos[randint(0, len(boletos) - 1)]

    # Seleccionar el proceso correspondiente al boleto ganador
    proceso_actual = next(proc for proc in procesos if proc['nombre'] == boleto_ganador)
    procesos.remove(proceso_actual)

    tiempo_inicio = tiempo_actual
    tiempo_espera = tiempo_inicio - proceso_actual['llegada']
    tiempo_ejecucion = proceso_actual['duración']
    tiempo_finalizacion = tiempo_inicio + tiempo_ejecucion
    tiempo_respuesta = tiempo_inicio - proceso_actual['llegada']
    proporcion_penalizacion = tiempo_respuesta / tiempo_ejecucion if tiempo_ejecucion else 0

    tabla_ejecucion.append({
        'proceso': proceso_actual['nombre'],
        'inicio': tiempo_inicio,
        'fin': tiempo_finalizacion,
        'tiempo_ejecucion': tiempo_ejecucion,
        'tiempo_respuesta': tiempo_respuesta,
        'tiempo_espera': tiempo_espera,
        'proporcion_penalizacion': proporcion_penalizacion
    })

    tiempo_total += tiempo_ejecucion
    tiempo_actual = tiempo_finalizacion

# Mostramos la tabla de ejecución
print("Tabla de ejecución:")
print("Proceso Inicio Fin      T       E       P")
for fila in tabla_ejecucion:
    print(f"{fila['proceso']}\t{fila['inicio']}\t{fila['fin']}\t{fila['tiempo_ejecucion']}\t{fila['tiempo_espera']}\t{fila['proporcion_penalizacion']:.1f}")

# Mostramos la duración total de la ejecución
print(f"\nDuración total: {tiempo_total}")