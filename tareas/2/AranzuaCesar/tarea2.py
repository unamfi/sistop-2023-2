#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
! Nombre del programa: tarea2.py
? Descripción: Especificando la carpeta (ruta absoluta) y la cantidad de días, se mostrará en pantalla el nombre, tamaño, permisos y fecha de actualización, de los archivos cuya fecha de modificación sea igual o menor a los días indicados: ./tarea2.py /home/user/Desktop 15
* Autor: César Octavio Aranzúa Chávez
Fecha: 3/6/23
Versión: 1.0
"""

import os, sys, stat
from datetime import datetime

ruta, dias = str(sys.argv[1]), int(sys.argv[2])
salida = []

if not (dias > 0):
  print("Debes especificar un número mayor que 0.\n")
  exit()

if not os.path.exists(ruta):
  print(f"[WinError 3] El sistema no encontró la ruta especificada. Verifica su existencia.\n")
  exit()

archivos_lista = os.listdir(ruta)                 # Obtener ficheros en carpeta, según la ruta indicada

print("\n\tNOMBRE\t\t\t   TAMAÑO\t\t\t     ULTIMA_MODIFICACIÓN\t\t  PERMISOS")
print("==========================================="*3)

for archivo in archivos_lista:
    archivo_ruta_abs = os.path.join(ruta, archivo) # Obtener ruta absoluta del elemento
    
    if os.path.isdir(archivo_ruta_abs):  continue  # Filtra si es directorio o fichero
    
    archivo_stats = os.stat(archivo_ruta_abs)      # Obtiene toda la información del archivo https://www.geeksforgeeks.org/ python-os-stat-method/
    
    # Bloque para validar la fecha de la última actualización (39-48)
    last_chagne = archivo_stats.st_mtime # Obtiene los segundos que han pasado desde la ultima modific
    fecha_modificacion = datetime.fromtimestamp(last_chagne) # Convierte segs a formato de fecha
    diferencia = datetime.now() - fecha_modificacion # Calcula cuántos días han pasado desde entonces
    result = diferencia.days  # Devuelve sólo los días transcurridos
    
    if result > dias: continue
    
    fecha_mod = fecha_modificacion.strftime("%d %b %Y, %I:%M %p") # Formatea el timestamp
    
    if archivo_stats.st_size <= 1024:               # Obtiene y convierte el tamaño del archivo
        tamaño = str(archivo_stats.st_size) + " B"
    elif 1024 < archivo_stats.st_size <= 1_048_576:
        tamaño = str(archivo_stats.st_size / 1024)[0:4] + " KiB"
    else:
        tamaño = str(archivo_stats.st_size / 2**20)[0:4] + " MiB"
    
    # Identifica permisos (en B), convierte a octal y los muestra con letras
    permisos = oct(archivo_stats.st_mode)[-3:] + " === " + stat.filemode(archivo_stats.st_mode)[1:]
    
    salida.append([archivo,tamaño,fecha_mod,permisos])

# Imprimir en formato de taabla
for i in salida:
    for j in i:
        print("{:<34}".format(j), end="")
    print()
print()

# print(f"{permisos}\t\t\t{tamaño}\t\t{fcha_mod}") https://stackoverflow.com/questions/53802256/python-print-string-alignment