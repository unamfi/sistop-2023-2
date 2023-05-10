import threading
import time

def saluda():
    print(f'{threading.current_thread().name} saluda')

    time.sleep(0.5)
    print(f'{threading.current_thread().name} dice byeee')


hilo1 = threading.Thread(target=saluda, name='Hilo 1')
hilo2 = threading.Thread(target=saluda, name='Hilo 2')
hilo3 = threading.Thread(target=saluda, name='Hilo 3')

hilo1.start()
hilo2.start()
hilo3.start()

print("Yo soy el hilo principal")
print(f'{threading.current_thread().name} {threading.get_native_id()}')