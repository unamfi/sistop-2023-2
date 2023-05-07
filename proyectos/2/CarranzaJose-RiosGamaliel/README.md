# **Proyecto 2:** Planificación por Retroalimentación Multinivel y por Lotería

<pre>
<b>Materia:</b> Sistemas Operativos
<b>Grupo:</b> 6
<b>Alumnos:</b> Carranza Ochoa, José David; Ríos Lira, Gamaliel
<b>Fecha:</b> 09/05/2023
</pre>

***
# Lenguaje de programación utilizado
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

La clase abstracta anterior se toma como clase padre para dos clases 
adicionales. Por un lado, se tiene la clase `MultilevelProcess`, la cual 
simplemente agrega el concepto de prioridad (a través del campo `priority`) 
para ponderar la urgencia con la que debe ser atendido un proceso. Por otro 
lado, se tiene la clase `LotteryProcess`, la cual implementa el concepto de 
_tickets_ (con el campo `tickets`), a través de los cuales un proceso puede 
acceder a la ejecución principal; de forma general, entre más tickets tenga, 
más probabilidad de ejecución tiene.

### Multinivel 

La carga de los procesos es predefinida antes de realizar su ejecución, esto se realiza desde los valores de los inputs al final de la página; no obstante, dichos parámetros son ajustables a como se desee, `processes` mantiene el registro de valores que serán cargados al programa.

Al ejecutarse el algoritmo, se obtienen los procesos que están listos para ser ejecutados, tal que se asigna una prioridad de -1 para establecer la auscencia de prioridad para todos los procesos. Con esto, `_exec` verifica si hay procesos nuevos y los agrega en la cola de prioridad, después escogemos aquel con la prioridad más alta (cola con prioridad más baja) y se ejecuta el primer proceso de la cola, el número de ticks depende de `2**n`.

En este punto ahora se consideran 2 casos para los procesos:
- Ha terminado de ejecutarse, se actualiza su prioridad y se elimina de la cola 
- No ha terminado de ejecutarse, se mueve a una cola de prioridad más baja con el fin de mantener un orden en ejecución entre procesos.

Cabe mencionar que la prioridad se establece en 0 tras la llegada de un proceso acorde al tiempo estimado. Tal y como se esperaría, los procesos con una prioridad 0 son los primeros en ejecutarse, esto hasta igualar o superar en el nivel de prioridad al resto de procesos.

Así mismo, cuando no existen procesos en ninguna de las colas (procesador inactivo), espera a que llegue uno nuevo ejecutando `setNextTick()` para incrementar el tick actual, todo esto mientas se le informa a JS la espera de un nuevo estado.


### Planificación por lotería

Se puede mencionar la similitud al menos en la estructura de almacenamiento de procesos e inicialización, por su parte este algorimo a diferencia del anterior, cuenta _No. Tickets_ quienes son modificables para aumentar la probabilidad de ocurrencia de cierto proceso. Es decir, la asignación de la prioridad es predeterminada, aunque desde los inputs se pueden modificar los valores

La llamada al algoritmo verifica el tick actual y los procesos que soliciten ejecutarse en se instante, luego, los tickets disponibles son distribuidos a los procesos que aún no terminan  para escoger un ticket aleatorio dentro de `selectedTicket`.

La ejecución de este algoritmo mantiene penalizaciones aleatorias, tendiendo a ser _justo_ en cuanto a las prioridades; sin embargo, los _quantums_ para cada tick despiertan y duermen a los procesos sucesivamente, teniendo pérdidas meramente burocráticas.

***
## Comparación

#### Multinivel

 - **¿Cómo se compararía este método con los otros abordados?** 
    Consideramos la ventaja de poder manipular múltiples niveles de procesamiento, donde desaparece la ejecución lineal de solo un proceso. Gracias a esto, cada proceso se puede interpretar de acuerdo a su complejidad y mencionando al despachador la importancia de ejecutar un proceso antes que otro.

 - **¿Para qué tipo de carga es más apto y menos apto?**
    Ayuda a los procesos cortos, ya que tras la llegada de cada uno, se ejecuta en la cola de mayor prioridad. Por otra parte, los procesos largos son los más castigados ya que cada tiempo que se ejecuta disminuye el nivel de prioridad.

    No obstante, modificando el valor de los parámetros del quamtum, tiende a equilibrar las cargas de ejecución.

 - **¿Qué tan susceptible resulta a producir inanición?**
    Muy susceptible, debido a que los procesos recien llegados se ejecutan al instante al menos una vez. Para evitar lo anterior, se requiere un mecanismo que monitoree el avance de cada proceso y tras cierto tiempo en espera de X, lo degrade a una cola de mayor privilegio.

 - **¿Qué tan justa sería su ejecución?**
    Resulta justa al asignar prioridades a cada proceso mientras se va ejecutando, solo es necesario considerar el tiempo de espera que pueden tomar los procesos largos si es que muchos procesos llegan.

 - **¿Qué modificaciones requeriría para planificar procesos con necesidades de tiempo real? (aunque sea tiempo real suave)**
    Entra en juego el tiempo de ejecución de cada proceso, donde se tenga en cuenta a los procesos que llevan mucho tiempo en espera, tales como subirlos en su cola de prioridad o retardar el tiempo de llegada frente a los recien llegados. 

 #### Lotería

 - **¿Cómo se compararía este método con los otros abordados?** 
    Respecto a la Ronda por ejemplo, no sufre de inanición al tener una oportunidad de ser ejecutados todos los procesos. Tampoco establece interbloqueo como lo realiza el algoritmo del banquero como también no cuenta con prioridad a los procesos recien llegados.

 - **¿Para qué tipo de carga es más apto y menos apto?**
    Resulta mejor para aquellos donde los tickets repartidos son mayores al resto, aunque hablando de procesos en general, favorece tanto a procesos largos como cortos.

 - **¿Qué tan susceptible resulta a producir inanición?**
    En principio no debería existir inanición al poder ejecutarse todos considerando el azar. Cabe destacar que la probabilidad de que nunca se ejecute un proceso no es 0, por lo que dependerá de las condiciones con las que opere el despachador para no caer en inanición.

 - **¿Qué tan justa sería su ejecución?**
    Al jugar con la aleatoriedad, las probabilidades dependen en gran medida del _No. Tickets_, por tanto, es más justo en sentido estricto de la palabra. 

    Sin embargo, lo anterior es también contraproducente, si los tickets asignados no se designan al azar, volvemos a un casos donde la prioridad se establece para los procesos que queremos ejecutar primero.

 - **¿Qué modificaciones requeriría para planificar procesos con necesidades de tiempo real? (aunque sea tiempo real suave)**
    Se debería cambiar por completo la lógica para que sea utilizado por ejemplo en sistemas interactivos.   
    La razón de esto deriva a necesitar considerar tiempos de ejecución y prioridades en cada proceso de llegada.  

    Una posible solución sería repartir una mayor cantidad de tickets a los procesos que necesiten ser más atendidos; también una sección de monitoreo para vigilar a aquellos que después de cierto tiempo siguen esperando poder ejecutarse. 

    Esto en términos computacionales resulta más caro de la implementación simple del algoritmo. 

***

 - **¿Alguna otra reflexión o inquietud que les provoque?**
    Los S.O. actuales establecen un monitoreo de los procesos, ¿Cómo lidian con el cálculo excesivo de cada proceso que lleva en espera?