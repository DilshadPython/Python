def welcome(msg):
    name = str(input('Enter your name: '))
    return f'{msg}, {name}'


print(welcome('Hello '))
