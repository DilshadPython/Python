'''
vals = [experession for value in collection if condition]

values = []
for value in collection:
	if condition:
		values.append(experession)
'''

some_sqrt = [num * num for num in range(24) if not num % 2]

print(some_sqrt)
