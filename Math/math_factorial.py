import math

x = math.sqrt(81)
y = math.sqrt(625)

print('x : ', x, ' = sqrt', '\ny : ',y, ' = sqrt')

i = math.factorial(4)
j = math.factorial(7)

print('i : ', i, ' = factorial', '\nj : ', j, ' = factorial')

m = 11
n = 5

result = math.factorial(m) / (math.factorial(n) * math.factorial(m - n))
print('Result is: ', result)

# OR
from math import factorial as fact
i = 7
j = 5
results = fact(i) / (fact(j) * fact(i - j))

print('Is: ', results)

other = fact(i) // (fact(j) * fact(i - j))
print('The other: ', other)

'''
     m!
____________
 n!(m - n)!

'''
x = 13
print('x : ', fact(x))

a = 100
b = 3

print('a : ', fact(a))

y = fact(a) // (fact(b) * fact(a - b))
print('y : ', y)

f = len(str(fact(a)))
print('f : ', f)
