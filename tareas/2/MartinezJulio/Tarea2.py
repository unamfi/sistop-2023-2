from os import scandir, getcwd
from os.path import abspath
import os
import time

def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

def lsn(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

def main():
    print("Ingresa la ruta\n")
    ruta=input()
    print("Ingresa el número de días\n")
    dias=input()
    
    diass=int(dias)*24*60*60 #Dias ingresados en segundos
    tiempoactual=time.time()
    resta=int(tiempoactual)-int(diass) #Fecha actual menos los dias ingresados
    
    lista = ls(ruta) #Se obtiene la ruta completa de cada archivo
    listan= lsn(ruta) #Obtiene solo los nombres de los arv¿chivos
    
    lon=len(lista)
    
    #print(tiempo)
    print ("{:<35} {:<30} {:<15} {:<0}".format('Nombre','Modificación','Modo','Tamaño'))
    for i in range(0,lon):
        tiempo=os.path.getmtime(lista[i])
        #if(tiempo>=resta):
        nombre=listan[i]
        estado=os.stat(nombre)
        mod=format(time.ctime(os.path.getmtime(lista[i])))
        tam=os.path.getsize(lista[i])
        modo=estado.st_mode
        if(int(tiempo)>=resta):
            print ("{:<35} {:<30} {:<15} {:<0}".format(nombre,mod,modo,tam))
main()