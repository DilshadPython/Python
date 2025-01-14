import sys
'''
We are using sys with argv together in the file when the user run python sys_argv.py
if the value in sys.argv[0] doesn't need any name or word but if sys.argv[1] we have 
to run this way python sys_argv.py Python 
and for sys.argv[2] run python sys_argv.py Java Python to see the layout of the print.
'''

# the file name is sys_arvg.py
# run python sys_argv.py
print('Welcome to tutorials of ', sys.argv[0])

# Whe you run this file you have to run python sys_argv.py Java or Python
print('Welcome to tutorials of ', sys.argv[1])

# Whe you run this file you have to run python sys_argv.py Java and Python
print('Welcome to tutorials of ', sys.argv[2])

#Outcome
'''
python sys_argv.py Java Python

Welcome to tutorials of  sys_argv.py
Welcome to tutorials of  Java
Welcome to tutorials of  Python

'''