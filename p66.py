import math

def is_square(n):
	if math.sqrt(n) == math.floor(math.sqrt(n)):
		return 1
	else:
		return 0


max_x = 0
max_D = 0
for D in range(2, 1001):
	if is_square(D):
		continue
	found = 0
	y = 1
	while(found == 0):
		if is_square(1 + D*y*y):
			found = 1
			x = math.sqrt(1 + D*y*y)
			if x > max_x:
				max_x = x
				max_D = D
				print max_x, max_D, y
			break
		y += 1
	if found == 0:
		print D
		break

print max_x
print max_D

