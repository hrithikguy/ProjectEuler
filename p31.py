import math

amount_we_want = 200

output = 0
for i1 in range(0, amount_we_want/200 + 1):
	for i2 in range(0, (amount_we_want - 200*i1)/100 + 1):
		for i3 in range(0, (amount_we_want - 200 * i1 - 100*i2)/50 + 1):
			for i4 in range(0, (amount_we_want - 200*i1 - 100*i2 - 50 * i3)/20 + 1):
				for i5 in range(0, (amount_we_want - 200*i1 - 100*i2 - 50*i3 - 20*i4)/10 + 1):
					for i6 in range(0, (amount_we_want - 200*i1 - 100*i2 - 50*i3 - 20*i4 - 10*i5)/5 + 1):
						for i7 in range(0, (amount_we_want - 200*i1 - 100*i2 - 50*i3 - 20*i4 - 10*i5 - 5*i6)/2 + 1):
							#for i8 in range(amount_we_want - 200*i1 - 100*i2 - 50*i3 - 20*i4 - 10*i5 - 5*i6 - 2*i7)/1 + 1):
							output += 1

print output
