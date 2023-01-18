keep_going = True
a = 0
b = 0
while keep_going:
    print('-----', "O", '-----')
    a = a + 5
    b = b + 7
    print(a, b)
    if a + b > 24:
        keep_going = False
        print(keep_going)
