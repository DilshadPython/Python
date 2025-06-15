name = 'Dilshad'

def myname():
    print('My name is ' + name)

myname()

first_name = 'Tomas'

def myfirstname():
    # here the func don't display Tomas and Julia because no print and no return only define
    # first name again with different name
    first_name = 'Julia'

myfirstname()
print('Your first name is  ' + first_name)


year = 1978

def myage():
    year = 1975
    print('My age is ', year)
    print('My age is ' + str(year))

myage()
print('But my age here is ' + str(year))

language = 'Python'

def like_func():
    language = 'Python'
    print('I love ', language)

like_func()

print(language + 'is my favourite language')