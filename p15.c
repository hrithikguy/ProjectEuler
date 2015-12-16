#include <stdio.h>
#include <math.h>

int main()
{
	float i = 1;
	int j;
	for (j = 1; j <= 20; ++j) {
		i = i * (20+j);
		i = i / (j);
	}
	printf("%ld\n", (long int) i);

}
