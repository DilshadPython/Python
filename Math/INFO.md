https://docs.python.org/3/library/math.html

>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

# In python that is how math works
1. exponentaition 3 ** 3   << called power
2. multiplication 2 * 3  or division
3. addition or subtraction

longs are narrow than floats
float are wider than longs
you can convert int to long

Any long you can convert to float but float can't convert to long
long are narrow than float but float are wider than long


You can't convert float to complex
a = 1.7865
a + 0j
when you try float(3.14 + 0j) get an error because you can,t convert float to complex therefore:
floats are narrow than complex numbers
complex are winder that float

# round() This will make a number to closet e.x 3.6 = 4
# ceil() take the number to the highest
# floor() take the number to lowest

>>> from math import *
>>> ceil(3.6)
4
>>> ceil(3.5)
4
>>> ceil(3.4)
4
>>> floor(3.4)
3
>>> floor(3.5)
3
>>> floor(3.7)
3
>>> round(3.7)
4
>>> round(3.5)
4
>>> round(3.4)
3
