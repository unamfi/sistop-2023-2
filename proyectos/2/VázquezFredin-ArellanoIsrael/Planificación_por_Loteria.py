import random

# Planificación por loteria

                                    # Creación de procesos por medio de un mapa
procesos = []        # Diccionario de procesos - mapa
procesos_terminados = {}
contador_procesos_terminados = 0

for i in range(random.randint(5,8)):
    procesos.append({
        'id':str(chr(ord('A') + i)),
        'llegada':random.randint(0,10*i),
        'duracion':random.randint(4,10),
        'boletos':0
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
        contador = contador+_

        print(" "+str(_)+" tick...      ",end='')
        i['duracion'] = i['duracion']-1
        if(i['duracion'] == 0):
            print("Proceso: "+i['id']+" terminado.")
            procesos_terminados[i['id']] = 1
            return (True,contador)
    print()
    return (False,contador)





#   ############################
#   ## Repartición de boletos ##
#   ############################

quantum = 3 # Duración de 3 ticks

print("\n---------------------------\nQuantum: "+str(quantum)+"\n---------------------------\n")

boletos_total = 0

for i in procesos:
    tmp = random.randint(4,1000)
    i['boletos'] =  tmp
    boletos_total = boletos_total+tmp
    
izquierda = 0
print("| Proceso | Cantidad de boletos | Rango de boletos")
for i in sorted(procesos, key=lambda i:i['boletos']):
    print("     "+str(i['id'])+"        "+str(i['boletos']) + "     "+str(izquierda+1)+" - "+str(izquierda+i['boletos']))
    izquierda = izquierda+i['boletos']

print("Cantidad de boletos "+str(boletos_total))




#   #############################
#   ## Sorteo con 1000 boletos ##
#   #############################
ticks_global = 0

while(contador_procesos_terminados < len(procesos)):
    
    print("\U0001F4A2 Tick actual = "+str(ticks_global))

    print(" \n-- !Se inicia el gran sorteo¡ -- \n")
    winner  = random.randint(0,boletos_total)
    print("Boleto ganador: "+str(winner)+"\n")

    buscando_ganador = 0

    bandera_cambiar = False

    for i in sorted(procesos, key=lambda i:i['boletos']):
        buscando_ganador = buscando_ganador + i['boletos']

        if(buscando_ganador > winner):
            #Se encuentra en ese rango, entonces ese proceso es el ganador
            if(procesos_terminados[i['id']] == 0):
                print("El proceso que ganó fue " + i['id'] + ", va a proceder a ejecutar un quantum:\n")
                
                flag = False
                t_tmp = 0
                (flag,t_tmp) = ejecucion_trabajo(i)

                ticks_global = ticks_global + t_tmp
                
                # Si terminó, entonces sus boletos se reasignan a los demás procesos de forma equitativa
                if(flag):
                    for index in sorted(procesos, key=lambda index:index['boletos']):
                        if( (i['id'] != index['id']) and (ticks_global>=index['llegada'])):
                            #Este es el inmediato de mayor prioridad
                            index['boletos'] = index['boletos'] + i['boletos']
                            i['boletos'] = 0
                            break5t65
                            
                    contador_procesos_terminados = contador_procesos_terminados + 1
                
                bandera_cambiar = True
                break
            
            else:
                # En caso que no se haya elegido ninguno se gastó un tick
                ticks_global = ticks_global + 1
                bandera_cambiar = True
                break
        
        if(bandera_cambiar):
            break
    
    
