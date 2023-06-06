			----Universidad Nacional Autónoma de México---
					Facultad de Ingeniería
	
						Proyecto 2

		Nombres:	Meneses Navarro Erick Sebastian 
				Mex Lozano Aerin Musette

Para ejecutar los programas, escriba en su shell el nombre del programa seguido de .py 

loteria.py
RetroMulti.py

Para este trabajo, se tomo que
1 tick = 10 ms
1 quantuum = 2 ticks
--Planificación por lotería
La forma en la cual decidimos implementar nuestra simulación fue mediante el uso de arreglos y por supuesto jugar con la suerte,
eso a grandes a rasgos, más en específico podemos observar los siguientes puntos:
Como se nos fue pedido, hacemos una carga aleatoria de trabajo de entre 5 y 8 procesos, estos procesos en nuestro código son 
objetos de la clase denominada "process", los cuales tienen diferentes atributos que la definen y facilita mucho la 
manipulación de los datos que queremos simular.
	   
     self.prioridad = random.randint(0,5) --> Asiganaremos prioridades aleaotrias, cada una diferente en cada ejecución
     self.numboletos = int(50/(self.prioridad+1)) --> De acuerdo con lo dado por el profesor "un proceso al que se le quiere dar mayor 											  		       prioridad simplemente tendrá más boletos"
     self.tiempo = random.randint(100,200)/1000 --> Cada proceso tendrá un tiempo aleatorio de entre 0.01 y 0.02 ms
     self.utilizados = 0 --> Para represenar los quantums cuando un proceso ha sido escogido al azar
     self.ejecucion = 0 --> Tiempo total del proceso desde su inicio hasta el final
     self.primeraPasada = 0 --> Para saber cuando un proceso está activo

Para poder implementar la idea de la planificación por lotería, lo que hicimos fue primeramente meter estos procesos en un arreglo 
llamado "procesos_creados", seguido metemos estos mismos procesos en otro arreglo llamado "loteria" con la diferencia de que, 
en este arreglo, los procesos son agregados tantas veces como boletos posee, es decir si el proceso A tiene 30 boletos, 
entonces en el arreglo habrán 30 copias de ese proceso.

Tenemos un ciclo while que se ejecutará mientras el tamaño del arreglo "loteria" sea mayor a cero, con un for para recorrer dicho
arreglo escogeremos un número random comprendido entre el cero y el tamaño del arreglo menos uno, una vez escogido al ganador, 
haremos una "copia" del objeto proceso en un lugar llamado "ganador" con la cual vamos a trabajar, aumentamos +1 la variable 
"utilizados" y para ejecución tomamos en cuenta que una vez el proceso es el ganador se le asigna 20 ms de ejecución y 
así cada vez que resulte ganador.

for i in range(0,len(loteria)):
            n = random.randint(0,len(loteria)-1)
            ganador = loteria[n]
            if(ganador.primeraPasada==0):
                print("El proceso ",ganador.nombre," esta activo\n")
                ganador.primeraPasada+=1
            ganador.utilizados += 1
            ganador.ejecucion += 0.02

Para saber que un proceso ha terminado de hacer su tarea usamos un if para preguntar si su tiempo de ejecución asignado en la 
loteria es mayor o igual a su tiempo asignado al principio, si es asi entonces, primeramente el proceso ha terminado su tarea y 
segundo quitaremos dicho proceso del arreglo lotería.

if(ganador.ejecucion >= ganador.tiempo):
                for j in range(ganador.numboletos):
                    loteria.remove(ganador)
                print("El proceso ",ganador.nombre," ha terminado\n")

Tenemos al final este if, el cual nos ayudara a romper con el ciclo while una vez hayan sido eliminados los elementos del arreglo 
loteria,lo que significa, que todos los procesos ya han acabado su ejecución.

if(len(loteria)==0):
                break

Explicamos como es que un proceso terminó su ejecuión, pero, ¿Cómo es que sabemos que un proceso está activo?, simple, tenemos un
atributo llamada "primeraPasada", y durante el proceso de esocger un ganador, preguntamos con un if si esta variable es igual a 
cero, si es así entonces está activo y le aumentamos +1 a esta variable, si es mayor a cero entonces ya estuvo activo.

Por último para presentar los datos, tenemos el orden de ejecución la cual le estuvimos concatenando a la variable "orden" el 
nombre de los procesos, y así al final podemos presentar su orden de ejecución, despues hicimos una suma del tiempo asignado y 
el tiempo que utilizó el proceso durante la lotería, para asi poder visualizar el tiempo total la cual debe de ser entre 80 y 
120 ticks, y podemos ver que si se cumple, pues nosotros usamos que 1 tick será igual a 1 ms.
Lo único que puede llegar a suceder es que se pase pr poquito este total de tiempo utilizado, osea que veamos un tiempo total de 
1.29, pero eso fue algo que solo nos ocurrió una vez, ahora si que es puro azar que suceda de nuevo.


-- Planificación Retroalimentación por Multinivel
Se tomo que cada n quantums se baje su prioridad.
Utilizando lo ya antes implementado en el de lotería, usamos la misma idea de usar los procesos como objetos las cuales tienen sus 
atributos, solo que ahora agregamos unas nuevas características.

	self.llegada = random.randint(1,10) --> tiempo de llegada del proceso
	self.final=0 --> tiempo en acabar el proceso
        self.inicio = 0 --> tiempo real en el que llega el proceso al sistema

Metemos en las colas de prioridad los procesos creados, todos iniciando desde la cola cero, esto porque en un principio lo ibamos a 
hacer de acuerdo a su prioridad pero tuvimos problemas con los tiempos de llegada.

Una vez realizado haremos un while por cada cola, los cuales son para "esperar" a que los procesos lleguen, entonces usamos un if para 
identicar si el tick coincide con el tiempo de llegada del proceso, si es así entonces en "utilizados" sumamos +1 pues quiere decir que 
ha usado un quantum así como tambien incrementar +1 el tiempo en acabar el proceso y como nos dice esta planificación le decrementamos a 
la prioridad del proceso al aumentar su valor, ya que va desde, 0 como más importante, hasta 4, el menos importante,lo removemos de la cola
y lo pasmos a la siguiente cola de prioridad; cabe destacar que , si se llega a la 
cola de prioridad 4 al ser la ultima, solo se va removiendo de esa cola en el momento que ya acabo el proceso

Así como en el de lotería para identificar si el proceso ha terminado o no usamos un if para preguntar si su tiempo de ejecución asignado 
es mayor o igual a su tiempo asignado al principio, si es asi entonces, primeramente el proceso ha terminado su tarea y segundo quitaremos 
dicho proceso de la cola.

if(i.utilizados >= i.tiempo):
                    cola_0.remove(i)
                    print("El proceso ",i.nombre," a terminado\n")

Tuvimos un problema al hacer que los tiempos de llegada coincidan con los quantums, es por eso que se verá medio extraño en la 
ejecución, no supimos como arregarlo.

Para la impresion de los datos, así como en loteria hicimos una concatenación en "orden" para mostar los procesos que se ejecutaron
y para la tabla, usamos la misma metodica que en el de lotería solo que ahora con nuevos datos, para obtener T es final-inicio 
ya que es el tiempo total del sistema en que tardo en acabar el proceso, para E es T-tiempo ya que es el tiempo en el que realmente
acabó el proceso