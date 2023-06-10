# Obteniendo información de un directorio

    Tarea creada: 2023.05.30
    Entrega: 2023.06.06

En el primer acercamiento que estamos realizando a archivos y
directorios, presentamos las principales operaciones que pueden
realizarse tanto sobre un archivo como sobre un directorio. Para esta
tarea, les pido que implementen un sencillo programa que entregue una
*lista parcial* de los archivos contenidos en un directorio, pero que
presente varios *detalles de información*. 

El program *no debe ser interactivo*, debe obtener todos sus
parámetros de su invocación desde la línea de comandos.

El programa recibe dos parámetros: El primero, la ruta del directorio
que va a procesar, y el segundo, el *número de dias*.

El programa debe *abrir el directorio* que fue especificado como
primer parámetro, e imprimir todos aquellos archivos *cuya última
modificación* tenga el número de días especificado o menos.

La salida del programa debe presentarse *ordenada lexicográficamente*
por nombre de archivo. El programa debe imprimir el nombre del
archivo, su longitud, la fecha en que fue modifcado por última vez, y
el *modo* (los permisos) que tiene.

Como restricción adicional: Su programa *no debe llamar* a ningún
programa externo para obtener información, todo debe ser hecho desde
el lenguaje que hayan elegido para implementar (y de ser posible,
desde su *biblioteca estándar*).

## ¡Ejercicio calificado!

Pueden ya consultar la [revisión de sus entregas para este
ejercicio](./revision.org).

## Ejemplo de ejecución

Como ejemplo, les pongo el resultado de 3 ejecuciones (claro, estas serán
diferente en el equipo de cada uno de ustedes):

    ✓ gwolf@yogurtu『1』~ $ ./referencia.py
	Invocación: vcs/sistop-2023-2/tareas/2/referencia.py <directorio> <días>
	⚠ 1 gwolf@yogurtu『2』~ $ vcs/sistop-2023-2/tareas/2/referencia.py /tmp/ 1
    Nombre                         Modificación     Modo   Tamaño
	==============================================================
	hsperfdata_gwolf               2023-05-29 23:01 040755 0
	impressive-a6whlbew_tmp.txt    2023-05-29 23:01 100644 24571
	kdenlive-OOkeFB.mlt            2023-05-29 23:53 100644 14472
	tracker-extract-3-files.1000   2023-05-30 00:13 040700 0
	✓ gwolf@yogurtu『3』~ $ ./referencia.py /tmp/ 3
    Nombre                         Modificación     Modo   Tamaño
	==============================================================
	Temp-1b4c16ec-826f-468e-bc74-dbf2f83f73bb 2023-05-27 00:18 040700 0
	comp-lambda-W5kxrH.eln         2023-05-27 00:24 100755 70168
	hsperfdata_gwolf               2023-05-29 23:01 040755 0
	impressive-a6whlbew_tmp.txt    2023-05-29 23:01 100644 24571
	kdenlive-OOkeFB.mlt            2023-05-29 23:53 100644 14472
	mosca                          2023-05-28 23:16 040755 0
	systemd-private-77eeac213cb94bf9b4476265c1e9f5b6-systemd-timesyncd.service-YtpTRd 2023-05-27 00:20 040700 6
	tracker-extract-3-files.1000   2023-05-30 00:13 040700 0
	✓ gwolf@yogurtu『4』~ $ vcs/sistop-2023-2/tareas/2/referencia.py /home/gwolf/vcs/sistop-2023-2/tareas/2 5
    Nombre                         Modificación     Modo   Tamaño
	==============================================================
	README.md                      2023-05-29 23:18 100644 1521
	referencia.py                  2023-05-30 00:12 100755 1773
