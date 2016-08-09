import math


def phi(n):
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result

min_val = 100
min_n = 1

for n in range(2, 10000001):
	if sorted(str(n)) == sorted(str(phi(n))):
		if float(float(n)/float(phi(n))) < min_val:
			min_val = float(float(n)/float(phi(n)))
			min_n = n
			print n, phi(n), float(float(n)/float(phi(n)))


print min_n, min_val