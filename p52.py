import math


for n in range(1, 1000000):
	multiples = map(str, [x*n for x in range(1, 7)])
	sorted_multiples = []
	for i in multiples:
		sorted_multiples.append("".join(sorted(i)))
	#print multiples
	#print sorted_multiples
	if len(set(sorted_multiples)) == 1:
		print n