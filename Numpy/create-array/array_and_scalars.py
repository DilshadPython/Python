import numpy as np

x = 5 / 2
print(x)

print('=============================')

y = 5.0 / 2
print(y)
print('=============================')
print('After import __future__ division')

from __future__ import division
z = 5 / 2
print(z)
