#!/usr/bin/python3
#
import os
import sys
import time


# función para obtener información del archivo
def get_file_info(filepath):
    file_stat = os.stat(filepath)
    filename = os.path.basename(filepath)  # guardar nombre del archivo
    size = file_stat.st_size  # guardar tamaño del archivo
    mod_time = time.strftime("%Y-%m-%d %H:%M", time.localtime(file_stat.st_mtime))  # guardar la fecha y hora de última modificación
    mode = str(oct(file_stat.st_mode))[-3:]  # últimos 3 dígitos para saber el modo del archivo

    return filename, size, mod_time, mode

# función principal 
def list_files(directory, days):

    # Se obtiene la hora y se le restan los días para obtener los archivos que cumplen
    current_time = time.time()  
    threshold_time = current_time - (days * 86400)  

    # En caso de que no exista
    if not os.path.isdir(directory):
        print(f"El directorio '{directory}' no existe.")
        return

    # Datos que se piden formateados para los nombres largos
    print("Nombre".ljust(50), "Tamaño(bytes)".ljust(15), "Modificación".ljust(19), "Modo")
    print("=" * 95)

    # Recorre los archivos en el directorio y sus subdirectorios (si los hay)
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)  # extraer la ruta completa del archivo
            
            # Verificar si se tiene acceso al archivo
            if os.access(filepath, os.R_OK):
                mod_time = os.path.getmtime(filepath)  # guarda la fecha y hora de modificación del archivo 

                if mod_time >= threshold_time:  # comparación de búsqueda de días
                    filename, size, mod_time, mode = get_file_info(filepath)  # información del archivo
                    # Finalmente se imprime lo solicitado
                    print(f"{filename.ljust(50)} {str(size).ljust(15)} {mod_time}    {mode}")
            else:
                print(f"No se tiene acceso al archivo: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) != 3: # Si no se proporcionan los argumentos exactos, mostrar mensaje de error
        print("Invocación: Tarea2-directorio.py <directorio> <días>")
    else:
        # Argumentos
        directory = sys.argv[1]   
        days = int(sys.argv[2])
        list_files(directory, days)

