using namespace std;

void split(int, int);

const int aSize = 10;
int input [aSize] = {20,14,21,3,6,56,4,1,7,34};

int main(int argc, char const *argv[])
{
	split (0, aSize -1);
	return 0;
}

void split(int low, int hi){

	if(low >= hi)
		return;
	int n = hi - low +1;
	int p = low;
	int q = (n/2)-1;
	int r = hi;
	split(p, q);
	split(q+1, r);

	merge()

}

void merge(int p, int q, int r){



}