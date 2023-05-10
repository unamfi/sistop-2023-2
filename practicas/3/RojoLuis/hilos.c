#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "omp.h"

#define length 10        //El tamaño de los arreglos a sumar lo definimos como constante en todo el código

int llenarAleatorio(int *arr, int n);
int imprimirArreglo(int *arr, int n);                                   //Son los prototipos de las funciones que utilizaremos
int sumarArreglos_sec(int *arr1, int *arr2, int *arr3, int n);
int sumarArreglos_parallel(int *arr1, int *arr2, int *arr3, int n);
int sumarArreglos_2hilos(int *arr1, int *arr2, int *arr3, int n);


int main()
{
	srand(time(0));                                         //Función que evita que nuestros arreglos aleatorios sean iguales en cada ejecución
    double t1, t2;                                          //Variables que nos ayudarán a medir el tiempo de ejecución
	
	int *a = (int *)malloc(sizeof(int) * length);           //Llenamos arreglos aleatorios utilizando memoria dinámica
	llenarAleatorio(a, length);
	
	int *b = (int *)malloc(sizeof(int) * length);
	llenarAleatorio(b, length);

	int *c = (int *)malloc(sizeof(int) * length);           //Estos serán los arreglos donde almacenaremos los resultados de las sumas
    int *d = (int *)malloc(sizeof(int) * length);
    int *e = (int *)malloc(sizeof(int) * length);

    printf("\n\n\n------Suma de arreglos (n=%d)-------\n\n\n",length);
    
    t1 = omp_get_wtime();
    sumarArreglos_sec(a,b,c,length);                        //Se ejecuta la función y se obtiene su tiempo de ejecución 
    t2 = omp_get_wtime();
    printf("Iniciando suma...\nTiempo secuencial %f",t2-t1);

    t1 = omp_get_wtime();
    sumarArreglos_2hilos(a,b,d,length);                     //Se ejecuta la función y se obtiene su tiempo de ejecución 
    t2 = omp_get_wtime();
    printf("\nUsando 2 hilos\nTiempo paralelo %f",t2-t1);

    t1 = omp_get_wtime();
	sumarArreglos_parallel(a,b,e,length);                   //Se ejecuta la función y se obtiene su tiempo de ejecución 
    t2 = omp_get_wtime();
    printf("\nUsando 8 hilos\nTiempo paralelo for %f\n\n",t2-t1);

    imprimirArreglo(a, length);                            //Se imprimen los arreglos que llenamos aleatoriamente
    printf("\n\n");
    imprimirArreglo(b, length);

    printf("\n\n-----------------------------------------------------------------------------------\n\n");

    printf("Secuencial:\n");
    imprimirArreglo(c, length);                             //Se imprimen los arreglos que tienen los resultados 
    printf("\nParalelo (2 hilos):\n");                      //obtenidos al sumar los arreglos aleatorios
    imprimirArreglo(d, length);
    printf("\nParalelo (pragma omp for):\n");
    imprimirArreglo(e, length);
    printf("\n");
}

int imprimirArreglo(int *arr, int n)                        //Con esta función imprimimos los arreglos 
{
    for(int i=0; i<n; i++)
	{
		printf("%d\t", arr[i]);
	}
}

int llenarAleatorio(int *arr, int n)                       //Con esta función llenamos aleatoriamente un arreglo
{                                   
	for(int i; i<n; i++)
	{
		arr[i] = rand() %10;                               //Se llenará con números del 0 al 9
	}
}

int sumarArreglos_sec(int *arr1, int *arr2, int *arr3, int n)   //Se suman los arreglos de manera secuencial
{
	for(int i=0; i<n; i++)
	{	
		arr3[i] = arr1[i] + arr2[i];
	}
}

int sumarArreglos_2hilos(int *arr1, int *arr2, int *arr3, int n)   //Se suman los arreglos utilizando solo 2 hilos
{
	#pragma omp parallel num_threads(2)
	{
		#pragma omp for
		for(int i=0; i<n; i++)
		{	
			arr3[i] = arr1[i] + arr2[i];
			//printf("hilo %d calculo arr3[%d] = %d\n",tid,i,arr3[i]);
		}
		
	}
}

int sumarArreglos_parallel(int *arr1, int *arr2, int *arr3, int n)  //Se suman los arreglos utilizando la función for de la libreria omp
{
	int tid;                                                        //En este caso se utilizaran todos los procesadores que posee nuestra computadora
	#pragma omp parallel private(tid)
	{
		tid = omp_get_thread_num();
		
		#pragma omp for
		for(int i=0; i<n; i++)
		{	
			arr3[i] = arr1[i] + arr2[i];
			//printf("hilo %d calculo arr3[%d] = %d\n",tid,i,arr3[i]);
		}
		
	}
}
