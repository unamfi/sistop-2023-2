''' Estos módulos proporcionan funciones para interactuar con el sistema operativo, 
acceder a información de archivos y manipular fechas y tiempos.'''
import os
import sys
import time

def informacion_archivo(archivo): #FUNCION PARA OBTENER LA INFORMACION DEL ARCHIVO
    #nombre = archivo
    nombre = os.path.relpath(archivo, "C:\\Users\\israe\\OneDrive\\Documentos\\CLUB PROBLEMS") #!NOMBRE
    longitud = os.path.getsize(archivo) #!TAMAÑO
    ultima_modificacion = os.path.getmtime(archivo) #!MODIFICACION
    modo = os.stat(archivo).st_mode #!PERMISOS
    return nombre, longitud, ultima_modificacion, modo

def imprecion_datos(nombre, longitud, ultima_modificacion, modo): #FUNCION PARA LA IMPRESION DEL ARCHIVO
    fecha_modificacion = time.ctime(ultima_modificacion)
    permisos = oct(modo)[2:]
    print(f"Nombre: {nombre}")
    print("*************************************************")
    print(f"Longitud: {longitud} bytes")
    print(f"Última modificación: {fecha_modificacion}")
    print(f"Modo (permisos): {permisos}")

def main():
    if len(sys.argv) != 3:
        print("formato no reconocido, inserte el formato adecuado")
        sys.exit(1)
    else:
         direc = sys.argv[1]
         days = sys.argv[2]  

    print(" ")
    print(direc+": <directorio> <número de días>")
    print(" ")
    directorio = str(direc)
    dias = int(days)
    if not os.path.isdir(directorio): #SI EL ARCHIVO NO EXISTE SE IMPRIME EL ERROR
        print("El directorio especificado no existe.")
        return

    archivos = os.listdir(directorio)
    archivos = [os.path.join(directorio, archivo) for archivo in archivos]

    archivos_seleccionados = []

    for archivo in archivos: #ARCHIVO
        if os.path.isfile(archivo):
            ultima_modificacion = os.path.getmtime(archivo)
            dias_transcurridos = (time.time() - ultima_modificacion) / (24 * 60 * 60) #CALCULO DEL TIEMPO
            if dias_transcurridos <= dias:
                archivos_seleccionados.append(archivo)

    archivos_seleccionados.sort()#Sorteo de los archivos para que vayan del que tiene mas tiempo modificado al que menos tiempo tiene.

    for archivo in archivos_seleccionados:
        nombre, longitud, ultima_modificacion, modo = informacion_archivo(archivo)
        imprecion_datos(nombre, longitud, ultima_modificacion, modo)
        print()

if __name__ == '__main__':
    main()
