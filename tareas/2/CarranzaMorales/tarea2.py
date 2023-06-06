#!/usr/bin/python3
import os
import time
import sys

def listar_archivos_por_fecha(ruta,dias):
    #Fecha actual
    fecha_actual = time.time()

    #Calcula la fecha límite en base al número de días especificado
    fecha_limite = fecha_actual - (dias * 86400)  # 86400 segundos en un día

    #Verifica que la ruta sea un directorio válido
    if not os.path.isdir(ruta):
        print("La ruta especificada no es un directorio válido.")
        return

    #Lista de archivos en el directorio
    archivos = os.listdir(ruta)

    #Encabezado de la tabla
    print("\n        Nombre                                           Modificación        Modo   Tamaño")
    print("=" * 100 + "\n")

    #Filtra y muestra los archivos según la fecha de modificación
    for archivo in sorted(archivos):
        ruta_archivo = os.path.join(ruta, archivo)

        #Información del archivo
        info = os.stat(ruta_archivo)

        #Filtra los archivos cuya última modificación es menor o igual a la fecha límite
        if info.st_mtime >= fecha_limite:

            #Información requerida
            nombre = archivo
            longitud = info.st_size
            ultima_modificacion = time.ctime(info.st_mtime)
            permisos = info.st_mode

            #Valores formateados en la tabla
            print(f"{nombre.ljust(50)} {ultima_modificacion.ljust(25)} {permisos} {longitud}")

ruta = sys.argv[1]
dias = int(sys.argv[2])

listar_archivos_por_fecha(ruta,dias)

