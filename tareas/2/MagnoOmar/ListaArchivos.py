import os
import time

#Creamos una funcion para nuestra tarea
def listar_archivos_modificados(directorio, num_dias): 
    #Usamos un arreglo para guardar los archivos para después imprimirlos:
    archivos_modificados = []

    #Calculamos la fecha actual
    fecha_actual = time.time()

    # Vamos a imrpimir solamente archivos dentro de un lapso de dias
    fecha_limite = fecha_actual - (num_dias * 24 * 60 * 60)

    #Empezamos a recorrer el directorio
    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)

        # Verificar si el archivo cumple con la condición de modificación
        if os.path.isfile(ruta_archivo) and os.path.getmtime(ruta_archivo) >= fecha_limite:
            # Obtenemos los detalles del archivo
            longitud = os.path.getsize(ruta_archivo)
            fecha_modificacion = time.ctime(os.path.getmtime(ruta_archivo))
            permisos = oct(os.stat(ruta_archivo).st_mode)[-3:]

            #Agregamos el archivo leido al arreglo
            archivos_modificados.append((archivo, longitud, fecha_modificacion, permisos))

    # Ordenamos la lista de archivos modificados lexicográficamente por nombre de archivo
    archivos_modificados.sort()

    return archivos_modificados

#------ZONA DE MODIFICACIÓN------------
#Aquí puedes cambiar al directorio y asignar el numero de días para visualizar los archivos
directorio = r"C:\Users\jakal\Downloads"  
num_dias = 10  
#------FIN ZONA DE MODIFICACIÓN--------

archivos_modificados = listar_archivos_modificados(directorio, num_dias)
print("Archivos modificados en los últimos", num_dias, "días:")
#Finalmente, imprimos los archivos

txnombre = "Nombre"
txlongitus = "Longitud"
txmodificacion = "Ult. Fecha Mod"
txpermisos = "Permisos"

print(f"{txnombre:^40}   {txlongitus:^20}   {txmodificacion:^30}   {txpermisos:^15} \n")

for archivo, longitud, fecha_modificacion, permisos in archivos_modificados:
    nombre_columna = f"{archivo}"
    longitud_columna = f"{longitud}"
    fecha_modificacion_columna = f"{fecha_modificacion}"
    permisos_columna = f"{permisos}"
    
    print(f"{nombre_columna:^40} | {longitud_columna:^20} | {fecha_modificacion_columna:^30} | {permisos_columna:^15}")

"""
Por ejemplo, en mi caso la salida generada seria:

                 Nombre                          Longitud                 Ult. Fecha Mod              Permisos

               838756.png                |       1332627        |    Mon Jun  5 22:15:30 2023    |       666
       DocumentacionProyecto.pdf         |        28713         |    Mon Jun  5 22:16:12 2023    |       666
           ProyectoFinal.dia             |        11907         |    Sun Jun  4 13:45:08 2023    |       666
           ProyectoFinal.dia~            |        11687         |    Sun Jun  4 13:40:33 2023    |       666
           ProyectoFinal.png             |        282087        |    Sun Jun  4 13:48:49 2023    |       666
             Update5Jun.sql              |         3736         |    Mon Jun  5 20:21:39 2023    |       666
             Windows10.iso               |      4810539008      |    Sun Jun  4 19:12:08 2023    |       666
             
"""