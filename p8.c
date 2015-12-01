#include <stdio.h>
#include <math.h>
#include <ctype.h>

int main()
{
	int array[1000];
	int i = 0;
	int j;
	char ch;
	printf ("Input number\n");
	while (i < 1000) {
		ch = fgetc(stdin);
		if (isdigit(ch)) {
			array[i] = ch - 48;
			++i;
		}
	}

	long int maxproduct = 0;
	long product;
	for (i = 0; i <= 998; ++i) {
		product = 1;
		for (j = i; j <= i + 12; ++j) {
			product *= array[j];
		}
		if (product > maxproduct) {
			maxproduct = product;
		}
	}
	printf("\n%lu\n", maxproduct);
}
