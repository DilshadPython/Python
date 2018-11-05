a = 12


def test():
    global a
    a += 1
    print('Result of a is : ', a)

test()
