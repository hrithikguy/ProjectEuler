#include <stdio.h>
#include <math.h>

int main()
{
	int array[400];
	int i = 0;
	int j;
	int input;
	printf ("Input number\n");
	while (i < 400) {
		scanf("%d", &input);
		array[i] = input;
		++i;
	}

	int matrix[20][20];
	for (i = 0; i < 400; ++i) {
		matrix[i/20][i % 20] = array[i];
	}

	long int maxproduct = 0;
	long int product;
	for (i = 0; i <= 16; ++i) {
		for (j = 0; j <= 16; ++j) {
			product = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3];
			if (product > maxproduct) {
				maxproduct = product;
			}
		}
	}

	for (i = 3; i < 20; ++i) {
		for (j = 0; j <= 16; ++j) {
			product = matrix[i][j] * matrix[i-1][j+1] * matrix[i-2][j+2] * matrix[i-3][j+3];
			if (product > maxproduct) {
				maxproduct = product;
			}
		}
	}



	for (i = 0; i < 20; ++i) {
		for (j = 0; j <= 16; ++j) {
			product = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3];
			if (product > maxproduct) {
				maxproduct = product;
			}
		}
	}
	for (i = 0; i <= 16; ++i) {
		for (j = 0; j < 20; ++j) {
			product = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j];
			if (product > maxproduct) {
				maxproduct = product;
			}
		}
	}
	

	printf("%lu\n", maxproduct);
}
