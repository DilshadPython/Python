def genarator_func():
    yield 2
    yield 3
    yield 4
    yield 5

for item in genarator_func():
    print(item)