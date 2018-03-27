import itertools


def alpha():
	for i in itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
		print(i)
		if i[25] == 'Z':
			break
		
alpha()