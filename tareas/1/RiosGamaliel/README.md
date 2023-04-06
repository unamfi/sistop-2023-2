# **Tarea 1:** Ejercicio de sincronización

<pre>
<b>Materia:</b> Sistemas Operativos
<b>Grupo:</b> 6
<b>Alumno:</b> Ríos Lira, Gamaliel
<b>Problema:</b> Intersección de caminos
<b>Fecha:</b> 06/04/2023
</pre>

***

## Lenguaje de programación utilizado

El lenguaje de programación utilizado fue `Java 17`, aunque todas las clases 
utilizadas están disponibles desde versiones anteriores. Se desarrolló 
haciendo uso del `OpenJDK 17`.

Se encontraron dos soluciones al problema, las cuales se encuentra en los 
directorios `1/` y `2/` respectivamente. Para poder compilarlo, se tiene que 
ejecutar el siguiente comando:
```bash
$ javac -d out/ --source-path <version>/ <version>/InterseccionCaminos.java
```
Posteriormente, para ejecutarlo se tiene que utilizar el siguiente comando:
```bash
$ java --class-path out InterseccionCaminos
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
- Hasta este punto, todo funcionó de forma adecuada. Los hilos _consumidores_ 
  detectaban la señalización del hilo _productor_ y desencolaban los autos.  
  Al comenzar a programar el mecanismo para pasar por las secciones de 
  intersección, me dí cuenta de que cada una de ellas era en realidad un 
  _mutex_, por lo que se implementó una de **cuatro _mutexes_**. Implementados 
  a través de la clase `Semaphore`. La parte más complicada del problema es 
  justamente lo siguiente. Una intersección sólo puede estar ocupada por un 
  solo carril (si no sucede de esta forma, existirían choques). Además, si un 
  auto está en una sección, no puede abandonarla hasta que la sección 
  siguiente esté libre (si sucede esto, alguien más puede llegar a la sección 
  recién liberada mientras la siguiente sección aún no ha sido liberada y el 
  auto estaría en una incertidubmbre cuántica por algunos instantes). Lo 
  primero fue identificar los movimientos posibles para cada carril:
  - **Continuar:** Se entra por una sección, se toma la que está 
    inmediatamente enfrente y se continúa por la calle.
  - **Giro derecha:** Se entra por una sección, se gira a la derecha y se 
    continúa por la calle.
  - **Giro izquierda:** Se entra por una sección, se avanza a la siguiente, se 
    gira a la izquierda, se toma la sección siguiente y se continúa por la 
    calle.

  Este moviemiento es el mismo para todas las secciones, lo único que cambia 
  es la orientación inicial que tiene cada carril. Al ejecutarlo sin ningún 
  mecanismo de sincrinización adicional se obtuvo el sigueinte estado de 
  inanición:
    | <!-- -->| <!-- -->|
    | --- | --- |
    |  ↓  |  ←  |
    |  →  |  ↑  |

  Tal como se puede ver, es imposible avanzar más ya que de forma transitiva 
  para que un carril avance, se necesita que otro carril avance, pero este 
  necesita que otro carril avance, pero este necesita que otro carril avance y 
  así hata llegar a que se necesita que el mismo hilo inicial avance (lo cual 
  es imposible).

  Justamente en este punto es en donde se encontraron las dos aproximaciones:
  1. Una forma de evitar el bloqueo de los cuatro hilos es colocar un 
     `multiplex` alrededor del procesamiento de cada auto. Para hacer más 
     eficiente la utilización de los recursos, basta con dejar fuera a un solo 
     hilo. Es decir, en este caso, sólo se permiten que hasta **tres 
     carriles** procesen sus autos al mismo tiempo. La forma de implementar el 
     _multiplex_ fue, nuevamente, a través de la clase `Semaphore`.
  2. La otra aproximación se basa en el funcionamiento de los cruces en la 
     realidad. En donde sólo los carriles que van en direcciones opuestas 
     pueden avanzar al mismo tiempo (luz verde), mientras que los otros dos 
     carriles deben esperar (luz roja). Esta situación no es más que una 
     _exclusión categórica_. La implementación de esta versión del programa se 
     realizó a través de un _lightswitch_ (o _apagador_ en español), en donde 
     se tienen dos categorías:
     - `VERTICAL`: Hace referencia a los carriles que se mueven a la izqueirda 
       y a la derecha.
     - `HORIZONTAL`: Hace referencia a los carriles que se mueven hacia abajo 
       y hacia arriba.

      La implementación de esta versión se complica un poco ya que se necesita 
      agregar más variables y poner más condiciones. Y al final, la eficiencia 
      disminuye con respecto a la versión anterior. En el caso anterior se 
      pueden tener hasta **tres hilos** ejecutándose al mismo tiempo, mientras 
      que en este caso sólo se pueden tener hasta **dos hilos** en ejecución 
      al mismo tiempo.

***
## Refinamientos
Inicialmente, se planteó una solución que ya consideraba el **Refinamiento 1** 
por si misma. Sin embargo, sólo se consideraban movimientos de frente; es 
decir, no se consideraban vuletas. Por ello, se creó una nueva versión donde 
se aplicaba el **Refinamiento 2** y es ahí donde surgió la enumeración 
`TipoAuto`, la cual indica qué tipo de movimiento hace cada auto.

***
## Comentarios adicionales
Considero que la solución cumple con el enunciado descrito; sin embargo, tiene 
algunas áreas de mejora. Por ejemplo, por la forma en que se planteó, un mismo 
carril podría ser capaz de manejar hasta tres secciones al mismo tiempo;
mejorando el uso de las secciones del cruce y del tiempo. A pesar de esto, 
sólo dejé un auto por carril ya que supuse que iban a salir más posibilidades 
de _inanición_.
