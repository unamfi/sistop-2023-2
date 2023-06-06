#!/usr/bin/python3
#
import os
import sys
import time


# función para obtener información del archivo o directorio
def get_file_info(filepath):
    file_stat = os.stat(filepath)
    filename = os.path.basename(filepath)  # guardar nombre del archivo o directorio
    size = file_stat.st_size  # guardar tamaño del archivo o directorio
    mod_time = time.strftime("%Y-%m-%d %H:%M", time.localtime(file_stat.st_mtime))  # guardar la fecha y hora de última modificación
    mode = str(oct(file_stat.st_mode))[2:]  # últimos 3 dígitos para saber el modo del archivo o directorio y los primeros 3 son 100 si es archivo y 40 si es directorio

    return filename, size, mod_time, mode

# función para listar los archivos y subdirectorios
def list_files(directory, days, indent=''):
    # Se obtiene la hora y se le restan los días para obtener los archivos que cumplen
    current_time = time.time()
    threshold_time = current_time - (days * 86400)

    # Recorre los archivos y directorios en el directorio actual
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)  # obtener la ruta completa del archivo o directorio

        # Verificar si se tiene acceso al archivo o directorio
        if os.access(filepath, os.R_OK):
            mod_time = os.path.getmtime(filepath)  # guardar la fecha y hora de modificación del archivo o directorio

            if mod_time >= threshold_time:  # comparación de búsqueda de días
                filename, size, mod_time, mode = get_file_info(filepath)  # información del archivo o directorio

                # Imprimir la información
                print(f"{filename.ljust(50)} {str(size).ljust(15)} {mod_time}    {mode}")

                # Si es un directorio, listar los archivos y subdirectorios
                if os.path.isdir(filepath):
                    list_files(filepath, days, indent + '  ')  # llamada recursiva con indentación incrementada
        else:
            print(f"No se tiene acceso al archivo o directorio: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) != 3:  # Si no se proporcionan los argumentos exactos, mostrar mensaje de error
        print("Invocación: Tarea2-directorio.py <directorio> <días>")
    else:
        # Argumentos
        directory = sys.argv[1]
        days = int(sys.argv[2])

        if os.path.isdir(directory):  # Verificar si el directorio existe
            print("Nombre".ljust(50), "Tamaño(bytes)".ljust(15), "Modificación".ljust(19), "Modo")
            print("=" * 95)

            list_files(directory, days)
        else:
            print(f"El directorio '{directory}' no existe.")


