#!/usr/bin/python3
#
from random import randint, random

def generacion_procesos():
    procesos = [{'nombre': chr(ord('A') + i),
                 'llegada': randint(0, 10 * i),
                 'duración': randint(4, 20),
                 'prioridad': randint(1, 5)}
                for i in range(randint(5, 8))]
    return procesos

def Tabla1(procesos):
    print("Carga de trabajo a simular en Lotería:")
    print("Tabla de carga de trabajo:")
    print("{:<8s}|{:>8s}|{:>8s}|{:>8s}".format("Proceso", "Duración", "Llegada", "Prioridad"))
    print("----------------+--------+--------+--------")
    for proceso in procesos:
        print("{:<8s}|{:>8d}|{:>8d}|{:>8d}".format(proceso['nombre'], proceso['duración'], proceso['llegada'], proceso['prioridad']))
    print("----------------+--------+--------+--------")

def planificacion_loteria(procesos):
    # Asigna un número de lotería a cada proceso según su prioridad
    tickets = []
    for proceso in procesos:
        for i in range(proceso['prioridad']):
            tickets.append(proceso['nombre'])
    
    # Ordena los procesos por su llegada
    procesos_ordenados = sorted(procesos, key=lambda p: p['llegada'])
    
    t = 0
    res = ''
    print('* Inicia ejecución')
    while procesos_ordenados:
        # Verifica si no hay más procesos pendientes
        if not tickets or not procesos_ordenados:
            break
        
        # Obtén el proceso que va a ejecutar en esta ronda por sorteo
        ticket_elegido = randint(0, len(tickets) - 1)
        proceso_elegido = None
        
        for p in procesos_ordenados:
            if p['nombre'] == tickets[ticket_elegido]:
                proceso_elegido = p
                break
        
        if proceso_elegido is None:
            tickets.remove(tickets[ticket_elegido])
            continue
        
        # Si el proceso llega después del tiempo actual, espera
        if t < proceso_elegido['llegada']:
            demora = proceso_elegido['llegada'] - t
            res += '-' * demora
            t += demora
            print("t={}: ... {} tickets sin agarrar".format(t, demora))
        
        # Ejecuta el proceso elegido
        res += proceso_elegido['nombre'] * proceso_elegido['duración']
        print("t={} antes de ingresar nuevo proceso".format(t))
        for i in range(t+proceso_elegido['duración'],t, -1):
            print("\t ⚙️  {} ingresando".format(proceso_elegido['nombre']))
        t += proceso_elegido['duración']
        print("t={}: ⚙️  {} finaliza con {} tickets ganados".format(t, proceso_elegido['nombre'], proceso_elegido['duración']))
        
        # Actualiza la lista de procesos pendientes y los tickets
        procesos_ordenados.remove(proceso_elegido)
        tickets.remove(proceso_elegido['nombre'])
        
    return res, t

    
def Calculos(procesos, res):
    pT=0;pE=0;pP=0;pR = 0
    for proc in procesos:
        inicio = res.index(proc['nombre'])
        fin = inicio + proc['duración']
        t = fin - proc['llegada']
        t1 = fin - inicio
        pT += t / len(procesos)
        espera = t - (fin - inicio)
        pE += espera / len(procesos)
        P = t / (fin - inicio) * 1.00
        pP += P / len(procesos)
        R = 1 / P
        pR += R / len(procesos)
        print("{:^8s}|{:^8d}|{:^5d}|{:^8d}|{:^8d}|{:^14.2f}|{:^10.2f}".format(
                proc['nombre'], inicio, fin, t1, espera, P, R))
    
    return pT, pE, pP, pR

def Tabla2(procesos, res):
    print("Planificación realizada: \n" + res)
    print("\n\nDuración total: %d" % len(res))

    print("\n\nTabla de ejecución:")
    print("Tabla de ejecución:")
    print("Proceso | Inicio | Fin | Tiempo | Espera | Penalización | Respuesta")
    print("--------+--------+-----+--------+--------+--------------+----------")
    pT, pE, pP, pR = Calculos(procesos, res)
    print("--------+--------+-----+--------+--------+--------------+----------")
    print('Promedio|        |     |%7.2f |%6.2f  |%9.2f     |%7.2f' % (pT, pE, pP, pR))
    print("--------+--------+-----+--------+--------+--------------+----------")

procesos = generacion_procesos()
Tabla1(procesos)
res, duration = planificacion_loteria(procesos)
Tabla2(procesos, res)



