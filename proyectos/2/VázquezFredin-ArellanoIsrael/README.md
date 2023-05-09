<h1 align='center'> Planificación por Retroalimentación Multinivel y por Lotería </h1>
<br>
<h2 align='center'> Planificación por Retroalimentación Multinivel</h2>

<div align='justify'>
<p>
<h3><u>Overview:</u></h3><br>
Este planificador únicamente se maneja para tener multitarea preventiva, no cooperativa.
<br><br>
La colocación del proceso en su respectiva cola será por medio del quantum, debido a que cada proceso se le estará  diciendo cuánto tiempo se va a ejecutar. Se van a crear varias colas de procesos, cada una tendrá diferente prioridad. 
El despachador estará tomando el proceso de la cola de mayor prioridad, manejando la estructura de selección FIFO. El proceso tomado pasa de ejecutado a listo ‘n’ veces, este es el parámetro. Una vez pasando estas 'n' ejecuciones el  proceso se degrada a la cola de prioridad inmediata inferior.<br><br>
Se define entonces:
<ul>
<li>n: Es la cantidad de ticks que se necesita para ser degradado a la cola de menor prioridad inmediata.</li>
<li>Q: Duración del quantum de las siguientes colas.</li>
</ul>
Por ende, se puede pensar, que mientras un quantum mayor a 'n', no se tendrá problemas debido a que la cantidad de ticks necesario para degradar a un proceso no va a ser restringido con respecto a la cantida de ticks restringido. O sea, que nosotros mientras n < q se tendrá que nuestro proceso va estarse ejecutando y no se va parar por q, sino que va a parar cuando la cantidad de ticks del proceso sea igual a n.<br><br>
En cambio, si nosotros ponemos q < n tendremos la situación que para que se haga un cambio de prioridad de cada proceso, o sea mover en otra cola, se tendrá que esperar a se complete esos n ticks, por ende aun cuando ya  no se haya llegado al tope de ticks de ese quantum se tendría que volver a escoger ese mismo proceso debido a que en realidad no se ha llegado a ese 'n' ticks necesario para bajar su prioridad.
<br><br>
En este enfoque se tendrá que n < q.
<br><br>
Lo que se estará entiendo es que en sí se iniciará siempre un primer proceso en 0, tal que este proceso estará comenzando con una prioridad de 0. Es de este manera que se tendrá.
<br><br>
<h3><u>Implementación</u></h3><br>
El tema de esto es que se tiene que estar revisando cuando van llegando cada proceso, por ende estar revisando esto conlleva a su vez que al momento de que llegue se debe de poner en ejecución.
<br><br>
Lo que se debe de entender es que al inicio todos estarán en la cola de mayor prioridad, por ende la forma de diferenciarlos será por medio del tick de llegada, de tal modo que al llegar se tendrá que poner en ejecución debido a que se tiene una prioridad de la más alta, o sea 0 para nuestra implementación. El tema es que es necesario cuidar que mantener en mente que para que se pueda realizar este cambio de proceso es necesario que el proceso que estaba ejecutándose ya haya ejecutado sus ‘n’ ticks, debido al concepto de ‘n’ que será la cantidad de ticks que se deben de ejecutar para poder degradar el proceso. 
<br><br>
Pero aquí es donde surgen diferentes problemas acerca de la implementación, esto se debe a que no se sabe cómo reaccionar al momento de tener dos procesos con la misma prioridad. Esto se debe a que podemos estar ejecutando el proceso A, y supongamos que todavía a esas ‘n’ ejecuciones por lo cual todavía no se puede degradar, por ende qué ocurre si llega un proceso con la misma prioridad, ¿cuál debería de ejecutarse?, ¿se debe de mantener el proceso A?, ¿se debe de cambiar al proceso B? 
<br><br>
Como esto no fue aclarado por todo entonces se estará entendiendo que finalmente se tiene que cambiar al proceso B, debido a que este debe ser atendido para poder, al menos por un tick, para después degradarlo.
<br><br>
Para entender el cómo realizar en sí la implementación se debe de contemplar que en realidad lo que se tiene es que todo se puede manejar como un simple manejo de prioridad. Esto es debido a que al momento de siempre contemplar un cambio de procesos se debe de contemplar que esto es producido porque llega un proceso con menor prioridad o que al terminar sus ‘n’ ejecuciones este se degrada para después ejecutar otro proceso de mayor prioridad.
<br><br>
Es por esto mismo que se tendrá solamente dos condiciones para producir un cambio de proceso:
<br><br>
<ol>
<li>Cuando llegue un nuevo proceso, la prioridad del proceso actual será menor a la prioridad del proceso que llegó.</li>
<li>Cuando se haya alcanzado las ‘n’ ejecuciones se degrada el proceso y es cuando queda propenso a ser reemplazado por un proceso de menor prioridad.</li>
</ol>
<br>
No obstante, este cambio puede unificarse debido a que están directamente relacionados con la prioridad del proceso actual y el proceso que llega. Es por esto mismo que al momento de realizar una ejecución lo que se deberá de revisar serán dos cosas. 
<br><br>
<img src="Images/1.jpg">
<br><br>
<ol>
<li>Si llegó un nuevo proceso en ese tick, por ende se deberá de atender a ese.</li>
<li>En caso de tener ‘n’ ejecuciones entonces se deberá se degrada y se busca a otro con mayor prioridad.</li>
</ol>

Por ende, para hacer un poco más fácil el entendimiento de esto se decidió tener como n=1 y el quantum igual, será de esta manera que por cada tick habrá un decremento de la prioridad del proceso. De tal manera que se estará teniendo algo similar a lo presentado en el libro y clase donde se veía el ejemplo con n = 1. Y este así que voy a poder asegurar que el tiempo de llegada no va sufrir cambios, se mantendrá igual.
<br><br>
Finalmente, queda hablar acerca de la forma en que fue asignado el tiempo para la llegada y la duración del proceso. Para esto se contempló lo siguiente: 
<img src="Images/2.jpg">
<p>
<div>