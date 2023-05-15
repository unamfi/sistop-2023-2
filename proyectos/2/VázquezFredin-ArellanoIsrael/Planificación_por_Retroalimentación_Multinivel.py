import random

# ---------------------------------
# -- Retroalimentación multinvel --
# ---------------------------------

num_procesos = random.randint(5,8)
n = 1                   # Cantidad de ticks para decrementar la prioridad de cada proceso                   
quantum = 1

suma_total = 0


                                    # Creación de procesos por medio de un mapa
procesos = []        # Diccionario de procesos - mapa
procesos_terminados = {}
contador_procesos_terminados = 0
planificacion_realizada = ''

for i in range(num_procesos):
    procesos.append({
        'id':str(chr(ord('A') + i)),
        'llegada':random.randint(0,15*i),
        'duracion':random.randint(10,15),
        'salida':0,
        'prioridad':0,
        'ticks':0
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

print("\n---------------------------\nParámetros del algoritmo:\nn: "+str(n)+"\nquantum: "+str(quantum)+"\nDuración total: "+str(suma_total)+"\n---------------------------\n")




# ################
# ## Simulación ##
# ################

def estado_actual(name,ticks,prioridad,t_total):
    print("\t|| Proceso "+name+" ejecutó "+str(ticks)+" ticks || Su prioridad es de: "+str(prioridad)+" || Cantidad de ticks totales: "+str(t_total)+"\n")


ticks_global = 0



# Se estará una ordenación por llegada, será dinámica ya que se estará cambiando debido a la prioridad
'''
Se tiene que siempre se ejecuta un proceso en 0, por ende se inicia siempre con una ejecución, pero para el segundo proceso ya no es
posible asegurar que t sea igual al tick de llegada del siguiente proceso
'''
procesos_esperando = []

for p_1 in sorted(procesos, key=lambda p_1:p_1['llegada']):
    
    
    if (ticks_global == p_1['llegada']):
        print(" \U0001F4A2 Tick actual = "+str(ticks_global),end='')   
        print("     Llegó el proceso: "+str(p_1['id'])+" \U0001F6A9	")

        # Se van ejecutando conforme van llegando y cada ejecución disminuye su prioridad
        planificacion_realizada = planificacion_realizada + p_1['id'] + " "

        p_1['ticks'] = p_1['ticks'] + 1 
        p_1['prioridad'] = p_1['prioridad'] + 1 # Se ejecuta 1 tick y n = 1, entonces se disminuye su prioridad
        estado_actual(p_1['id'],1,p_1['prioridad'],p_1['ticks'])

        procesos_esperando.append(p_1)
        ticks_global = ticks_global + 1     # Avanzando el tick
    else:
        while(ticks_global < p_1['llegada']):
            # En caso que no sea el mismo se podrá buscar otros procesos que estén esperando y se toma al de mayor prioridad
            print("\U0001F4A2 Tick actual = "+str(ticks_global))
            bandera = True
            for p_Wait in sorted(procesos_esperando, key = lambda p_Wait:p_Wait['prioridad']):
                if(procesos_terminados[p_Wait['id']] == 0):
                    planificacion_realizada = planificacion_realizada + p_Wait['id'] + " "

                    # Si no ha termino, entonces es el escogido y ese se ejecuta
                    p_Wait['ticks'] = p_Wait['ticks'] + 1
                    p_Wait['prioridad'] = p_Wait['prioridad'] + 1

                    ticks_global = ticks_global + 1     # Avanzando el tick

                    # Un proceso a terminado:
                    if(p_Wait['ticks'] == p_Wait['duracion']):
                        contador_procesos_terminados = contador_procesos_terminados + 1
                        procesos_terminados[p_Wait['id']] = 1
                        print(" -- El proceso "+str(p_Wait['id'])+" finalizó -- \U0001F7E2")
                        p_Wait['salida'] =  ticks_global

                    # Continuando
                    estado_actual(p_Wait['id'],1,p_Wait['prioridad'],p_Wait['ticks'])

                    bandera = False

                    break

            # Considerar cuando no hay procesos listos:
            # En este caso simplemente es tiempo muerto
            if(bandera):
                print(" \U0001F480 T i e m p o   M u e r t o . . .      ",end='')
                ticks_global = ticks_global + (p_1['llegada']-ticks_global)
                break

        planificacion_realizada = planificacion_realizada + p_1['id'] + " "
        print("\U0001F4A2 Tick actual = "+str(ticks_global),end='')    
        print("     Llegó el proceso: "+str(p_1['id'])+" \U0001F6A9	")

        # Se van ejecutando conforme van llegando y cada ejecución disminuye su prioridad
        #p_1['duracion'] =  p_1['duracion'] - 1 # Se ejecuta 1 tick, entonces su duracion disminuye en uno
        p_1['ticks'] = p_1['ticks'] + 1 
        p_1['prioridad'] = p_1['prioridad'] + 1 # Se ejecuta 1 tick y n = 1, entonces se disminuye su prioridad
        estado_actual(p_1['id'],1,p_1['prioridad'],p_1['ticks'])

        procesos_esperando.append(p_1)
        ticks_global = ticks_global + 1     # Avanzando el tick



'''
Después de esto habrá algunos que hayan terminado, pero otros que no, es por esto mismo que será necesario al final completar todos.
Desde luego habrá procesos que hayan acabado anterioremnte, ahora ya no va llegar ningún proceso nuevo, solamente se va atacar
aquellos que falten. Se van a completar.
'''

# Ahora en lugar que sea tick hasta el siguiente que llegue, será hasta terminar todos
while(contador_procesos_terminados < len(procesos)):
    print("\U0001F4A2 Tick actual = "+str(ticks_global))
    bandera = True
    for p_Wait in sorted(procesos_esperando, key = lambda p_Wait:p_Wait['prioridad']):
        if(procesos_terminados[p_Wait['id']] == 0):
            planificacion_realizada = planificacion_realizada + p_Wait['id'] + " "
            
            # Si no ha terminado, se procesa
            p_Wait['ticks'] = p_Wait['ticks'] + 1
            p_Wait['prioridad'] = p_Wait['prioridad'] + 1
            ticks_global = ticks_global + 1     # Avanzando el tick

            # Un proceso a terminado:
            if(p_Wait['ticks'] == p_Wait['duracion']):
                contador_procesos_terminados = contador_procesos_terminados + 1
                procesos_terminados[p_Wait['id']] = 1
                print(" -- El proceso "+str(p_Wait['id'])+" finalizó -- \U0001F7E2")
                p_Wait['salida'] =  ticks_global

            #Continuando
            estado_actual(p_Wait['id'],1,p_Wait['prioridad'],p_Wait['ticks'])
            break


# #################
# ## Finalizando ##
# #################

print("\nTabla de ejecución: ")
print("Planificación realizada: " + planificacion_realizada)
print("\n --------------------------------------------------\n| Proceso | Inicio |  Fin  |   T   |   E   |   P   |\n --------------------------------------------------\n")

for i in procesos_esperando:
        print("    "+str(i['id']) +"         "+ str(i['llegada']) +"        "+ str(i['salida']) 
        +"     "+ str(i['salida']-i['llegada']) +"      "+ str( (i['salida']-i['llegada'])-i['duracion'] ) +"       "+ str( (i['salida']-i['llegada'])/i['duracion'] ))
        
