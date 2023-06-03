# Tarea 2

**Integrantes:** Sánchez Hernández Marco Antonio y Terán García Rodolfo Mario
**Lenguaje de programación utilizado:** Rust
**Consideraciones:** Este programa únicamente funciona en sistemas operativos GNU/Linux debido a los métodos utilizados. Es posible que la presentación de los datos de los diferentes archivos contenidoss en un directorio se impriman con desplazamientos y sin una alineación uniforme, principalmente por el tamaño del nombre del archivo, esto no afecta al funcionamiento del programa pero si a la presentación de los resultados para el usuario.

El programa lleva por nombre *Not ls* (nls) y hace uso de la librería estándar de Rust para obtener la información de directorios y archivos, sin embargo, se apoya en un crater adicional (*chrono*) para trabajar con la fecha de modificación de un archivo, realizar operaciones aritméticas y de comparación y dar formato a esta para presentarla al usuario.

Para que el programa funciona deben pasarse exactamente dos argumentos adiconales, la ruta absoluta o relativa hacia un directorio y el número de días, en caso de pasarse más o menos argumentos el programa le mostrará un mensaje de error descriptivo al usuario para hacerle notar este problema. Una vez el número de argumentos satisface el criterio, el programa procederá a verificar la existencia del archivo o directorio especificado por la ruta, en caso de no existir se mostrará un mensaje de error propio del lenguaje de programación el cual indica esto. Después de verificar la existencia se procederá a saber si es un directorio o no, si este no lo es se mostrará un mensaje de error para denotarlo.

Si los argumentos proporcionados son correctos y no se cae en alguno de los casos anteriormente mencionados se procede a listar los datos de todos los archivos contenidos en el directorio especificado por la ruta que cumplan con el número de días especificado. Debido a la lógica y protecciones de Rust, al obtener ciertos datos del archivo deben colocarse estructuras similares, más no iguales, a un *Try Catch* generando que en caso de error durante la obtención de estos datos el programa se detenga e informe al usuario de esto.

La lógica para listar los archivos inicia con el cálculo de la fecha de referencia (fecha y hora en el instante en la cual se ejecuta el comando) menos el número de días especificado la cual se comparará con las fechas de modificaciónde los archivos, en caso de esta ser mayor a la fecha de referencia, es decir, días después de la fecha de referencia, serán considerados para imprimir los demás datos (nombre, permisos y tamaño), en caso de no satisfacer este criterio el programa simplemente omite el obtener todos los datos de ese archivo y continúa con el siguiente archivo hasta terminar de listar cada archivo.

Si ningún archivo satisface el criterio la salida del programa será únicamente una fila con las palabras *Nombre*, *Modificación*, *Modo* y *Tamaño* seguido de una línea constituida por el caracter "=". En caso de no contar con permisos sobre la carpeta especificada, el programa no producirá salida alguna.

En los días es posible introducir números negativos, sin embargo, el resultado será el mismo que en el caso de que ningún archivo satisface el criterio, ya que estamos hablando de archivos que debieron ser modificados en días futuros.

### Ejecución del programa

El programa puede ser ejecutado de dos formas, a través de *cargo run* estando dentro de la carpeta del proyecto (*nls*): *cargo run -- </ruta/al/directorio> <dias>*

La otra forma de ejecutar el programa es a través de la ruta absoluta al archivo binario el cual se genera después de ejecutar *cargo run* dentro del directorio *./nls/target/debug/nls </ruta/al/directorio> <dias>*.

Opcionalmente puede moverse el archivo binario mencionado anteriormente a un directorio especificado en la variable de entorno *$PATH* para ejecutarlo de la siguiente manera: *nls </ruta/al/archivo> <dias>*
