# Una solucion al problema de Santa Claus

**Nota:** Este documento, asi como los comentarios e impresiones presentes en el codigo, contienen errores ortograficos de asentuacion debido a que en el sistema utilizado para la creacion del programa unicamente se cuenta con el *keyboard layout* EN-US.

**Lenguaje de programacion utilizado:** C
**Compilador utilizado:** gcc 12.2.1
**Requisitos:** contar con los POSIX *pthread.h* y *semaphore.h*
**Consideraciones:** Este codigo fue desarrollado completamente en un entorno Linux x86-64.

## Instrucciones de compilacion y ejecucion

1. Compilar el codigo fuente, archivo *main.c* con ayuda de gcc mediante el comando *gcc main.c -o main*.

2. Ejecutar el archivo binario generado mediante el comando */main*.

## Estrategia de sincronizacion utilizada

Para la solucion de este problema se utilizo un mutex, para evitar que mas de tres elfos puedan estar con Santa Claus al mismo tiempo y que este pueda verificar los contadores de ambos (renos y elfos). Ademas se utilizaron semaforos para permitir a los renos y elfos avisar a Santa de su presencia y para que santa pueda iniciar el viaje con los renos. 

## Puntos debiles

A pesar de ser una solucion completa, debe tenerse en cuenta que, al compilar el codigo fuente GCC produce cuatro mensajes de advertencia relacionados a uno de los argumentos en la funcion *pthread_create()*, especificamente el ultimo argumento, si bien no genera algun problema visible o facil de identificar es posible que puedan existir errores inesperados a raiz de esto.

Otra consideracion importante es que, al ejecutar el codigo, se mostraran ambos casos, Santa Claus ayuda a los elfos y esta listo para viajar con sus renos, sin embargo, no es posible observar la impresion de lineas previas a esta accion como se observa al dejar correr el programa. Finalmente, a lo largo de la ejecucion del programa puede parecer que el programa siempre genera la misma salida, pero, existiran pequenias variaciones asociadas posiblemente al tiempo en el cual se manda a dormir un hilo.
