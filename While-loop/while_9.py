keep_going = True
a = 0
b = 0

print(' a + b > 24 when reach to this point the loop is end')
while keep_going:
    print('----', "===================", '----')
    if a + b > 24:
        keep_going = False
    a = a + 5
    b = b + 7

    print('First add a = {} and b = {}: '.format(a, b))
