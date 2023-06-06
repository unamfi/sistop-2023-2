# **Tarea 2:** Obteniendo información de un directorio

<pre>
<b>Materia:</b> Sistemas Operativos
<b>Grupo:</b> 6
<b>Alumno:</b> Ríos Lira, Gamaliel
<b>Fecha:</b> 06/06/2023
</pre>

***

## Lenguaje de programación utilizado

El lenguaje de programación utilizado fue `Java 17`, aunque todas las clases 
utilizadas están disponibles desde versiones anteriores. Se desarrolló 
haciendo uso del `OpenJDK 17`.

Para ejecutarlo, se puede hacer directamente con el comando:
```bash
$ java Main.java <directorio> <dias>
```

Con esto, `Java` compilará y ejecutará de forma automática el programa.

---

## Descripción del programa

La mayoría de la lógica que proporciona `Java` para el manejo de archivos, se 
encuentra dentro de la clase `File` del paquete `java.io`.

El funcionamiento de programa realizado consta de las siguientes etapas:
- *Obtención y validación de los parámetros*: En esta etapa, se valida que los 
parámetros de ejecución sean válidos. Por una parte, se verifica que el 
directorio listado exista y que efectivamente sea un directorio. Además, se 
toma el valor de los días para filtrar. Para esto, se colocó la lógica 
dentro del método `getParams()`.
- *Obtener los archivos dentro del directorio*: Para esto, se hace uso del 
método `listFiles()` de la clase `File`. Se le aplica un filtro a través de 
la clase `FileFilter` y a través de las clases de _tiempo y fecha_ que 
proporciona el lenguaje se calcula el número de días de la última modificación 
del archivo. Esto se encapsuló dentro del método `listDirectoryFiles()`.
- *Ordenar los archivos con base en su nombre*: Para esto, no se hizo más que 
aplicar un algorimo de ordenamiento a la lista obtenida en el paso anterior 
con ayuda de una herramienta llamada _streams_ que proporciona el lenguaje. La 
comparación se implementó de forma no sensitiva a letras mayúsculas a través 
del nombre del archivo. Esto se implementó dentro del método `sortFiles()`.
- *Mostrar la información*: Se itera sobre la lista de archivos y se va 
listando la información solicitada en forma de tabular. En esta sección, se 
implementó el método auxiliar `getOctalPermissions()` con la finalidad de 
obtener la cadena mostrada en las instrucciones. La lógica de este listado 
de muestra dentro de `showFilesInformation()`.

Con todo lo anterior, la ejecución del programa resultó en:

```bash
$ java Main.java /home/gamarl/sistop-2023-2/tareas/2/ 50
```
<pre>
Mostrando: /home/gamarl/sistop-2023-2/tareas/2/
Última modificación: Max 10 days

                   Nombre	      Modificación	  Modo	    Tamaño	
==========================================================================
                README.md	  30-05-2023 22:00	100664	      3220
             RiosGamaliel	  05-06-2023 23:41	040775	      4096
</pre>

---
## Comentarios adicionales
Por más que estuve investigando a profundidad, no encontré cómo mostrar en 
formato octal el modo de cada archivo. Lo más cercano que se encontró fue el 
método `Files.getPosixFilePermissions()`, el cual devuelve los permisos y a 
través de ellos se obtener el formato octal haciendo cada una de las 
comparaciones necesarias. Además, en un comienzo no entendí bien qué eran los 
primeros tres dígitos al comienzo del formato de modo mostrado en la captura.  
Investigando un poco más, pude concluir que se tiene:
- `100`: Para indicar que es un archivo
- `040`: Para indicar que es un directorio

Simplemente realicé una comparación para gregar la cadena correspondiente.
