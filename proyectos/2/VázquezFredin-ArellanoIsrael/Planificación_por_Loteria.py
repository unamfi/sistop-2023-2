import random

# ---------------------------------
# -- Retroalimentación multinvel --
# ---------------------------------

                                    # Creación de procesos por medio de un mapa
procesos = []        # Diccionario de procesos - mapa
procesos_terminados = {}
contador_procesos_terminados = 0
planificacion_realizada = ''

for i in range(random.randint(5,8)):
    procesos.append({
        'id':str(chr(ord('A') + i)),
        'llegada':random.randint(10,15),
        'salida':0,
        'duracion':random.randint(10,15),
        'boletos':0,
        'ticks':0,
        'iniciado':False            # Cuando es falso es porque es posible modificar el tick en donde va llegar el proceso
    })




#   ################################################
#   ## Carga de trabajo a simular de cada proceso ##
#   ################################################

print("\nCarga de trabajo a simular durante la ejecución del programa:")

# Se procede a imprimir la tabla de información de los procesos
print("| Proceso | Duración | Llegada |")

for i in procesos:
    print("      " + str(i['id']) + "       " + str(i['duracion']) + "          " + str(i['llegada']))
    procesos_terminados[i['id']] = 0


# Ejecución de ticks
def ejecucion_trabajo(i):
    contador = 0
    print("Proceso: "+str(i['id'])+"    Ejecutando",end='')
    for _ in range(quantum):
        contador = contador+1

        print(" "+str(contador)+" tick...      ",end='')
        i['ticks'] = i['ticks'] + 1
        if(i['ticks'] == i['duracion']):
            print(" \U000026AA Proceso: "+i['id']+" terminado.")
            return (True,contador)
    print()
    return (False,contador)





#   ############################
#   ## Repartición de boletos ##
#   ############################

quantum = 3 # Duración de 3 ticks

print("\n---------------------------\nQuantum: "+str(quantum)+"\n---------------------------\n")



for i in procesos:
    tmp = random.randint(1,1000)
    i['boletos'] =  tmp
    
izquierda = 0
print("| Proceso | Cantidad de boletos ")
for i in sorted(procesos, key=lambda i:i['boletos']):
    print("     "+str(i['id'])+"        "+str(i['boletos']))
    izquierda = izquierda+i['boletos']





#   #############################
#   ## Sorteo con 1000 boletos ##
#   #############################
ticks_global = 0
boletos_total = 0
procesos_listos = []


# Primera sección
'''
En esta primera parte se trata a todos aquellos que van llegando
'''
for p_Wait in sorted(procesos, key=lambda p_Wait:p_Wait['llegada']):

    procesos_listos.append(p_Wait)

    buscando_ganador = 0
    boletos_total = boletos_total + p_Wait['boletos']
    
    print("\U0001F4A2 Tick actual = "+str(ticks_global))
    print(" \n-- !Se inicia el gran sorteo¡ -- \n")
    winner  = random.randint(1,boletos_total)
    print("Boleto ganador: "+str(winner)+"\n")

    # Siempre se escoge un proceso, siempre está ocupado el procesador, excepto si no hay procesos 
    # Buscando al proceso
    for i in procesos_listos:
        if(procesos_terminados[i['id']] == 0):
            buscando_ganador = buscando_ganador + i['boletos']

            if((buscando_ganador >= winner)):
                
                # Checando si es la primera vez que se llama
                if(i['iniciado'] == False):
                    # Primera vez, por ende se coloca su inicio
                    i['llegada'] = ticks_global
                    i['iniciado'] = True
                

                print(" \U0001F7E2 Proceso seleccionado: " + i['id']+"\n")
                

                # Se hace la ejecución del quantum
                tmp_c = 0
                isOver = False
                (isOver,tmp_c) = ejecucion_trabajo(i)

                ticks_global = ticks_global + tmp_c

                for i_ in range(tmp_c):
                    planificacion_realizada = planificacion_realizada + i['id'] + " "

                if(isOver):
                    # Colocando el tick del final:
                    i['salida'] = ticks_global

                    # Si ya terminó entonces se quita sus boletos de la suma 
                    procesos_terminados[i['id']] = 1
                    contador_procesos_terminados = contador_procesos_terminados + 1
                    boletos_total = boletos_total - i['boletos']

                    


                # Se procede a buscar otro
                break

# Segunda sección
'''
Probablemente, no todos los procesos terminaron anteriormente, en esta segunda parte se trata para terminar de ejecutar los procesos y que vayan saliendo.
'''

while(contador_procesos_terminados < len(procesos)):

    buscando_ganador = 0

    print("\U0001F4A2 Tick actual = "+str(ticks_global))
    print(" \n-- !Se inicia el gran sorteo¡ -- \n")
    winner  = random.randint(1,boletos_total)
    print("Boleto ganador: "+str(winner)+"\n")
    
    # Ya llegaron todos los procesos, ahora me importa ordenarlos por cantidad de boletos
    for p_Wait in sorted(procesos_listos, key = lambda p_Wait:p_Wait['boletos']):

        # Revisar si no ha terminado 
        if(procesos_terminados[p_Wait['id']] == 0):
            buscando_ganador = buscando_ganador + p_Wait['boletos']
            

            if((buscando_ganador >= winner)):
                # Se encontró al proceso ganador
                print(" \U0001F7E2 Proceso seleccionado: " + p_Wait['id']+"\n")
                
                
                # Se hace la ejecución del quantum
                tmp_c = 0
                isOver = False
                (isOver,tmp_c) = ejecucion_trabajo(p_Wait)

                ticks_global = ticks_global + tmp_c

                for i_ in range(tmp_c):
                    planificacion_realizada = planificacion_realizada + p_Wait['id'] + " "
                    

                if(isOver):
                    # Colocando el tick del final:
                    p_Wait['salida'] = ticks_global
                    
                    # Si ya terminó entonces se quita sus boletos de la suma 
                    procesos_terminados[p_Wait['id']] = 1
                    contador_procesos_terminados = contador_procesos_terminados + 1
                    boletos_total = boletos_total - p_Wait['boletos']

                    


                # Se procede a buscar otro
                break


# #################
# ## Finalizando ##
# #################

print("\nTabla de ejecución: ")
print("Planificación realizada: " + planificacion_realizada + " longitud " + str(len(planificacion_realizada)))
print("\n --------------------------------------------------\n| Proceso | Inicio |  Fin  |   T   |   E   |   P   |\n --------------------------------------------------\n")

for i in procesos_listos:
        print("    "+str(i['id']) +"         "+ str(i['llegada']) +"        "+ str(i['salida']) 
        +"     "+ str(i['salida']-i['llegada']) +"      "+ str( (i['salida']-i['llegada'])-i['duracion'] ) +"       "+ str( (i['salida']-i['llegada'])/i['duracion'] ))
        