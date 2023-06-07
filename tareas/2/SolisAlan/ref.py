'''
    Solis González Alan David
    Tarea 2
    Sistemas Operativos
    Obteniendo información de un directorio

    
    Para la ejecución del programa es necesario colocar como primer parámetro la ruta del directorio
    y como segundo parámetro el número de dias que se quiere contar.
'''


import sys
import os
import datetime

#La ruta se guarda en p
p = (sys.argv[1])

#El número de dias esta dado por la variable d
d = (sys.argv[2])

#Convertimos los dias d en enteros para que se puedan restar
date = datetime.datetime.today() - datetime.timedelta(days=int(d))

#Se busca el directorio donde se quiere buscar
dir_entries = os.scandir(p)

print("\n\nNombre\t\t\t\t\t\tModificacion\tModo\tTamaño\n",
      "=======================================================================================", sep='')
#Se busca elemento por elemento en el directorio
for entry in dir_entries:
    #Comprueba la fecha y decide
    if (datetime.datetime.fromtimestamp(os.path.getmtime(entry.path)) >= date):

        #Obtención de la fecha y hora
        mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(entry.path))

        #Obtensión de los permisos
        permissions = oct(os.stat(entry.path).st_mode)[-4:]

        #Dando a conocer el modo de opearación
        lenght = os.stat(entry.path).st_size

        #Muestra el tamaño del archivo
        print(f'{entry.name}', "   "+ mod_time.strftime("%d-%m-%Y %H:%M"), "    ", permissions, "   " ,lenght)
