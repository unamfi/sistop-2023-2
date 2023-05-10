# Proyecto 2: Planificación por retroalimentación multinivel y por lotería
	Rivera García Mauricio
	Ruiz Flores Laura Andrea

## Retroalimentación multinivel
La implementación para simular esta planificación hizo el uso de una lista de diccionarios que representarán a los procesos, cada uno con información como la duración, el tiempo de llegada, su identificador y una prioridad, la cual servirá para ver las colas de prioridad que hacen funcionar a este mecanismo. 
La idea de esto es ordenar varias listas y utilizar el atributo de prioridad para saber cuál es el elemento siguiente. Se tuvieron que tomar varias consideraciones en el diseño de esta implementación:

1. Una vez que todas las prioridades de los procesos sean mayores a cero, se irán restando para que la mínima sea cero (sin perder el orden de las prioridades, basicamente solo se les hace un decremento a uno a todas), esto principalmente para no trabajar con valores de Quantum demasiado grandes (los Quantum se manejan con potencias de dos)
2. Los incrementos de nivel de la cola de prioridad se realizan por cada ejecución.
3. En algunos casos se ajusta el nivel del Quantum cuando pasa a ser más grande del tamaño restante de un proceso, esto para fines de visualización del programa.
4. Esta implementación va filtrando a los procesos involucrados por cada tick, después se ordena la prioridad y se ejecuta la menor.
5. Se manejan los posibles espacios vacíos cuando no hay procesos involucrados en el tiempo analizado, esto realizando comparaciones entre todas las duraciones de los procesos. Para fines de visualización y de un mejor manejo, la duración está siendo constantemente manipulada según avanza el proceso, por lo que, si las duraciones ya llegaron a cero quizás pueda significar que el programa ya acabó, pero sino, entonces hay un hueco vacío.

## Lotería

Para la lotería asignamos la prioridad conforme se crearon los procesos, es decir, siendo el primero el proceso 'A' y el último el proceso que correspondiera a la letra del alfabeto de la máxima cantidad de procesos. Se decidió manejar con ayuda de listas, de esta forma toda la información relativa a los procesos se encontraría en un sólo lugar.
Al momento en que hay un boleto ganador de un proceso ya terminado, se emite un mensaje indicando que dicho proceso ya ha terminado y se vuelve a ejecutar hasta que todos los procesos tengan una duración de cero, es decir, hayan terminado.
Asimismo, se verifican varias condiciones para asignar el inicio y fin del proceso, como que haya tenido por primera vez un boleto ganador, para el inicio, y que el boleto ganador final lo lleve a una duración, o tiempo restante, de cero.

## Preguntas de razonamiento
1. ¿Cómo se compararía este método con los otros abordados?

La retroalimentación multinivel en realidad aprovecha un sistema muy simple que aprovecha las colas de prioridad. Principalmente permite abstraer mejor un poco el como se relevan y "coordinan" los procesos aunque terminen de alguna manera perjudicando a los más largos (aunque con la modificación de los quantum se arregla un poco esto)

La lotería es prácticamente todo lo contrario ya que no se basa realmente en ese orden en los procesos, sino en un sistema aleatorio del cual dependerá de probabilidades de "ganar la lotería", por lo que no sigue realmente unas reglas tan sólidas, pero resulta mucho más sencillo de entender e implementar.

2. ¿Para qué tipo de carga es más apto y menos apto?

La retroalimentación multinivel a veces presentaba un poco de problemas para los procesos largos y también los procesos ya tardíos en la carga de trabajo, pues como la mayoría de los procesos están en colas superiores a veces daba avances muy cortos aunque fueran más seguidos.

La lotería podría ser para procesos en los cuales no se necesiten tantas colaboraciones entre sí y cuyas prioridades realmente no importen tanto. A veces también puede ser útil lanzar una moneda al aire. Generalmente puede resultar útil en cargas pequeñas con poca cantidad de procesos, ya que el rango en que estarán los boletos ganadores resulta menor. Sin embargo, tampoco es una garantía, ya que puede haber lapsos de tiempo donde no haya una ejecución.


3. ¿Qué tan susceptible resulta a producir inanición?

En la retroalimentación multinivel es uno de los problemas principales, pues si un proceso queda con una prioridad muy alta y de repente llegan muchos procesos nuevos va a tardar muchisimo en acabar.

Lotería es muy suceptible a inanición si no se implementa que otros procesos que hayan terminado puedan ceder sus boletos a otros procesos, ya que, al "caer" un boleto ganador de un proceso ya terminado, no se realiza ninguna acción, por lo que genera este estado de inanición hasta que se obtenga un boleto ganador de un proceso sin terminar.

4. ¿Qué tan justa sería su ejecución?

La retroalimentación multinivel parece justa si se sabe controlar el tamaño de los quantums, de lo contrario, insisto, provocaría muchos problemas a los procesos largos. Aún así, con todo y modificaciones algunos procesos aún se ven afectados, aunque realmente se traten de casos muy particulares.

La lotería, al jugar con probabilidades, puede parecer muy justa o injusta. Además, las prioridades no inlfuyen realmente en el resultado, sino en el orden en que se van a asignar los valores de los boletos, por lo que depende totalmente del azar. 


5. ¿Qué modificaciones requeriría para planificar procesos con necesidades de tiempo real? (aunque sea tiempo real suave)

En FB como tal es un sistema ya planteado de tal forma que maneja cietos procesos al mismo tiempo y los controla para que pase uno por uno, sin embargo, sería muy necesario herramientas como usar bloqueos mutuos por cada ejecución del primer proceso en la cola.

Para la lotería debería de cambiar muchas cuestiones en su lógica, naturalmente los procesos podrían colaborar para darles más probabilidades a otro para ejecutar ciertos procesos, aunque no siempre llegue a funcionar, de esta forma podemos evtar la inanición y hacer que haya realmente un aprovechamiento del tiempo de ejecución.


6. ¿Alguna otra reflexión o inquietud que les provoque?
En la lotería hay que tener cuidado con la carga y la cantidad de procesos que se vayan a ejecutar. Es interesante ver cómo es que la ejecución es completamente aleatoria, pero el hecho de tener bastante tiempo donde no se realizan ejecuciones es lo que más se quiere evitar en este tipo de métodos.