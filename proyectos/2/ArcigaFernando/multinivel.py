# Código hecho por Fernando Arciga Guzmán
from random import randint
    
procesos = []
q0 = []
q1 = []
q2 = [] # la queso

tiempo_inicial = {}
tiempo_final = {}

Quantums = [32, 64 , 128]

n = 0 # tick actual
cola_en_exe = q0

primer_proc = 'A'
plan=""
lista_colores = ['\033[92m', '\033[91m',
                 '\033[93m', '\033[94m',
                 '\033[96m', '\033[95m',
                 '\033[97m', '\033[90m']

for i in range(randint(5,8)):
    # Genero los 4 a 8 procesos aleatorios
    procesos.append({
        'nombre': chr( ord(primer_proc)+i ),
        'llegada': randint(0, 10*i),
        'duración': randint(80,120),
        'prioridad': randint(0,3),
        'color': lista_colores[i]
    })

print('\nLista de procesos:')
print("proceso\tllegada\tduración|prioridad")
for proc in procesos:
    print("%2s\t%3d\t%3d\t|%3d" % (proc['nombre'], proc['llegada'], proc['duración'], proc['prioridad']))
    if proc['prioridad'] == 0:
        q0.append(proc)
    if proc['prioridad'] == 1:
        q1.append(proc)
    if proc['prioridad'] >= 2:
        q2.append(proc)

while len(q0) >= 1 or len(q1) >= 1 or len(q2) >= 1:
    if len(q0) >= 1:
        cola_en_exe = q0
    elif len(q1) >= 1:
        cola_en_exe = q1
    else:
        cola_en_exe = q2

    proceso_actual = cola_en_exe.pop(0)
    plan += proceso_actual['color'] + proceso_actual['nombre'] + '\033[0m'

    if proceso_actual['nombre'] not in tiempo_inicial:
        tiempo_inicial[proceso_actual['nombre']] = n

    if cola_en_exe == q0:
        for i in range(Quantums[0]):
            n += 1
            proceso_actual['duración'] -= 1
    elif cola_en_exe == q1:
        for i in range(Quantums[1]):
            n += 1
            proceso_actual['duración'] -= 1
    else:
        for i in range(Quantums[2]):
            n += 1
            proceso_actual['duración'] -= 1

    if proceso_actual['duración'] <= 0:
        tiempo_final[proceso_actual['nombre']] = n
    elif proceso_actual['duración'] > 0:
        if cola_en_exe == q0:
            q1.append(proceso_actual)
        else:
            q2.append(proceso_actual)

print("\nPlanificador:\n", plan)

print("\nTabla de ejecución")
print("Proceso\tinicio\tETA\tfinal")
for p in procesos:
    print("{}\t{}\t{}\t{}".format(
            p['nombre'],
            tiempo_inicial[p['nombre']],
            tiempo_final[p['nombre']] - tiempo_inicial[p['nombre']],
            tiempo_final[p['nombre']]
        )
    )

