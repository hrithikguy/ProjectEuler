import math


def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True    


output = 0

for a in range(11, 1000000):
	if is_prime(a) == 1:
		k = len(str(a))
		truncatable = 1
		for i in range(1, k):
			#print int(str(a)[i:])

			if is_prime(int(str(a)[i:])) != 1:
				truncatable = 0
				#break
		for i in range(1, k+1):
			#print int(str(a)[:i])

			if is_prime(int(str(a)[:i])) != 1:
				truncatable = 0
				#break
		if truncatable == 1:
			print a
			output += a

print output
