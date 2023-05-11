from random import randint

procesos = []
primer_proc = 'A'

# Para evitar INANICIÓN se usa una duración máxima en caso de que un proceso sea muy largo
duracion_maxima = randint(7,10) # Duración máxima aleatoria
print(f"\n\033[32;1m---- DURACION MAXIMA: {duracion_maxima}\033[0m\n")

# Generar procesos aleatorios
for i in range(randint(5,8)):
    procesos.append({'nombre': chr( ord(primer_proc)+i ),
                     'llegada': randint(0, 10*i),
                     'duracion': randint(4,11),
                     'ticks_ejecutados': 0
                     })

print("\033[31;1m---------- Procesos ----------\033[0m")
print(f"\033[31;1m{'NOMBRE'}\t {'LLEGADA'}\t {'DURACION'}\033[0m")

for proc in procesos:
    print(f"\033[31m{proc['nombre']}\t  {proc['llegada']}\t\t  {proc['duracion']}")


t = 0 # Guarda la duracion total
res = '' # Guarda la planificacion general

# Se usa para guardar los procesos listos para ejectuarse
cola = []

# Se usa para guardar los procesos que han alcanzado su duración máxima
espera = []

# 'A' llega siempre en 0 ('llegada' es aleatorio entre 0 y 5*0)
print('\n\033[34;1mINICIO...\033[0m')

while procesos or cola:
    print("\033[34m")
    # Agregar procesos que han llegado a la cola
    for p in procesos:
        if p['llegada'] == t:
            cola.append(p)
            
    procesos = [p for p in procesos if p not in cola]

    # Ordenar la cola por prioridad
    cola = sorted(cola, key=lambda p: p['nombre'])

    # Ejecutar el primer proceso en la cola
    if cola:
        p = cola[0]
        res += p['nombre']
        p['ticks_ejecutados'] += 1

        # Verificar si el proceso ha alcanzado su duración máxima
        if p['ticks_ejecutados'] == duracion_maxima:
            cola.pop(0)
            espera.append(p)
            print(f"\033[31m    ⌚ {p['nombre']} ({p['duracion']} ticks, duración máxima alcanzada)\033[0m")
            print(f"\033[33;1m\nSe manda {p['nombre']} a espera por exceder la duracion maxima !!!\033[0m")
            
        else:
            # Verificar si el proceso ha finalizado
            if p['ticks_ejecutados'] == p['duracion']:
                terminado = cola.pop(0)

                print(f"    ⌚ {p['nombre']} ({p['duracion']} ticks)")
                print(f"\n\033[34;1mTERMINANDO {terminado['nombre']}\033[0m")
                
            else:
                print(f"    ⌚ {p['nombre']} (tick {p['ticks_ejecutados']})")
                
                
    else:
        res += '-'

    t += 1
   
if espera:
    print("\n\033[33;1mSe preparan los procesos que se encuentran en espera\033[0m")

while espera:
    for p in espera:
        if espera:
            print("\033[34m")
            p = espera[0]
            res += p['nombre']
            p['ticks_ejecutados'] += 1
            
            if p['ticks_ejecutados'] == p['duracion']:
                    terminado = espera.pop(0)
                    print(f"   ⌚ {p['nombre']} ({p['duracion']} ticks)")
                    print(f"\033[34;1mTERMINANDO {terminado['nombre']}")
            
            else:
                print(f"   ⌚ {p['nombre']} (tick {p['ticks_ejecutados']})")
                
                espera.pop(0)
                break
            

print("\n\033[32;1mPlanificación realizada: \n" + res)
print(f"Duración total: {t}\033[0m")

