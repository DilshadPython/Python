
a = 3 + 5.7j

print('The type of a is: ', type(a))
''' Testint

Type-number $ python2
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 3 +5.7j
>>> a
(3+5.7j)
>>> type(a)
<type 'complex'>
>>> a.real
3.0
>>> a.img
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'complex' object has no attribute 'img'
>>> a.imag
5.7
>>> 
'''
i = 1.5687
j = 1.5687 + 0j
print(j)

x = complex(15687)
print('here is x now: ', x)

print('')
y = float(1.5687 + 0j)
print(' Here is y now: ', y)
