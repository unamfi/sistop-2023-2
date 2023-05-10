# Manual y Documentación de la Tarea 1
* Problema a Resolver: 	Ejercicio del varias alumnos y el asesor
* Lenguaje utilizado: 	Python

Para que el archivo en Python funcione correctamente, es necesario tener las bibliotecas threading, random y time instaladas en la computadora. Ya teniendo las bibliotecas, desde una terminal se tiene que ubicar en el directorio donde se encuentra el archivo y ejecutar el siguiente comando.
        
                py asesor.py

Una vez ejecutado el programa, lo primero que se mostrará será el número total de alumnos y el número total de sillas.  Ya que al definir estos valores de forma aleatoria, como aparece en la siguiente imagen, se pueden presentar 3 casos:

                num_alumnos = random.randint(0,35)
                num_sillas  = random.randint(10,20)
 
1. El número de alumnos sea mayor al número de sillas.
2. El número de sillas sea mayor al número de alumnos.
3. Ambos sean iguales.

De acuerdo con estos casos, el planteamiento de los semáforos para utilizar las sillas es el mismo, pero su comportamiento es diferente. Se crea un semáforo de acuerdo con el número de sillas que se presenta.

                sillas_libres = threading.Semaphore(num_sillas)

Cuando se llame a la función threading.Thread() con objetivo la función alumno, se buscará adquirir una silla, si se logra con éxito entonces se mostrará que el alumno entro al salón con x dudas. El número de dudas será de forma aleatoria desde 1 hasta 5. También se crea un mutex para el profesor con valor de 1, esto funciona de tal manera que el profesor puede responder solamente una pregunta de un alumno a la vez, después puede tomar una duda del mismo alumno o de otro.

## Planteamiento para resolver dudas

Para realizar esta solución de dudas se tienen tres plantemientos:

1. Que extraiga la primera pregunta insertada en la lista
 
                pareja = orden_preguntas.pop(0)

2. Que extraiga la última pregunta insertada.

                pareja = orden_preguntas.pop()

3. Que se de forma aleatoria

                index  = random.randint(0,len(orden_preguntas)-1)
                pareja = orden_preguntas.pop(index)

### Comportamiento del orden de dudas

El comportamiento de cada una de estas implementaciones son las siguientes:

1. Cuando la implementación es que extraiga la primera en ingresar, la solución de dudas empieza desde el alumno con menor índice hasta el que tiene mayor índice. Además, de que las dudas son secuenciales; esto quiere decir que primero resuelve todas las dudas de alumno 0, después todas las del alumno 1 y así sucesivamente. Esta forma de solución es mas eficiente para los primeros alumnos, pero es menos eficiente para los últimos alumnos.

2. Al utilizar esta solución se presenta el caso inverso al anterior. El último alumno en entrar al salón será la primera persona en resolver sus dudas. De igual forma es secuencial y avanza con el siguiente alumno hasta terminar todas las dudas del actual. La diferencia radical es que aquí las dudas si son respondidas en el orden adecuado.
 
3. Al ser de forma aleatoria la duda del alumno que resuelve es impredecible, por lo tanto, es imposible determinar si es la mejor más eficiente para que un alumno no pierda tanto tiempo. Con este método se hace la simulación de que se puede resolver otra duda de cualquiera de los alumnos dentro del salón, no necesariamente en orden.
 
Independientemente de cuál método se trabaje para contestar las dudas, cuando el número de alumnos es mayor que el de sillas, primero entran los alumnos equivalentes al número de sillas, y una vez que uno salga del salón sin dudas, otro alumno entra a tomar la silla. El nuevo alumno que entra tiene que esperar su turno para que sus dudas sean resueltas.
 
Para hacer la simulación de que los alumnos llegan de forma no secuencial, se puede poner un time.sleep() con parámetro aleatorio antes de adquirir una silla. De esta forma, la llegada de los alumnos al salón es aleatorio.

                time.sleep(random.randint(0,10))
                sillas_libre.acquire()

Al finalizar todas las dudas, el profesor se vuelve a dormir, el problema que luego presenta el programa es que se va a dormir y luego vuelve a resolver dudas pero no dice cual se duda está resolviendo y después se vuelve a dormir. Intuitivamente se tienta que la esto se debe a la condición de carrera por escribir en la consola. En este caso hay un momento en donde la lista de dudas está vacía, el profesor se duerme y luego vuelven a llegar más alumnos a contestar sus dudas, pero por la condición de carrera no se logra observar adecuadamente.
 
                Todas las dudas del alumno 12 han sido resueltas y sale del salon
                El profesor está durmiendo
                El profesor empieza a resolver dudas
                El profesor está durmieno