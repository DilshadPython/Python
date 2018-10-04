import os
import glob

# first define the current pat
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path, ' << current directory')

# another way to find current path

cwd = os.getcwd()
print(cwd, ' << second way')

# check what is in current directory
os.chdir(dir_path)

for file in glob.glob('*.py'):
	print(file)
