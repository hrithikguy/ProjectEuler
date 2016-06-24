import math

output = 0
for n in range(3, 1000000):
	factorial_sum = 0
	for i in str(n):
		factorial_sum += math.factorial(int(i))
	if factorial_sum == n:
		output += n

print output