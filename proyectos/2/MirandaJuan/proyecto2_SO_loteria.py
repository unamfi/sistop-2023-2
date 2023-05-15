import random
import time

procesos = []
primer_proc = 'A'
total_tiempo = random.randint(80, 120)

for i in range(random.randint(5, 8)):
    # Genero los 5 a 8 procesos aleatorios
    procesos.append({'nombre': chr(ord(primer_proc)+i),
                     'llegada': random.randint(0, total_tiempo),
                     'duración': random.randint(5, 20)
                     })

print('Lista de procesos:')
for proc in procesos:
    print("%2s  %3d  %3d" % (proc['nombre'], proc['llegada'], proc['duración']))
time.sleep(1)
t = 0
res = ''
# 'A' llega siempre en 0 ('llegada' es aleatorio entre 0 y 5*0)
print('\n* Inicia ejecución\n')
for p in sorted(procesos, key=lambda p: p['llegada']):
    print("t=%d" % t)
    # Manejamos el caso de que no haya ningún proceso listo para
    # ejecutar
    if t < p['llegada']:
        demora = p['llegada'] - t
        res += '-' * demora
        t += demora
        print("    ... %d tick" % demora)
        print("t=%d" % t)
    # El proceso se ejecuta por toda la carga de trabajo que tiene
    res += p['nombre'] * p['duración']
    t += p['duración']
    # Calculamos P y R para el proceso
    T = t - p['llegada']  # Tiempo de retorno
    t_estimado = sum([proc['duración'] for proc in procesos if proc['llegada'] <= t])  # Tiempo estimado de los procesos que ya llegaron
    p['P'] = T / p['duración']
    p['R'] = t_estimado / T
    print("    ⌚ %s %d tick" % (p['nombre'], p['duración']))
    print("    |   Llegada: %d   Duración: %d   Tiempo inicio: %d   Tiempo fin: %d  P=%.2f  R=%.2f"   % (p['llegada'], p['duración'], t-p['duración'], t, p['P'], p['R']) )
    print("    ----------------------------------------------------")
    
time.sleep(1)
print("Planificación realizada: \n" + res)
print("\nDuración total: %d\n" % t)


repeticiones = {}
for p in res:
    if p in repeticiones:
        repeticiones[p] += 1
    else:
        repeticiones[p] = 1

mas_repetido = max(repeticiones, key=repeticiones.get)
menos_repetido = min(repeticiones, key=repeticiones.get)
time.sleep(1)
print("\nEl proceso más repetido es", mas_repetido, "con", repeticiones[mas_repetido], "repeticiones")
print("El proceso menos repetido es", menos_repetido, "con", repeticiones[menos_repetido], "repeticiones")


