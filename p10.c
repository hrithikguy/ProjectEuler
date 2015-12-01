#include <stdio.h>
#include <math.h>

int primechecker (int n)
{
	if (n == 2) {
		return 1;
	}
	int i;
	for (i = 2; i <= ceil(sqrt(n)); ++i) {
		if (n % i == 0) {
			return 0;
		}
	}
	return 1;
}


int main()
{
	int i;
	long int output = 0;
	for (i = 2; i <= 2000000; ++i) {
		if (primechecker(i) == 1) {
			output += i;
		}
	}
	printf("%lu\n", output);
}
