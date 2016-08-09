import math
from fractions import gcd


min_val = 100
min_num = 1
min_den = 1
for n in range(500000, 1000001):
	k = 3*n/7 - 3
	while 3.0/7.0 > float(k)/float(n):
		if 3.0/7.0 - float(k)/float(n) < min_val:
			min_num = k
			min_den = n
			min_val = 3.0/7.0 - float(k)/float(n)
			print min_num, min_den, min_val
		k += 1
print min_num, min_den, min_val