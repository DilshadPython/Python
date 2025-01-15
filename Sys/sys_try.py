import sys
'''

'''

# the file name is sys_arvg.py
# run python sys_argv.py
try:
    # Whe you run this file you have to run python sys_argv.py display line 15
    print('Welcome to tutorials of ', sys.argv[3])
except IndexError:
    print('You didn\'t enter any value or less argument')


# Outcome
'''
python sys_argv.py 

You didn't enter any value or less argument

python sys_try.py Java 
You didn't enter any value or less argument

python sys_try.py Python Java
You didn't enter any value or less argument

python sys_try.py Java Python JavaScript

Welcome to tutorials of  JavaScript

'''