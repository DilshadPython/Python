import os
from contextlib import contextmanager

'''
In this Python Programming Tutorial, we will be learning how to use context managers to
properly manage resources. Context Managers are great for when we need to setup or teardown
some resources during use. So these can be used for: open and closing files, opening and closing 
'''

@contextmanager
def change_dir(location):
	try:
		current_directory = os.getcwd()
		# chdir stand for changing directory
		os.chdir(location)

		yield
	finally:
		os.chdir(current_directory)

with change_dir('dir-first'):
	print(os.listdir())

with change_dir('dir-second'):
	print(os.listdir())
