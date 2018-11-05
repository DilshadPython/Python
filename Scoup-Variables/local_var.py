"""
Local, Enclosing, Global, Built-in (LEGB)
"""


def search_variable(c):
    local = 'I am Local variable (b) only access in my function search_variable'
    print('\n', c)

search_variable('\n I am Local variable a')

# a and b are local not able to access display an error
# search_variable(b)
# search_variable(a)
