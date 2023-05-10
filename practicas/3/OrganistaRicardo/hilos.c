#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

#define NTHREADS 10

sem_t mutex; // declarar el semáforo globalmente para que todas las funciones lo vean

void *thread_func(void *arg)
{
    int id = *(int*) arg;
    printf("Hilo %d: iniciando\n", id);
    
    // Entrar en la sección crítica
    sem_wait(&mutex);
    printf("Hilo %d: en la sección crítica\n", id);
    // hacer algo en la sección crítica
    sleep(1);
    printf("Hilo %d: saliendo de la sección crítica\n", id);
    sem_post(&mutex);
    
    printf("Hilo %d: finalizado\n", id);
    pthread_exit(NULL);
}

int main()
{
    pthread_t threads[NTHREADS];
    int ids[NTHREADS];
    int i;

    sem_init(&mutex, 0, 1); // inicializar el semáforo a 1

    for (i = 0; i < NTHREADS; i++) {
        ids[i] = i;
        pthread_create(&threads[i], NULL, thread_func, &ids[i]);
    }

    for (i = 0; i < NTHREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    sem_destroy(&mutex); // liberar los recursos del semáforo
    return 0;
}
