import os
import sys
import time
from tabulate import tabulate


def obteniendo_archivos(directorio,ndias):
    #Cachamos el error para que se mande un mensaje en vez de FileNotFoundError
    try:
        # Obtenemos la fecha actual y calculamos la fecha límite
        factual = time.time()
        flimite = factual - (ndias * 24 * 60 * 60)  #Convertimos los dias a segundos
        archivos = os.listdir(directorio)# Obtenemos la lista de archivos en el directorio

        datos = [] #Para poder agregar los datos en la tabla que vamos a imprimir
        for archivo in archivos:
            rutaArchivo = os.path.join(directorio,archivo)
            if os.path.isfile(rutaArchivo):
                info_archivo = os.stat(rutaArchivo)
                fmodificacion = info_archivo.st_mtime

                if fmodificacion >= flimite:
                    longitud = info_archivo.st_size
                    permisos = oct(info_archivo.st_mode)[2:]  # Obteniendo los permisos en forma octal
                    datos.append([archivo, time.ctime(fmodificacion), permisos, longitud]) #Agregando los datos en la tabla

        formato = {"headers": ["Nombre", "Modificación", "Modo", "Tamaño"]}
        tabla = tabulate(datos, **formato)
        print(tabla)

    except FileNotFoundError:
        print("La ruta del directorio no existe")

#Parametros que seran recibidos en la linea de comado: el directorio y el numero de dias
directorio = sys.argv[1]  # Variable que guarda el directorio dado en consola, en Windows hay que poner \\
ndias = int(sys.argv[2])  #Variable que garda el numero de dias dado en consola

#Ejemplo de como escribimos en consola de Windows el directorio C:\\Users\\ProBook\\Desktop\\Aerin

obteniendo_archivos(directorio, ndias)