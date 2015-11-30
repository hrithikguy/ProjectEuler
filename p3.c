#include <stdio.h>
#include <math.h>

int main()
{
	long int input = 600851475143;
	long int largestprime;
	long int i;
	for (i = 2; i < floor(sqrt(600851475143)); ++i) {
		if (input % i == 0) {
			largestprime = i;
		}
		while (input % i == 0) {
			input = input/i;
			//printf ("input is now %lu\n", input);
		}
	}
	printf ("%lu\n", largestprime);
}
