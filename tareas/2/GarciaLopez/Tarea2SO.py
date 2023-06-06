import os
import sys
import time

# Para obtener los argumentos de la línea de comandos
# Hacer que el programa sea no interactivo
argumentos = sys.argv

# Comprobar argumentos
# Debe ser diferente a 3 o dara error
if len(argumentos) != 3:
    print("Error en los parámetros")
    print("Argumento 1: Ruta del directorio que se va a procesar")
    print("Argumento 2: Número de días")
    sys.exit(1)

# Guardando los parámetros 
ruta = argumentos[1]
numDias = int(argumentos[2])

# Comprobar si la ruta del directorio existe
if not os.path.isdir(ruta):
    print("Directorio inválido")
    sys.exit(1)

# Fecha límite
# time.time() da el tiempo actual en segundos
# (numDias * 24 * 60 * 60) el numero del usuario se multiplica por 24 (horas), 60 (minutos) y 60 (segundos) para obtener el tiempo en segundos
fecha_limite = time.time() - (numDias * 24 * 60 * 60)

# Encabezado
print("{:<30s} {:<24s} {:<8s} {:<10s}".format("Nombre", "Modificación", "Modo", "Tamaño"))

# Recorrer los archivos en el directorio con un for y ordenando con el metodo sorted
for nombre_archivo in sorted(os.listdir(ruta)):
    ruta_archivo = os.path.join(ruta, nombre_archivo)

    # Comprobar si es un archivo regular
    if os.path.isfile(ruta_archivo):
        # Obtener la información del archivo
        try:
            info = os.stat(ruta_archivo)
        except OSError as e:
            print(f"No se puede obtener información de {ruta_archivo}: {e}")
            continue

        fecha_modificacion = info.st_mtime  # Última fecha de modificación del archivo

        # Comprobar si la fecha de modificación es menor o igual a la fecha límite
        if fecha_modificacion >= fecha_limite:
            tamaño = info.st_size  # Longitud del archivo

            # Obtener los permisos del archivo
            ## modo = oct(info.st_mode)[-4:]
            modo2 = info.st_mode
            modo = str(modo2)


            # Imprimir la información del archivo
            print("{:<30s} {:<20s} {:<8s} {:<10d}".format(nombre_archivo, time.ctime(fecha_modificacion), modo, tamaño))
