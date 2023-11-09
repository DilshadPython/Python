keep_going = True

a = 0
b = 0
while keep_going:
    print('0')
    a = a + 5
    b = b + 7
    print('Add the two value: ', a, b)    # added for test
    if a + b >= 24:
        print('Add them for second time: ', a, b)    # added for test
        keep_going = False
