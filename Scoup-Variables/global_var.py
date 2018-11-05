
'''
We create  a function called itself when is run called clouser function
this function also work like global and local variable
'''
name = ' Global name is Hello Python'


def university():

    def student():
        print(f'\n 1. {name}')

    student()  # sub function
    print(f'\n 2. {name}')

university()  # main function
print('\n 3. ', name)
