import math

def self_power(n):
	if n == 1:
		return 1
	if n == 2:
		return 4
	output = 1
	for k in range(0, n):
		output = output * n
		output = output % 10000000000
	#print output
	return output

sum = 0
for n in range(1, 1001):
	#print n
	sum = sum + self_power(n)
	sum = sum % 10000000000

print sum