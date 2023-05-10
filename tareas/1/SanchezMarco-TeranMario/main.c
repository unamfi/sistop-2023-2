////////////////////////////////////////////////////////
//                                                    //
// Title: El problema de Santa Claus                  //
// Autores: Marco Sanchez & Mario Teran               //
// Ultima modificacion: 2023-04-14 00:52 CST (UTC -6) //
//                                                    //
////////////////////////////////////////////////////////

#include <stdio.h>
#include <stdlib.h>     // Generar numeros aleatorios random()
#include <stdbool.h>    // Incluir true
#include <unistd.h>     // Incluir la funcion sleep()
#include <pthread.h>    // Biblioteca para implementar hilos
#include <semaphore.h>  // Biblioteca para implementar semaforos y mutex

#define NO_TOTAL_RENOS 9
#define NO_TOTAL_ELFOS 10
#define NO_PERMITIDO_ELFOS 3

int no_elfos = 0;
int no_renos = 0;
sem_t sem_santa_claus, sem_reno, mut_elfo, mutex;

void *santa_claus();
void *elfo(void *);
void *reno(void *);

int main(void) {
	int crear_hilo;
	pthread_t santa;
	pthread_t renos;
	pthread_t elfos;

	sem_init(&sem_santa_claus,0,0);
	sem_init(&sem_reno,0,0);
	sem_init(&mut_elfo,0,1);
	sem_init(&mutex,0,1);

	crear_hilo = pthread_create(&santa,NULL,&santa_claus,NULL);
	if(crear_hilo != 0)
		return 1;

	for(int i=0; i<NO_TOTAL_ELFOS; i++) {
		crear_hilo = pthread_create(&elfos,NULL,&elfo,(void *)i+1);
		if(crear_hilo != 0)
			return 1;
	}

	for(int j=0; j<NO_TOTAL_RENOS; j++) {
		crear_hilo = pthread_create(&renos,NULL,&reno,(void *)j+1);
		if(crear_hilo != 0)
			return 1;
	}

	pthread_join(santa,NULL);

	sem_destroy(&sem_santa_claus);
	sem_destroy(&sem_reno);
	sem_destroy(&mut_elfo);
	sem_destroy(&mutex);
}

void *santa_claus() {
	printf("Santa esta durmiendo.\n");
	while(true) {
		sem_wait(&sem_santa_claus);
		sem_wait(&mutex);
		if(no_renos == NO_TOTAL_RENOS) {
			printf("Santa se despierta e inicia su recorrido.\n");
			for(int i=0; i<NO_TOTAL_RENOS; i++)
				sem_post(&sem_reno);
			no_renos = 0;
		} else if(no_elfos == NO_PERMITIDO_ELFOS)
			printf("Santa se despierta y ayuda a los elfos.\n");
		sem_post(&mutex);
	}
}

void *elfo(void *id) {
	int id_elfo = (int)id;
	while(true) {
		sem_wait(&mut_elfo);
		sem_wait(&mutex);
		no_elfos++;
		if(no_elfos == NO_PERMITIDO_ELFOS)
			sem_post(&sem_santa_claus);
		else
			sem_post(&mut_elfo);
		sem_post(&mutex);

		printf("Elfo %d le da lata a Santa Claus.\n",id_elfo);
		sleep(3);
	
		sem_wait(&mutex);
		no_elfos--;
		if(no_elfos == 0)
			sem_post(&mut_elfo);
		sem_post(&mutex);
		sleep(1+random()%5);
	}
}

void *reno(void *id) {
	int id_reno = (int)id;
	while(true) {
		sem_wait(&mutex);
		no_renos++;
		if(no_renos == NO_TOTAL_RENOS)
			sem_post(&sem_santa_claus);
		sem_post(&mutex);
		sem_wait(&sem_reno);
		printf("Reno %d regresa de sus vacaciones y esta listo.\n", id_reno);
		sleep(6);
	}
}
