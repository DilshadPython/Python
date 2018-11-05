'''
 Because Python has first-class functions they can
 be used to emulate switch/case statements
 https://www.getdrip.com/deliveries/iksa2qbgqiepw2auuyty?__s=qyvy26twbzapeofqm1wx
'''


def dispatch_dict(operator):
    op = print(['add', 'sub', 'mul', 'div', 'rem'])
    operator = str(input('Plese Select on of the operators above: '))
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))

    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
        'rem': lambda: x % y,
    }.get(operator, lambda: None)()

print(dispatch_dict(input))
