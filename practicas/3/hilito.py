import threading
import random
from time import sleep


def ejecutar():
    sleep(random.random() * 10)  # esperamos entre 0 y 10 segundos
    print(f'{threading.current_thread().name} te saluda')

    sleep(random.random() * 10)  # esperamos entre 0 y 10 segundos
    print(f'{threading.current_thread().name} se despide')


# creamos los hilos
hilo1 = threading.Thread(target=ejecutar, name='Hilo 1')
hilo2 = threading.Thread(target=ejecutar, name='Hilo 2')
hilo3 = threading.Thread(target=ejecutar, name='Hilo 3')

# ejecutamos los hilos
hilo1.start()
hilo2.start()
hilo3.start()
