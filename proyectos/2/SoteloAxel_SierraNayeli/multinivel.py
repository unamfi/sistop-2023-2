import random

procesos = []
boletos = []
llegadas = []
procesosEjecucion = []
noProcesos = random.randint(5, 8)
noBoletosTotal = 960
prioridadUno = []
prioridadDos = []
prioridadTres = []

ticketMinimo = 5
ticketMaximo = 1

def ejecutarProceso(proceso):
    resu = ''
    #Se ejecutan todos los procesos de aqui
    for i in range(p['duracion']):
        print(proceso['nombre'], end='')
        resu = resu+proceso['nombre']
    return resu

for i in range(noProcesos):
    #Se genera un numero aleatorio enre 80 y 120 para saber en qué momento va a llegar el proceso
    llegada = random.randint(80, 120)
    #Se agrega el momento de llegada a la lista llegadas
    llegadas.append(llegada)

    #se genera un numero aleatorio entre 1 y 3 para saber en que lista se guardará
    prioridad = random.randint(1,3)
    
    #Se crea el proceso y después se va a agregar a la lista de procesos
    proceso = {
        'nombre': chr(ord('A') + i),
        'llegada': llegada,
        'duracion': random.randint(ticketMinimo, ticketMaximo),
        'prioridad': prioridad,
        'inicio':0,
        'fin':0,

    }

    #Agregando proceso a lista de procesos
    procesos.append(proceso)

    #Dependiendo la prioridad se agrega a una lista.
    if prioridad == 1:
        prioridadUno.append(proceso)
    elif prioridad == 2:
        prioridadDos.append(proceso)
    elif prioridad == 3:
        prioridadTres.append(proceso)


#Se imprimen los detalles de cada proceso
print('Detalles de procesos:')
print('Nombre  Llegada  Duración Prioridad')
for proc in procesos:
    print('%6s  %7d  %8d %8d' %
          (proc['nombre'], proc['llegada'], proc['duracion'], proc['prioridad']))

#Se ordena la lista de las llegadas para saber que proceso iniciara
llegadas = sorted(llegadas)
print("llegadas: ", end="")
print(llegadas)


#Se da inicio a los procesos
print('\nIniciando procesos')
t = 0
res = ''
print('* Inicia ejecución')

#Se recorren todos los procesos
for indice, p in sorted(enumerate(procesos), key=lambda x: x[1]['llegada']):
    
    print(f't = {t}')
    print(p['nombre'], end='')
    print(' prioridad:'+str(p['prioridad']))
    temp = p['llegada']
    
    #Se recorre cada ticks del proceso
    for i in range(p['duracion']):
        t=t+1
        print(p['nombre'], end='')
        res = res + p['nombre']
        if(temp in llegadas):
            if len(llegadas) != 0:
                llegadas.remove(temp) 
            #Se comprueba que haya un proceso siguiente
            if indice + 1 < len(procesos):
                #en caso de que si se comprueba su prioridad
                siguienteProceso = procesos[indice + 1]
                #Se comprueba que prioridad tiene el siguiente proceso
                if siguienteProceso['prioridad'] >= p['prioridad']:
                    print('\nCambio de proceso por prioridad, ahora ejecutando '+siguienteProceso['nombre'])
                    procesos.remove(siguienteProceso)
                    res = res+ejecutarProceso(siguienteProceso)
                    t=t+siguienteProceso['duracion']
        temp = temp+1
    print("    \n       ⌚ %s %d tick" % (p['nombre'], t))
    

print(f"\nPlanificación realizada: {res}")
print("Duración total: %d" % t)
# print('Proceso  Inicio   Fin')
# procesos2 = sorted(procesos2, key=lambda x: x['prioridad'])
# for proceso in procesos2:
#     print(proceso['nombre'] + '         '+str(proceso['llegada']) + '      ' +str(proceso['duracion']))