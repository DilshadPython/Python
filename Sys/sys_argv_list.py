import sys

'''
python sys_argv_list.py Python Java C++ Django Flask JavaScript
'''

if len(sys.argv) < 2:
    sys.exit('The file run with less argument')

# Display the last argument only
'''
python sys_argv_list.py Python Java C++ Django Flask JavaScript

Welcome to  JavaScript  tutorials
'''

for arg in sys.argv[-1:]:
    print('Welcome to ', arg, ' tutorials')

print('\n##########################\n')
'''
Welcome to  JavaScript  tutorials
Welcome to  Flask  tutorials
Welcome to  Django  tutorials
Welcome to  C++  tutorials
Welcome to  Java  tutorials
Welcome to  Python  tutorials
Welcome to  sys_argv_list.py  tutorials
'''
for arg in sys.argv[6::-1]:
    print('Welcome to ', arg, ' tutorials')

'''
Welcome to  JavaScript  tutorials
Welcome to  Flask  tutorials
Welcome to  Django  tutorials
Welcome to  C++  tutorials
Welcome to  Java  tutorials
Welcome to  Python  tutorials
'''

print('\n**************************\n')
for arg in sys.argv[6:0:-1]:
    print('Welcome to ', arg, ' tutorials')