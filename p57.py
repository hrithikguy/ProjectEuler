from fractions import gcd
def next_frac(a, b):
	k = gcd(a,b)
	return (a + 2*b)/k, (b+a)/k


a = 3
b = 2
output = 0
for n in range(0, 1001):
	if len(str(a)) > len(str(b)):
		output = output + 1
		#print a, b
	a,b = next_frac(a,b)

print output