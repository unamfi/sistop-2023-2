#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
int main() {
    pid_t rf;
    rf = fork();
    switch(rf){
        case -1:
        printf("no he podido crear el prceso del hijo \n");
        break;
        case 0:
        printf("Soy el hijo, mi PID es %d y mi PID es %d \n",getpid(),getpid());
        sleep(2);
        break;
        default:
        printf("Soy el padre, mi PID es %d y el PID de mi hijo es  %d \n",getpid(),rf);
        sleep(2);
    }
    printf("Final de ejecucion de %d \n",getpid());
}
