import math

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

def get_value(n):
  digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  x = math.factorial(10)
  desired_index = n

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

  return output
output = 0

for i in range(0, math.factorial(10)):
  value = str(get_value(i))
  #print get_value(i)
  if int(value[1:4]) % 2 == 0 and int(value[2:5]) % 3 == 0 and int(value[3:6]) % 5 == 0 and int(value[4:7]) % 7 == 0 and int(value[5:8])%11 == 0 and int(value[6:9]) % 13 == 0 and int(value[7:10]) % 17 == 0:
    print value 
    output = output + int(value)

print output



