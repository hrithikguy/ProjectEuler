import math

powers = set()

for a in range(2, 101):
	for b in range(2, 101):
		powers.add(math.pow(a, b))

#print powers
print len(powers)