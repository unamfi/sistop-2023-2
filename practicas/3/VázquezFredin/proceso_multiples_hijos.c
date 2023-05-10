/*
        **************************************************************************************
        ******      Programa que crea un proceso, y a su vez éste crea diferentes       ******
        ******             procesos hijos que calculan números aleatorios.              ******
        **************************************************************************************
*/

// Librerias
#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/wait.h>

#define NUM_CHILD 5

int proceso_hijo_accion(){
    int num_random;
    srand(getpid());                 // id del proceso
    num_random = (rand() % 256);     // Para mantenerlo en el rango que admite exit
    printf("HIJO: Hola, soy un proceso hijo con pid: %d, he calculado el valor random = %d.\n",getpid(),num_random);
    return num_random;
}

int main()
    {
        pid_t p_idC;
        int status;

        for(int i=0;i<NUM_CHILD;i++){
            p_idC = fork();
            
            // Padre se está ejecutando: seguirá creando hijos, por ende se continua.
            if(p_idC>0)         continue;

            // El hijo se está ejecutando: realizará una acción y después el hijo termina.
            else if(p_idC==0)   exit(proceso_hijo_accion());    // Valor con el que termina de 0 - 255.

            // Ninguna de los anteriores: se tiene une error.
            else puts(">>> Error <<<");
        }

        // El padre espera que los hijos terminen para saber su valor de retorno.
        for(int i=0;i<NUM_CHILD;i++){
            p_idC = wait(&status);      // Devuelve el identificador del proceso que ha terminado.
            printf("PADRE: Hola, soy el padre con pid: %d, mi hijo de pid: %d ha terminado y su estado es: %d.\n",getpid(),p_idC,WEXITSTATUS(status));
        }

        // El padre se quedará en un bucle para dormir
        while(1) sleep(10);

        return 0;
    }