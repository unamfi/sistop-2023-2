# Tarea 2. Obteniendo información de un directorio

**Integrantes**

 - Carranza Ochoa José David
 - Morales Ortega Carlos

## Ejecución
El programa fue realizado desde Python, por lo que puede ser ejecutado desde la terminal de Windows o Linux, al tenerlo instalado.

Como entrada principal, se debe especificar desde la terminal 2 parámetros, la ruta de un directorio seguida de un número quien representa a los días desde la última modificación.

Al especificarse la cadena como 

>   sh-5.1$ <binario de python\> <directorio a buscar\> <días>

Obteniendo así una correcta interpretación de los archivos, por ejemplo

> sh-5.1$ /bin/python /../../../tarea2.py /home/david/Escritorio 8

## Funcionamiento
Se tiene una sola función quien es la encargada de realizar el trabajo; al pasar los parámetros a `listar_archivos_por_fecha` primero se obtiene la fecha actual del sistema, a partir de esto es posible realizar una comparación entre los días que se han agregado como parámetros con el día de hoy (considerando la conversión de días a segundos).

Con esto, procedemos a listar los archivos de la ruta ingresada, tal que por medio de un bucle se ordenen los mismos mientras se itera.

El bucle realiza una función especial, ya que este para cada archivo del directorio obtiene su información y establece las variables solicitadas (nombre, tamaño, fecha de modificación y modo).

El formato de impresión solo resulta en agregar una cabecera al programa seguida de la descripción formateada de cada elemento previamente mencionado, ajustando en la pantalla el valor esperado.

