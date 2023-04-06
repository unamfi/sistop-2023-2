# **Tarea 1:** Ejercicio de sincronización

<pre>
<b>Materia:</b> Sistemas Operativos
<b>Grupo:</b> 6
<b>Alumno:</b> Ríos Lira, Gamaliel
<b>Problema:</b> Intersección de caminos
</pre>

***

## Lenguaje de programación utilizado

El lenguaje de porgramación utilizado fue `Java 17`, aunque todas las clases 
utilizadas están disponibles desde versiones anteriores. Se desarrolló 
haciendo uso del `OpenJDK 17`.

Se encontraron dos soluciones al problema, las cuales se encuentra en los 
directorios `1/` y `2/` respectivamente. Para poder ejecutarse, se tiene que 
ejecutar el siguiente comando:
```bash
$ javac -d out/ -source-path <version>/ <version>/InterseccionCaminos.java
```

---

## Estrategia de sincronización
Durante la solución del problema, se encontraron varias cuestiones importantes 
de atender.
1. La generación de autos
2. El procesamiento de cada auto en un carril específico
3. Si se procesan los cuatro carriles exactamente al mismo tiempo, se llega a 
   una situación de inanición.

De forma general, estas situaciones se atendieron de la siguiente forma:
- La generación de autos se hizo a través del patrón `productor/consumidor`.  
  El _hilo productor_ cada cierto tiempo genera dos númoros aleatorios. El 
  primero indica a qué carril llegará el nuevo auto, mientras que el segundo 
  indica qué tipo de auto será; se tienen tres tipos de auto:
  - `CONTINUAR`: Es un auto que continúa derecho sobre el mismo carril.
  - `GIRO_DER`: Es un auto que hace un giro a la derecha.
  - `GIRO_IZQ`: Es un auto que hace un giro a la izquierda.

  Por otra parte, el papel de _hilos consumidores_ es tomado por por cuatro 
  hilos; cada uno representa un solo carril.
  - `IZQ`: El carril que se mueve a la izquierda.
  - `DER`: El carril que se mueve a la derecha.
  - `ABJ`: El carril que se mueve hacia abajo.
  - `ARR`: El carril que se mueve hacia arriba.
  
  La disposición utilizada fue la siguiente:
    | <!-- -->| <!-- -->| <!-- -->| <!-- -->|
    | --- | --- | --- | --- |
    |     |  ↓  |     |     |
    |     |  +  |  +  |  ←  |
    |  →  |  +  |  +  |     |
    |     |     |  ↑  |     |

  Los autos que se van generando se almacenan en una lista con un índice 
  asociado al carril. Tal como se vio en clase, para lograr una operación 
  correcta entre todos los hilos, fue importante agregar una región crítica al 
  rededor de las operaciones `add()` y `remove()` de la lista con los autos.  
  Para esto, se utilizó un patrón similar a los _mutexes_; sin embargo `Java` 
  implementa por sí mismo las directivas para crear regiones críticas a través 
  de hilos haciendo uso de los bloques `sinchorized`. Se usa la siguiente 
  estructura:
  ```java
  synchronized(recurso) {
    // Código de la región crítica
  }
  ```

  Todos los hilos para los que la referencia al objeto `recurso` sea la misma 
  entrarán uno a uno a la región crítica. Esta herramienta proporcionada por 
  Java únicamente funciona para el caso de las regiones críticas y simplifica 
  el uso de tantos _mutexes_.
- Para lograr que el hilo _consumidor_ consumiera los autos generados por el 
  hilo _productor_ se utilizó una señalización entre hilos a través de una 
  lista de objetos de tipo `Semaphore`. Cada objeto `Semaphore` sólo se libera 
  después de producir un auto, y sólo se adquiere antes de consumirlo. Para 
  esto, se utilizan los  métodos de instancia `release()` y `acquire()`.

Tal como ya se describió anteriormente, el
