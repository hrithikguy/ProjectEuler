import itertools
import math
import numpy as np


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
found = 0
for n in range(11, 1000000):
  if found == 1:
    break
  if is_prime(n) == 1:
    #print n
    length = len(str(n))
    combs = []
    lst = np.arange(length)
    for i in range(1, length):
      els = [list(x) for x in itertools.combinations(lst, i)]
      combs.extend(els)
    #print combs
    for i in combs:
      counter = 0
      if 0 not in i:
        for m in range(0, 10):
          k = list(str(n))
          for j in i:
            k[j] = str(m)
          #print k
          #print "".join(k), "end"
          k = "".join(k)
          if is_prime(int(k)) == 1:
            counter = counter + 1
            #print k
        if counter == 8:
          found = 1
          print n, i, counter, "case 1"
          for m in range(0, 10):
            k = list(str(n))
            for j in i:
              k[j] = str(m)
              #print k
              #print "".join(k), "end"
            k = "".join(k)
            if is_prime(int(k)) == 1:
              print int(k)
      else:
        for m in range(1, 10):
          k = list(str(n))
          for j in i:
            k[j] = str(m)
          #print k
          #print "".join(k), "end"
          k = "".join(k)
          if is_prime(int(k)) == 1:
            counter = counter + 1
            #print k
        if counter == 8:
          found  = 1
          print n, i, counter, "case 2"
          for m in range(1, 10):
            k = list(str(n))
            for j in i:
              k[j] = str(m)
              #print k
              #print "".join(k), "end"
            k = "".join(k)
            if is_prime(int(k)) == 1:
              print int(k)
