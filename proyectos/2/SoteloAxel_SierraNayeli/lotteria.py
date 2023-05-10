import random

procesos = []
boletos = []
llegadas = []
procesosEjecucion = []
procesosNoEjecucion = ['A','B','C','D','E','F','G','H']
noProcesos = random.randint(5, 8)
noBoletosTotal = 960

listaPrioridad = [1, 2, 3, 4, 5, 6, 7, 8]

def ejecutarProceso(procesos, ganador):
    # Código a ejecutar para el proceso ganador
    resu = ''
    for proceso in procesos:
        if proceso['nombre'] == ganador:
            print(f"Proceso {proceso['nombre']} es el ganador del sorteo y se va a ejecutar.")    
            for i in range(proceso['duracion']):
                print(proceso['nombre'], end="")
                resu = resu + proceso['nombre']
    
    return resu

def loteria(array):
    boletoGanador = random.choice(array)
    print(f'Ganador: {boletoGanador}')
    return boletoGanador

def generarBoletos(procesos):
    boletos = []
    for proceso in procesos:
        for i in range(proceso['prioridad']):
            boletos.append(proceso['nombre'])
    return boletos

#se crean los procesos
for i in range(noProcesos):
    #se toma un valor aleatorio de la lista prioridad para asignarlo al proceso
    prioridad = random.choice(listaPrioridad)
    #se elimina el valor escogido para no volverlo a seleccionar
    listaPrioridad.remove(prioridad)

    #se genera un valor en donde se aparece el proceso
    llegada = random.randint(80, 120)
    #se agrega ese valor a una lista donde estaran todos los valores de llegada
    llegadas.append(llegada)

    #se crea el proceso
    proceso = {
        'nombre': chr(ord('A') + i),
        'llegada': llegada,
        'duracion': random.randint(5, 12),
        'prioridad': prioridad,
    }

    #se agrega el proceso a la lista de procesos
    procesos.append(proceso)



#SE INICIA EL CODIGO

#Se muestran los procesos
print('Carga de procesos:')
print('Nombre  Llegada  Duración Prioridad')
for proc in procesos:
    print('%6s  %7d  %8d %8d' %
          (proc['nombre'], proc['llegada'], proc['duracion'], proc['prioridad']))


#Se ordenan las llegadas de menor a mayor y se imprimen
llegadas = sorted(llegadas)
print("Llegadas: ",end="")
print(llegadas)

#Se inician los procesos
print('\nIniciando procesos')
res = ""
print('* Inicia ejecución')

#se recorre la lista ordenada por el valor de llegada de procesos
for indice, p in sorted(enumerate(procesos), key=lambda x: x[1]['llegada']):
    
    #Guardo llegada en temp
    temp = p['llegada']
    print(p['nombre'], end='')
    procesosEjecucion.append(p)
    procesosNoEjecucion.remove(p['nombre'])

    for i in range(p['duracion']):
        temp=temp+1
        print(p['nombre'], end='')
        res = res + p['nombre']
        if(temp in llegadas):
            print('\nNuevo proceso entrando')
            if indice + 1 < len(procesos):
                #es el siguiente proceso
                siguienteProceso = procesos[indice + 1]
                procesosEjecucion.append(siguienteProceso)
                print('Se hace loteria para ver quien sigue')
                boletos = generarBoletos(procesosEjecucion)
                boletoGanador  = loteria(boletos)
                if loteria != p['nombre']:
                    res = res + ejecutarProceso(procesosEjecucion, boletoGanador )
    

print('\n\nresultado final:')
print(res)
        

    

    
