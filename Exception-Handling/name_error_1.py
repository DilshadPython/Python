
try:
    print('Running try before except ....')
    print('23' + a)

# except Exception, e: in python2.7
except TypeError as t:
    print('Running except ..............')
    print('\nNameError a not define ')
# we add NameError to execute the error from line 4
except NameError as n:
    print('This is Name error triggered')
