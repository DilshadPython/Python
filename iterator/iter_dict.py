names = {'Alan': 23, 'Sara': 30, 'Tom': 28, 'Raechel': 27, 'Anja': 25}

# This to show how we read dict using forloop
# for name in names.keys():
# 	print(name, names[name])

itr = iter(names)
print(next(itr))
print(next(itr))
print(next(itr))

# we starting using for loop for the dictionar made as itr
for key in names:
	print(key, names[key])