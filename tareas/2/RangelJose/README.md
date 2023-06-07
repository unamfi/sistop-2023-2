# TAREA 2

Para la ejecución de este programa, es necesario que se tengan las siguientes bibliotecas de python.
* sys
* os
* tabulate
* datetime

Ya que sin ellas el programa no podra ser ejecutado correctamente. Una vez teniendo dichas bibliotecas, el programa se puede ejecutar de la siguiente forma.

        py referencias.py <RUTA> <DIAS>

La ruta debe ser válida, de lo contrario no correra el programa. Los días deben ser mayores o iguales a 0. Si se escribe el 0 de dias, se entenderá que la búsqueda de documentos será que fueron modicados hoy. La ruta que acepta el programa puede ser absoluta o relativa, como se muentra en los siguientes dos ejemplos de su ejecución. 
  
        C:\Users\ga-becario it\Documents\SO\sistop-2023-2\tareas\2\RangelJose>py referencia.py ..\..\..\..\..\. 8
        -------------------------------------------------  --------------------------  --------------------------  -----  --------------
        Nombre                                             Creacion                    Modificacion                Modo   Tamaño [Bytes]
        DNC José Rangel.pptx                               2023-05-30 13:18:36.068030  2023-05-30 13:18:39.090702  33206  2958028
        Eshop                                              2023-03-28 11:46:54.944327  2023-06-05 10:56:38.809894  16895  4096
        Evaluación Diagnostica PowerPoint Versailles.pptx  2023-05-30 09:57:07.347083  2023-05-30 13:17:50.760556  33206  2958899
        Outlook Files                                      2023-05-16 09:40:10.604791  2023-06-05 13:10:59.583799  16895  0
        -------------------------------------------------  --------------------------  --------------------------  -----  --------------


        C:\Users\ga-becario it\Documents\SO\sistop-2023-2\tareas\2\RangelJose>py referencia.py "C:\Users\ga-becario it\Documents" 8
        -------------------------------------------------  --------------------------  --------------------------  -----  --------------
        Nombre                                             Creacion                    Modificacion                Modo   Tamaño [Bytes]
        DNC José Rangel.pptx                               2023-05-30 13:18:36.068030  2023-05-30 13:18:39.090702  33206  2958028
        Eshop                                              2023-03-28 11:46:54.944327  2023-06-05 10:56:38.809894  16895  4096
        Evaluación Diagnostica PowerPoint Versailles.pptx  2023-05-30 09:57:07.347083  2023-05-30 13:17:50.760556  33206  2958899
        Outlook Files                                      2023-05-16 09:40:10.604791  2023-06-05 13:10:59.583799  16895  0
        -------------------------------------------------  --------------------------  --------------------------  -----  --------------