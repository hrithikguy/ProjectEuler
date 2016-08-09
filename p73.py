import math
from fractions import gcd
counter = 0
for n in range(2, 12001):
	k = n/3 - 1
	for k in range(n/3-1, n):
		if float(k)/float(n) < 1.0/2.0 and float(k)/float(n) > 1.0/3.0 and gcd(k,n) == 1:
			# if 3.0/7.0 - float(k)/float(n) < min_val:
			# 	min_num = k
			# 	min_den = n
			# 	min_val = 3.0/7.0 - float(k)/float(n)
			# 	print min_num, min_den, min_val
			#print float(k)/float(n)
			counter += 1


print counter