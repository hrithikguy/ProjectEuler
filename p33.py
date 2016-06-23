import math
import fractions

aproduct = 1
bproduct = 1
for a in range(1, 100):
	for b in range(a+1, 100):
		newa = a
		newb = b
		if len(str(a)) == 2 and len(str(b)) ==2 and str(a)[0] == str(b)[0]:
			newa = int(str(a)[1])
			newb = int(str(b)[1])
		if len(str(a)) == 2 and len(str(b)) ==2 and str(a)[0] == str(b)[1]:
			newa = int(str(a)[1])
			newb = int(str(b)[0])
		if len(str(a)) == 2 and len(str(b)) ==2 and str(a)[1] == str(b)[1]:
			newa = int(str(a)[0])
			newb = int(str(b)[0])
		if len(str(a)) == 2 and len(str(b)) ==2 and str(a)[1] == str(b)[0]:
			newa = int(str(a)[0])
			newb = int(str(b)[1])

		if a * newb == b * newa and a != newa and str(a)[1] != "0":
			aproduct *= a
			bproduct *= b

print bproduct/fractions.gcd(aproduct, bproduct)