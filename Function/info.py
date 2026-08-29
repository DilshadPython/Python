
'''
Type of argument in function
keywords
required

Important info kwargs must come last required must come first
See the Examples:
To test remove #. The a is a keyword argument which is come first we get and syntax error here
'''
# def func(a = 0, b):
# 	return a + b
# func(a, 10)


def myfunc(a, b=1):
    return a + b

print(myfunc(4))
''' in the above function a is required argument which is come first, to call the function you
just need to give a value for a argument the b is optional don't need however you can try to use
b argument but you need to give a value '''

print(myfunc(8, 7))
