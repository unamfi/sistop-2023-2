#include <stdio.h>
#include <pthread.h>

#define N 8
#define M 16

const char *mensaje[2] = {"Hola Mundo", "Mundo Hola"};
const int cantidad[2] = {N, M};

void imprime_mensaje(void *ptr) {
        int i;
        int id;

        id = *(int *) ptr;
        for(i=0; i<cantidad[id]; i++)
                printf("%s\n",mensaje[id]);
        return;
}


int main(int argc, char *argv[])
{
        pthread_t hilo0, hilo1;
        int id0=0, id1=1;

        pthread_create(&hilo0, NULL, (void *) &imprime_mensaje, (void *) &id0);
        pthread_create(&hilo1, NULL, (void *) &imprime_mensaje, (void *) &id1);

        pthread_join(hilo0, NULL);
        pthread_join(hilo1, NULL);

        return 0;
	/* Hice un comentario en esta parte*/

}
