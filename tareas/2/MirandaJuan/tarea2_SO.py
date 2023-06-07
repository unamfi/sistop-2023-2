# -*- coding: utf-8 -*-


"""
Para esta tarea lo que hay que considerear es tener el modulo 'tabulate' 
que se usa para que el formato en el que se presentan los datos, sea mas entendible

"""

import os
import sys
import time
from tabulate import tabulate

def get_file_details(file_path):
    # Obtener detalles del archivo
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    file_mtime = os.path.getmtime(file_path)
    file_mode = os.stat(file_path).st_mode

    # Formatear la fecha de la última modificación
    file_mtime_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_mtime))

    # Obtener los permisos en formato octal
    file_mode_formatted = oct(file_mode)[-3:]

    return [file_name, file_size, file_mtime_formatted, file_mode_formatted]

def list_files(directory, days):
    # Obtener la fecha actual
    current_time = time.time()

    try:
        # Recorrer los archivos y directorios del directorio
        file_list = []
        for root, dirs, files in os.walk(directory):
            for file_name in files + dirs:
                file_path = os.path.join(root, file_name)

                # Verificar si el archivo o directorio cumple con el criterio de días
                if current_time - os.path.getmtime(file_path) <= days * 24 * 60 * 60:
                    file_list.append(get_file_details(file_path))

        # Ordenar la lista alfabéticamente por nombre de archivo
        file_list = sorted(file_list, key=lambda x: x[0])

        # Mostrar los resultados en una tabla
        headers = ["Nombre", "Tamaño", "Última modificación", "Modo"]
        print(tabulate(file_list, headers=headers, tablefmt="grid"))
    except OSError:
        print("Error al acceder al directorio.")

# Obtener los argumentos de la línea de comandos
if len(sys.argv) != 3:
    print("Uso: python file_list.py <directorio> <días>")
else:
    directory = sys.argv[1]
    days = int(sys.argv[2])
    list_files(directory, days)
