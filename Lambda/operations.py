

ops = {
#	key: value
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b,
    '%': lambda a, b: a % b,
    '*': lambda a, b: a * b,
    '**': lambda a, b: a ** b,
}


def calc(a, b, op):
    return ops[op](a, b)


print(calc(7, 9, '+'))
print(calc(7, 9, '-'))
print(calc(7, 9, '/'))
print(calc(7, 9, '%'))
print(calc(7, 9, '*'))
print(calc(7, 9, '**'))
