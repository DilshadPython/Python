
try:
    print('Running try before except ....')
    print('23' + a)

# except Exception, e: in python2.7
except TypeError as t:
    print('Running except ..............')
    print('>>>> ', str(t))
    print('\nNameError a not define ')

except NameError as n:
    print('This is Name error triggered')
    print('>>>> ', str(n))

except Exception as e:
    print('General exception ....')
    print('>>>> ', str(e))
