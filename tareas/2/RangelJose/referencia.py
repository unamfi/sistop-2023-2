import os
from tabulate import tabulate
import sys 
from datetime import datetime, timedelta

ruta = sys.argv[-2]
dias = sys.argv[-1] 

if (not os.path.exists(ruta)) :
    print("Directorio incorrecto.")
    exit()
elif(int(dias) < 0):
    print("Dias mayores o igual a 0")
    exit()
else:
    ruta = os.path.abspath(ruta)
    today = datetime.now()
    today += timedelta(days = -1 * int(dias))
    listDir = [["Nombre","Creacion", "Modificacion","Modo","Tamaño [Bytes]"]]
    list = os.listdir(ruta)
    for i in list:
        try:
            aux = []
            stats = os.stat(f"{ruta}\\{i}")
            t_c = datetime.fromtimestamp(os.path.getctime(f"{ruta}\\{i}"))
            t_m = datetime.fromtimestamp(os.path.getmtime(f"{ruta}\\{i}"))
            mode = stats.st_mode
            size = stats.st_size
            if(t_m.date() >= today.date()):
                aux.append(i)
                aux.append(t_c)
                aux.append(t_m)
                aux.append(mode)
                aux.append(size)
                listDir.append(aux)
        except:
            pass
    
    print(tabulate(listDir))