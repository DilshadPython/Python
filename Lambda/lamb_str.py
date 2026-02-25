# lambda is a small function with unknown name

name = str(input('Enter your name: '))

result = lambda name: name + ' Abdulla'

print('You entered {}  '.format(name, result(name)))
# title set the first character to upper
print('Full name: ', result(name.title()))
