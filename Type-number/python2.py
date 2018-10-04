# int, long, float, comlex

# Whole numbers: int, long
x = 421
print(' This is int: ', type(x))

# to find out the limit we need to import sys
import sys
a = sys.maxint
print('The maximum int is >>', a)
'''
Here is the output:
python2 python2.py 
(' This is int: ', <type 'int'>)
('The maximum int is >>', 9223372036854775807)
'''
b = 9223372036854775807
print('here is the type of b: ', type(b))
print(b)

d = 9223372036854775808
print('here is the type of d: ', type(d))
print(d)
'''
TESTING
Type-number $ python2
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 9223372036854775807
>>> type(a)
<type 'int'>
>>> b = 9223372036854775808
>>> type(b)
<type 'long'>
>>> b
9223372036854775808L
>>> 
'''
