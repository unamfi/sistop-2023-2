from random import randint
from time import sleep

Q0 = []
Q1 = []
Q2 = []
Q3 = []
colas=[Q0,Q1,Q2,Q3]

tick = 0
procesos= []

#Parametros
n = 1
Quantum = 2

#funciones
def num_llegada(lista):
    return lista['inicio']

def flag(colas):
    cont=0
    for i in range(4):
        cont+=len(colas[i])
    if(cont>0):
        return True
    else:
        return False

def check_proceso(proceso):
    return

#generacion de procesos 
procesos.append({
    'id':'A',
    'inicio':0,
    'duracion':randint(10,15),
    'procesado':0
})

for i in range(randint(4,7)):
    procesos.append({
        'id':chr(i+66),
        'inicio':randint(1,50),
        'duracion':randint(10,15),
        'procesado':0
    })

procesos = sorted(procesos,key=num_llegada)

print('Procesos:')

for proceso in procesos:
    print(proceso)

#Multinivel
colas[0].append(procesos.pop(0))

print('\nInicio de ejecución')
print('\nTick = %d' %tick)
while (flag(colas) or (len(procesos)!=0)):
    bandera=0
    for i in range(4):
        if len(colas[i])==0:
            continue
        else:
            for j in range(Quantum):
                romper=0
                print('En uso el proceso '+colas[i][0]['id']+' Cola '+str(i))
                print('Procesado '+str(1+colas[i][0]['procesado']))

                if(colas[i][0]['procesado']+1==colas[i][0]['duracion']):
                    print('El proceso '+colas[i][0]['id'] +' terminó')
                    colas[i].pop(0)
                    romper =1
                    break

                bandera=1
                tick+=1
                print('\nTick = %d' %tick)

                while len(procesos)!=0:
                    if tick == procesos[0]['inicio']:
                        print('Llego el proceso '+procesos[0]['id'])
                        colas[0].append(procesos.pop(0))
                    else:
                        break 
                
                
                colas[i][0]['procesado']+=1
                sleep(1)
                

            if romper==1:
                break

            if(i<=2):
                print("Degradando "+colas[i][0]['id']+' a la cola '+str(i+1))
                colas[i+1].append(colas[i].pop(0))
                break
    if bandera == 0:
        tick+=1
        print('\nTick = %d' %tick)
        while len(procesos)!=0:
                    if tick == procesos[0]['inicio']:
                        print('Llego el proceso '+procesos[0]['id'])
                        colas[0].append(procesos.pop(0))
                    else:
                        break 
    

