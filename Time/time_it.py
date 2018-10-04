import timeit


'''
timeit use to measure the execution time of the small bits of python code.
'''

def time_test():
	check = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
	return print(check)


time_test()

print()

def time_list():
	check_list = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
	return print(check_list)

time_list()

print()
def time_map():
	check_map = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
	return print(check_map)

time_map()