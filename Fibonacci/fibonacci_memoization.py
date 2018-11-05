'''
Fibonacci Sequence
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''
'''
Memoization
1. Implement explicity
2. Use builtin python tools
'''

fibonacci_cache = {}


def fibonacci(x):
    # if we have cached value, then return it
    if x in fibonacci_cache:
        return fibonacci_cache[x]

    # compute the nth term
    if x == 1:
        return 1
    elif x == 2:
        return 1
    elif x > 2:
        value = fibonacci(x - 1) + fibonacci(x - 2)

    # cache the value and return it
    fibonacci_cache[x] = value
    return value

for x in range(1, 501):
    print(x, ': ', fibonacci(x))
