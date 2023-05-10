from random import randint

procesos = []
primer_proc = 'A'

#Crea procesos con cargas de trabajo totales de entre 80 y 120 ticks
def gen_procesos(): 
    var = randint(5,8)
    dur1 = round(80/var)
    dur2 = round(120/var)
    print("Var: %d" %var)
    print("Dur1: %d" %dur1)
    print("Dur2: %d" %dur2)
    for i in range(var):
      procesos.append({'nombre': chr(ord(primer_proc)+i),
                        'llegada': randint(0,dur2*i),
                       'duración': randint(dur1,dur2),
                       'prioridad': 0,
                       })
    print('Lista de procesos:')
    print("Proceso\tLlegada\tDuración")
    for proc in procesos:
        print("%2s\t%3d\t%3d" % (proc['nombre'], proc['llegada'], proc['duración']))
    multinivel();

def multinivel():
    #Como durante el proceso modifica varias veces la duración del proceso para saber en que momento
    #finaliza, se guardarán todos tiempos de ejecución en un arreglo.
    resp=[]
    for proc in procesos:
        resp.append(proc['duración'])


    #Algunas utilidades
    print('Planificación multinivel')
    n=1
    Q=1
    t = 0
    res = ''
    recorrido=True
    recorrer=True
    orden=sorted(procesos, key=lambda p: p['llegada'])
    enactivo=[]
    fin=[]
    priomin=0


    print('* Inicia ejecución')
    while t<=120:
        #Verifica el número minimo de todas las colas. Si esta no es cero, entonces resta todas las prioridades
        #para que la mínima sea de cero (esto para no manejar quantums muy grandes más adelante)
        for proc in orden:
            recorrer=True
            if proc['prioridad']==priomin:
                recorrer=False
                break
        if recorrer==True:
            for proc in orden:
                proc['prioridad']-=1
            print("\tTodas las colas bajan de prioridad un nivel")

        #Se realizan condicionales, ¿el proceso ya se está ejecutando? ¿ya terminó de ejecutarse? Los procesos con
        #los que se trabajen durante el tiempo analizada son guardadas en otra lista para saber cuales habrá que considerar.
        print("t%d:\n" % t)
        for proc in orden: 
            if proc['llegada']<=t:
                enactivo.append(proc)
            if proc['duración']<=0:
                enactivo.pop()

        #Con todos los procesos involucrados, se ordenará de menor a mayor la prioridad y el primer elemento que salga
        #de la lista será el ejecutado en el tic.
        if(len(enactivo)!=0):
            enactivo=sorted(enactivo,key=lambda p:p['prioridad']) #ordena por prioridad
            Q=2**(enactivo[0]['prioridad'])
            print("\tTamaño del Quantum: %d"%Q)
            #for proc in enactivo:
            #    proc['duración']-=1

            #Verifica si un proceso ya terminó.
            if enactivo[0]['duración'] <= Q:
                Q=enactivo[0]['duración']
                print("\t//%s ya terminó//"%(enactivo[0]['nombre']))
                fin.append({'nombre': enactivo[0]['nombre'],
                            'fin': t+Q,
                            })
            enactivo[0]['duración']-=Q
            print("\t⌚tick... Proceso: %s Duración restante %d Prioridad %d" % (enactivo[0]['nombre'], enactivo[0]['duración'],enactivo[0]['prioridad']))
            if enactivo[0]['duración'] >= Q:
                enactivo[0]['prioridad']+=1
                print("\tProceso %s sube de prioridad a %d" % (enactivo[0]['nombre'], enactivo[0]['prioridad']))
            res += enactivo[0]['nombre']*Q
            t=t+Q
        else:
            #En esta parte se menejan los posibles espacíos vacíos, un espacio vacío puede significar que un proceso aún no llega mientras
            #los demás terminan, o bien, que el programa ya terminó. Se hace prueba con la duración de los procesos (la cual va gradualmente
            #disminuyendo para ilustrar el avance y término del proceso
            recorrido=True
            for proc in orden:
                if proc['duración']>0:
                    print("    ... %d tick")
                    recorrido=False
                    t=t+Q
                    res += '-'*Q
                    break
            if recorrido==True:
                print("\tFinalizado\n")
                break
        enactivo.clear();

    print("Planificación realizada:" + res)
    print("Duración total: %d" % t)

    fin=sorted(fin, key=lambda p: p['nombre'])
    i=0

    inicio=0
    end=0
    duracion=0
    tiempo=0


    print("\n\n\t  ///Tabla de ejecución///")
    print("Proceso\tInicio\tFin\tT\tE\tP")
    for p in procesos:
        inicio=p['llegada']
        end=fin[i]['fin']
        tiempo=resp[i]
        duracion=end-inicio
        espera=duracion-tiempo
        penalty=round(duracion/tiempo,2)
        print("%2s\t%3d\t%3d\t%3d\t%3d\t" % (p['nombre'], inicio, end, duracion,espera),penalty)
        i=i+1

gen_procesos();