# create func
def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)

# start from 0 to 2 but don't multiply to 2
f(2)

# start from 0 to 2 but don't multiply to 2
f(3, [3, 2, 1])
# start from 0 to 3 but don't multiply to 3
f(3)
f(5)
f(6, [3, 2, 1])

fname = 'Tom'
point = 72

print(f'My name is {fname} and my point is {point}')
print('My name is %s and my point is %d .' % (fname, point))
print('My name is {0} and my point is {1} .'.format(fname, point))

program = {'language': 'Python', 'version': '3.6'}
print('I like {language} the new version of {version} .'.format(**program))