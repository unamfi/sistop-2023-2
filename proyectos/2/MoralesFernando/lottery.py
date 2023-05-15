import random
from random import randint
from time import sleep

tick = 0
procesos= []
ids = []
boletos = []

#funciones
def elegir_proceso(ids,probabilidad):
    elegido = random.choices(ids,weights=probabilidad,k=1)
    return elegido[0]

def reacomodo(ids,boletos):
    maxi = max(boletos)
    mini = min(boletos)
    diff = (maxi-mini)/4
    print('\nReacomodando boletos de %s:%f a %s:%f' % (
        ids[boletos.index(maxi)],max(boletos),
        ids[boletos.index(mini)],min(boletos)
    ))
    n_min=boletos.index(mini)
    n_max=boletos.index(maxi)
    boletos[n_min]+=diff
    boletos[n_max]-=diff
    print('Resultado de %s:%f a %s:%f' % (
        ids[n_max],boletos[n_max],
        ids[n_min],boletos[n_min]
    ))
    

#generacion de procesos 
for i in range(randint(5,8)):
    procesos.append({
        'id':chr(i+65),
        'boletos':randint(5,99),
        'duracion':randint(10,15),
        'procesado':0
    })

print('Procesos:')
for proceso in procesos:
    print(proceso)
    boletos.append(proceso['boletos']/100)
    ids.append(proceso['id'])

#loteria
while len(ids)!=0:
    print('\nTick: %d' % tick)

    procesar= elegir_proceso(ids,boletos)
    for proceso in procesos:
        if procesar == proceso['id']:
            proceso['procesado']+=1
            print('Procesando %s' % proceso['id'])
            print ('Procesado %d' % proceso['procesado'])
            if proceso['procesado'] == proceso['duracion']:
                print("El proceso %s ha terminado" % proceso['id'])
                num = ids.index(proceso['id'])
                ids.pop(num)
                boletos.pop(num)
            sleep(1)
            break

    if((tick)%10==0):
       reacomodo(ids,boletos)

    tick+=1

print("La ejecuccion ha termiando")

