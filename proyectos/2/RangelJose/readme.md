# Planificación por Lotería
Para iniciar con este método de planificación por lotería, primero enemos que seleccionar los procesos el número de procesos que se van a ejecutar; para ello obtiene un número aleatorio entre 5 y 8.

        for i in range(random.randint(5,8)):
            procesosCreados.append(Proceso(letras[i]))

La clase Proceso será encargada de almacenar todos los datos necesarios para identiicar al proceso. Para ello, se tienen los siguientes atributos:
* Nombre: Para diferencias los procesos.
* Prioridad: Nivel de prioridad que tiene el proceso.
* Tiempo: Número de segundos que tarda el proceso en ejecutarse.
* NumTickets: Número de tickets que son asosiados a dicho proceso.
* Utilizados: Número de tickets utilizados al finalizar su proceso.
* Ejecucion: Tiempo en segundos que tardó su ejecución.

        class Proceso:
            def __init__(self,nombre):
                self.nombre = nombre
                self.prioridad = random.randint(0,4)
                self.tiempo = random.randint(50,200)/1000
                self.numTickets = int(35/(self.prioridad+1))
                self.utilizados = 0
                self.ejecucion = 0

Según la explicación de los libros, entre mayor prioridad tenga el proceso mayor será el número de tickets que se le asignarán; y por cada ticket que es ganado en la lotería, se le asigna un total de 20 milisegundos de tiempo de ejecucón, después se hará una nueva lotería para darle 20 milisegundos a otro o al mismo proceso. Esta característica está definida de la siguiente forma:

        time.sleep(0.001)
        boleto = Loteria.sacaTicket()
        boleto.utilizados += 1
        boleto.ejecucion += 0.02  

boleto.utilizado es un contador para el número de loterías que ha ganado. Mientras que boleo.ejecucion serán los 20 milisegundos de tiempo de ejecución. Aunque con time.sleep se le asigna 0.001, se hace la referencia de que son 20 ms.

El método para matar un proceso o saber si ya se terminó es que el siguiente:

        if(boleto.ejecucion >= boleto.tiempo):

Si el tiempo de ejecución es mayor al que teoricamente tarda en terminar, entonces se considera como una tarea ejecutada correctamente. 

Para poner un proceso activo, se acordó que no se agregarán de manera secuencial, sino que gracias al time.sleep puede ser activdo el proceso H como que el último en entrar activo el A. Después de ello, se agregarán los numeros de tickets correpondientes a ese proceso a una lista donde se sacará de maera aleatoria un proceso. 

        time.sleep(random.randint(0,20)/100)
        for num in range(proceso.numTickets):
            Loteria.agregaTicket(proceso)
        print(f"->Proceso {proceso.nombre} ahora está activo")


Inicialmente se hará una presentación de todos los procesos que será utilizados para la simultación, y otro tipos de datos. Quedando de la siguiente manera.

        Carga de trabajo a simular por loterφa:
        Proceso    Prioridad    NumTickets    Tiempo[S]
            A         2            11             0.396
            B         4            7             0.202
            C         2            11             0.2
            D         3            8             0.241
            E         3            8             0.283
            F         2            11             0.26
            G         1            17             0.355
            H         3            8             0.359
                 Totales:          81

Dentro de las diferentes pruebas que se hicieron del programa, s enotaron ciertos comportamientos que se explicarán a continuación.

## 1. Solamente se tiene un proceso activo.
En este caso, los únicos tickets que se sacarán serán del mismo proceso y se ejecutará hasta termiar. Después de su ejecución se esperará a que otro proceso sea agregado.

        ->En espera de un proceso
        ->Proceso F ahora estß activo
            ->Proceso F 
                ->Ticket 1
            ->Proceso F 
                ->Ticket 2
        ...
            ->Proceso F 
                ->Ticket 14
                    ->Proceso F termina

        ->En espera de un proceso
        ->Proceso D ahora estß activo
        ->Proceso G ahora estß activo
            ->Proceso G 
                ->Ticket 1

## 2. Existen 2 o más procesos activos.
Para este caso se realizará de manera aleatoria hasta que uno de ellos termine su ejecución y después segirá con el faltante.

        ->Proceso D ahora estß activo
        ->Proceso G ahora estß activo
            ->Proceso G 
                ->Ticket 1
            ->Proceso G 
                ->Ticket 2
            ->Proceso G 
                ->Ticket 3
            ->Proceso G 
                ->Ticket 4
            ->Proceso D 
                ->Ticket 1
                ...
            ->Proceso G 
                ->Ticket 18
                    ->Proceso G termina
            ->Proceso D 
                ->Ticket 8
            ->Proceso D 
            ...
            ->Proceso D 
                ->Ticket 13
                    ->Proceso D termina
## 3. Se agregan nuevos procesos mientras está en ejecución uno.
Existen casos en donde un proceso no se ha termiado, pero otro proceso entra en activo. En este caso el nuevo proceso también entrará a la lotería con su número de tickets según su prioridad.

            ->Proceso B 
                ->Ticket 8
            ->Proceso A 
                ->Ticket 10
        ->Proceso E ahora estß activo
            ->Proceso A 
                ->Ticket 11
        ->Proceso H ahora estß activo
            ->Proceso H 
                ->Ticket 1
            ->Proceso H 
                ->Ticket 2
            ->Proceso B 

Al final, al ser un método puramente aleatorio, no se sabe si el proceso con mayor prioridad será el primero o el último en terminar. En el programa se mostrará las siguientes cadenas para saber el orden en el que se eecutaron y el orden en que terminaron los procesos.

        ============================
        Orden de ejecuci≤n de todos los tickets
        FFFFFFFFFFFFFFGGGGDGDGDGGGGGDGDDGGGDGGGDDDDDDABCAACCCCCCAABCBCABACCAABBBBAAHHBBHBEHEAAAEHEHHEEEAAEAHAHHEAAHHEEEEEEHHHHHH
        ============================
        Listado de como temrinaron los procesos
        FGDCBAEH

Adicionalmente, se muestra una tabla como la primera para hacer una relación del número de veces que gano la lotería y el tiempo del procesador necesario para terminar su ejecución.

        Proceso    Prioridad    NumTickets    TicketsUtilizados    Tiempo[S]    TiempoUtilizado[S]
            A         2            11                  20              0.396             0.4
            B         4            7                  11              0.202             0.22
            C         2            11                  11              0.2             0.22
            D         3            8                  13              0.241             0.26
            E         3            8                  15              0.283             0.3
            F         2            11                  14              0.26             0.28
            G         1            17                  18              0.355             0.36
            H         3            8                  18              0.359             0.36
                Totales:          162

## COMENTARIOS
En la entrega se anexan cuatro archivos .txt, el llamado loteriaDoc.txt la salida de la simulación y de ella se extajeron los datos mostrados en la presente documentación. Los llamados literia1, loteria2 y loteria3.txt son otros ejemplos donde se modificó solamente la presentación final, pero el planteamiento de resolución es el mismo.
# Planificación por Retroalimentación Multinivel
Para ejecutar una planeación por retroalimentación, fue necesario se planteó la misma forma de solución, crear una clase llamada Proceso en donde se almacenarán todas los datos relevantes de la misma, como nombre, tiempo, etc. Adicionalmene se agrega la variable llegada, la cual corresponderá el segundo donde inicia dicho proceso, fin será la variable que indicará el segundo donde termina su ejecución, mientras que espera serán los segundos después de que está activo y antes de que termine su proceso y que no fue ejecutado.

        class Proceso:
            def __init__(self,nombre):
                self.nombre = nombre
                self.prioridad = random.randint(0,4)
                self.tiempo = random.randint(3,10)
                self.llegada = random.randint(0,15)
                self.numTickets = int(35/(self.prioridad+1))
                self.utilizados = 0
                self.ejecucion = 0
                self.fin = 0
                self.espera =  0

La definición de la lotaría queda exactamente igual. Hay un cambio en cuanto al agregar un proceso activo, ya que su tiempo de espera no será aleatoria, sino que esperará según su llegada. Para la ejecución de procesos, ahorá se mostrará el contador de tiempo para entender el orde. Para ello, la tabla inicial que mostrará será la siguiente:

        Proceso    Prioridad    NumTickets    Tiempo[S]      Llegada
        A           4             7           3              2
        B           4             7           6              5
        C           4             7           5             12
        D           0            35           8              8
        E           0            35           8             12
        Totales:                 91          30

Si no existen procesos que inicien en t=0, entonces ese tiempo no ejecutará nada.

        ->t = 0
        ->t = 1
        ...
Después, gracias a la tabla sabemos que el proceso A entra en el segundo 2. Afortunadamente, en este proceso no existió un segundo proceso que interrumpe, entonces se ejecutará A hasta que se termine.

        ->t = 2
        ->Proceso A ahora esta activo
            ->Proceso A 
            ->Ticket 1
        ->t = 3
            ->Proceso A 
            ->Ticket 2
        ->t = 4
            ->Proceso A 
            ->Ticket 3
                ->Proceso A termina
Ahora para los siguientes casos, D entra en acción mientras B también está activo, entonces se realizaráel mismo proceso de lotería para seleccionar qué proceso será el siguiente en ejecutarse.

        ->t = 5
        ->Proceso B ahora esta activo
            ->Proceso B 
            ->Ticket 1
        ->t = 6
            ->Proceso B 
            ->Ticket 2
        ->t = 7
            ->Proceso B 
            ->Ticket 3
        ->t = 8
        ->Proceso D ahora esta activo
            ->Proceso D 
            ->Ticket 1
        ->t = 9
            ->Proceso D 
            ->Ticket 2
        ->t = 10
            ->Proceso D 
            ->Ticket 3
        
Al final de igual forma se utilizará el mismo método para saber el orden de ejecucuión y el orden de terminación

        ============================
        Orden de ejecuci≤n de todos los tickets
        AAABBBDDDDBEDECCDEEDDBEEEECBCC
        ============================
        Listado de como temrinaron los procesos
        ADEBC
    
Al final, la tabla que se utiliza es la siguiente:

        Proceso    Inicio    Fin    T[S]     E[S]     P
           A          2        4      2       -1    0.667
           B          5       29     24       18      4.0
           C         12       31     19       14      3.8
           D          8       22     14        6     1.75
           E         12       27     15        7    1.875
