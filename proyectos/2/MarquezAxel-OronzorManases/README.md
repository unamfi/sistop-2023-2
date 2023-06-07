# Proyecto 2: Planificación por Retroalimentación Multinivel y por Lotería

    Planteamiento: 2023.04.27
	Entrega: 2023.05.09

# La planificación por Lotería

        Archivos: planificacion_por_retroalimentacion_loteria.py
                y planificacion_por_retroalimentacion_loteria_2.py 


Abordamos solo el primer programa sobre  _planificación por lotería_

    def generar_carga_trabajo():
    cantidad_procesos = random.randint(5, 8) #Procesos
    duracion_total = 120  # Máximo de ticks
    
    carga_trabajo = []
    
    for i in range(cantidad_procesos):
        proceso = {
            'nombre': chr(65 + i),  # Procesos desde la A en adelante
            'llegada': random.randint(0, duracion_total), #Tick en que llega
            'duracion': random.randint(1, duracion_total // cantidad_procesos), #Ticks que necesita
            'boletos': random.randint(1, 100), #Probabilidades de participar
            'tick_inicio': -1,
            'tick_final': -1
        }
        carga_trabajo.append(proceso) # se van agregando a la carga de trabajo los procesos
    
    return carga_trabajo

Explicaremos un poco la funcion anterior:

import random: Importa el módulo random, el cual permite generar números aleatorios.

def generar_carga_trabajo():: Define la función generar_carga_trabajo().

cantidad_procesos = random.randint(5, 8): Genera un número aleatorio entre 5 y 8 (ambos inclusive) y lo asigna a la variable cantidad_procesos. Esta variable representa la cantidad de procesos que se generarán en la carga de trabajo.

duracion_total = 120: Asigna el valor 120 a la variable duracion_total. Este valor representa la duración máxima en ticks para los procesos en la carga de trabajo.

carga_trabajo = []: Crea una lista vacía llamada carga_trabajo que almacenará los procesos generados.

for i in range(cantidad_procesos):: Inicia un bucle que se ejecutará cantidad_procesos veces. El bucle se encarga de generar los procesos y agregarlos a la lista carga_trabajo.

proceso = {...}: Crea un diccionario llamado proceso que representa un proceso individual en la carga de trabajo. El diccionario tiene las siguientes claves y valores:

'nombre': chr(65 + i): La clave 'nombre' representa el nombre del proceso y se genera usando la función chr() para convertir el número 65 + i en su correspondiente carácter ASCII. Esto asignará nombres a los procesos empezando desde la letra 'A' y aumentando en orden alfabético.

'llegada': random.randint(0, duracion_total): La clave 'llegada' representa el tick en el que llega el proceso y se asigna un número aleatorio entre 0 y duracion_total (inclusive) utilizando la función random.randint().

'duracion': random.randint(1, duracion_total // cantidad_procesos): La clave 'duracion' representa la cantidad de ticks que necesita el proceso para completarse. Se asigna un número aleatorio entre 1 y duracion_total // cantidad_procesos (la división entera de duracion_total entre cantidad_procesos).

'boletos': random.randint(1, 100): La clave 'boletos' representa las probabilidades de participación del proceso. Se asigna un número aleatorio entre 1 y 100.

'tick_inicio': -1 y 'tick_final': -1: Estas claves representan los ticks de inicio y finalización del proceso. Se inicializan con el valor -1 para indicar que aún no han sido asignados.

carga_trabajo.append(proceso): Agrega el diccionario proceso a la lista carga_trabajo, es decir, añade el proceso generado a la carga de trabajo.

return carga_trabajo: Devuelve la lista carga_trabajo que contiene todos los procesos generados.


            def simular_planificacion (carga_trabajo){...} No pondremos todo el codigo, es mucho :c


La función simular_planificacion(carga_trabajo) realiza una simulación de la planificación de procesos en una carga de trabajo. La simulación se realiza en ticks, donde cada proceso tiene una duración y puede participar en la ejecución según su llegada y probabilidades de participación.

La simulación se divide en dos pasadas. En la primera pasada, se ejecutan los procesos que están listos en cada tick, siguiendo un esquema de probabilidades basado en los boletos asignados a cada proceso. Se actualizan los ticks de inicio y finalización de los procesos, se registra la secuencia de ejecución y se incrementan los boletos de los procesos que no están siendo ejecutados.

Si al final de la primera pasada aún quedan procesos sin completar, se realiza una segunda pasada para ejecutar los procesos restantes hasta que todos se completen.

El resultado de la simulación es una cadena llamada ejecucion que contiene la secuencia de ejecución de los procesos.

En si, la función simula la planificación de procesos en una carga de trabajo, siguiendo un esquema de probabilidades y registrando los ticks de inicio y finalización de cada proceso.

carga_trabajo = generar_carga_trabajo()

		# Se muestran los datos generales de los procesos
		print("Carga de trabajo generada:")
		for proceso in carga_trabajo:
		    print(f"Proceso {proceso['nombre']}: Llegada={proceso['llegada']}, Duración={proceso['duracion']}, Boletos={proceso['boletos']}")

		# Se realiza la simulacion de los ticks y se guarda el orden en "Orden ejecucion"
		orden_ejecucion = simular_planificacion(carga_trabajo)

		# Orden de ejecucion de los procesos
		print("\nOrden de ejecución:")
		print(orden_ejecucion)

		# Tabla de informacion de los proceos
		print("\nInformación detallada de cada proceso:")
		for proceso in carga_trabajo:
		    tick_inicio = proceso['tick_inicio']
		    tick_final = proceso['tick_final']
		    if tick_inicio != -1 and tick_final != -1:
		        tick_total = tick_final - tick_inicio + 1
		    else:
		        tick_total = 0
		    print(f"Proceso {proceso['nombre']}: Inicio={tick_inicio}, Final={tick_final}, Total={tick_total}")


Finalmente nos encontramos con la parte de la ejecucion donde podemos visualizar mas como se comporta nuestro codigo, es asi que manda a llamar las funciones para su ejecucion.
Es por ello que debemos de entender un poco sobre lenguaje de programacion basica para poder entender el como se ejecutan uno a uno los procesos y las llamadas de estos, como tal aqui ya vemos tanto el orden de ejecucion como las dos tablas con los datos.

Comentarios: En este programa vemos como se efectua de manera lineal, dependiendo de como ganen el tiket y su prioridad se ejecutaran en conjunto, planteamos algo similar en el segundo programa pero tomando en consideracion de espacios vacios y con otra forma de programacion, esta a partir de funciones y con otra organizacion en la forma en que se muestran los datos.

#Planificacion por multinivel

		  Programa: planificacion_por_retroalimentacion_multinivel

Abordaremos el programa por algunas partes mas importantes:

		 def generacion_procesos():
		    procesos = [{'nombre': chr(ord('A') + i),
		                 'llegada': randint(0, 10 * i),
		                 'duración': randint(4, 10)} #Aqui en varias ejecuciones se puede mostrar huecos
		                 #'duración': randint(4, 20)} #Aqui ya es poco probable que presente huecos
		                for i in range(randint(5, 8))]

		    return procesos

Explicaremos esta funcion:

Se define una función llamada generacion_procesos() sin ningún parámetro.
La variable num_procesos se inicializa con un número aleatorio entre 5 y 8 utilizando la función randint(a, b) de la librería random.
La variable max_llegada se calcula multiplicando num_procesos por 10. Esto establece el rango máximo para los tiempos de llegada de los procesos en función del número de procesos generados.
La variable procesos se inicializa como una lista vacía.
Se utiliza una comprensión de listas para generar los procesos. Para cada valor i en el rango de num_procesos:
Se crea un diccionario que representa un proceso con las siguientes claves:
'nombre': Un carácter que se obtiene sumando el valor ASCII de 'A' con i. Esto generará nombres consecutivos como 'A', 'B', 'C', etc.
'llegada': Un número aleatorio entre 0 y max_llegada utilizando randint(0, max_llegada).
'duración': Un número aleatorio entre 4 y 10 utilizando randint(4, 10).
Se retorna la lista procesos que contiene los procesos generados.

		def ejecucion_procesos(procesos):
		    t = 0
		    res = ''
		    print('* Inicia ejecución')
		    
		    # Lista de colas de procesos
		    colas = [[] for _ in range(3)]  # 3 niveles de colas
		    quantum = [4, 8, 12]  # Quantum para cada nivel
		    
		    # Parte donde se distribuyen los procesos en las colas según su llegada
		    for proceso in procesos:
		        nivel = 0
		        if proceso['llegada'] >= 10:
		            nivel = 2
		        elif proceso['llegada'] >= 5:
		            nivel = 1
		        colas[nivel].append(proceso)
		    
		    while any(cola for cola in colas):
		        for i, cola in enumerate(colas):
		            if cola:
		                proceso = cola.pop(0)
		                print("t=%d" % t)
		                if t < proceso['llegada']:
		                    demora = proceso['llegada'] - t
		                    res += '-' * demora
		                    t += demora
		                    print("    ... %d tick" % demora)
		                    print("t=%d" % t)
		                
		                duracion_restante = proceso['duración']
		                if duracion_restante <= quantum[i]:
		                    res += proceso['nombre'] * duracion_restante
		                    t += duracion_restante
		                    print("    ⌚ %s %d tick (Nivel %d)" % (proceso['nombre'], duracion_restante, i+1))
		                else:
		                    res += proceso['nombre'] * quantum[i]
		                    t += quantum[i]
		                    print("    ⌚ %s %d tick (Nivel %d)" % (proceso['nombre'], quantum[i], i+1))
		                    proceso['duración'] -= quantum[i]
		                    cola.append(proceso)
		                break

		    return res, t

Explicaremos un poco el codigo:

Se inicializan las variables t y res. t representa el tiempo actual y res almacena la secuencia de ejecución de los procesos.
Se crea una lista colas para representar las colas de procesos de cada nivel. En este caso, se crean 3 colas vacías utilizando una comprensión de listas.
Se define una lista quantum que contiene los valores de quantum para cada nivel. En este ejemplo, se establecen valores de 4, 8 y 12 para los niveles 0, 1 y 2 respectivamente.
Se recorren los procesos y se asignan a las colas correspondientes según su tiempo de llegada. Si el tiempo de llegada es mayor o igual a 10, el proceso se asigna al nivel 2. Si es mayor o igual a 5, se asigna al nivel 1. De lo contrario, se asigna al nivel 0.
Se inicia un bucle principal que se ejecuta mientras haya procesos en alguna de las colas.
Se recorren las colas en orden, comenzando desde el nivel más alto (nivel 2) hasta el nivel más bajo (nivel 0).
Para cada nivel, se verifica si hay procesos en la cola. Si la cola no está vacía, se extrae el primer proceso de la cola.
Se comprueba si el tiempo actual es menor que el tiempo de llegada del proceso. Si es así, se agrega una cadena de guiones ("-") a res para representar el tiempo de espera.
Se verifica la duración restante del proceso. Si es menor o igual al quantum del nivel actual, se ejecuta el proceso completo. Se agrega la secuencia de caracteres correspondiente al proceso en res y se actualiza el tiempo actual.
Si la duración restante del proceso es mayor que el quantum, se ejecuta solo el quantum del nivel actual. Se agrega la secuencia de caracteres al res, se actualiza el tiempo actual y se reduce la duración restante del proceso.
Después de ejecutar el proceso, se agrega nuevamente a la cola correspondiente si aún tiene una duración restante.
Si se ejecutó un proceso en algún nivel, se rompe el bucle interno y se pasa al siguiente ciclo del bucle principal.
La función retorna la secuencia res y el tiempo t al finalizar la ejecución de todos los procesos.

tenemos tambien una seccion de calculos llamada:

		 def calculos(procesos, res):
		    pT = 0;pE = 0;pP = 0;pR = 0
		    for proc in procesos:
		        inicio = res.index(proc['nombre'])
		        fin = inicio + proc['duración']
		        t = fin - proc['llegada']
		        t1 = fin - inicio
		        pT += t / len(procesos)
		        E = t - (fin - inicio)
		        pE += E / len(procesos)
		        P = t / (fin - inicio) * 1.00
		        pP += P / len(procesos)
		        R = 1 / P
		        pR += R / len(procesos)
		        print("{:^8s}|{:^8d}|{:^5d}|{:^8d}|{:^8d}|{:^14.2f}|{:^10.2f}".format(
		                proc['nombre'], inicio, fin, t1, E, P, R))
		    
		    return pT, pE, pP, pR

Aqui es donde entran en juego los conceptos que se leyeron en el libro sobre este tema, estos procesos se pueden esplicar de la siguiente manera:

Se inicializan las variables pT, pE, pP y pR para almacenar los promedios de tiempo de retorno, tiempo de espera, penalización y respuesta respectivamente.
Se recorren los procesos en la lista procesos.
Para cada proceso, se obtiene el índice de inicio en la secuencia res utilizando el método index(). El índice de fin se calcula sumando la duración del proceso al índice de inicio.
Se calcula el tiempo de retorno (t) restando el tiempo de llegada del proceso al índice de fin.
El tiempo de ejecución del proceso (t1) se calcula restando el índice de inicio del índice de fin.
Se calcula el tiempo de espera (E) restando la duración real del proceso (índice de fin - índice de inicio) al tiempo de llegada del proceso.
Se calcula la penalización (P) dividiendo el tiempo de retorno entre el tiempo de ejecución real del proceso y multiplicando por 1.0.
Se calcula el tiempo de respuesta (R) como el inverso de la penalización.
Se acumulan los valores de tiempo de retorno, tiempo de espera, penalización y respuesta en las variables pT, pE, pP y pR respectivamente.
Se imprime una línea de información para cada proceso que muestra los valores calculados.
Finalmente, se retorna los promedios de tiempo de retorno, tiempo de espera, penalización y respuesta.

Estas son las funciones mas importantes del programa, ya al final solo se llama a otra tabla donde estan todos los datos y dentro de ella la funcion anterior para mostrar los datos calculados.

Comentarios: En este programa que fue donde mas nos llevo tiempo codificar, principalmente por su logica, aprendimos mas sobre el uso de la planificacion por multinivel, se tuvo que recurrir a la ayuda de los libros y mas a aparte las presentaciones vistas en clase.

#Parte de las preguntas:

¿Cómo se compararía este método con los otros abordados?

La planificación por lotería es más equitativa y justa, ya que todos los procesos tienen una oportunidad de ser seleccionados para la ejecución.
El algoritmo de retroalimentación multinivel permite la ejecución de procesos en múltiples niveles de prioridad y tiene la capacidad de ajustar las prioridades en tiempo de ejecución.

¿Para qué tipo de carga es más apto y menos apto?

La planificación por lotería puede ser adecuada para cargas de trabajo heterogéneas, donde los procesos tienen diferentes requerimientos y prioridades.
Pero es  menos adecuado para cargas de trabajo con requisitos de tiempo real estrictos, donde se necesita garantizar tiempos de respuesta predecibles y mínimos.

Por lo tanto la planificacion por loteria es menos apto y la planificacion por multinivel es mas apto para procesos reales.

¿Qué tan susceptible resulta a producir inanición?

La planificación por lotería es menos susceptible a producir inanición porque todos los procesos tienen una probabilidad de ser seleccionados para la ejecución en cada ronda de lotería.

¿Qué tan justa sería su ejecución?

La planificación por lotería se considera justa ya que todos los procesos tienen una oportunidad igual de ser seleccionados para la ejecución.

¿Qué modificaciones requeriría para planificar procesos con necesidades de tiempo real? (aunque sea tiempo real suave)

Para planificar procesos con necesidades de tiempo real, como tiempo real suave, se podrían introducir modificaciones para asignar una mayor cantidad de tickets a los procesos con mayores requisitos de tiempo y prioridades más altas. Esto aumentaría las posibilidades de que esos procesos sean seleccionados para la ejecución.

¿Alguna otra reflexión o inquietud que les provoque?

Si, bueno en lo personal nos gustaria ver su implementacion sobre estos dos plantamientos para hacer correcciones para mejorar nuestra implrmentacion en el codigo.

Fin :D



