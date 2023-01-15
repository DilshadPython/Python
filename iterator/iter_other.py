numbers = range(1, 11)

itr = iter(numbers)
print(next(itr))
print(next(itr))
print(next(itr))

# from here we use another way to working with iterations
# import os to give access to current directory
import os

# popen is 
files = os.popen('dir *.py')
# change to iterator
itrfile = iter(files)
print(next(itrfile))
