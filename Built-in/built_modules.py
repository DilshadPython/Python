# built in own module

import os
import math

# we create files to open current path with files ending with .py
files = os.popen(" *.py")

for file in files:
	print(file, end='')


print(math.fabs(-123.45))