import sys

'''
python sys_exist.py 
The file run with less argument

python sys_exist.py dilshad
Welcome to  dilshad  tutorials

python sys_exist.py java python
The file run with more arguments

Notice
If remove sys.exit and change to print it display IndexError 
'''

if len(sys.argv) < 2:
    sys.exit('The file run with less argument')
elif len(sys.argv) > 2:
    sys.exit('The file run with more arguments')

# removed else and use sys.exit to get out of display IndexError
print('Welcome to ', sys.argv[1], ' tutorials')