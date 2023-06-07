import time
import os
direccion=input("Ingrese la dirección a examinar: ")
dias=input("Ingrese el número de días desde la última modificación: ")
dias= float(dias)*86400.0
fecha_comparacion=time.time() - dias
print('\n\nSe va a utilizar el siguiente formato:     nombre del archivo           fecha de modificacion        permisos          tamaño (KB)\n\n')
directorios = os.listdir(direccion)
directorios = sorted (directorios)
for i in directorios:
    if((os.path.getmtime(direccion+'/'+i))>=fecha_comparacion):
        status = os.stat(direccion+'/'+i)
        print(direccion+'/'+i+'       '+(time.ctime(os.path.getmtime(direccion+'/'+i)))+'       '+str(status.st_mode)+'       '+str(status.st_size / 1024)+'\n')
    