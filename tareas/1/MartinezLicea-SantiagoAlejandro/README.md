# **Ejercicio *Cruce del Rio***

## **Integrantes**
- Santiago Alejandro Aldo
- Martinez Licea Christian Jair

**Fecha: 13/04/2023**

***

## **Lenguaje y Entorno**
Se ha desarrollado en lenguaje ***Python 3.10***. Se uso el editor de texto **VSC (Visual Studio Code)**.

## **Estrategia**
La estrategia implementada en el código es utilizar semáforos para controlar el acceso de los hackers y serfs a la balsa, de modo que la balsa no se sobrecargue. Se utiliza un semáforo para controlar el acceso de los hackers y otro para controlar el acceso de los serfs, de manera que se garantice que solo se suba al máximo número de personas permitido en la balsa, que en este caso es 4.

Además, se uso un semáforo auxiliar para el control del acceso a la balsa. De esta forma, se asegura que la balsa cruce cuando este llena.

Para simular el recorrido y regreso de la balsa, se uso el módulo **time** de **Python** para pausar la impresión del estado de la balsa.

- Para que pueda funcionar la pausa sin que otro hilo comience, es necesario imprimir antes de liberar el ***mutex***.



