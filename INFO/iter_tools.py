import itertools


def alpha():
	for i in itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
		print(i)
		if i == 'Z':
			break
		


alpha()