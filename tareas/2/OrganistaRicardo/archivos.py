import os
import time
from datetime import datetime,timedelta

def main():
    direccion = input('Ruta:')
    dias = input('Numero de dias:')
    listar_archivos(direccion, dias)

def listar_archivos(direccion, dias):    
    datos = []
    largo = 0
    fecha_actual = datetime.now().date()
    fecha_usar = fecha_actual - timedelta(days=int(dias))
    print('Se mostraran archivos a partir de la fecha: ',fecha_usar)
    try:
        files = os.listdir(direccion)
        files.sort()
        count = 0
        for arc in files:
            if len(arc) > largo:
                largo = len(arc)
            ruta = direccion + arc
            info = os.stat(ruta)
            fecha_mod = time.strftime("%Y-%m-%d",time.localtime(info.st_mtime))
            fecha_mod = datetime.strptime(fecha_mod,'%Y-%m-%d').date()
            tamaño = info.st_size
            modo = info.st_mode
            if fecha_usar < fecha_mod:
                datos.append([arc,str(fecha_mod),tamaño,modo])
                count += 1
        formato = "{:<"+str(largo+2)+"} {:<14} {:<8} {:<5}"
        print("Nombre".ljust(largo+3)+"Modificación".ljust(14)+"Tamaño".ljust(10)+"Modo")
        largo = largo+32
        print("="*largo)
        for fila in datos:
            print(formato.format(*fila))
    

    except FileNotFoundError:
        print('No se encontro la ruta especificada')

main()