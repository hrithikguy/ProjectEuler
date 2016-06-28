import math
import numpy as np


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


size = 1000000

memo = np.zeros((size))
#print memo

prime_lists = []
prime_lists.append([0])
prime_lists.append([1])
prime_lists.append([2])

memo[0] = 0
memo[1] = 0
memo[2] = 1
for i in range(3, size):
	for j in range(2, int(math.sqrt(i))+2):
		if i % j == 0:
			if j not in prime_lists[i/j]:
				memo[i] = memo[i/j] + 1
				cur_prime_list = []
				for k in prime_lists[i/j]:
					cur_prime_list.append(k)
				cur_prime_list.append(j)
				prime_lists.append(cur_prime_list)
				break
			else:
				memo[i] = memo[i/j]
				prime_lists.append(prime_lists[i/j])
				break
			break
	if is_prime(i):
		memo[i] = 1
		prime_lists.append([i])

memo = np.asarray(memo)
memostring = ""
for i in memo:
	memostring += str(int(i))
findstring = "4444"
print memostring.index(findstring)
