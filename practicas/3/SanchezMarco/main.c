// NOTA: Este codigo esta inspirado en un codigo ejemplo presentado por Sri2 Manikanta Palakollu en su libro Practical System Programming with C.
// Descripcion: Este programa muestra la implementacion de hilos en C a traves de la POSIX pthread.h

#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *threadFunction();

int main(){
	pthread_t thread;	// Thread Descriptor
	int status;			// Variable to store the thread's status
	status = pthread_create(&thread, NULL, threadFunction, NULL);	// Create a thread and saves it's status

	// Verify thread creation
	if(!status){
		printf("Thread Created Successfully.\n");
	} else {
		printf("Can't Create Thread.\n");
		return 0;
	}

	for(int i=0; i<10; i++){
		printf("I am a process :)\n");
		sleep(1);
	}

	return 0;
}

void *threadFunction(){
	for(int i=0; i<10; i++){
		printf("Hello World! I am thread :P\n");
		sleep(1);
	}
}
