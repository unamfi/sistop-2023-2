#!/urs/bin/python3
#
import random

def generar_carga_trabajo():
    cantidad_procesos = random.randint(5, 8) #Procesos
    duracion_total = 120  # Máximo de ticks
    
    carga_trabajo = []
    
    for i in range(cantidad_procesos):
        proceso = {
            'nombre': chr(65 + i),  # Procesos desde la A en adelante
            'llegada': random.randint(0, duracion_total), #Tick en que llega
            'duracion': random.randint(1, duracion_total // cantidad_procesos), #Ticks que necesita
            'boletos': random.randint(1, 100), #Probabilidades de participar
            'tick_inicio': -1,
            'tick_final': -1
        }
        carga_trabajo.append(proceso) # se van agregando a la carga de trabajo los procesos
    
    return carga_trabajo

def simular_planificacion(carga_trabajo):
    duracion_total = sum(p['duracion'] for p in carga_trabajo)
    tiempo_actual = 0
    ejecucion = ''
    
    #paque no se pase de 120 ticks
    while tiempo_actual < duracion_total and tiempo_actual < 120:
        procesos_listos = [p for p in carga_trabajo if p['llegada'] <= tiempo_actual and p['duracion'] > 0]
        
        #huecos porque no estan listos
        if len(procesos_listos) == 0:
            print(f"Tick {tiempo_actual}: -")
            tiempo_actual += 1
            continue
        
        #Se calcula las probabilidades de ejecucion dependiendo la cantidad de boletos
        suma_boletos = sum(p['boletos'] for p in procesos_listos)
        probabilidades = [p['boletos'] / suma_boletos for p in procesos_listos]
        
        #Se toma al ganador de los procesos que esten listos
        proceso_elegido = random.choices(procesos_listos, weights=probabilidades)[0]

        #Si gana reduce un tick al proceso 
        proceso_elegido['duracion'] -= 1
        ejecucion += proceso_elegido['nombre']
        
        #Se establece en 0 el tiempo si es que aun no se inicia el proceso 
        if proceso_elegido['tick_inicio'] == -1:
            proceso_elegido['tick_inicio'] = tiempo_actual
        
        #Va imprimiendo y aumentano los ticks en consola
        print(f"Tick {tiempo_actual}: {proceso_elegido['nombre']}")
        tiempo_actual += 1
        
        #Pa darles mas chance a los perdedores
        for p in carga_trabajo:
            if p['nombre'] != proceso_elegido['nombre'] and p['duracion'] > 0:
                p['boletos'] += proceso_elegido['boletos']
        
        #bandera para los que ya acabaron 
        if proceso_elegido['duracion'] == 0:
            proceso_elegido['tick_final'] = tiempo_actual - 1
    
    # Verifica si hay procesos incompletos y continua hasta que todos terminen, es como la segunda pasada
    while any(p['duracion'] > 0 for p in carga_trabajo):
        procesos_listos = [p for p in carga_trabajo if p['duracion'] > 0]
        
        suma_boletos = sum(p['boletos'] for p in procesos_listos)
        probabilidades = [p['boletos'] / suma_boletos for p in procesos_listos]
        
        proceso_elegido = random.choices(procesos_listos, weights=probabilidades)[0]
        proceso_elegido['duracion'] -= 1
        ejecucion += proceso_elegido['nombre']
        
        if proceso_elegido['tick_inicio'] == -1:
            proceso_elegido['tick_inicio'] = tiempo_actual
        
        print(f"Tick {tiempo_actual}: {proceso_elegido['nombre']}")
        
        tiempo_actual += 1
        
        for p in carga_trabajo:
            if p['nombre'] != proceso_elegido['nombre'] and p['duracion'] > 0:
                p['boletos'] += proceso_elegido['boletos']
        
        if proceso_elegido['duracion'] == 0:
            proceso_elegido['tick_final'] = tiempo_actual - 1
    
    return ejecucion

# Inicio del programa
carga_trabajo = generar_carga_trabajo()

# Se muestran los datos generales de los procesos
print("Carga de trabajo generada:")
for proceso in carga_trabajo:
    print(f"Proceso {proceso['nombre']}: Llegada={proceso['llegada']}, Duración={proceso['duracion']}, Boletos={proceso['boletos']}")

# Se realiza la simulacion de los ticks y se guarda el orden en "Orden ejecucion"
orden_ejecucion = simular_planificacion(carga_trabajo)

# Orden de ejecucion de los procesos
print("\nOrden de ejecución:")
print(orden_ejecucion)

# Tabla de informacion de los proceos
print("\nInformación detallada de cada proceso:")
for proceso in carga_trabajo:
    tick_inicio = proceso['tick_inicio']
    tick_final = proceso['tick_final']
    if tick_inicio != -1 and tick_final != -1:
        tick_total = tick_final - tick_inicio + 1
    else:
        tick_total = 0
    print(f"Proceso {proceso['nombre']}: Inicio={tick_inicio}, Final={tick_final}, Total={tick_total}")

