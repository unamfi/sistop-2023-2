from collections import deque
from random import randint

procesos = []
primer_proc = 'A'

for i in range(randint(5,8)):
    # Genero los 4 a 8 procesos aleatorios
    procesos.append({'nombre': chr( ord(primer_proc)+i ),
                     'llegada': randint(0, 10*i),
                     'duración': randint(80,120)
                     })

print('Lista de procesos:')
print('{:<7}  {:<7} {:<7}'.format('Nombre','Duracion','llegada'))
for proc in procesos:
    print('{:<7}  {:<7} {:<7}'.format(proc['nombre'], proc['duración'], proc['llegada']))

# Definimos las colas para cada nivel
colas = [deque() for i in range(3)]

# Asignamos los procesos a su nivel correspondiente
for proc in procesos:
    if proc['duración'] < 95:
        colas[0].append(proc)
    elif proc['duración'] < 110 and proc['duración'] > 95:
        colas[1].append(proc)
    else:
        colas[2].append(proc)

# Establecemos el quantum para cada nivel
quantum = [5, 15, 25]

t = 0
res = ''
procesos_terminados = []
print('* Inicia ejecución')
while any(colas):
    for i, cola in enumerate(colas):
        # Ejecutamos los procesos de la cola actual
        while cola:
            p = cola[0]
            if p['nombre'] not in procesos_terminados:
                print("t=%d" % t)
            # Ejecutamos el proceso actual por el quantum establecido
            duracion_restante = p['duración'] - p.get('ejecutado', 0)
            duracion_ejecucion = min(duracion_restante, quantum[i])
            res += p['nombre'] * duracion_ejecucion
            t += duracion_ejecucion
            p['ejecutado'] = p.get('ejecutado', 0) + duracion_ejecucion
            if duracion_ejecucion > 0:
                print("    ⌚ %s %d tick" % (p['nombre'], duracion_ejecucion))
            # Movemos el proceso actual al nivel anterior si no ha terminado su ejecución
            if duracion_ejecucion < duracion_restante:
                if i-1 >= 0:
                    colas[i-1].append(p)
                else:
                    colas[i].append(p)
                break
            else:
                if p['nombre'] not in procesos_terminados:
                    print("   Proceso terminado!!!")
                    procesos_terminados.append(p['nombre'])
                    p['fin'] = t
                    p['T'] = p['fin'] - p['llegada']
                    p['E'] = p['T'] / p['duración']
                cola.popleft()

print("Planificación realizada: \n" + res)
print("Tabla de ejecución:")
print('{:<7}  {:<7} {:<7} {:<7} {:<7} {:<7}'.format('Proceso','Inicio','Fin','T','E','P'))
for proc in procesos:
    # print("%2s      %d    %d    %d  %.2f  %.2f" % (proc['nombre'], proc['llegada'], proc['fin'], proc['T'], proc['E'], proc['duración']))
    print('{:<7}  {:<7} {:<7} {:<7} {:<7} {:<7}'.format(proc['nombre'], proc['llegada'], proc['fin'], proc['T'], proc['E'], proc['duración']))
promedio_E = sum([proc['E'] for proc in procesos]) / len(procesos)
promedio_P = sum([proc['duración'] / proc['E'] for proc in procesos]) / len(procesos)

