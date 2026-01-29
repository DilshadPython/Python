'''
LEGB
Is stand for Local, Enclosing, Global, Built-in
'''

fname = 'global Dilshad'

def legb():
    lname = 'local Abdulla'
    # we call the local var (lname)
    print(lname)
    # now we call the global var (fname)
    print(fname)


legb()
# we can print the global fname but we can't print the lname because is in the methods not access