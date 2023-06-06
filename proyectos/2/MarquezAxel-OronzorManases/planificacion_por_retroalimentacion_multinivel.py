#!/usr/bin/python3
#
from random import randint

def generacion_procesos():
    procesos = [{'nombre': chr(ord('A') + i),
                 'llegada': randint(0, 10 * i),
                 'duración': randint(4, 10)} #Aqui en varias ejecuciones se puede mostrar huecos
                 #'duración': randint(4, 20)} #Aqui ya es poco probable que presente huecos
                for i in range(randint(5, 8))]

    return procesos

def Tabla1(procesos):
    print("Carga de trabajo a simular en Retroalimentación Multinivel:")
    print("Tabla de carga de trabajo:")
    print("{:<8s}|{:>8s}|{:>8s}".format("Proceso", "Duración", "Llegada"))
    print("----------------+--------+--------")
    for proceso in procesos:
        print("{:<8s}|{:>8d}|{:>8d}".format(proceso['nombre'], proceso['duración'], proceso['llegada']))
    print("----------------+--------+--------")


def ejecucion_procesos(procesos):
    t = 0
    res = ''
    print('* Inicia ejecución')
    
    # Lista de colas de procesos
    colas = [[] for _ in range(3)]  # 3 niveles de colas
    quantum = [4, 8, 12]  # Quantum para cada nivel
    
    # Parte donde se distribuyen los procesos en las colas según su llegada
    for proceso in procesos:
        nivel = 0
        if proceso['llegada'] >= 10:
            nivel = 2
        elif proceso['llegada'] >= 5:
            nivel = 1
        colas[nivel].append(proceso)
    
    while any(cola for cola in colas):
        for i, cola in enumerate(colas):
            if cola:
                proceso = cola.pop(0)
                print("t=%d" % t)
                if t < proceso['llegada']:
                    demora = proceso['llegada'] - t
                    res += '-' * demora
                    t += demora
                    print("    ... %d tick" % demora)
                    print("t=%d" % t)
                
                duracion_restante = proceso['duración']
                if duracion_restante <= quantum[i]:
                    res += proceso['nombre'] * duracion_restante
                    t += duracion_restante
                    print("    ⌚ %s %d tick (Nivel %d)" % (proceso['nombre'], duracion_restante, i+1))
                else:
                    res += proceso['nombre'] * quantum[i]
                    t += quantum[i]
                    print("    ⌚ %s %d tick (Nivel %d)" % (proceso['nombre'], quantum[i], i+1))
                    proceso['duración'] -= quantum[i]
                    cola.append(proceso)
                break

    return res, t

def calculos(procesos, res):
    pT = 0;pE = 0;pP = 0;pR = 0
    for proc in procesos:
        inicio = res.index(proc['nombre'])
        fin = inicio + proc['duración']
        t = fin - proc['llegada']
        t1 = fin - inicio
        pT += t / len(procesos)
        E = t - (fin - inicio)
        pE += E / len(procesos)
        P = t / (fin - inicio) * 1.00
        pP += P / len(procesos)
        R = 1 / P
        pR += R / len(procesos)
        print("{:^8s}|{:^8d}|{:^5d}|{:^8d}|{:^8d}|{:^14.2f}|{:^10.2f}".format(
                proc['nombre'], inicio, fin, t1, E, P, R))
    
    return pT, pE, pP, pR

def Tabla2(procesos, res):
    print("Planificación realizada: \n" + res)
    print("\n\nDuración total: %d" % len(res))
    print("\n\nTabla de ejecución:")
    print("Proceso | Inicio | Fin | Tiempo | Espera | Penalización | Respuesta")
    print("--------+--------+-----+--------+--------+--------------+----------")
    pT, pE, pP, pR = calculos(procesos, res)
    print("--------+--------+-----+--------+--------+--------------+----------")
    print('Promedio|        |     |%7.2f |%6.2f  |%9.2f     |%7.2f' % (pT, pE, pP, pR))
    print("--------+--------+-----+--------+--------+--------------+----------")

procesos = generacion_procesos()
Tabla1(procesos)
res, duration = ejecucion_procesos(procesos)
Tabla2(procesos, res)

