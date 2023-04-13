#!/usr/bin/python3
import os
import signal
import time

def chld_handler(signum, frame):
    pid, status = os.wait()
    if status == 0:
        print(" ** Hijo %d: OK!" % pid)
    else:
        print("-!- El hijo %d terminó con estado %d" % (pid,status))

def int_handler(signum, frame):
    # print("OK, OK, no seas impaciente, ya me voy!")
    # exit(0)
    print("No me voy, ¡no y no!")

def window_change_handler(signum,frame):
    print("Cambió el tamaño de la terminal.")

# Registramos los manejadores de señal que tenemos definidos
signal.signal(signal.SIGCHLD, chld_handler)
signal.signal(signal.SIGINT, int_handler)
signal.signal(signal.SIGWINCH, window_change_handler)

# Para "separar" el proceso actual en dos procesos usamos fork()
for i in range(10):
    pid = os.fork()
    if pid == 0:
        # Proceso hijo
        print("¡Saludos desde el proceso hijo %d!" % os.getpid() )
        time.sleep(3)
        print("El hijo termina y sale.")
        exit(1)
    else:
        # Proceso padre
        print("El PID del proceso hijo es %d" % pid)
        time.sleep(5)
        print("Continúa el ciclo...")
