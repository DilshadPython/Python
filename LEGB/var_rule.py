"""
LEGB
Local, Enclosing, Global, Built-in
"""


def test_func():
    global a
    # This is local veriable define
    a = 'local l'
    print(' calling from function, ', a, ' var')

# this function has access to local and global variable
test_func()

print('\n Calling from print :', a, '\n')


