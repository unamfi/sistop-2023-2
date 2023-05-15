## Aranzúa Chávez César Octavio

#### ¿Cómo se compararía este método con los otros abordados?
Es una planifiacfión más jsuta, basada en el probabildiad y que no beneficia a un proceso en particuolar

#### ¿Para qué tipo de carga es más apto y menos apto?
Es óptimo para procesos de baja prioridad que se ejecutan con frecuencia. Al ser de base probabilistica, los procesos de baja prioridad todavía tienen oportunidad de ejecutarse, sin embargo, no es el mejor para cargas de trabajo con un número limitado de procesos de alta prioridad que deber ejecutarse de manera urgente.

#### ¿Qué tan susceptible resulta a producir una inanición?
Es menos susceptibles que otros, pues cada proceso tiene una probabilidad igual de ser seleccionado para su ejecución, independimente de su prioridad. Además, hay manera de evitar la inanición en esta planificación, como asignar un número mínbimo de loterías a cada proceso o asignar prioridades en función del tiempo de espera del proceso

####  ¿Qué tan justa sería su ejecución?
La lotería (normal) se cosndiera justa en función de la proprocionalidad de la lotería y la cantidad de procesos, de manera que cada uno tiene la misma probabilidad de ejecutarse, sin embargo, cuando se consdiera la prioridad de los procesos, podría no resaltar la planificación por lotería, pues depende de la distribución de las prioridades de los procesos.
Por otro lado, hay una versión llamda lotería esxclusiva, la cual resulta más justa que la _normal_, en donde cada proceso tiene una cantidad determianda de loterías y de esa  manera se vuelve equitativa  de la oportunidad que tiene de ser seleccionado.

#### ¿Qué modificaciones requeriría para planificar procesos con necesidades de tiempo real?
* Asignar prioridades basadad en tiempo. En lugar de asignar prioridades conforme a la importancia del proceso, se pueden asignar prioridades basadas en un tiempo límite que cada proceso debe cumplir
* Establecer un tiempo máximo de tiempo de espera en la cola