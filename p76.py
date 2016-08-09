import math


hashes = {}

def p(sum,largest):
	#print sum,largest
	if (sum, largest) in hashes:
		return hashes[(sum, largest)]
	#print hashes
	if largest==0:
		hashes[(sum, largest)] = 0 
		return 0
	if sum==0: 
		hashes[(sum, largest)] = 1 
		return 1
	if sum<0: 
		hashes[(sum, largest)] = 0 
		return 0
	if (sum, largest-1) in hashes and (sum-largest, largest) in hashes:
		hashes[(sum, largest)] = hashes[(sum, largest-1)] + hashes[(sum-largest, largest)] 
	return p(sum, largest-1) + p(sum-largest, largest)


for i in range(1, 101):
	print i
	print i, p(i,i) - 1