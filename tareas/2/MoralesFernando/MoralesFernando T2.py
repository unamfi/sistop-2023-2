import os
import sys
import time

def mostrar_archivos_modificados(directorio, dias):
    # Obtenemos la fecha actual
    fecha_actual = time.time()

    # Convertimos los días a segundos
    segundos_por_dia = 24 * 60 * 60
    segundos = dias * segundos_por_dia

    # Lista para almacenar los archivos modificados
    archivos_modificados = []

    # Recorremos todos los archivos del directorio
    for file in os.listdir(directorio):
        ruta = os.path.join(directorio, file)

        # Verificamos si es un archivo
        if os.path.isfile(ruta):
            # Obtenemos la fecha de modificación del archivo
            fecha_modificacion = os.path.getmtime(ruta)

            # Calculamos la diferencia en segundos entre la fecha actual y la fecha de modificación
            diferencia = fecha_actual - fecha_modificacion

            # Comparamos la diferencia con la cantidad de segundos especificada
            if diferencia <= segundos:
                # Obtenemos la longitud del archivo
                longitud = os.path.getsize(ruta)

                # Obtenemos los permisos del archivo
                permisos = oct(os.stat(ruta).st_mode)[-3:]

                # Agregamos los datos a la lista de archivos modificados
                archivos_modificados.append([file, str(longitud), time.ctime(fecha_modificacion), permisos])

    # Ordenamos la lista de archivos modificados por nombre de archivo
    archivos_modificados.sort(key=lambda x: x[0])

    # Mostramos la información de los archivos modificados en una tabla
    print("{:<40} {:<20} {:<30} {:<10}".format("Archivo", "Longitud", "Última modificación", "Permisos"))
    print("-" * 90)
    for archivo in archivos_modificados:
        nombre_archivo, longitud, fecha_modificacion, permisos = archivo
        print("{:<40} {:<20} {:<30} {:<10}".format(nombre_archivo, longitud + ' bytes', fecha_modificacion, permisos))

# Verificamos si se proporcionaron los argumentos requeridos
if len(sys.argv) < 3:
    print("Uso: python programa.py directorio dias")
    sys.exit(1)

# Obtenemos los argumentos de la línea de comandos
directorio = os.path.abspath(sys.argv[1])
dias = int(sys.argv[2])

# Llamamos a la función para mostrar los archivos modificados
mostrar_archivos_modificados(directorio, dias)
