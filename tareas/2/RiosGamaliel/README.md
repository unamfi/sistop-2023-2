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

---
## Comentarios adicionales
Por más que estuve investigando a profundidad, no encontré cómo mostrar en formato octal 
el modo de cada archivo. Lo más cercano que se encontró fue el método `Files.getPosixFilePermissions()`,
el cual devuelve los permisos y a través de ellos se obtener el formato octal haciendo cada una 
de las comparaciones necesarias. Además, en un comienzo no entendí bien qué eran los primeros tres dígitos al comienzo del formato de modo mostrado en la captura. Investigando un poco más, pude concluir que se tiene:
- `100`: Para indicar que es un archivo
- `040`: Para indicar que es un directorio