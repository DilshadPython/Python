"""
LEGB
Local, Enclosing, Global, Built-in
"""

# This is global veriable define
x = 'global x'

def test_func():
    # This is local veriable define
    y = 'local l'
    print(x, ' 1 this is a global var')
    print(y, ' 2 this is a the local var')

# this function has access to local and global variable
test_func()

print('\n 3 This is a global var :', x, '\n')

# if you try to access y throw print(y) doesn'y access

a = 'Global a'
b = 'Global B'

def test_func():
    global a
    global b
    # This is local veriable define
    b = 'Local b'

    print(b, ' 4 this is a, ', b, ' var \n')
    print(a, ' 5 this is a the local var \n')
    print(b, ' 6 this is a the local var \n')

# this function has access to local and global variable
test_func()

print('\n 7 This is a global var :', a)
print('\n 8 This is a global var :', b)
