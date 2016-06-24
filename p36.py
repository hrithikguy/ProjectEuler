import math

def is_palindrome(n):
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

for n in range(1, 1000000):
	if is_palindrome(str(n)) and is_palindrome(str(bin(n)[2:])):
		print n
		output += n

print output

