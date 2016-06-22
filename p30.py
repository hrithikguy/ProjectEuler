import math


powers = 5

output = 0
for i in range(2, 1000000):
	sumofpowers = 0
	for j in str(i):
		sumofpowers += math.pow(int(j), powers)
	if sumofpowers == i:
		output += i

print output