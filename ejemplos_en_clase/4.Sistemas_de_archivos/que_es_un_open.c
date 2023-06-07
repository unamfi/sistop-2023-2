#include <stdio.h>
#include <unistd.h>

void main() {
  FILE *fh;
  fh = fopen("que_es_un_open.c", "r");
  printf("Lo que recibí es: %d\n", fileno(fh));
  sleep(100);
  fclose(fh);
}
