# Proyecto 2: Planificacion por loteria y retroalimentacion por multinivel

**Sanchez Hernandez Marco Antonio**
**Teran Garcia Rodolfo Mario**

## Generalidades
**Lenguaje de programacion utilizado:** Rust 2021
**Notas adicionales:** Para ejecutar el programa debe instalarse manualmente el crater rand o requiere unicamente de utilizarse el comando *cargo run* dentro del directorio del proyecto.

## Loteria

El algoritmo de loteria realizar la planificacion de proyectos de manera aleatoria basada en la cantidad de tickets de un proceso, entre mayor sea la cantidad de boletos, mayor es la probabilidad de que el proceso sea seleccionado. Basado en este funcionamiento basico, la implementacion presentada funciona a partir de generar primero un numero aleatorio de procesos entre 5 y 8 para facil visualizacion de la ejecucion nombrados de la A hasta la H, cada uno de estos procesos tiene una llegada, siendo A 0, y una duracion. Una vez han sido creados los proyectos, lo siguiente es generar son los tickets, el numero de boletos esta especificado por una constante y estos son representados en un vector, el cual ira asignando tickets al mismo tiempo que los genera. Una vez los tickets se han entregado, comienza el sorteo para ver quien sera el proceso al cual le tocara tiempo de ejecucion, el mecanismo es simple, el proceso con el boleto ganador tendra el tiempo de ejecucion para ello se selecciona un numero aleatorio entre el 0 y el numero de boletos generados, como ejemplo, luego el resultado de la planificacion es mostrado de acuerdo a los boletos seleccionados. La tabla de ejecucion no es mostrada debido a las dificultades encontradas al momento de utilizar el lenguaje de programacion Rust, especialmente por el tratamiento que este lenguaje tiene con los tipos de datos y por evitar las advertencias y posibles estados de panico por parte del compilador y la herramienta cargo no forma parte del codigo ejecutable.
