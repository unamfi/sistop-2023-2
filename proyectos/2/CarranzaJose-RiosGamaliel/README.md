# **Proyecto 2:** Planificación por Retroalimentación Multinivel y por Lotería

<pre>
<b>Materia:</b> Sistemas Operativos
<b>Grupo:</b> 6
<b>Alumnos:</b> Carranza Ochoa, José David; Ríos Lira, Gamaliel
<b>Fecha:</b> 09/05/2023
</pre>

***
# Lenguaje de programción utilizado
Para el proyecto no se sugirió el uso de ningún lenguaje de programación en específico; por ello, se decidió hacer una págica web a la que se le brindó interacción a través del lenguaje de programación `JavaScript` en combinación con las tecnologías `HTML 5` y `CSS 3`. De esta forma, se logró construir una interfaz de usuario más atractiva y con más funcionaliad que lo que sería un entorno de terminal.

***
## Desarrollo del programa
Nos enfocaremos a explicar más el funcionamiento de los algoritmos programados 
que la interfaz de usuario diseñada, aunque se destacarán algunos aspectos de 
la misma.

La mayor parte de la lógica se encuentra dentro del archivo 
[common.js](./common.js). Se comenzó por diseñar las clases referentes a los 
procesos que admitiría cada algoritmo. `JavaScript` por sí mismo no tiene un 
paradigma orientado a objetos convencional, pero se intentaron asimilar 
algunos conceptos que manejas otros lenguajes como `Java` o `C#`.

La primer clase que se creó fue `Process`, la cual pretende ser una clase 
abstracta que encapsule los sigueintes campos:
- `name`: El nombre del proceso (que para este caso, a todos los procesos que 
  les asigna una letra).
- `duration`: El número de _ticks_ necesario para ejecutar el proceso.
- `start`: El momento en el que llega el proceso a la ejecución principal.
- `end`: El momento en la ejecución principal en la que el proceso termina su 
  ejecución. En un comienzo, este valor está dado por `null`; lo cual se puede 
  usar como una condición para vreificar si un proceso ha terminado o no.
- `metrics`: Devuelve un objeto con las propiedades `T`, `E` y `P`, las cuales 
  describen algunas estadísticas de un proceso a través de las cuales se puede 
  medir el rendimiento del mismo.

La clase abstracta anterior se toma como clase padre para dos clses 
adicionales. Por un lado, se tiene la clase `MultilevelProcess`, la cual 
simplemente agrega el concepto de prioridad (a través del campo `priority`) 
para penderar la urgencia con la que debe ser atendido un proceso. Por otro 
lado, se tiene la clase `LotteryProcess`, la cual implementa el concepto de 
_tickets_ (con el campo `tickets`), a través de los cuales un proceso puede 
acceder a la ejecución principal; de forma general, entre más tickets tenga, 
más probabilidad de ejecución tiene.
