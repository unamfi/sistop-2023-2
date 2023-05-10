#Este código debería generar un archivo txt, el cual git debería ignorar.

from time import sleep, perf_counter

def aThread():
    
    print('Usamos un Hilo para este proceso')
    
    print('Creamos un archivo')
    f = open('ignorame.txt','w')
    f.write('Este texto tiene muchas incongruencias, como por ejemplo, 2+2 = pez o que el PRI va a llegar a la presidencia, por lo tanto debe ser ignorado')
    
    sleep(1)
    
    print('Done')
    
start_time = perf_counter()

aThread()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')    