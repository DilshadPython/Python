''' How random works inside function '''
import random


def run_func():
    ''' define the func for random number '''
    result = random.randint(0, 101)
    return result


def cal(x, y):
    ''' calculate the numbers '''
    print('x = ', x, 'y = ', y)
    a = x + y
    b = x - y
    c = x * y
    d = x // y
    e = x % y
    f = x / y
    return a, b, c, d, e, f


print(cal(run_func(), run_func()))
