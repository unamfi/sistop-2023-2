#include <stdio.h>
#include <pthread.h>
#include <math.h>

void *calculoP(void *argm){
	int i,num = 2;
	int *pot = (int *)argm;
	int numero = pow(num,*pot);
	printf("\n El numero 2 elevado a la potencia %i es : %i \n",*pot,numero);

}

main(){
	int cant,i;
	printf("\n Calculadora de Potencia de 2:\n\n");
	printf("Ingrese un nume que indique hasta que potencia se calculara 2: ");
	scanf("%i",&cant);
	for (i=0;i<=cant;i++){
		pthread_t rephilo;
		pthread_create(&rephilo, NULL, calculoP,(void*)&i);
		pthread_join(rephilo,NULL);
	}
}
