# Python has first class function they can be used to emulate switch/case
# statements


def dispatch_if(operator):
    op = print(['add', 'sub', 'mul', 'div', 'rem'])
    operator = str(input('Enter the the operator: '))
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))

    if operator == 'add':
        return print('Result: ', x + y)
    elif operator == 'sub':
        return print('Result: ', x - y)
    elif operator == 'mul':
        return print('Result: ', x * y)
    elif operator == 'div':
        return print('Result: ', x / y)
    elif operator == 'rem':
        return print('Result: ', x % y)
    else:
        return print('Unknowen operatoer pleatry again!')

print(dispatch_if(input))
