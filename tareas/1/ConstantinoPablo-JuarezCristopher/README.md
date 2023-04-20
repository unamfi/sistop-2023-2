# Tarea 1: Cruce de rio
---
### *Integrantes*

*	Pablo Giovani Constantino Cruz
*	Cristopher Israel Juarez Paniagua

#### *Lenguaje y entorno de desarrollo*

Lenguaje de programación PYTHON versión 3.10.2 en un editor de texto plano.

#### *¿Qué tengo que saber / tener / hacer para ejecutar su programa en mi computadora?*

Para poder ejecutar este programa es necesario tener una versión compatible de Python y deberemos establecer el número de hilos (tripulantes) en múltiplos de 4 ya que deben ser forzosamente 4 tripulantes en la balsa.

#### *Estrategia de sincronización (mecanismo / patrón) que les funcionó*

##### Variables:
*	tripulantes: se utiliza para llevar un registro del número de tripulantes que suben a la balsa. 
*	num_Hackers y num_Serfs: se utilizan para llevar un registro del número de hackers y serfs que están esperando para subir a la balsa. La función hackers y serfs utilizan estas variables para decidir si la balsa se llenara con 4 desarrolladores del mismo tipo o con 2 de cada tipo.

*	num_Viaje: se utiliza para llevar un registro del número de viajes que se han hecho. 

*	Hackers y Serfs: se utilizan para sincronizar los threads de hackers y serfs. Se liberan cuando hay suficientes hackers o serfs para llenar la balsa.

*	mutexBote: se utiliza para proteger el acceso a la variable tripulantes.

##### Funciones:
*	**suben_hackers y suben_serfs**
	-	Estas funciónes se encargan de controlar la cantidad de Hackers y Serfs que suben al bote en base a la cantidad de Hackers y Serfs  que haya en dicha instancia.

	-	La función incrementa en 1 a "num_Hackers"/”num_Serfs” para indicar que un Hacker/Serf se ha subido a la balsa.

	-	Si la cantidad de Hackers/Serfs llega a 4, la función libera el acceso al bote para los 4 Hackers/Serfs utilizando una lista de comprensión y el método "release()", despues se vacía los contadores "num_Hackers"/”num_Serfs”. 

	-	Si la cantidad de Hackers es 2 y la cantidad de Serfs también es 2, hay suficientes pasajeros de ambos tipos para poder llenar el bote, por lo tanto la función libera el acceso al bote para 1 Hacker y 2 Serfs en el caso de la función "suben_hackers” y 2 Hacker y 1 Serfs en el caso de la función "suben_serfs”   utilizando el método "release()", ademas de poner en 0 los contadores de Hackers y Serfs. 

	-	Si ninguna de las condiciones anteriores se cumple, la función utiliza el método "acquire()" para bloquear el acceso ala balsa hasta que se libere un espacio.

*	**zarpar**
	-	Se utiliza un mutex para proteger la variable tripulantes, la cual es un contador de los tripulantes que suben a la balsa (máximo 4).
	-	La función recibe el argumento desarrollador (el cual puede ser Hacker o Serf), que se utiliza para imprimir un mensaje que indica el nombre del desarrollador que está subiendo a la balsa y su número de tripulante (de 1 a 4). 
	-	Se incrementa el contador de tripulantes y la función verifica si hay cuatro tripulantes en la balsa. Si este es el caso, imprime un mensaje indicando que la balsa zarpa, espera un segundo y reinicia el contador de tripulantes para la siguiente balsa. 
	-	Se incrementa el contador num_Balsa para llevar un registro del número de viajes que se han hecho con la balsa.

### *Dudas*

La duda que nos surge fue el como hacer para que nos lance un error al momento de que haya un numero de desarrolladores que no sea múltiplo de 4 ya que como el problema lo especifica la balsa es demasiado ligera, y con menos de cuatro puede volcarse.