# built-in model in python
import pdb


def calculate(i, j):
    a = i + j
    b = i - j
    c = i * j
    d = i / j
    return a, b, c, d

a = 7
b = 5
c = 81
d = 4

# breakepoint
pdb.set_trace()
calculate(4, 3)
print('a = ' + str(a))

n = calculate(7, 2)
print('n = ' + str(n))

s = calculate(9, 9)
print('s = ', str(s))

b = calculate(12, 3)
print('b = ', str(b))
