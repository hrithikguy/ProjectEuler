import math


output = 0

for n in range(1, 10000):
	x= math.pow(10, float(n-1)/float((n)))
	output +=  10 - math.ceil(x) 
	if 10 - math.ceil(x) == 0:
		break
print output