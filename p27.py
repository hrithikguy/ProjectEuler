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


maxcounter =  0

for a in range(-1000, 1000):
	for b in range(-1000, 1000):
		if is_prime(math.fabs(b)) == 1:
			counter = 0
			while is_prime(math.pow(counter, 2) + a * counter + b) == 1:
				counter += 1
			if counter > maxcounter:
				print str(a) + " " + str(b) + " " + str(counter)
				print a * b
				maxcounter = counter


