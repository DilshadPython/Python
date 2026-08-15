"""
Print demonstration: end parameter, data types, and type comparisons.
"""

# Notice:
# 1. Using end='' inside print() keeps both words on the same line to be printed.
# 2. The end='' parameter replaces the default newline character ('\n') in print().

# -----------------------------------------------------------------
# 1. 'end' parameter demonstration
# -----------------------------------------------------------------
# [Old & Current Version]
print('Hello', end='')
print(' Python !')

# [Python 3.6+ f-string alternative]
greeting_start = 'Hello'
greeting_lang = 'Python !'
print(f"{greeting_start} {greeting_lang}")

print()

# -----------------------------------------------------------------
# 2. Integer Data Types & Type Comparison
# -----------------------------------------------------------------
a = 2
b = int(3)

# [Old Version / Legacy print]
print(type(a), ' a')
print(type(b), 'b')

# [New Version / Python 3.6+ f-string]
print(f"{type(a)} a")
print(f"{type(b)} b")

# Notice: In Python, type(a) == type(b) or isinstance(a, int) can be used.
# 'is' or 'isinstance()' is preferred for checking types cleanly.
print('Are a and b the same data type?')

# [Old Version / If-Statement]
if type(a) == type(b):
    print(True)

# [New Version / Python 3.6+ clean expression]
print(f"Result: {type(a) is type(b)} (Both are {type(a).__name__})")

print()

# -----------------------------------------------------------------
# 3. Float Data Types & Type Comparison
# -----------------------------------------------------------------
c = 3.2
d = float(4)

# [Old Version / Legacy print]
print(type(c), ' c')
print(type(d), ' d')

# [New Version / Python 3.6+ f-string]
print(f"{type(c)} c")
print(f"{type(d)} d")

print('Are c and d the same data type?')

# [Old Version / If-Statement]
if type(c) == type(d):
    print(True)

# [New Version / Python 3.6+ clean expression]
print(f"Result: {type(c) is type(d)} (Both are {type(c).__name__})")
