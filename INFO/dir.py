# In python2
print(dir())

# output
['__builtins__', '__doc__', '__name__', '__package__']

# In python3
print(dir())

# output
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']


import math

print(dir())
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'math']

print(help(__doc__))


test = (1, 'a', 1.1)

dir(help(test))