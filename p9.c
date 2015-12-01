#include <stdio.h>
#include <math.h>

int main()
{
	int a, b, c;
	long int output;
	for (a = 1; a <= 1000; ++a) {
		for (b = 1; b <= 1000; ++b) {
			c = 1000 - a - b;
			if (a*a + b*b == c*c && c > 0) {
				output = a * b * c;
				printf("%lu\n", output);
				return 1;
			}
		}
	}
}
