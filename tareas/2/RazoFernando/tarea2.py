import os
import sys
import time


def print_file_info(file_path):
    stat_info = os.stat(file_path)
    file_size = stat_info.st_size
    file_mode = stat_info.st_mode
    file_mtime = stat_info.st_mtime

    # Obtener la fecha de modificación en formato legible
    modification_time = time.strftime("%Y-%m-%d %H:%M", time.localtime(file_mtime))

    # Obtener los permisos del archivo en formato legible
    file_permissions = oct(file_mode)[-3:]

    # Imprimir los detalles del archivo
    print("{:<30} {:<20} {:<7} {:<20}".format(os.path.basename(file_path), modification_time, file_permissions, file_size))


def main():
    # Verificar que se proporcionen los argumentos necesarios
    if len(sys.argv) != 3:
        print("Invocación: python referencia.py <directorio> <días>")
        return

    directory = sys.argv[1]
    days = int(sys.argv[2])

    # Verificar que el directorio existe
    if not os.path.isdir(directory):
        print("El directorio especificado no existe.")
        return

    # Obtener la fecha actual
    current_time = time.time()
    print('\n\n------------------------------------------------------------------------------')
    print('{:<30} {:<20} {:<7} {:20}'.format("Nombre", "Modificación", "Modo", "Tamaño"))
    print('------------------------------------------------------------------------------')
    # Recorrer todos los archivos del directorio
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Verificar si el archivo cumple con el criterio de días especificado
        if os.path.isfile(file_path):
            file_mtime = os.stat(file_path).st_mtime
            days_difference = (current_time - file_mtime) / (60 * 60 * 24)

            if days_difference <= days:
                print_file_info(file_path)


main()