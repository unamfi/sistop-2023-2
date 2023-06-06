#Realizado por: Rojo Lopez Luis Felipe

import os
from datetime import datetime, timedelta

#La ruta de donde seran examinados los archivos
ruta = 'C:\Escuela\BD'

#Se veran los archivos que fueron modificados entre el numero de dias puesto y la fecha actual
dias = 3

#Funcion para obtener la fecha actual
ahora = datetime.now()

#Le restamos a la fecha actual los dias que queremos para ver los documentos 
fechaAnterior = ahora - timedelta(days=dias)


#Funcion para listar los archivos dentro del directorio en la ruta seleccionada 
archivos = os.listdir(ruta)
archivos.sort()


#Se forman las rutas para cada archivo del directorio examinado
docs = []
#Utilice dos arreglos para que uno sea recorrido y en el otro se eliminen los
#archivos que no coinciden con la fecha requerida
docs2 = []
for i in archivos:
    #Se forman las rutas de los archivos
    nombre = ruta + "\\" +  i
    docs.append(nombre)
    docs2.append(nombre)
   

#Se eliminan los archivos que no coinciden con las fechas puestas
for a in (docs):
    tiempo = os.path.getmtime(a)
    tiempoReal = datetime.fromtimestamp(tiempo)
    if tiempoReal < fechaAnterior:
        docs2.remove(a)

nombres = []
modif = []
modo = []
tamano = []
#Aqui se extrae la informacion de cada archivo 
for i in range (len(docs2)):
    nombres.append(os.path.basename(docs2[i]))
    modif.append(os.path.getmtime(docs2[i]))
    stats = os.stat(docs2[i])
    modo.append(stats.st_mode)
    tamano.append(os.path.getsize(docs2[i]))


#Ejecucion
print('\nruta:',ruta, '\tDias: ',dias )
print('\nNombre\t\t\tModificacion\t\t\tModo\t\tTamaño\n=================================================================================')
for i in range (len(docs2)):
    print(nombres[i],'\t',datetime.fromtimestamp(modif[i]),'\t\t',modo[i],'\t\t',tamano[i])