import sys

'''
python sys_slices.py Python Java C++ Django Flask JavaScript

Welcome to  Python  tutorials
Welcome to  Java  tutorials
Welcome to  C++  tutorials
Welcome to  Django  tutorials
Welcome to  Flask  tutorials
Welcome to  JavaScript  tutorials

'''

if len(sys.argv) < 2:
    sys.exit('The file run with less argument')

# r
for arg in sys.argv[1:]:
    print('Welcome to ', arg, ' tutorials')