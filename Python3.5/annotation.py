'''
 Python 3.5+ supports 'type annotations' that can be
 used with tools like Mypy to write statically typed Python:
'''

def add_item(a: int, b: int) -> int:

	return a + b 

print(add_item(2, 3))	

print()
print(add_item(2, 3.3))	


print()
print(add_item(2.9, 3.3))

print()
def add_me(a: float, b: float) -> float:

	return a + b 


print(add_me(2.9, 5.8))
print()

print(add_me(2, 3.3))
print()

print(add_me(2, 8))
print()