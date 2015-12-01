#include <stdio.h>
#include <math.h>

int main()
{
	int i, j;
	long int output = 0;
	for (i = 1; i <= 100; ++i) {
		for (j = i+1; j <= 100; ++j) {
			if (j != i) {
				output += 2*i*j;
			}
		}
	}
	printf ("%lu\n", output);
}
