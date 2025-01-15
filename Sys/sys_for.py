import sys

'''
python sys_slices.py Python Django Java Flask

Welcome to  sys_slices.py  tutorials
Welcome to  Python  tutorials
Welcome to  Django  tutorials
Welcome to  Java  tutorials
Welcome to  Flask  tutorials

'''

if len(sys.argv) < 2:
    sys.exit('The file run with less argument')

# removed else and use sys.exit to get out of display IndexError
for arg in sys.argv:
    print('Welcome to ', arg, ' tutorials')