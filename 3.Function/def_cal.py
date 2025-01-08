def my_func():
    lang = 'Python'
    machine = 'Calculator'
    return print('Welcome {} {}'.format(lang, machine))

my_func()


def your_func():
    x = int(input(' Enter a number: '))
    y = int(input(' Enter second number: '))

    total = x + y
    return print(f' We add them together {x} + {y} is: {total}')

your_func()
