'''
we have to run mypy example.py output should be
Success: no issues found in 1 source file

'''
# we defile n: int
def number(n: int):
    for _ in range(n):
        # we try to repeat 5 time the str below
        print('Hello Python mypy')
# we can define a num like below num: int -, but if we not put int()
# in front of input(0 we will still get an error
# num: int = input('Enter a number: ')
# Solution
num: int = int(input('Enter a number: '))
number(num)
