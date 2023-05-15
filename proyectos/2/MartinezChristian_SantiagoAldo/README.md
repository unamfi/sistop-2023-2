# **Proyecto 02**

**Integrantes:**
- Santiago Alejandro Aldo
- Martinez Licea Christian Jair

---

***Lo más destacable:***

*En la línea siguiente:*

```python
duracion_maxima = randint(7,10) # Duración máxima aleatoria
```

*El crea un número aleatorio que se encuentra entre el rango de duración de los procesos. Este número lo usaremos como base para determinar la duración máxima de cada proceso. Es decir, si un proceso alcanza la duración máxima, se pone en espera de su nuevo turno para poder concluir.*

---

## **Preguntas**

- **¿Para qué tipo de carga es más apto y menos apto?**

    - *Es apto para simular una carga de trabajo que consta de varios procesos que llegan en diferentes momentos y tienen diferentes duraciones. Este algoritmo selecciona el proceso con la hora de llegada más temprana y lo ejecuta hasta que se completa o se bloquea, y luego selecciona el siguiente proceso en orden de llegada.*

    - *No es apto para los casos en los que se presenten procesos más complejos, ya que, el programa no cuenta con que puede no haber procesos ejecutandose en ciertos periodos.*

- **¿Qué tan susceptible resulta a producir inanición?**

    *Es probable que sufra de inanición cuando un proceso sea demasiado largo y no le otogue el control a otro proceso. Para solucionarlo se planteó un tipo de limitante de 'tiempo máximo' que se encargaría de pasarle el turno a otro proceso mientras el proceso que no ha finalizado vuelve a esperar su turno.*

- **¿Qué tan justa es la ejecución?**
    
    *En la solución planteada, aunque se usa un 'tiempo_maximo' para evitar la inanición entre procesos cada proceso, cada uno de estos es ejectuado de acuerdo a su prioridad de llegada, es decir, de acuerdo a como ingresaron a la cola.*

- **¿Qué modificaciones requeriría para planificar procesos con necesidades de tiempo real? (aunque sea tiempo real suave)**

    *Podría requerir el programa para planificar procesos con necesidades de tiempo real es la implementación de mecanismos de sincronización y de comunicación entre procesos. De esta manera, se permite compartir información entre procesos para la realización de tareas complejas.*