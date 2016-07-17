import math
import numpy as np
import matplotlib.pyplot as plt


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


size = 100001

def up(a, b):
	return a-1, b

def right(a,b):
	return a, b+1

def left (a, b):
	return a, b-1

def down (a, b):
	return a+1, b

matrix = np.zeros((size, size))


lengths = []
for i in range(1, size):
	lengths.append(i)
	lengths.append(i)

lengths.append(size-1)


x = (size - 1)/2
y = (size - 1)/2
counter = 1
number = 1
primes = 0
total_diagonal_primes =0

while (counter < 2*size):
	#print counter
	matrix[x, y] = number
	#plt.scatter(x, y)
	#plt.pause(0.05)
	number += 1
	if counter % 4 == 1:
		for i in range(0, lengths[counter-1]):
			x,y = right(x,y)
			matrix[x,y] = number
			#plt.scatter(x, y)
			#plt.pause(0.05)
			number += 1
		cur_sum = 0
		corners = [(size-1)/2 - (counter-1)/4, (size-1)/2 + (counter-1)/4]
		for m in corners:
			for n in corners:
				if is_prime(matrix[m,n]) == 1:
					total_diagonal_primes += 1


#		for m in range((size-1)/2 - (counter - 1)/4, (size-1)/2 + (counter -1)/4 + 1):
#			for n in range((size-1)/2 - (counter - 1)/4, (size-1)/2 + (counter -1)/4 +3 1):
#				if m == n or m + n == size - 1:

					#print matrix[m,n]
#					if (is_prime(matrix[m,n]) == 1):
						#print matrix[m,n]
						#print "is prime"
#						cur_sum += 1
		#print cur_sum
		#print (2*((counter-1)/2+1) - 1)
		#print "\n"
		fraction =  float(total_diagonal_primes)/float((2*((counter-1)/2+1) - 1))
		print (counter-1)/2 + 1, fraction
		if fraction <= 0.1 and counter > 5:
			print (counter-2)/2 + 1
			break

	elif counter % 4 == 2:
		for i in range(0, lengths[counter-1]):
			x,y = down(x,y)
			matrix[x,y] = number
			#plt.scatter(x, y)
			#plt.pause(0.05)

			number += 1

	elif counter % 4 == 3:
		for i in range(0, lengths[counter-1]):
			x,y = left(x,y)
			matrix[x,y] = number
			#plt.scatter(x, y)
			#plt.pause(0.05)

			number += 1
	else:
		for i in range(0, lengths[counter-1]):
			x,y = up(x,y)
			matrix[x,y] = number
			#plt.scatter(x, y)
			#plt.pause(0.05)

			number += 1
	#print matrix
	number -=1 
	counter += 1







