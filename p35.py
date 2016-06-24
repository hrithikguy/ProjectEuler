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


for n in range(2, 1000000):
	if is_prime(n) == 1:
		circular = 1
		k = len(str(n))
		for i in range(1, k):
			l = int(str(n)[i:] + str(n)[:i])
			if is_prime(l) != 1:
				circular = 0
				break
		if circular == 1:
			print n
			output += 1

print output