#!/usr/bin/python3
#
# ¡No hagan esto en casa! Esto emplea modificación SIN sincronización.
# Depende de que el programador sea muy diligente y no meta las patas
#
# Y yo las meto todo el tiempo...
import threading
import time

arreglo = [0,0,0,0,0,
           0,0,0,0,0]
print("Arreglo inicial: %s" % arreglo)

def avanza_por_el_arreglo(base):
    print("Lanzando hilo con base en %d" % base)
    global arreglo
    for i in range(5):
        arreglo[base + i] = i
        time.sleep(1)

threading.Thread(target=avanza_por_el_arreglo, args=[0]).start()
threading.Thread(target=avanza_por_el_arreglo, args=[5]).start()

while True:
    print("Arreglo: %s" % arreglo)
    time.sleep(1)
