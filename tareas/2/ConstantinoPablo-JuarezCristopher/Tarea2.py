import os
import time
import sys

def info_archivos(ruta, dias):
    conta = 0
    tiempo_actual = time.time()
    dif = dias * 24 * 60 * 60
    final = tiempo_actual - dif
    print("Fecha Restada:", time.strftime("%Y-%m-%d", time.localtime(final)))

    archivos = ruta

    with os.scandir(archivos) as archivos_v:
        archivos_ordenados = sorted(archivos_v, key=lambda a: a.name)

        for archivo in archivos_ordenados:
            ti_c = os.path.getctime(archivo)
            ti_co = int(ti_c)
            c_ti = time.ctime(ti_co)
            c_ti_epoca = time.mktime(time.strptime(c_ti))
            info = os.stat(archivo)

            if c_ti_epoca >= final:
                conta += 1
                tam = os.path.getsize(archivo)
                permisos = info_permisos(archivo.path)
                
                print('Archivo: {} | Modificacion: {} | Tamaño: {} bytes | Permisos: {}'.format(archivo.name, c_ti, tam, permisos))
    
    print('\ntotal de archivos: {}'.format(conta))

def info_permisos(path):
    permisos = ""
                
    if os.access(path, os.R_OK):
        permisos += "r"
    else:
        permisos += "-"
                
    if os.access(path, os.W_OK):
        permisos += "w"
    else:
        permisos += "-"
                
    if os.access(path, os.X_OK):
        permisos += "x"
    else:
        permisos += "-"

    return permisos


if len(sys.argv) != 3:
    print("Argumentos incorrectos")
    sys.exit(1)
else:
    ruta = sys.argv[1]
    dias = sys.argv[2]

info_archivos(str(ruta), int(dias))
