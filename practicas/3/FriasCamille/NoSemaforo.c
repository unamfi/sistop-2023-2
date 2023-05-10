#include <stdio.h>
int aquiere(int semaforo);
int realese(int semaforo);
int init();
void main ()
{
	int semaforo, opc=0;
	semaforo=init();
	
	do
	{
		
		switch(opc)
		{
			case 0:
				printf("\n \t Que desea hacer:_");
				printf("\n \t 1)... aquiere \n \t 2)... realese \n \t 3)... salir \n \t _" );
				scanf("%i",&opc);
				break;
			case 1:
				semaforo=aquiere(semaforo);
				opc=0;
				if (semaforo != 0)
				{
					printf("\n \t Estoy libre no te preocupes");
				}
				else
				{
					printf("\n \t Ya me ocupe no molestes");
				}
				break;
			case 2:
				semaforo=realese(semaforo);
				opc=0;
				if (semaforo != 0)
				{
					printf("\n \t Estoy libre no te preocupes");
				}
				else
				{
					printf("\n \t Ya me ocupe no molestes");
				}
				break;
			case 3: 
				printf("\n \t gracias por ver el ejemplo");
				break;
			default: printf("\n \t Esa no es una opcion");
		}
		
	}while (opc!=3);
	
}

int init ()
{
	int inicio=0;
	printf("\n \t Ingrese el valor inicial del semaforo:_");
	scanf("%i", &inicio);
	printf("\n \t El valor inicial del semaforo es: %i", inicio);
	
	return inicio;
}
int aquiere(int semaforo)
{
	semaforo=semaforo-1;
	return semaforo;
}

int realese(int semaforo)
{
	semaforo=semaforo+1;
	return semaforo;
}




