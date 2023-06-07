#include <stdio.h>
void main() {
  int *no_funciona;
  no_funciona = 0x0000aaaab0ca0000;
  printf("%d\n", *no_funciona);
  printf("Todo bien :-)\n");
}
