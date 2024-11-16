# from here we use another way to working with iterations
# import os to give access to current directory
import os, sys


# popen is  use to access the current path of all file are exisit
files = os.popen('dir *.py')
# change to iterator
fileitr = iter(files)

print(next(fileitr))

# for file in files:
# 	print(file)


 # There is an error this file not working because of the version of python.!