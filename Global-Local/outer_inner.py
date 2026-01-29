'''
LEGB
Is stand for Local, Enclosing, Global, Built-in
'''
# lang = 'global Python'


def outer_func():
    lang = 'Outer Python'

    def inner_func():
        lang = 'Inner Python'
        print(lang, ' <<')

    ## call inner_func
    inner_func()
    print(lang, ' <<<<')

## call outer function
outer_func()

print('#######################')
def outer_func():
    lang = 'Outer Python'

    def inner_func():

        print(lang, ' <<')

    ## call inner_func
    inner_func()
    print(lang, ' <<<<')

## call outer function
outer_func()