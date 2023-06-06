# Aranzúa Chávez César Octavio
# Lenguaje d Programación: Python

from random import randint

procesos = []
primer_proc = 'A'

for i in range(randint(5, 8)):
    procesos.append({'nombre': chr(ord(primer_proc)+i),
                     'llegada': randint(0, 10*i),
                     'duración': randint(8, 150)
                     })

print('Lista de procesos:')
print(' Proceso\t Duración\t Llegada')

for proc in procesos:
    print(f"{proc['nombre']}\t\t    {proc['llegada']}\t\t  {proc['duración']}")
    # print("%2s  %3d  %3d" % (proc['nombre'], proc['llegada'], proc['duración']))


t = 0
res = ''
ejecucion = []
# 'A' llega siempre en 0 ('llegada' es aleatorio entre 0 y 5*0)
print('\n==*** Inicia ejecución ***==')
while procesos:
    print(f"t={t}")
    # Manejamos el caso de que no haya ningún proceso listo para ejecutar
    if t < procesos[0]['llegada']:
        demora = procesos[0]['llegada'] - t
        res += '-' * demora
        t += demora
        print(f"    ... {demora} tick")
        print(f"t={t}")
    # Generamos un número aleatorio en el rango de la suma de las duraciones
    # de los procesos restantes
    suma_duracion = sum(p['duración'] for p in procesos)
    loteria = randint(0, suma_duracion-1)
    i = 0

    # Buscamos el proceso ganador de la lotería
    while loteria >= procesos[i]['duración']:
        loteria -= procesos[i]['duración']
        i += 1
    p = procesos.pop(i)
    ejecucion.append(
        {'nombre': p['nombre'], 'inicio': t, 'fin': t+p['duración']})

    # El proceso se ejecuta por toda la carga de trabajo que tiene
    res += p['nombre'] * p['duración']
    t += p['duración']
    print(f"    ⌚ {p['nombre']} {p['duración']} ticks")

print("Planificación realizada: \n" + res)
print(f"Duración total: {t}\n\n")

print("Tabla de ejecución:")
print("Proceso  | Inicio  | Fin")
for e in ejecucion:
    print(f"   {e['nombre']}     |   {e['inicio']}     |   {e['fin']}")
