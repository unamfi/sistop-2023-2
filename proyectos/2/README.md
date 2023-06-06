# Proyecto 2: Planificación por Retroalimentación Multinivel y por Lotería

    Planteamiento: 2023.04.27
	Entrega: 2023.05.09

Vimos el tema de _planificación de procesos_: Cómo el sistema
operativo selecciona de entre los procesos que están en la cola de
_Listos_, y pone a uno de ellos a ejecutar en el procesador.

Hay un esquema adicional a los que presentamos en clase. Su
planteamiento es, pienso yo, muy interesante. Para este proyecto, les
pido que implementen una _simulación_ del planificador por lotería.

# ¡Calificaciones listas!

¡Disculpen la demora! Pero bueno, por lo menos ya puedo compartirles
que /ya quedó/. ¡Ya pueden [consultar sus
calificaciones](./calificaciones.org) para este proyecto.

# ¿Cómo es la planificación por Lotería?

Abordamos en clase la _planificación por Retroalimentación
Multinivel_, por lo que no considero necesario replantearla aquí, pero
sí les presento la _planificación por lotería_. Como sea, están
explicadas respectivamente en las secciones 4.2.6 y 4.2.7 del [libro de
la materia](https://sistop.org/pdf/sistemas_operativos.pdf) (páginas
145 a 149).

La planificación por lotería fue propuesta por Andrew Tannenbaum, y su
implementación (en el sistema operativo Minix) acompaña a su libro,
_[Sistemas Operativos: Diseño e
Implementación](https://drive.google.com/file/d/0BxWDaelvgrvCMWUxZjk1MzctYTQ1Yy00Y2U1LTg2YWQtYjNhNjAyNjg1OWEy/view?resourcekey=0-yRikrU5vy0oSWcZq4O-A1A)_.

Bajo el esquema de la _lotería_, cada proceso tiene un número
determinado de boletos, y cada boleto le representa una oportunidad de
jugar a la lotería. Cada vez que el planificador tiene que elegir el
siguiente proceso a poner en ejecución, elige un número al azar, y
otorga el siguiente quantum al proceso que tenga el boleto ganador. El
boleto ganador _no es retirado_, esto es, la probabilidad de que
determinado proceso sea puesto en ejecución no varía entre
invocaciones sucesivas del planificador.

Las prioridades pueden representarse en este esquema de forma muy
sencilla: un proceso al que se le quiere dar mayor prioridad
simplemente tendrá más boletos; si el proceso _A_ tiene 20 boletos y
el proceso _B_ tiene 60, será tres veces más probable que el siguiente
turno toque a _B_ que a _A_.

El esquema de planificación por lotería considera que los procesos
puedan cooperar entre sí: si _B_ estuviera esperando un resultado de
_A_, podría transferirle sus boletos para aumentar la probabilidad de
que sea puesto en ejecución.

# ¿Qué tenemos que hacer?

Para el proyecto #2 les pido que _implementen un simulador_ de
planificación por estos dos mecanismos. Su implementación debe:

- Generar e imprimir una _carga de trabajo aleatoria_, con entre 5 y 8
  procesos, y con entre 80 y 120 _ticks_ de duración total. Los
  procesos pueden _aparecer_ en cualquier momento de la simulación
  (¡ojo! ¿Puede presentarse la situación de tener _huecos_ sin ningún
  proceso listo para ejecutar? ¿Cómo lidiarían con ellos?)
- Al planificar estos proceso, se toman varias decisiones. ¿Les están
  asignando determinada prioridad? ¿Están subiendo o bajando de cola?
  etc.

  Sean explícitos respecto a estos puntos, esto es, impriman o
  representen el avance sobre ellos.
- ¿Hay puntos que sienten que mi planteamiento deja pendientes?
  Recuerden que _tienen libertad para decidir sobre los detalles no
  especifcados de los problemas_. Les pido, eso sí, que _documenten_
  las decisiones que toman.
- Entreguen un documento detallando lo que se entrega, su programa (o
  sus programas, como prefieran).

Una ejecución ejemplo del planificador (más corta, sin llegar a los
80-120 ticks ni 5-8 procesos) podría ser:

    $ ./planificador_FB.py
	Carga de trabajo a simular en Retroalimentación Multinivel:
	Proceso   Duración   Llegada
	A         4          0
	B         8          3
	C         3          7
	D         5          11
	Parámetros del algoritmo: 
	n = 2
	Q = n+1
	* Inicia ejecución
	t=0
	  ⇒A
	  A:prio:0
	  ⌚: A: 1 tick
	t=1
	  A: prio:1
	  ⌚: A: 2 tick
	t=3
	  ⇒B
	  A: prio:2; B: prio:0
	  ⌚: B: 1 tick
	t=4
	  A: prio:2; B: prio:1
	  ⌚ B: 2 tick
	t=6
	  A: prio:2; B: prio:2
	  ⌚ A: 3 tick
	t=7
	  A 👍; ⇒C
	  B: prio:2; C: prio:0
	  ⌚ C: 1 tick
	t=8
	(...)
	Planificación realizada:
	AAABBBAC...
    Tabla de ejecución:
	Proceso Inicio Fin   T  E  P
	A       0      7     7  3  2.1
	B       3      (...)
	C       7      (...)
	D       11     (...)
	Prom           (...)

# Un poquito de razonamiento 😉

Estudiar e implementar diferentes esquemas de planificación debe
llevarnos a desarrollar un poco de sentido crítico sobre de ellos. A
tal fin, les pido que desarrollen para ambos algoritmos:

- ¿Cómo se compararía este método con los otros abordados?
- ¿Para qué tipo de carga es más apto y menos apto?
- ¿Qué tan susceptible resulta a producir inanición?
- ¿Qué tan _justa_ sería su ejecución?
- ¿Qué modificaciones requeriría para planificar procesos con
  necesidades de tiempo real? (aunque sea _tiempo real suave_)
- ¿Alguna otra reflexión o inquietud que les provoque?

# La entrega

Recuerda hacer tu entrega en este mismo repositorio Git, siguiendo la
nomenclatura especificada en el [punto 4 de la práctica
1](../../practicas/1/README.md). Recuerda que te _sugiero_ hacerlo en
una rama temática (`git branch proyecto2`).

Las entregas pueden realizarse de forma individual o en equipos de 2
integrantes.

# A modo de ejemplo

¡No se compliquen de más! No es necesario implementar hilos, comunicar
sincronización con semáforos, ni nada por el estilo. Les regalo aquí
la implementación del algoritmo más sencillo (FIFO); únicamente me
salté la tabla de ejecución (que no debe ser nada difícil de
desarrollar para ustedes 😉)

    from random import randint
    
    procesos = []
    primer_proc = 'A'
    
    for i in range(randint(4,8)):
        # Genero los 4 a 8 procesos aleatorios
        procesos.append({'nombre': chr( ord(primer_proc)+i ),
                         'llegada': randint(0, 10*i),
                         'duración': randint(4,10)
                         })
    
    print('Lista de procesos:')
    for proc in procesos:
        print("%2s  %3d  %3d" % (proc['nombre'], proc['llegada'], proc['duración']))
    
    
    t = 0
    res = ''
    # 'A' llega siempre en 0 ('llegada' es aleatorio entre 0 y 5*0)
    print('* Inicia ejecución')
    for p in sorted(procesos, key=lambda p: p['llegada']):
        print("t=%d" % t)
        # Manejamos el caso de que no haya ningún proceso listo para
        # ejecutar
        if t < p['llegada']:
            demora = p['llegada'] - 5
            res += '-' * demora
            t += demora
            print("    ... %d tick" % demora)
            print("t=%d" % t)
        # El proceso se ejecuta por toda la carga de trabajo que tiene
        res += p['nombre'] * p['duración']
        t += p['duración']
        print("    ⌚ %s %d tick" % (p['nombre'], p['duración']))
    
    print("Planificación realizada: \n" + res)
    print("\n\nDuración total: %d" % t)
