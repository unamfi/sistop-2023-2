Tarea 1

Alumnos:
Aranzúa Chávez César Octavio
Carranza Ochoa José David

Problema: Los alumnos y el asesor
Un profesor asesora a varios estudiantes en su horario de atención.
Se debe modelar la interacción durante este horario de modo que la espera (para todos) sea tan corta como sea posible

- Un propfesor tiene x sillas en su cubículo. Cuando no hay alumnos que atender, las sillas sirven como sofá para que el profesor se acueste a la siesta
- Los alumnos pueden tocar a su puerta en cualquier momento, pero no pueden entrar más de w alumnos
- Para evitar confudnir al profesor, sólo un alumno puede presentar su duda (y epserar por la respuesta)
- Los demás alumnos deben esperar sentados su turno
- Cada alumno puede preguntar desde 1 hasta n preguntas (intercalando con las preguntas de los demás alumnos entre una pregunta y otra)


Lenguaje de Progrmación utilizado: Python3 (cualquier version)
Entorno de Desarrollo: Tener instalado Python3
Bibliotecas importadas: threading, objetos: Thread y Semaphore; time y random


Estrategia: 
Es una versión del problema del productor-consumidor clásico considerando un buffer y una lista de arreglos pares para representar a los alumnos y la cantidad de sus preguntas
Para poder tener el control sobre las preguntas y el tiempo de respuesta que tiene cada alumno, se implementó un multiplex** externo a la definición de alumno y profesor.
Se requiere un proceso de salida del sistema para evitar que se quede colgado, aunque claro que no es un punto recomendable en la implementación.
Se maneja un semáforo para que al estar manejando los hilos, se controle la impresión en pantalla
Se utiliza otro semáforo para despertar al profesor y los demás métodos de sincronización son mutex

Refinamiento:
No se inncluye ningún refinamiento, puesto que la delimitación del problema no prevía ninguno

Dudas:
¿Cómo detener de forma segura el programa o cuál es el hilo que deja colgada la ejecución?
¿De qué otra manera se pudiera modelar a los alumnos y sus preguntas?
¿Por qué es necesarias las funciones integradas de "global" para trabajr las variables en las funciones de alumno y profesor?


** Idea inspirada en el video de Gunnar Wolf (YouTube), recuperado de: https://www.youtube.com/watch?v=fxVAfCchI6k&t=2326s&ab_channel=GunnarWolf

