def abundantcheck (n):
	sumofdivisors = 0
	for i in range(1, n/2 + 2):
		if n % i == 0:
			sumofdivisors += i

	if sumofdivisors > n:
		return 1
	return 0


abundant_list = []
for i in range(3, 28123):
	if abundantcheck(i) == 1:
		abundant_list.append(i)

print abundant_list
print len(abundant_list)


sum_list = set()
for i in abundant_list:
	for j in abundant_list:
		sum_list.add(i+j)


print sum_list
print len(sum_list)

sum = 0
for i in range(1, 28124):
	if i not in sum_list:
		sum += i

print sum