#include <stdio.h>
#include <math.h>


long int gcd(long int m, long int n)
{
	if (m == 0) {
		return n;
	}
	if (n == 0) {
		return m;
	}
	if (m > n) {
		return gcd (m % n, n);
	}
	else {
		return gcd (n % m, m);
	}
}

long int lcm(long int m, long int n) 
{
	return (m * n)/gcd(m, n);
}


int main()
{
	long int output = 1;
	long int i;
	for (i = 1; i <= 20; ++i) {
		output = lcm(output, i);
	}
	printf("%lu\n", output);
}
