# Unordered collection of unique, immutable objects

a = {14, 19, 28, 44, 107, 555, 69874}
print(a)
print(type(a))

print
print(set(a))
print('--------------------')
b = {}

print
print(type(b))
print('--------------------')
c = set()

print(c)
print('--------------------')

x = [1, 4, 3, 5, 1, 5, 9, 2, 5, 8]
print('Do not display duplication')
print(set(x))


i = 7
for i in x:
	if i == 7:
		print(i)
	print(False)
