#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void* run(void* data)
{
	size_t thread_num = (size_t)data;
	printf("Hola mundo desde el hilo %zu\n", thread_num);
	return NULL;
}

int main(void)
{
	pthread_t thread;
	pthread_create(&thread, NULL, run, (void*)1);
	pthread_create(&thread, NULL, run, (void*)2);
	pthread_create(&thread, NULL, run, (void*)3);
	pthread_create(&thread, NULL, run, (void*)4);
	printf("Hola mundo desde el hilo principal\n");
	int i;
	for (i=0;i<3;i++){
	pthread_join(thread, NULL);
	}

	return 0;
}