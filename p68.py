import math
import itertools



x= itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)

y =  list(x)
output = 0
for i in y:
	if i[0] != 10 and i[3] != 10 and i[5] != 10 and i[7] != 10 and i[9] != 10:
		continue
	if i[0] > i[3] or i[0] > i[5] or i[0] > i[7] or i[0] > i[9]:
		continue
	if i[0] + i[1] + i[2] != i[3] + i[2] + i[4]:
		continue
	if i[3] + i[2] + i[4] != i[6] + i[4] + i[5]:
		continue
	if i[6] + i[4] + i[5] != i[8] + i[6] + i[7]:
		continue
	if i[8] + i[6] + i[7] != i[1] + i[8] + i[9]:
		continue
	cur = str(i[0]) + str(i[1]) + str(i[2]) + str(i[3]) + str(i[2]) + str(i[4]) + str(i[5]) + str(i[4]) + str(i[6]) + str(i[7]) + str(i[6]) + str(i[8]) + str(i[9]) + str(i[8]) + str(i[1])
	if int(cur) > output:
		output = int(cur)


print output