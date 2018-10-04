# this is in python2
# int, long, float, comlex


import sys
a = -sys.maxint -1
print('Here is the a: ', type(a))
print(a)

''' TESTING
>>> a = -sys.maxint -1
>>> print('Here is the a: ', type(a))
('Here is the a: ', <type 'int'>)
>>> print(a)
-9223372036854775808
>>> a
-9223372036854775808
>>> 
>>> a
-9223372036854775808
>>> b = -9223372036854775809
>>> type(b)
<type 'long'>
>>> b
-9223372036854775809L
>>> 
'''

i = 33L
j = 33.13
print(type(i), type(j))
print('')

long(i)
float(j)
print('I  now is', i, ' and j is now ', j)
print(' longs are narrower than floats\n')
print(' floats are winder than longs\n')
print(type(i), type(j))
