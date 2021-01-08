# Python 3.5+ supports 'type annotations' that can be
# used with tools like Mypy to write statically typed Python:
import random
from random import randint


def my_add(a: int, b: int) -> int:
    return a + b

print(my_add(4, 56))

# I have installed the following python3 -m pip install mypy to test the error
# to run  mypy add_int.py

# def str_add(a: int, b: int) -> int:
# 	return 'Welcome'

# print(str_add(4, 56))


def add_num(x: int, y: int) -> int:
    return random.randint

print(add_num(7, 3))


def add_me(x: int, y: int) -> int:
    return 10

print(add_me(7, 9))
