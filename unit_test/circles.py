from math import pi


def circle_area(r):
	if type(r) not in [int, float]:
		raise TypeError('The radius must be a non-negative real number')

	if r < 0:
		raise ValueError('The radius cannot be negative.')
	return pi*(r**2)

# test function
# we gave some example of different nums
# radii 	= [2, 0, -3, 2 + 5j, True, 'radius']

# message = 'Area of circle with r = {radius} is {area}.'

# for r in radii:
# 	A = circle_area(r)
# 	print(message.format(radius=r, area=A))

# OUTPUT
'''
python sample.py

Area of circle with r = 2 is 12.566370614359172.
Area of circle with r = 0 is 0.0.
Area of circle with r = -3 is 28.274333882308138.
Area of circle with r = (2+5j) is (-65.97344572538566+62.83185307179586j).
Area of circle with r = True is 3.141592653589793.
Traceback (most recent call last):
  File "sample.py", line 14, in <module>
    A = circle_area(r)
  File "sample.py", line 5, in circle_area
    return pi*(r**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int
'''