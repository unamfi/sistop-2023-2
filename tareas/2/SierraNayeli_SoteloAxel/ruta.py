import sys
import os 
import time
import stat
from datetime import datetime

# Obtener los argumentos de línea de comandos
argumentos = sys.argv

# Verificar si se proporcionaron suficientes argumentos
if len(argumentos) < 3:
    print("Debes de incluir los dos argumentos")
    print("Uso: python programa.py <arg1> <arg2>")
    sys.exit(1)

# Obtener los valores de los argumentos
directorio = sys.argv[1]
numero_dias = int(sys.argv[2])

# Obtener la ruta absoluta del directorio
ruta_directorio = os.path.abspath(directorio)

# Obtener la lista de archivos en el directorio
archivos = os.listdir(ruta_directorio)

# Filtrar los archivos según la última modificación
archivos_filtrados = []
for archivo in archivos:
    ruta_archivo = os.path.join(ruta_directorio, archivo)
    if os.path.isfile(ruta_archivo):
        # Obtener la información de la última modificación
        ultima_modificacion = os.stat(ruta_archivo).st_mtime
        dias_transcurridos = (time.time() - ultima_modificacion) / (24 * 3600)
        if dias_transcurridos <= numero_dias:
            archivos_filtrados.append(archivo)


# Ordenar la lista de archivos por nombre
archivos_filtrados.sort()

print('Nombre                 Tamaño                Ultima modificación                 Modo')
print('----------------------------------------------')

# Imprimir los detalles de los archivos filtrados
for archivo in archivos_filtrados:
    ruta_archivo = os.path.join(ruta_directorio, archivo)
    tamano = os.path.getsize(ruta_archivo)
    ultima_modificacion = os.path.getmtime(ruta_archivo)
    ultima_modificacion = datetime.fromtimestamp(ultima_modificacion).strftime('%Y-%m-%d')
    modo = oct(os.stat(ruta_archivo).st_mode)[-4:]  # Representación en formato octal
    print(f'{archivo}    ||    {tamano}    ||    {ultima_modificacion}    ||    {modo}')
