import math

string = ""

for n in range(1, 1000000):
	string += str(n)


output = 1
for i in range(0, 7):
	output *= int(string[int(math.pow(10, i)-1)])

print output