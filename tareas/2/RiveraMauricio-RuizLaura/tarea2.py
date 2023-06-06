import os
import time
import sys

def mostrarArchivos(ruta,lim):
	#Para delimitar las fechas. La información está en segundos
	#por lo que es necesario convertir (lim*segundos*dias*horas)
	hoy=time.time()
	flim=hoy-(lim*60*60*24)

	#Obtienen la lista de archivos del directorio
	archivos=os.listdir(ruta)


	print("Nombre                                  \tÚlt. Modificacion       \tModo \tTamaño[bytes]")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t~~~~~~~~~~~~~~~~~~~~~~~~\t~~~~~\t~~~~~~~~~~~~~")

	#Ciclo, tomando la lista de archivos en orden lexicografico
	for archivos in sorted(archivos):
		data=os.stat(os.path.join(ruta,archivos))
		if flim <= data.st_mtime:
			#Primero imprime el nombre del archivo
			print(archivos.ljust(40),end="\t")

			#Después, su última modificación
			print(time.ctime(data.st_mtime),end="\t")

			#Después, su modo
			print(data.st_mode,end="\t")

			#Después, el tamaño en bytes
			print(data.st_size)

mostrarArchivos(sys.argv[1],int(sys.argv[2]))