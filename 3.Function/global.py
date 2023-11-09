# global var
a = 12


def test():
    # call the global var inside the function
    global a
    a += 3
    print('Result of a is : ', a)

test()
