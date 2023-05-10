			----Universidad Nacional Autónoma de México---
					Facultad de Ingeniería
	
						Tarea 1

		Nombres:	Meneses Navarro Erick Sebastian 
				Mex Lozano Aerin Musette

--Problema a realizar: Santa Claus

--Lenguaje de programación: Python

--Ejecución: Escribir "Tarea1-Santa.py" en su shell para ejecutar el programa y para poder detener la ejecución haga click en la tecla para pooder detenerlo, no sabemos cual es la que usted usa, pero básicamente es hacer lo que usted realiza cuando nos presenta los programas en clases.

--Estrategia:
Existen dos variables que serán compartidas tanto en los hilos de los renos como el de los elfos, las cuales son llamadas "renos" y "elfos" pues ambas funcionan como contadores, y para poder controlar dicho acceso, es necesario un mutex.

Vemos que tenemos dos semáforos de los elfos, el primero "elfoSema" es el semáforo "general" y es el que nos ayudará a controlar los elfos que ya resolvieron su duda con Santa, el segundo "elfosSema" nos ayudará a controlar el grupo de 3 que pasaran a dar su duda con santa.

En la función de los renos veremos nuestro primer mutex "mutexR", esto porque encontraremos la variable compartida "renos", asi que, tenemos la sección crítica la cual al momento de que, si la cantidad de renos es igual a 9 entonces despierta a Santa para poder realizar su acción, si este es menor 9 quiere decir que los renos aun no regresan de sus vacaciones.

Para la función de los elfos, seguimos la misma metodología, encontramos nuestro mutex "mutexE", puesto que tendremos nuestra sección crítica, la cual al momento de que sean el grupo total de elfos despertarán a santa y aclarará sus dudas.


¿Cómo es que Santa sabe que ya llegaron los 9 renos de vacaciones y que se juntaron los 3 elfos con dudas?
Primeramente, para los renos, en la función "Santa", vemos un if, donde preguntamos si el número de renos es igual al total, osea 9, si se cumple entonces reiniciamos el contador de los renos, y vamos liberando los 9 hilos con un cilo for, sin embargo si el numero de elfos con dudas es igual a 3 entonces reinicamos el contador de elfos y observamos dos for, el primer for libera la "barrera" que deja pasar a solamente grupos de 3 en 3 elfos, y el segundo for va liberando a cada elfo que ya pasó.

¿Cómo identificamos que ya llegó el último reno de vacaciones y que ya esta el tercer elfo con duda?
Simplemente con los print, usando el identificador del hilo, vemos quien es el último hilo en llegar y el que desertará a Santa y sabemos que ese lo despertará pues liberamos el semáforo de santa.

print("El reno",n,"Llego de vacaciones T_T y despertó a santa")
santaSema.release()

print("El elfo ",n,"tiene una duda o_O y despierta a santa")
santaSema.release()

-- Dudas ó alguna mejora
Se podría decir que hicimos una implementación de "barrera" al momento de crear el semáforo "elfosSema" sin embargo queriamos hacer una barrera pero no quedaba del todo bien pues no sabiamos en que lugar poner lo que sería el acquire y release, asi que hicimos lo que ya fue descrito anteriomente.
