import math

pandigital_products = set()

for a in range(1, 100):
	#print a
	for b in range(a, 10000):
		string = list(str(a) + str(b) + str(a*b))
		#string = string.sort()
		sortedstring =  "".join(sorted(string))
		if len(sortedstring) == 9 and  sortedstring == "123456789":
			#print sortedstring
			print a, b, a*b
			pandigital_products.add(a*b)

print pandigital_products
output = 0
for i in pandigital_products:
	output += i

print output