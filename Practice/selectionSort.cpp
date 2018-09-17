#include <iostream>
using namespace std;

int getSmallest();
const int n = 10;
int input[n] = {1,5,8,3,6,10,4,20,2,9};

int main(){

	for(int i=0; i<n-2; i++){
		int x = getSmallest(i+1);
	}

	return 0;
}

int getSmallest(int pi){
	int result = pi;
	for (int i = pi+1; i<=n-1; i++){
		if(input[i]<input[result]){
			result = i;
		}
	}
	return result;
}