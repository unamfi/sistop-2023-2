#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>


int main(void) {

  int pid, estado;
  pid = fork();

  if (pid == 0){
    sleep(1);
    printf("[H] MiPadre = %5d Yo = %5d\n", getppid(), getpid());
  }else {
      printf("[P] MiPadre = %5d Yo= %5d MiHijo=%5d\n", getppid(), getpid(), pid);
      pid = wait(&estado);
      printf("[P]: Termino el hijo %d con estado %d\n", pid, estado);

  }

}
