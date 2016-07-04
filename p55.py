import math

def is_palindrome(k):
	n = str(k)
	if len(n) == 1:
		return 1
	if len(n) == 2:
		if int(n) % 11 == 0:
			return 1
		else:
			return 0
	if n[0] != n[-1]:
		return 0
	else:
		return is_palindrome(n[1:-1])

output = 0
for n in range(1, 10000):
	k = n
	lyc = 1
	for i in range(1, 51):
		k = k + int(str(k)[::-1])
		if is_palindrome(k):
			lyc = 0
	if lyc == 1:
		output += 1
		#print n


print output