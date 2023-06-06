import os
import time

def listar_archivos_directorio(ruta, num_dias):
    # Obtener la fecha límite
    fecha_limite = time.time() - (num_dias * 24 * 60 * 60)

    # Obtener la lista de archivos en el directorio
    archivos = os.listdir(ruta)

    # Filtrar y ordenar los archivos por fecha de modificación
    archivos_filtrados = []
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_archivo):
            fecha_modificacion = os.path.getmtime(ruta_archivo)
            if fecha_modificacion >= fecha_limite:
                archivos_filtrados.append((archivo, fecha_modificacion))

    archivos_filtrados.sort(key=lambda x: x[0])  # Ordenar lexicográficamente por nombre de archivo

    # Imprimir la información de cada archivo
    for archivo, fecha_modificacion in archivos_filtrados:
        ruta_archivo = os.path.join(ruta, archivo)
        tamano = os.path.getsize(ruta_archivo)
        permisos = oct(os.stat(ruta_archivo).st_mode)[-3:]  # Obtener los permisos como una cadena de caracteres
        fecha_modificacion_str = time.ctime(fecha_modificacion)
        print(f"Archivo: {archivo} | Tamaño: {tamano} bytes | Última modificación: {fecha_modificacion_str} | Permisos: {permisos}")


path= "C:/Users/Ansotec/Downloads/Temp" # directorio supongo debe cambiarlo 
day=5 # cantidad de días
listar_archivos_directorio(path, day) #llamada a función 