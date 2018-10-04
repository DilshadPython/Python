
# use contextmanager as decorator to docorate a gentertor function
from contextlib import contextmanager

'''
Everyting above yield function is equlvent to the class method __enter__ function 
Everyting after yield function is equlvent to the class method __exit__ function 

'''
@contextmanager
def open_text_file(filename, mode):

	file = open(filename, mode)
	yield file
	file.close()


# if you use with function you don't need to close the file 
with open_text_file('context_manager_added.txt', 'w') as file:
	file.write('We have import the contextlib to use contextmanager as decorator to decorate\
				a generator function. Its like the privouse file just updated with new idea.')

# to make sure that the file is close run the print line
print(file.closed)
