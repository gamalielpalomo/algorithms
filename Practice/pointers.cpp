#include <iostream>

using namespace std;
const int MAX = 3;

int main(){
	/*int var1;
	char var2[10];

	cout << "Address of var1 variable: ";
	cout << &var1 << endl;

	cout << "Address of var2 variable: ";
	cout << &var2 << endl;

	int var = 20;
	int *ip;

	ip = &var;

	cout << "Value of var variable: ";
	cout << var << endl;

	cout << "Address stored in ip variable: ";
	cout << ip << endl;

	cout << "Value of *ip variable: ";
	cout << *ip << endl;

	*ip = 30;

	cout << "Value of *ip variable after change: ";
	cout << var << endl;
	*/

	int array[MAX] = {10, 100, 200};
	int *ptr;

	ptr = array;

	for (int i = 0; i < MAX; i++){
		
		cout << "Address of var[" << i << "] = ";
		cout << ptr << endl;

		cout << "Value of var[" << i << "] = ";
		cout << *ptr << endl;

		ptr++;
	}


	return 0;
}