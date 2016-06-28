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



prime_list = []

for n in range(1, 1000000):
	if is_prime(n) == 1:
		prime_list.append(n)

reverse_prime_list = prime_list[::-1]
length = len(prime_list)/3
found = 0
while found == 0:
	for i,j in enumerate(reverse_prime_list):
		stop_searching_index = j/length + 100
		for k,l in enumerate(prime_list):
			if l > stop_searching_index:
				stop = k
				break
		cut = sum(prime_list[0:length])
		if cut > j:
			break
		if cut == j:
			found = 1
			print j
		for k in range(0, stop+1):
			cut = cut - prime_list[k] + prime_list[k + length]
			if cut > j:
				break
			if cut == j:
				found = 1
				print j
	length = length - 1