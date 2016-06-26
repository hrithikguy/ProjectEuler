import math

def pandigital_check(n):
	counter = 1
	string = ""
	for i in range(1, 10):
		string += str(n*i)
		if counter == 0:
			break
		if len(string) > 9:
			counter = 0
		sortedstring =  "".join(sorted(string))
		if len(sortedstring) == 9 and sortedstring == "123456789":
			counter = 1
			break
	if counter == 1:
		return 1, string
	else:
		return 0, ""

		
highest = 0
for n in range(1, 10000):
	x,y = pandigital_check(n)
	if x== 1:
		#print n, y
		if y > highest:
			highest = y

print highest