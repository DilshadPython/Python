def call(to='python'):
    print('Hello, ', to)


call()

print()


def hello():
    print('Hello, ', name)


name = input('Enter first name: ')
hello()


def hello(to):
    print('Hello, ', to)


name = input('Enter second name: ')
hello(name)
