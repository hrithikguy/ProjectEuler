import math


array3 = []
array4 = []
array5 = []
array6 = []
array7 = []
array8 = []

for n in range(1, 20000):
	if (n*(n+1))/2 < 10000 and (n*(n+1))/2 >= 1000:
		array3.append((n*(n+1))/2)
	if n*n < 10000 and n*n >= 1000:
		array4.append(n*n)
	if (n*(3*n-1))/2 < 10000 and (n*(3*n-1))/2 >= 1000:
		array5.append((n*(3*n-1))/2)
	if n*(2*n-1) < 10000 and n*(2*n-1) >= 1000:
		array6.append(n*(2*n-1))
	if (n*(5*n-3))/2 < 10000 and (n*(5*n-3))/2 >= 1000:
		array7.append((n*(5*n-3))/2)
	if n*(3*n-2) < 10000 and n*(3*n-2) >= 1000:
		array8.append(n*(3*n-2))

nodes = []
for i in array3:
	nodes.append([i,1])
for i in array4:
	nodes.append([i,2])
for i in array5:
	nodes.append([i,3])	
for i in array6:
	nodes.append([i,4])
for i in array7:
	nodes.append([i,5])
for i in array8:
	nodes.append([i,6])



#print nodes

edges = []
for i in nodes:
	for j in nodes:
		if str(i[0])[2:4] == str(j[0])[0:2] and i[1] != j[1]:
			edges.append([i, j])


#print edges

triples = []

for i in edges:
	for j in edges:
		if i[1] == j[0] and j[1][1] != i[0][1]:
			cur = []
			cur.append(i[0])
			cur.append(i[1])
			cur.append(j[1])
			if cur not in triples:
				triples.append(cur)

print triples
print len(triples)


quadruples = []
for i in triples:
	for j in edges:
		if i[2] == j[0] and j[1][1] != i[0][1] and j[1][1] != i[1][1] and j[1][1] != i[2][1]:
			cur = []
			cur.append(i[0])
			cur.append(i[1])
			cur.append(i[2])
			cur.append(j[1])
			if cur not in quadruples:
				quadruples.append(cur)

print quadruples
print len(quadruples)


quintuples = []
for i in quadruples:
	for j in edges:
		if i[3] == j[0] and j[1][1] != i[0][1] and j[1][1] != i[1][1] and j[1][1] != i[2][1] and j[1][1] != i[3][1]:
			cur = []
			cur.append(i[0])
			cur.append(i[1])
			cur.append(i[2])
			cur.append(i[3])
			cur.append(j[1])
			if cur not in quintuples:
				quintuples.append(cur)


print quintuples
print len(quintuples)

sextuples = []
for i in quintuples:
	for j in edges:
		if i[4] == j[0] and j[1][1] != i[0][1] and j[1][1] != i[1][1] and j[1][1] != i[2][1] and j[1][1] != i[3][1] and j[1][1] != i[4][1]:
			if str(j[1][0])[2:4] == str(i[0][0])[0:2]:
				cur = []
				cur.append(i[0])
				cur.append(i[1])
				cur.append(i[2])
				cur.append(i[3])
				cur.append(i[4])
				cur.append(j[1])
				if cur not in sextuples:
					sextuples.append(cur)




print sextuples
print len(sextuples)

for i in sextuples:
	print i[0][0] + i[1][0] + i[2][0] + i[3][0] + i[4][0] + i[5][0]

# triples = []
# for i in pairs:
# 	for j in pairs:
# 		if i[1] == j[0] and j[1][1] != i[0][1]:
# 			cur = i
# 			cur.append(j[1])
# 			print "cur", cur

# print triples
# print len(pairs)
