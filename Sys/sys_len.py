import sys

'''
python sys_len.py 
The file run with less argument

python sys_len.py java python
The file run with more arguments

python sys_len.py java 
Welcome to  java  tutorials
'''

if len(sys.argv) < 2:
    print('The file run with less argument')
elif len(sys.argv) > 2:
    print('The file run with more arguments')
else:
    print('Welcome to ', sys.argv[1], ' tutorials')
