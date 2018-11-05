from functools import lru_cache

'''
LRU Cache
Least Recently Used Cache
'''


@lru_cache(maxsize=1000)
def fibonacci(num):
    if num == 1:
        return 1

    elif num == 2:
        return 1

    elif num > 2:
        return fibonacci(num - 1) + fibonacci(num - 2)


for num in range(1, 501):
    print(num, ': ', fibonacci(num))
