"""
Local, Enclosing, Global, Built-in (LEGB)
"""
a = 'I am Gloabal variable: a'


def search_variable():
    a = 'I am Local variable (a) only access in my function search_variable'
    print('\n', a)

search_variable()

print('\n The Global variable can be access outside the function as well.\n ', a)
