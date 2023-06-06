import random
import time

# Lista de procesos y sus números de lotería y duración
procesos = [("A", 1), ("B", 2), ("C", 3), ("D", 4), 
            ("E", 8), ("F", 7), ("G", 6), ("H", 5)]

# Total de números de lotería en la lista de procesos
total_loteria = sum([p[1] for p in procesos])

print('total_loteria: {}'.format(total_loteria))

# Generar un número aleatorio entre 5 y 8
num_procesos = random.randint(5, 8)

# Ejecución de los procesos
ticks_total = 0
res = ''

print('numero de procesos a ejecutar: {}'.format(num_procesos))

for i in range(num_procesos):  # Ejecutar entre 5 y 8 procesos
    # Generar un número de lotería al azar
    loteria = random.randint(1, total_loteria)
    acumulado = 0
    # Buscar el proceso correspondiente a la lotería generada
    for p in procesos:
        print(p)
        acumulado += p[1]
        #print(acumulado)
        if loteria <= acumulado:
            duracion_ticks = 3
            print('se realiza la rifa\nProceso {} ha obtenido el número de lotería {}'.format(p[0], loteria))
            res += p[0]*duracion_ticks
            print("Ejecutando proceso {} por {} ticks".format(p[0], duracion_ticks))
            ticks_total += duracion_ticks  # Sumar el tiempo de ejecución del proceso
            break

print("Tiempo total de ejecución: {} ticks".format(ticks_total))

print(res)
