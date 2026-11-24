def genarator_func():
    yield 2
    yield 3
    yield 4
    yield 5


new_gen = genarator_func()
print(next(new_gen))
print(next(new_gen))
print(next(new_gen))
print(next(new_gen))