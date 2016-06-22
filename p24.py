import math

desired_index = 1000000
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = math.factorial(10)


output = ""
for i in range(0, 10):
	x = x/(10 - i)
	current = digits[(desired_index-1)/x]
	desired_index = desired_index % x
	output += str(current)
	new_digits = []
	for i in digits:
		if i != current:
			new_digits.append(i)
	digits = new_digits

print output
