# lambda is a small function with unknown name

name = str(input('Enter your name: ' ))

result = lambda name: name + ' Abdulla'

print('You entered {}  '.format(name, result(name)))

print('Full name: ', result(name))