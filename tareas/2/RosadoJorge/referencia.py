import os
import sys
import time

def list_files_in_directory(directory, days):
    # Obtener la lista de archivos en el directorio
    files = os.listdir(directory)

    # Filtrar los archivos por fecha de modificación
    filtered_files = []
    for file in files:
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            modified_time = os.path.getmtime(path)
            if modified_time >= time.time() - (days * 24 * 60 * 60):
                filtered_files.append(file)

    # Ordenar los archivos por nombre
    filtered_files.sort()

    # Imprimir la lista de archivos filtrados con detalles
    print("Nombre                         Modificación     Modo   Tamaño")
    print("=" * 62)
    for file in filtered_files:
        path = os.path.join(directory, file)
        size = os.path.getsize(path)
        mode = oct(os.stat(path).st_mode)[-4:]
        modified_time = time.strftime("%Y-%m-%d %H:%M", time.localtime(os.path.getmtime(path)))
        print(f"{file.ljust(30)}{modified_time} {mode} {size}")

if len(sys.argv) < 3:
    print("Uso: python untitled3.py <directorio> <días>")
else:
    directory = sys.argv[1]
    days = int(sys.argv[2])
    list_files_in_directory(directory, days)


