def method(*args, **kwargs):
    print('Enter your details: ', args)

method('Dilshad', 'Abdulla', 'Developer')
method(50, 'Brentwood', 175, 'German')
method('Dilshad')
method(fname='Dilshad')

print('\n###############################')
# This time we use kwargs
def detail(*args, **kwargs):
    print('Enter your details: ', kwargs)

detail(fname='Dilshad', lname='Abdulla', height=175)
detail(fname='Dilshad', height=175)
detail(fname='Dilshad', lname='Abdulla', age=44, job='Python developer', city='Brentwood')

print('\n###############################')
# we use both
def user(*args, **kwargs):
    print('Enter user details', args, kwargs)

user('Adam', 'Smith', 44, 170, 'Brentwood', 'UK')
user(fname='Adam', lname='Smith', age=44, height=170, city='Brentwood', country='UK')
