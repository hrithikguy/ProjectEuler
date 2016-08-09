import math
from collections import Counter


cubes = []

for i in range(1, 10000):
	cubes.append(math.pow(i, 3))

#print cubes

cubes2 = []

for i in cubes:
	cubes2.append(str(sorted(str(int(i)))))

#print cubes2

c = Counter(cubes2)
#print c.most_common(5)
for i in c.most_common(5):
	if i[1] == 5:
		for j,k in enumerate(cubes2):
			if k == i[0]:
				print j+1
				print int(math.pow(j+1, 3))
				break


