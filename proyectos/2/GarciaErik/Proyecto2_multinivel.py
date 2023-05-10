# Multinivel
from random import randint

procesos = []
primer_proc = 'A'

for i in range(randint(5, 8)):
    # Genero los 5 a 8 procesos aleatorios
    procesos.append({
        'nombre': chr(ord(primer_proc) + i),
        'llegada': randint(0, 10 * i),
        'duración': randint(4, 10),
        'prioridad': randint(0, 4)
    })

print('Lista de procesos:')
print("Proceso   Llegada   Duración    Prioridad")
for proc in procesos:
    print("%2s         %3d         %3d         %d" % (proc['nombre'], proc['llegada'], proc['duración'], proc['prioridad']))

print('\n* Inicia ejecución\n')

tiempo_actual = 0
tiempo_total = 0
tabla_ejecucion = []
planificacion_realizada = ''

while procesos:
    proceso_actual = None

    # Prioridad 0
    if procesos and procesos[0]['llegada'] <= tiempo_actual:
        proceso_actual = procesos.pop(0)

    # Prioridades 1 a 4
    elif any(proc['llegada'] <= tiempo_actual for proc in procesos):
        for i in range(1, 5):
            if any(proc['llegada'] <= tiempo_actual and proc['prioridad'] == i for proc in procesos):
                proceso_actual = next(
                    proc for proc in procesos if proc['llegada'] <= tiempo_actual and proc['prioridad'] == i)
                procesos.remove(proceso_actual)
                break

    if proceso_actual:
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

        planificacion_realizada += proceso_actual['nombre']
    else:
        tiempo_actual += 1
        planificacion_realizada += ' '

# Mostramos la planificación realizada
print(f"\nPlanificación realizada: {planificacion_realizada}")

# Mostramos la tabla de ejecución
print("Tabla de ejecución:")
print("Proceso Inicio Fin      T       E       P")
for fila in tabla_ejecucion:
    print(f"{fila['proceso']}\t{fila['inicio']}\t{fila['fin']}\t{fila['tiempo_ejecucion']}\t{fila['tiempo_espera']}\t{fila['proporcion_penalizacion']:.1f}")
    
# Mostramos la duración total de la ejecución
print(f"\nDuración total: {tiempo_total}")

