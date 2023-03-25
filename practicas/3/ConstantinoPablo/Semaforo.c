#include <stdio.h>
#include <semaphore.h>
#include <pthread.h>

static void * thread_1_fun(void* arg);
static void * thread_2_fun(void* arg);

sem_t sem;

int main(void)
{
	pthread_t thread_1, thread_2;

	sem_init(&sem, 0, 1);

	pthread_create(&thread_1, NULL, *thread_1_fun, NULL);
	pthread_create(&thread_2, NULL, *thread_2_fun, NULL);

	pthread_join(thread_1, NULL);
	pthread_join(thread_2, NULL);
	return 0;
}

static void * thread_1_fun(void* arg){

	printf("%d\n",1 );
	sem_post(&sem);
	sem_wait(&sem);
	printf("%d\n",3 );
	sem_post(&sem);
}

static void* thread_2_fun(void* arg){

	sem_wait(&sem);
	printf("%d\n",2 );
	sem_post(&sem);
	sem_wait(&sem);
	printf("%d\n",4 );
}


