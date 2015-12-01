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
	int counter = 1;
	int i = 2;
	while (counter <= 10001) {
		if (primechecker(i) == 1) {
			if (counter == 10001) {
				printf ("%d\n", i);
			}
			counter++;
		}
		++i;
	}
}
