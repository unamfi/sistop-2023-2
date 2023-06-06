import os
import sys
import time


def read_archivo(ruta_archivo):
    # Obtenemos el nombre, tamaño, fecha de modificacion
    # y el modo del archivo a partir de la ruta establecida
    #como parametro 
    nombre = os.path.basename(ruta_archivo)
    size = os.path.getsize(ruta_archivo)
    tiempo_modificacion = os.path.getmtime(ruta_archivo)
    fecha_modificacion = time.strftime("%y-%m-%d  %H:%M:%S", time.localtime(tiempo_modificacion))
    modo = os.stat(ruta_archivo).st_mode
    return nombre, size, fecha_modificacion, modo


def directorio(ruta_directorio, num_dias):
        # Verifica si la ruta proporcionada no es un directorio válido
        # En caso contrario arrojamos un error
    if not os.path.isdir(ruta_directorio):
        print("Error: La ruta proporcionada no es un directorio válido.")
        return
    
    # Tiempo límite de modificación de archivos
    
    tiempo_actual = time.time()
    tiempo_limite = tiempo_actual - (num_dias * 24 * 60 * 60)

    lista_archivos = []
    
    # Obtiene la ruta completa y el tiempo de modificación
    # de cada archivo
    for raiz, directorios, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            
            ruta_archivo = os.path.join(raiz, archivo)
            tiempo_modificacion_archivo = os.path.getmtime(ruta_archivo)
            # Se agrega a la lista si el archivo ha sido modificado
            # dentro del límite de tiempo especificado 
            if tiempo_modificacion_archivo >= tiempo_limite:
                
                lista_archivos.append(ruta_archivo)

    # Ordenamos la lista por orden lexicográfico
    lista_archivos_ordenada = sorted(lista_archivos)

    # Codigo de impresion
    print("---"*40)
    print("\n")
    for ruta_archivo in lista_archivos_ordenada:
        nombre, size, modificado_archivo, modo = read_archivo(ruta_archivo)
        print("Nombre:", nombre)
        print("Modificación:", modificado_archivo)
        print("Tamaño en bytes:", size)
        print("Modo:", modo)
        print("\n")
    print("---"*40)

# Verifica si se proporcionaron los argumentos correctos = 2
# en caso contrario arrojamos error
if len(sys.argv) != 3:
    print("Error: Numero de argumentos invalido")
else:
    ruta_directorio = sys.argv[1]
    num_dias = int(sys.argv[2])
    # Pasamos al programa los parámetros especificados
    directorio(ruta_directorio, num_dias)
