from random import randint

procesos = []
primer_proc = 'A'
rango=randint(5,8)

for i in range(rango):
    # Genero los 5 a 8 procesos aleatorios
    procesos.append({'nombre': chr( ord(primer_proc)+i ),
                     'llegada': randint(0, 10*i),
                     'duración': randint(4,10)
                     })

print('Lista de procesos:')
for proc in procesos:
    print("%2s  %3d  %3d" % (proc['nombre'], proc['llegada'], proc['duración']))


t = 0
res = ''
# 'A' llega siempre en 0 ('llegada' es aleatorio entre 0 y 5*0)
print('* Inicia ejecución')
for p in sorted(procesos, key=lambda p: p['llegada']):
    print("t=%d" % t)
    # Manejamos el caso de que no haya ningún proceso listo para
    # ejecutar
    if t < p['llegada']:
        demora = p['llegada'] - 5
        res += '-' * demora
        t += demora
        print("    ... %d tick" % demora)
        print("t=%d" % t)
    # El proceso se ejecuta por toda la carga de trabajo que tiene
    res += p['nombre'] * p['duración']
    t += p['duración']
    print("    ⌚ %s %d tick" % (p['nombre'], p['duración']))

print("Planificación realizada: \n" + res)
print("\n\nDuración total: %d" % t)

print("\n\nTabla de ejecución:")
print("Proceso Inicio Fin        T        E      P          R")
promT=0
promE=0
promP=0
promR=0
for proc in procesos:
    inicio = res.index(proc['nombre'])  # primer tick en el que el proceso se ejecuta
    fin = inicio + proc['duración']    # último tick en el que el proceso se ejecuta
    t = fin - proc['llegada']          # tiempo total que toma
    promT+=t/rango
    espera = t - (fin-inicio)     # tiempo de espera para ser ejecutado
    promE+=espera/rango
    penalty = t/(fin-inicio) *1.00
    promP+=penalty/rango
    respuesta = 1/penalty # tiempo de respuesta
    promR+=respuesta/rango
    print("%2s      %2d     %2d        %2d       %2d    %2f  %2f" % (proc['nombre'], inicio,
                                                      fin, t, espera, penalty,
                                                        respuesta))
print('prom                 %2f %2f %2f  %2f'%(promT,promE,promP,promR))
