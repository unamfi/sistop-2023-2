# Aldo Santiago

import datetime
import argparse
import os
import time
import calendar

# Codigos de colores
cod_rojo = "\033[0;31m"
cod_verde = "\033[0;32m"
cod_azul = "\033[0;34m"
cod_mag = "\033[0;35m"
res_color = "\033[0m"

parser = argparse.ArgumentParser()
# Agrega argumentos
parser.add_argument('path', type=str, help='Path')
parser.add_argument('dias', type=int, help='Dias')
# Analiza argumentos
args = parser.parse_args()

# Se calcula la diferencia de dias
fecha_actual = datetime.datetime.now()
delta = datetime.timedelta(days=args.dias)
fecha_diferencia = fecha_actual - delta

# Entra al directorio
os.chdir(path=args.path)

archivos = os.listdir()
archivos.sort()
contador = 0
for archivo in archivos:

    ruta = args.path + "\\" + archivo
    
    # Calcular fechas de modificacion
    fecha_modificacion = os.path.getmtime(ruta)
    fecha_modificacion_ = time.ctime(fecha_modificacion)
    fecha_split = fecha_modificacion_.split()
    
    
    # Calcula tamanio
    tam = os.path.getsize(ruta)
    
    info_archivo = os.stat(ruta)
    permisos = info_archivo.st_mode
        
    
    if not os.path.isdir(ruta):
        dia_mod = fecha_split[2]
        mes_mod = fecha_split[1]
        mes_mod = list(calendar.month_abbr).index(mes_mod)
        anio_mod = fecha_split[-1]
        
        nueva_fecha = datetime.datetime(int(anio_mod), int(mes_mod), int(dia_mod))
        if fecha_diferencia < nueva_fecha:
            contador += 1
            print(f"{cod_azul}{archivo}\t{cod_rojo}{fecha_modificacion_}\t{cod_verde}{tam} bytes\t{cod_mag}{permisos}")
            # Resetear colores    
            print(res_color)
            


print(f"\n\n\t\tSE ENCONTRARON {contador} ARCHIVOS.\n\n")