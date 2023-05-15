from random import randint

desplazamiento_A=0
desplazamiento_B=0
desplazamiento_C=0
procesos_A= []
procesos_B= []
procesos_C= []
colaGeneral=[]
colaFinal=[]
primer_proc_A = 'A'
primer_proc_B = 'D'
primer_proc_C = 'G'
duracion_A = 0
duracion_B = 0
duracion_C = 0
primeraAparicion=0
tiempos=0
ultimaAparicion=0

for i in range(randint(0,3)):
    procesos_A.append({'nombre': chr( ord(primer_proc_A)+i ),
                     'llegada': randint(0, 10*i),
                     'duración': 13
                     })
for i in range(0,3):
    procesos_B.append({'nombre': chr( ord(primer_proc_B)+i ),
                     'llegada': randint(0, 10*i),
                     'duración': 16
                     })
for i in range(0,2):
    procesos_C.append({'nombre': chr( ord(primer_proc_C)+i ),
                     'llegada': randint(0, 10*i),
                     'duración': 16
                     })

print('Lista de procesos A:')
for proc in procesos_A:
    print("%2s  %3d  %3d" % (proc['nombre'], proc['llegada'], proc['duración']))
    duracion_A+=proc['duración']
    for i in range(0,proc['duración']):
        colaGeneral.append(proc['nombre'])
print('Duración de los procesos en A:')
print(duracion_A)
print('Lista de procesos B:')
for proc in procesos_B:
    print("%2s  %3d  %3d" % (proc['nombre'], proc['llegada'], proc['duración']))
    duracion_B+=proc['duración']
    for i in range(0,proc['duración']):
        colaGeneral.append(proc['nombre'])
print('Duración de los procesos en B:')
print(duracion_B)
print('Lista de procesos C:')
for proc in procesos_C:
    print("%2s  %3d  %3d" % (proc['nombre'], proc['llegada'], proc['duración']))
    duracion_C+=proc['duración']
    for i in range(0,proc['duración']):
        colaGeneral.append(proc['nombre'])
print('Duración de los procesos en C:')
print(duracion_C)
print('Duración total:')
print(len(colaGeneral))
for i in range(0,len(colaGeneral)):
    if((duracion_C-desplazamiento_C)>=(duracion_B-desplazamiento_B) and (duracion_C-desplazamiento_C)>=(duracion_A-desplazamiento_A) and (duracion_C-desplazamiento_C)>=0):
        colaFinal.append(colaGeneral[duracion_A+duracion_B+desplazamiento_C])
        desplazamiento_C+=1
    elif((duracion_B-desplazamiento_B)>=(duracion_C-desplazamiento_C) and (duracion_B-desplazamiento_B)>=(duracion_A-desplazamiento_A) and (duracion_B-desplazamiento_B)>=0):
        colaFinal.append(colaGeneral[duracion_A+desplazamiento_B])
        desplazamiento_B+=1
    elif ((duracion_A-desplazamiento_A)>=0):
        colaFinal.append(colaGeneral[desplazamiento_A])
        desplazamiento_A+=1
for i in range(0,(len(colaFinal))):
    print(colaFinal[i],end="")
print(" ")
print("Tabla de ejecución:")
print("Proceso    Inicio    Fin    Ticks")


for proc in procesos_A:
    for i in range(0,len(colaFinal)):
        if(colaFinal[i]==proc['nombre']):
            ultimaAparicion=i
    
    for i in range(len(colaFinal)-1,-1,-1):
        if(colaFinal[i]==proc['nombre']):
            primeraAparicion=i
    tiempos+=(ultimaAparicion-primeraAparicion)
    print("%2s         %3d       %3d       %3d" % (proc['nombre'], primeraAparicion, ultimaAparicion, ultimaAparicion-primeraAparicion))


for proc in procesos_B:
    for i in range(0,len(colaFinal)):
        if(colaFinal[i]==proc['nombre']):
            ultimaAparicion=i
    
    for i in range(len(colaFinal)-1,-1,-1):
        if(colaFinal[i]==proc['nombre']):
            primeraAparicion=i
    tiempos+=(ultimaAparicion-primeraAparicion)
    print("%2s         %3d       %3d       %3d" % (proc['nombre'], primeraAparicion, ultimaAparicion, ultimaAparicion-primeraAparicion))

for proc in procesos_C:
    for i in range(0,len(colaFinal)):
        if(colaFinal[i]==proc['nombre']):
            ultimaAparicion=i
    
    for i in range(len(colaFinal)-1,-1,-1):
        if(colaFinal[i]==proc['nombre']):
            primeraAparicion=i
    tiempos+=(ultimaAparicion-primeraAparicion)
    print("%2s         %3d       %3d       %3d" % (proc['nombre'], primeraAparicion, ultimaAparicion, ultimaAparicion-primeraAparicion))

print('Ticks promedio: %3d'%(tiempos/(len(procesos_A)+len(procesos_B)+len(procesos_C))))