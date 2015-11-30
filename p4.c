#include <stdio.h>
#include <math.h>


//returns 1 if n is a palindrome; 0 otherwise
int palindromecheck (int n) 
{
	int numdigits = floor(log10(n)) + 1;
	//printf ("numdigits is %d\n", numdigits);
	int array[numdigits];
	int i;
	for (i = 0; i < numdigits; ++i) {
		array[i] = n % 10;
		n = n/10;
	}
	for (i = 0; i < numdigits; ++i) {
		if (array[i] != array[numdigits - i - 1]) {
			return 0;
		}
	}
	return 1;
}


int main()
{
	int i, j;
	int largestpalindrome = 0;
	for (i = 100; i < 1000; ++i) {
		for (j = 100; j < 1000; ++j) {
			if (palindromecheck(i * j) == 1) {
				largestpalindrome = i*j < largestpalindrome ? largestpalindrome : i * j;
			}
		}
	}
	printf ("%d\n", largestpalindrome);
}
