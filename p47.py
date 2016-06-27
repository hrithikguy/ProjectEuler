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
prime_lists.append([3])
prime_lists.append([2])
prime_lists.append([5])
prime_lists.append([2,3])

memo[0] = 0
memo[1] = 0
memo[2] = 1
memo[3] = 1
memo[4] = 1
memo[5] = 1
memo[6] = 2
for i in range(7, size):
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
	#print memo
	#print prime_lists

#print memo
#print prime_lists

# array = []
# def prime_count(n):
# 	output = 0	
# 	for i in range(2, n):
# 		if n % i == 0:
# 			output += 1
# 			while n % i == 0:
# 				n = n/i
# 	return output

# for n in range(1, size):
# 	array.append(prime_count(n))

#print "done"
find = [3, 3, 3]
find = np.asarray(find)
memo = np.asarray(memo)
memostring = ""
for i in memo:
	memostring += str(int(i))
findstring = "4444"

#print memostring
#print memostring.index("333")
print memostring.index(findstring)
# for n in range(1, size-2):
# 	if memo[n] == 4 and memo[n+1] == 4 and memo[n+2] == 4 and memo[n+3] == 4:
# 		print n
# 		#print n+2, prime_count(n+2)