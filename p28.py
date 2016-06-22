import math
import numpy as np
#import matplotlib.pyplot as plt


size = 1001

def up(a, b):
	return a-1, b

def right(a,b):
	return a, b+1

def left (a, b):
	return a, b-1

def down (a, b):
	return a+1, b

matrix = np.zeros((size, size))

#print matrix

#plt.axis([0, size, 0, size])
#plt.ion()

#for i in range(10):
#    y = np.random.random()
#    plt.scatter(i, y)
#    plt.pause(0.05)

#while True:
#    plt.pause(0.05)


lengths = []
for i in range(1, size):
	lengths.append(i)
	lengths.append(i)

lengths.append(size-1)
#print lengths

x = (size - 1)/2
y = (size - 1)/2
counter = 1
number = 1
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

#print matrix
#plt.pause(5)
output = 0
for i in range(0, size):
	for j in range(0, size):
		if i == j or i + j == size - 1:
			output += matrix[i][j]

print int(output)