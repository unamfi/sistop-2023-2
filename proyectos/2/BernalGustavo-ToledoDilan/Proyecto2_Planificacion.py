from random import randint

procesos = []
primer_proc = 'A'
rango=randint(5,8)

for i in range(rango):
    # Genero los 5 a 8 procesos aleatorios
    llegada=randint(0, 15*i)
    if(i==(rango-1)and llegada<80):
        llegada=80
        print(i)
        #para que la instruccion de 80-120 ticks se cumpla, forzamos a que el ultimo parametro lo haga
    procesos.append({'nombre': chr( ord(primer_proc)+i ),
                     'llegada': llegada,
                     'duración': randint(4,10)
                     })
print('Lista de procesos:')
print('Proceso   Llegada   Duración')
for proc in procesos:
    print("%2s         %3d        %3d" % (proc['nombre'], proc['llegada'], proc['duración']))
t = 0
res = ''
# 'A' llega siempre en 0 ('llegada' es aleatorio entre 0 y 5*0)
print('* Inicia ejecución')
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
    print("    ⌚ %s %d tick" % (p['nombre'], p['duración']))

print("Planificación realizada: \n" + res)
print("\n\nDuración total: %d" % t)

print("\n\nTabla de ejecución:")
print("Proceso Inicio Fin        T        E      P          R")
PromedioT=0
PromedioE=0
PromedioP=0
PromedioR=0
for proc in procesos:
    inicio = res.index(proc['nombre'])  # primer tick en el que se ejecuta el proceso
    fin = inicio + proc['duración']    # último tick en el que se ejecuta el proceso
    t = fin - proc['llegada']          # tiempo total que toma el trabajo
    PromedioT+=t/rango
    espera = t - (fin-inicio)     # tiempo que esperó el proceso para ejecutarse
    PromedioE+=espera/rango
    penalizacion = t/(fin-inicio) *1.00      # tiempo de penalización
    PromedioP+=penalizacion/rango
    respuesta = 1/penalizacion # fracción de tiempo de respuesta
    PromedioR+=respuesta/rango
    print("%2s      %2d     %2d        %2d       %2d    %2f  %2f" % (proc['nombre'], inicio,
                                                      fin, t, espera, penalizacion,
                                                        respuesta))
print('Prom                 %2f %2f %2f  %2f'%(PromedioT,PromedioE,PromedioP,PromedioR))