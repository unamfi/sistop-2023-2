import os
import sys
import time

def informacion(file_path):

    info = os.stat(file_path)
    ultimaModificacion = time.strftime("%Y-%m-%d %H:%M", time.localtime(info.st_mtime))
    permisos = oct(info.st_mode & 0o777)
    print("{:<50} || {:<20} || {:<10} || {:<10}".format(os.path.basename(file_path), ultimaModificacion, permisos, info.st_size))

def main():

    if len(sys.argv) != 3:
        print("Invocación: python referencia.py <directorio> <días>")
        return

    directorio = sys.argv[1]
    numDias = int(sys.argv[2])
    if not os.path.isdir(directorio):
        print("El directorio esta mal escrito o no existe.")
        return

    tiempoActual = time.time()
    files = os.listdir(directorio)
    files.sort()
    print("Nombre                                                Modificación            Modo          Tamaño")
    print("===================================================================================================")
    for nombredelArchivo in files:
        file_path = os.path.join(directorio, nombredelArchivo)
        if os.path.isfile(file_path):
            ArUltimaModificacion = os.path.getmtime(file_path)
            diferenciaDias = (tiempoActual - ArUltimaModificacion) / (24 * 60 * 60)
            if diferenciaDias <= numDias:
                informacion(file_path)

if __name__ == "__main__":
    main()
