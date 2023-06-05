import os
import sys
import time

def mostrar_files(directorio, num_dias):
    fecha_actual = time.time()
    segundos = num_dias * 24 * 60 * 60

    archivos_modificados = []
    for file in os.listdir(directorio):
        ruta = os.path.join(directorio, file)
        
        if os.path.isfile(ruta):
            fecha_modificacion = os.path.getmtime(ruta)
            diferencia = fecha_actual - fecha_modificacion

            if diferencia <= segundos:
                longitud = os.path.getsize(ruta)
                permisos = oct(os.stat(ruta).st_mode)[-3:]
                archivos_modificados.append([file, str(longitud), time.ctime(fecha_modificacion), permisos])

    archivos_modificados.sort(key=lambda x: x[0])

    # Mostramos la tabla
    print("{:<40} {:<20} {:<30} {:<10}".format("Archivo", "Longitud", "Última modificación", "Permisos"))
    print("-" * 90)
    for archivo in archivos_modificados:
        nombre_archivo, longitud, fecha_modificacion, permisos = archivo
        print("{:<40} {:<20} {:<30} {:<10}".format(nombre_archivo, longitud + ' bytes', fecha_modificacion, permisos))

directorio = os.path.abspath(sys.argv[1])
num_dias = int(sys.argv[2])

mostrar_files(directorio, num_dias)
