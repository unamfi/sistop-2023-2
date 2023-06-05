#**Tarea 2**
###Armenta Chora Luis Fabian

El programa realizado en Python devuelve una lista parcial de los archivos contenidos en un directorio, que presenta varios detalles de información tales como lo son:
+ Nombre del archivo
+ Tamaño del archivo
+ Modo (permisos)
+ Última fecha de modificación

Dicho programa debe tener como párametro la ruta del directorio y el número de días.

El programa consta de dos principales funciones:

+ ***read_archivo(ruta_archivo)*** 
+ ***directorio(ruta_directorio, num_dias)***

La función ***read_archivo()*** recibe la ruta de un archivo y utiliza varias funciones del módulo os tales como os.path.basename y os.path.getsize para obtener la información previamente sobre el archivo, la función retorna esta información en una tupla.

La función ***directorio()*** recibe la ruta de un directorio y el número de días límite. La función primero verifica si la ruta proporcionada es un directorio válido utilizando la función os.*path.isdir()*. Si no es un directorio válido, muestra un mensaje de error y retorna.


Posteriormente, *tiempo_actual* representa el tiempo actual en segundos y multiplicamos num_dias por 24 para obtener el número de horas correspondiente y luego por 60 * 60 para convertirlo a segundos.

El resultado final en *tiempo_limite* es el límite de tiempo en segundos antes del cual se considera que un archivo ha sido modificado. Todos los archivos cuya fecha de modificación sea igual o posterior a este límite se consideran válidos para su inclusión en la lista de archivos modificados en los últimos N días

A continuación, la función utiliza *os.walk()* para recorrer todos los directorios y archivos dentro del directorio especificado. Para cada archivo, obtiene su ruta completa y su tiempo de modificación utilizando *os.path.join()* y *os.path.getmtime()* respectivamente.

Luego, compara el tiempo de modificación del archivo con el tiempo límite calculado. Si el archivo ha sido modificado dentro del límite de tiempo, agrega su ruta a una lista.

Después de recorrer todos los archivos, la función ordena la lista de archivos utilizando *sorted()* para que estén en orden lexicográfico.

Finalmente, la función itera sobre la lista ordenada de archivos y utiliza la función ***read_archivo()*** para obtener la información detallada de cada archivo. Esta información se imprime en la consola.

Por último, se verifica si se proporcionaron los argumentos correctos en la línea de comandos utilizando len(sys.argv). Si no se proporcionaron los argumentos correctamente, se muestra un mensaje de error. Si los argumentos son correctos, se asignan a las variables ruta_directorio y num_dias, y se llama a la función ***directorio()*** con estos argumentos.


*********

##Ejecución

Como se mencionó, un requisito era que no debía ser interactivo por lo que al momento de ejecutar el programa debemos de insertar a su vez los parámetros.

    python tarea2.py /rutadirectorio <num_dias>

Por ejemplo para que ejecutamos nuestro programa desde la línea de comandos pasando como ruta mi carpeta de descargas personal y el número de días =  18 días deberíamos poner:

    python tarea2.py D:\Users\52554\Downloads 18