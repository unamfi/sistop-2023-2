# Tarea2.Obteniendo información de un directorio.   Alumno:Uriarte Oryiz Enrique Yahir

import os
import sys
import time

def get_file_info(file_path):
    file_name = os.path.basename(file_path) # Obtener nombre del archivo.
    file_size = os.path.getsize(file_path) # Longitud del archivo en bytes.
    modification_time = os.path.getmtime(file_path) # Fecha de última modificación.
    modification_date = time.strftime('%Y-%m-%d %H:%M', time.localtime(modification_time))
    file_mode = oct(os.stat(file_path).st_mode)[-4:]  # permisos del archivo.

    return file_name, modification_date, file_mode, file_size

def list_files(directory, days):# Fecha límite de comparación.
    current_time = time.time()
    threshold = current_time - (days*24*60*60)

    files = os.listdir(directory)# Lista de archivos en el directorio.

    filtered_files = []# Filtro y orden.
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            modification_time = os.path.getmtime(file_path)
            if modification_time >= threshold:
                filtered_files.append(get_file_info(file_path))

    filtered_files.sort(key=lambda x: x[0])# Ordenar alfabéticamente.

    print("=" * 62)# Formato
    print("Nombre                         Modificación     Modo   Tamaño")# Formato
    print("=" * 62)# Formato

    for file_info in filtered_files:# Detalles de archivo.
        file_name, modification_date, file_mode, file_size = file_info
        print(f"{file_name:30s} {modification_date:16s} {file_mode:6s} {file_size}")

if len(sys.argv) != 3:# Parámetros de línea de comandos.
    print("Uso: python Ejecucion.py <directorio> <dias>")
    sys.exit(1)

directory = sys.argv[1]
days = int(sys.argv[2])

if not os.path.isdir(directory):# Verificar existencia.
    print("La direccion no exixte en el equipo, verificala o intenta con otra.")
    sys.exit(1)

list_files(directory, days)# Listar archivos y detalles.
