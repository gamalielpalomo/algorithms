#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

int* Recorrimiento(int*);
int* Ordenamiento(int*);
void Recursividad(int*);
bool existsInArray(int*, int);
int limite;

int main ()
{

	int input[8]={2, 2, 4, 5, 7, 2, 3, 6};				//Esta es la secuencia de entrada
	limite = (sizeof(input)/sizeof(input[0])) - 1;		//Establecemos el limite para poder hacer la reducción de la secuencia sin utilizar más memoria
	
	cout<<"Arreglo inicial: ";
	for(int i=0; i<=limite;i++)							//Este ciclo imprime el arreglo
		cout << input[i] << "  ";

	int suma = 0; 										//Iniciamos la suma  en 0
	for (int i=0; i<=limite; i++)						//Realizamos la suma de todos los elementos del array
		suma += input[i];			
	cout << "\nLa suma inicial es " << suma;

	if (suma % 2!=0)
	{
		cout << "\nNo es la secuencia de un grafo, finalizando...";	//La suma no es par, nada que hacer
		exit(EXIT_FAILURE);											//Terminar el programa
	}
	cout<<"\nIniciando recursividad...";
	Recursividad(input);									//En caso contrario, entrar en la recursividad

}

void Recursividad (int* A)
{

	int* arrayOrdenado = Ordenamiento(A);

	int Delta = arrayOrdenado[0];							//Máximo valor del array ordenado (el valor Delta)

	if (Delta > limite)																				//limite también nos sirve para saber cuántos elementos hay en el arreglo, sin contar el primero
	{
		cout << "\nDelta("<<Delta<<")>limite("<<limite<<"), no es un grafico, finalizando...";		//Si Delta sobrepasa la cantidad de elementos a su derecha en el array, nada que hacer, no es un grafico
		exit(EXIT_FAILURE);																			//Terminar el programa
	}

	int* arrayRecorrido = Recorrimiento(arrayOrdenado);		//Eliminamos al primero recorriendo el array a la izquierda

	for (int i=0; i<=Delta; i++)
	{
		arrayRecorrido[i]--;				//Es decir A[i]=A[i]-1
	}
	
	cout<<endl;
	for(int i=0; i<=limite;i++)							//Este ciclo imprime el arreglo
		cout << arrayRecorrido[i] << "  ";

	if (!existsInArray(arrayRecorrido,0))				//Comprobamos que no haya un 0 en el array resultante
		Recursividad(arrayRecorrido);					//Si no hay un 0, seguimos realizando el algoritmo
	else 
	{
		cout << "\nCero encontrado, finalizando...";	//Si encuentra un 0, entonces no es un grafico
		exit(EXIT_FAILURE);								//Terminar el programa
	}
}


int* Recorrimiento(int* A)						//Esta función realiza un recorrimiento de los elementos del array...
{												//...hacia la izquierda para borrar al primer elemento
	for (int i=0; i<=limite; i++)
		A[i]=A[i+1];
	limite--;									//Reducimos el tamaño del array

	return A;									
}


//insertion sort para ordenar

int* Ordenamiento(int* A)         		//int* para Arreglos
{
	int n = limite + 1;					//Obtenemos el valor de n
	for (int j=1; j<=n-1; j++) 
	{
		int key = A[j];					//Valor de A actual
		int i=j-1;						//Posición en el vector A antrior

		while (i>=0 && A[i]<key)		//Mientras la posición sea mayor a 0 y si la posicion anteior es menor que la actual
		{							
			A[i+1]=A[i];
			i=i-1;
		}

		A[i+1]=key;
	}
	return A;
}

bool existsInArray(int* A, int elemento)		//Esta función busca el número entero "elemento" en el array "A"
{
	for(int i=0; i<=limite; i++){
		if (elemento = A[i])
			return true;						//El elemento ha sido encontrado, responde con "true"
	}
	return false;								//Terminó el ciclo y no encontró a "elemento", responde con "false"
}