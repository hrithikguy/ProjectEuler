import math


def combination(n, k):
	return math.factorial(n)/(math.factorial(k) * math.factorial(n-k))

counter = 0
for n in range(1, 101):
	for k in range(0, n+1):
		if combination(n, k) > 1000000:
			#print n, k, combination(n,k)
			counter += 1

print counter