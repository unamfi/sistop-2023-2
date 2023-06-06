#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#define n 10

void llenaArreglo (int *a);
void suma (int *a, int *b, int *c);

int main(int argc, char const *argv[])
{
    
    int max, *a, *b, *c;

    a = (int *)malloc(sizeof(int)*n);
    b = (int *)malloc(sizeof(int)*n);
    c = (int *)malloc(sizeof(int)*n);

    llenaArreglo(a);
    llenaArreglo(b);

    suma (a, b, c);

    return 0;
}

void llenaArreglo (int *a){

    int i;
    for (i = 0; i < n; i++){
        a[i] = rand()%n;
        printf("%d\t", a[i]);
    }
    printf("\n");

}

void suma (int *A, int *B, int *C){

    int i, tid;// inicio, fin;
    //omp_set_num_threads(2);
    //#pragma omp parallel private (inicio, fin , tid, i)
    #pragma omp parallel private(tid)
    {
        tid = omp_get_thread_num();
        /*inicio = tid* 5;
        fin = (tid+1)*5-1;

        for (i = inicio; i < fin; i++){
            C[i] = A[i] + B[i];
            printf("hilo %d calculo C[%d] = %d\n", tid, i, C[i]);
        }
        */
       #pragma omp for
       for (i = 0; i < n; i++){
           C[i] = A[i] + B[i];
           printf("hilo %d calculo C[%d] = %d\n", tid, i, C[i]);
       }

    }

}
