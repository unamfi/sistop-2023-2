from random import randint

procesos = []
primer_proc = 'A'

for i in range(randint(5,8)): # Genero los 5 a 8 procesos aleatorios
    procesos.append({'nombre': chr( ord(primer_proc)+i ),
                     'tickets': randint(0, 10*i),
                     'duración': randint(80,120)
                     })

print('Lista de procesos:\n\nProceso   Tickets   Duracion\n')
for proc in procesos:
    print("  %2s        %3d        %3d" % (proc['nombre'], proc['tickets'], proc['duración']))

# Calcular la cantidad total de tickets
total_tickets = sum([p['tickets'] for p in procesos])

t = 0
res = ''
print('\n - Comenzemos 😎 -\n')
while total_tickets > 0:
    # Seleccionar un número aleatorio entre 0 y el total de tickets
    n = randint(0, total_tickets-1)
    # Seleccionar el proceso que tenga el ticket ganador
    p = None
    for proc in procesos:
        if n < proc['tickets']:
            p = proc
            break
        else:
            n -= proc['tickets']
    # Manejar el caso en el que el proceso aún no llega
    if t < p['tickets']:
        demora = p['tickets'] - t
        res += '-' * demora
        t += demora
        print("t=%d" % t)
    # Ejecutar el proceso
    duracion = min(p['duración'], total_tickets)
    res += p['nombre'] * duracion
    p['duración'] -= duracion
    total_tickets -= duracion
    t += duracion
    print("t=%d  ⌚ %s %d tick" % (t, p['nombre'], duracion))
    # Eliminar el proceso si ya ha terminado
    if p['duración'] == 0:
        procesos.remove(p)

print("\n - Orden de los resultados por loteria 🤓 : -\n" + res)
print("\n - Duración total ⏱️ : %d -" % t)
