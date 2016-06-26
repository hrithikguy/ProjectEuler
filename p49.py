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


for a in range(1000, 10000):
	if is_prime(a) == 1:
		for b in range(a+1, 100000):
			c = 2*b - a
			if is_prime(b) == 1 and is_prime(c) == 1:
				a_sorted = "".join(sorted(str(a)))
				b_sorted = "".join(sorted(str(b)))
				c_sorted = "".join(sorted(str(c)))
				if a_sorted == b_sorted and b_sorted == c_sorted:
					print a, b, c
