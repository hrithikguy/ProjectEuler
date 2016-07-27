import math
import numpy as np



#print "hi"
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

for n in range(1, 10000):
	if is_prime(n) == 1:
		prime_list.append(n)

pair_list = set()

for i in prime_list:
	for j in prime_list:
		if j > i:
			if is_prime(int(str(i) + str(j))) == 1 and is_prime(int(str(j) + str(i))) == 1:
				pair_list.add((i,j))

print "pairs done"
print pair_list

triple_list = set()
for i in pair_list:
	for j in prime_list:
		if j > i[1] and is_prime(int(str(i[0]) + str(j))) == 1 and is_prime(int(str(j) + str(i[0]))) == 1:
			if is_prime(int(str(i[1]) + str(j))) == 1 and is_prime(int(str(j) + str(i[1]))) == 1:
				triple_list.add((i[0], i[1], j))
print "triples done"
print triple_list

quadruple_list = set()
for i in triple_list:
	for j in prime_list:
		if j > i[2] and is_prime(int(str(i[0]) + str(j))) == 1 and is_prime(int(str(j) + str(i[0]))) == 1:
			if is_prime(int(str(i[1]) + str(j))) == 1 and is_prime(int(str(j) + str(i[1]))) == 1:
				if is_prime(int(str(i[2]) + str(j))) == 1 and is_prime(int(str(j) + str(i[2]))) == 1:
					quadruple_list.add((i[0], i[1], i[2], j))

print "quadruples done"
print quadruple_list

quintuple_list = set()
for i in quadruple_list:
	for j in prime_list:
		if j >i[3] and is_prime(int(str(i[0]) + str(j))) == 1 and is_prime(int(str(j) + str(i[0]))) == 1:
			if is_prime(int(str(i[1]) + str(j))) == 1 and is_prime(int(str(j) + str(i[1]))) == 1:
				if is_prime(int(str(i[2]) + str(j))) == 1 and is_prime(int(str(j) + str(i[2]))) == 1:
					if is_prime(int(str(i[3]) + str(j))) == 1 and is_prime(int(str(j) + str(i[3]))) == 1:
						quintuple_list.add((i[0], i[1], i[2], i[3], j))

print "quintuples done"
print quintuple_list




