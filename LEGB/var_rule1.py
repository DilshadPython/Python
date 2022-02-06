"""
LEGB
Local, Enclosing, Global, Built-in
"""


def test_func(x):
    # This is local veriable define
    a = 'local a'
    print(x)

# this function has access to local and global variable
test_func('local x')
