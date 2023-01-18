# using end="" inside print use for keep the both words in the same line tobe printed

print('Hello', end='')
print(' Python !')

# Data type

a = 2 
b = int(3)

print(type(a), ' a')
print(type(b), 'b')

print('Are a and b same data type?')
if type(a) == type(b):
	print(True)



c = 3.2
print(type(c), ' c')

d = float(4)
print(type(d), ' d')

print('Are the c and d same data type?')
if type(c) == type(d):
	print(True)
