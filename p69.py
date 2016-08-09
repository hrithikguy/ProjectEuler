import math
import time


# def phi(n):
# 	output = n
# 	for i in range(2, n+1):
# 		counter = 0
# 		while (n % i == 0):
# 			n = n/i
# 			counter = counter + 1
# 		if counter > 0:
# 			output  = output * (1 - float(1.0/i))
# 	return output

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



max_val = 0
max_n = 1

for n in range(2, 1000001):
	#start = time.time()
	if float(float(n)/float(phi(n))) > max_val:
		max_val = float(float(n)/float(phi(n)))
		max_n = n
		print max_val, max_n
	#end = time.time()
	#print n, end-start

	if n % 10000 == 0:
		print n
print max_val, max_n