#include <stdio.h>
#include <pthread.h>
void *func_hilo (void *arg) {
printf("Hilo creado: ¡Hola mundo!\n");
}
int main(void) {
pthread_t tid;
pthread_attr_t atrib;
printf("Hilo principal: INICIO\n");
pthread_attr_init(&atrib);
pthread_create(&tid, &atrib, func_hilo, NULL);
printf("Hilo principal: HILO CREADO\n");
pthread_join(tid, NULL);
printf("Hilo principal: FIN\n");
}